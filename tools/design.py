"""
AEP Solution Design Advisor.

Gathers existing sandbox context (namespaces, schemas, field groups, datasets,
placements) and returns it alongside Adobe best-practice guidelines so Claude
can produce a tailored design recommendation before any implementation begins.
"""

from auth import aep_get
from tools.usage_logger import track

# ── Best-practice knowledge base ─────────────────────────────────────────────

_BEST_PRACTICES = {
    "schema": {
        "summary": "Choose the right XDM class, reuse standard field groups, enable for profile only when needed.",
        "guidelines": [
            "Use XDM Individual Profile for person-centric data; XDM ExperienceEvent for time-series behavioural events; Lookup class for reference/dimension data.",
            "Always check existing global and tenant field groups before creating custom ones — reuse avoids union schema bloat.",
            "Enable a schema for Real-Time Customer Profile only if records in that dataset need to be merged into a unified profile. Lookup and reference schemas rarely need profile enablement.",
            "Keep custom field group names descriptive and org-scoped (e.g. '_yourOrg.loyaltyDetails') — avoid generic names like 'customFields'.",
            "Avoid deeply nested objects (>3 levels) — they are harder to query in Query Service and slower to ingest.",
            "Mark exactly one field as the primary identity per profile schema. Composite keys are not supported.",
            "For ExperienceEvent schemas, always include the mandatory 'eventType' and 'timestamp' fields from the XDM ExperienceEvent class.",
            "Use 'format: date-time' for all timestamp fields; use ISO-8601 strings, not epoch integers.",
        ],
    },
    "identity": {
        "summary": "Pick a stable, deterministic primary identity; use ECID for anonymous stitching.",
        "guidelines": [
            "Primary identity must be stable and unique — avoid email (users change it) or phone as primary unless business requires it. Prefer an internal persistent ID (e.g. ProxyID, MemberID, CRMId).",
            "ECID (Experience Cloud ID) is Adobe's cookie-based anonymous identifier — it should be a secondary identity used for pre-login stitching, never a primary.",
            "Create a custom identity namespace for each business key (e.g. 'LoyaltyID', 'MemberID'). Use a descriptive code in UPPER_SNAKE_CASE.",
            "Namespace type matters: use 'Cross_Device' for person-level IDs, 'Cookie' for device/browser IDs, 'Device' for hardware IDs.",
            "Never store raw PII (SSN, DOB) as an identity field — hash it or use a surrogate key.",
            "Plan for identity graph depth: each profile can have up to 50 identity links. Avoid creating too many device-level namespaces per profile.",
        ],
    },
    "dataset": {
        "summary": "One dataset per schema type; match ingestion mode to data velocity.",
        "guidelines": [
            "Create one dataset per schema — do not reuse a dataset across multiple schemas.",
            "Enable a dataset for Profile ingestion only if its schema is profile-enabled and records are intended for the unified profile.",
            "For batch ingestion (CRM, loyalty, offline): use scheduled batch connectors or direct API upload.",
            "For streaming ingestion (web, mobile, real-time events): use the Streaming Connection / Data Collection endpoint.",
            "Name datasets consistently: '{org}-{domain}-{type}' e.g. 'aetna-loyalty-profile' or 'aetna-web-events'.",
            "Tag test/dev datasets clearly (e.g. prefix 'test-') and set a TTL via Data Hygiene to avoid sandbox pollution.",
            "Avoid ingesting raw un-validated data directly into a profile-enabled dataset — validate schema compliance first.",
        ],
    },
    "offer": {
        "summary": "Structure the offer hierarchy clearly; always define a fallback; keep eligibility rules simple.",
        "guidelines": [
            "AJO Offer Decisioning hierarchy: Placement → Offer (with Representation) → Eligibility Rule → Collection → Decision Activity.",
            "Define one Placement per channel/surface (email, push, web, in-app). Reuse placements across campaigns.",
            "Every Decision Activity must have a Fallback Offer — without it, decisioning fails when no offer qualifies.",
            "Keep eligibility rules simple PQL expressions. Complex rules with many joins degrade decisioning latency.",
            "Use Collections to group related offers (e.g. by tier, by product line) — decisions reference collections, not individual offers.",
            "Set offer priority (0–100) for tie-breaking when multiple offers qualify and no AI ranking model is used.",
            "If using AI ranking (auto-optimisation), ensure sufficient conversion events are flowing before enabling — minimum ~1000 events per offer.",
            "Offer representations (the actual content) must match the placement content type — HTML for web/email, JSON for API, image URL for push.",
            "Publish offers before creating the decision activity — unpublished offers are invisible to the decisioning engine.",
        ],
    },
    "namespace": {
        "summary": "Namespace planning is foundational — get it right before schema design.",
        "guidelines": [
            "Plan all identity namespaces upfront — changing a namespace code after data is ingested is extremely disruptive.",
            "One namespace per business identifier type. Do not overload a namespace (e.g. do not put both email and phone in 'Contact').",
            "Standard Adobe namespaces (ECID, Email, Phone, AAID, IDFA) are available by default — only create custom ones for proprietary IDs.",
            "Namespace codes are case-sensitive and immutable after creation. Use a consistent convention across the org.",
            "Document which namespace is the primary identity for each schema — this drives profile merge and identity graph construction.",
        ],
    },
}

_SCOPE_CHOICES = {"schema", "identity", "namespace", "dataset", "offer"}


def register(mcp) -> None:

    @mcp.tool()
    @track("design_aep_solution")
    def design_aep_solution(
        requirements: str,
        scope: str = "schema,identity,namespace,dataset",
        sandbox: str = "",
    ) -> dict:
        """Design advisor: given business requirements, returns existing sandbox context
        and Adobe best-practice guidelines so Claude can propose a design before
        any implementation begins.

        Always call this BEFORE create_schema / create_dataset / create_segment etc.
        when the user is describing a new capability they want to build.

        Args:
            requirements: Plain-English description of what the user wants to build
                          (e.g. 'loyalty programme tracking Gold/Silver/Bronze members
                          with purchase events and personalised email offers').
            scope: Comma-separated areas to advise on.
                   Options: schema, identity, namespace, dataset, offer.
                   Default: schema,identity,namespace,dataset
            sandbox: Sandbox name (defaults to active profile sandbox).
        """
        try:
            sb = sandbox or None
            scopes = {s.strip().lower() for s in scope.split(",") if s.strip()} & _SCOPE_CHOICES

            context: dict = {}

            # ── Fetch existing sandbox resources ──────────────────────────────

            if "namespace" in scopes or "identity" in scopes:
                ns_resp = aep_get(
                    "/data/core/idnamespace/identities",
                    sandbox=sb,
                )
                namespaces = ns_resp if isinstance(ns_resp, list) else ns_resp.get("namespaces", [])
                context["existing_identity_namespaces"] = [
                    {
                        "name": n.get("name"),
                        "code": n.get("code"),
                        "type": n.get("idType"),
                        "custom": not n.get("shared", True),
                    }
                    for n in namespaces
                    if n.get("code")
                ]

            if "schema" in scopes:
                schema_resp = aep_get(
                    "/data/foundation/schemaregistry/tenant/schemas",
                    sandbox=sb,
                    params={"limit": 50},
                    accept="application/vnd.adobe.xed-id+json",
                )
                context["existing_schemas"] = [
                    {"title": s.get("title"), "id": s.get("$id", "").split("/")[-1]}
                    for s in schema_resp.get("results", [])
                    if not any(
                        p in s.get("title", "").lower()
                        for p in ["adhoc", "ajo ", "channel tracking", "step event"]
                    )
                ]

                fg_resp = aep_get(
                    "/data/foundation/schemaregistry/tenant/fieldgroups",
                    sandbox=sb,
                    params={"limit": 50},
                    accept="application/vnd.adobe.xed-id+json",
                )
                context["existing_field_groups"] = [
                    {"title": fg.get("title"), "id": fg.get("$id", "").split("/")[-1]}
                    for fg in fg_resp.get("results", [])
                ]

            if "dataset" in scopes:
                ds_resp = aep_get(
                    "/data/foundation/catalog/dataSets",
                    sandbox=sb,
                    params={"limit": 50, "properties": "name,description,tags"},
                )
                context["existing_datasets"] = [
                    {"name": v.get("name"), "id": k}
                    for k, v in (ds_resp.items() if isinstance(ds_resp, dict) else {})
                ][:30]

            if "offer" in scopes:
                pl_resp = aep_get("/data/core/dps/placements", sandbox=sb, params={"limit": 20})
                context["existing_placements"] = [
                    {"name": p.get("name"), "id": p.get("id"), "channel": p.get("channel")}
                    for p in pl_resp.get("items", [])
                ]
                coll_resp = aep_get("/data/core/dps/offer-collections", sandbox=sb, params={"limit": 20})
                context["existing_collections"] = [
                    {"name": c.get("name"), "id": c.get("id")}
                    for c in coll_resp.get("items", [])
                ]

            # ── Build best-practice guidelines for requested scopes ───────────

            guidelines = {
                area: _BEST_PRACTICES[area]
                for area in scopes
                if area in _BEST_PRACTICES
            }

            return {
                "requirements": requirements,
                "scope": sorted(scopes),
                "existing_sandbox_context": context,
                "best_practices": guidelines,
                "design_instructions": (
                    "Using the requirements, existing sandbox context, and best practices above, "
                    "propose a concrete design for each scope area. For each component specify: "
                    "(1) what to REUSE from existing resources, "
                    "(2) what to CREATE new, "
                    "(3) key decisions and trade-offs, "
                    "(4) any risks or Adobe-specific gotchas to flag before implementation. "
                    "Do NOT start implementing — present the design for user approval first."
                ),
                "documentation_skills": (
                    "For deeper Adobe documentation on any topic, use the built-in slash skills: "
                    "/aep (XDM, ingestion, profiles, segmentation, Query Service, governance), "
                    "/ajo (journeys, campaigns, offers, decisioning), "
                    "/cja (Customer Journey Analytics, data views, reports), "
                    "/rtcdp (destinations, audience activation, data governance). "
                    "These fetch live content from Adobe Experience League with cited sources."
                ),
            }

        except Exception as exc:
            return {"error": str(exc)}
