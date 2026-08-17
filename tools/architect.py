"""
Architect-phase delivery asset generators.

Fetches live sandbox context and returns pre-populated consulting templates:
  - generate_data_layer_spec  → Experience Data-Layer Specification
  - generate_journey_canvas   → AJO Journey Design Canvas
"""

from auth import aep_get
from tools.usage_logger import track


def register(mcp) -> None:

    # ── Experience Data-Layer Specification ──────────────────────────────────

    @mcp.tool()
    @track("generate_data_layer_spec")
    def generate_data_layer_spec(sandbox: str = "") -> dict:
        """Generate a pre-populated Experience Data-Layer Specification document.

        Fetches existing schemas, identity namespaces, identity descriptors, field
        groups, and datasets from the sandbox and returns a filled-in Markdown
        template ready for the analyst/engineer to complete.

        Args:
            sandbox: Sandbox name (defaults to active profile sandbox).
        """
        try:
            sb = sandbox or None

            # ── Fetch live platform data ─────────────────────────────────────

            ns_resp = aep_get("/data/core/idnamespace/identities", sandbox=sb)
            namespaces = ns_resp if isinstance(ns_resp, list) else ns_resp.get("namespaces", [])
            custom_ns = [n for n in namespaces if not n.get("shared", True) and n.get("code")]
            standard_ns = [n for n in namespaces if n.get("shared", True) and n.get("code")
                           and n["code"] in ("ECID", "Email", "Phone", "AAID", "IDFA", "GAID")]

            schema_resp = aep_get(
                "/data/foundation/schemaregistry/tenant/schemas",
                sandbox=sb,
                params={"limit": 50},
                accept="application/vnd.adobe.xed-id+json",
            )
            schemas = [
                s for s in schema_resp.get("results", [])
                if not any(p in s.get("title", "").lower()
                           for p in ["adhoc", "ajo ", "channel tracking", "step event"])
            ]

            desc_resp = aep_get(
                "/data/foundation/schemaregistry/tenant/descriptors",
                sandbox=sb,
                params={"property": "xdm:descriptorType==xdm:descriptorIdentity", "limit": 100},
            )
            descriptors = desc_resp.get("results", desc_resp) if isinstance(desc_resp, dict) else desc_resp

            fg_resp = aep_get(
                "/data/foundation/schemaregistry/tenant/fieldgroups",
                sandbox=sb,
                params={"limit": 50},
                accept="application/vnd.adobe.xed-id+json",
            )
            field_groups = fg_resp.get("results", [])

            ds_resp = aep_get(
                "/data/foundation/catalog/dataSets",
                sandbox=sb,
                params={"limit": 50, "properties": "name,description,schemaRef,tags"},
            )
            datasets = [
                {"id": k, "name": v.get("name", ""), "schema": v.get("schemaRef", {}).get("id", "").split("/")[-1],
                 "profile_enabled": bool((v.get("tags") or {}).get("unifiedProfile"))}
                for k, v in (ds_resp.items() if isinstance(ds_resp, dict) else {})
            ][:30]

            active_sandbox = sandbox or "active profile sandbox"

            # ── Build identity rows ──────────────────────────────────────────

            def _ns_id_row(ns):
                return (f"| {ns.get('name')} | {ns.get('code')} | {ns.get('id', '—')} "
                        f"| [ source ] | [ ] | identityMap.{ns.get('code')} | [ ] |")

            # Find primary identity fields from descriptors
            primary_fields = {}
            for d in (descriptors if isinstance(descriptors, list) else []):
                if d.get("xdm:isPrimary") and d.get("xdm:sourceSchema"):
                    schema_id = d["xdm:sourceSchema"].split("/")[-1]
                    primary_fields[schema_id] = d.get("xdm:sourceProperty", "—")

            identity_rows = "\n".join([
                f"| ECID | ECID | (auto) | Web SDK | No | identityMap.ECID | device identity |"
            ] + [_ns_id_row(n) for n in custom_ns[:8]])

            # ── Build schema rows ────────────────────────────────────────────

            schema_rows = "\n".join(
                f"| {s.get('title')} | {s.get('$id', '').split('/')[-1]} | [ ] | [ ] |"
                for s in schemas[:15]
            )

            # ── Build dataset rows ───────────────────────────────────────────

            dataset_rows = "\n".join(
                f"| {d['name']} | {d['id']} | {d['schema']} | [ ingestion method ] | [ ] | {'profile-enabled' if d['profile_enabled'] else '—'} |"
                for d in datasets[:15]
            )

            # ── Build field group rows ────────────────────────────────────────

            fg_rows = "\n".join(
                f"| {fg.get('title')} | {fg.get('$id', '').split('/')[-1]} |"
                for fg in field_groups[:10]
            )

            # ── Assemble markdown ────────────────────────────────────────────

            md = f"""# Experience Data-Layer Specification

The contract that makes measurement and personalization trustworthy: what events fire, what data they
carry, how it maps to XDM, how it's collected via Adobe Tags / Web SDK, and how identity and
consent are handled.

> Generated from sandbox **{active_sandbox}**. Bracketed fields `[ ]` require manual input.

---

## 1. Collection approach

| Field | Value |
|---|---|
| Collection method | [ Web SDK (alloy) / Adobe Tags ] |
| Data layer | [ Adobe Client Data Layer / custom ] |
| Properties in scope | [ sites / apps ] |
| Datastream / edge config | [ ] |
| AEP sandbox (dev) | {active_sandbox} |
| AEP sandbox (prod) | [ prod sandbox name ] |
| Environments | [ dev / stage / prod ] |

---

## 2. Event taxonomy

| Event | Trigger | Page/scope | Key data elements | XDM field group | XDM schema | Notes |
|---|---|---|---|---|---|---|
| pageView | [page load] | [all] | [pageName, section, locale] | [web.webPageDetails] | [ ] | [ ] |
| productView | [PDP load] | [product] | [productId, price, category] | [commerce / custom] | [ ] | [ ] |
| addToCart | [click] | [product/cart] | [productId, qty] | [commerce.productListAdds] | [ ] | [ ] |
| formSubmit | [submit] | [lead] | [formId, consent] | [custom] | [ ] | [ ] |
| [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |

---

## 3. Data elements

| Data element | Source (DOM / data layer / var) | Type | Example | Required |
|---|---|---|---|---|
| pageName | [data layer] | string | [home] | Yes |
| productId | [data layer] | string | [SKU123] | Conditional |
| userAuthState | [data layer] | enum | [auth / anon] | Yes |
| [ ] | [ ] | [ ] | [ ] | [ ] |

---

## 4. Identity namespaces

**Custom namespaces in this sandbox:**

| Identity | Namespace code | Namespace ID | Source | Primary? | XDM path | Notes |
|---|---|---|---|---|---|---|
{identity_rows}

**Standard namespaces available:** {', '.join(n['code'] for n in standard_ns)}

---

## 5. Consent

- **Consent mechanism:** [CMP / Adobe Consent Service]
- **Consent signals captured:** [collect, personalize, share/ads]
- **XDM consent field group:** [field group name / schema path]
- **Enforcement points:** [collection, AEP audiences, AJO journeys, activation destinations]
- **Default state (pre-consent):** [ ]

---

## 6. XDM schemas in sandbox

| Schema title | Schema ID | Class | Profile-enabled |
|---|---|---|---|
{schema_rows}

**Custom field groups available:**

| Field group | ID |
|---|---|
{fg_rows if fg_rows else "| (none yet) | — |"}

---

## 7. XDM mapping summary

| Data element | XDM schema | Field group | Field path |
|---|---|---|---|
| pageName | [ ] | web.webPageDetails | web.webPageDetails.name |
| productId | [ ] | [ ] | [ ] |
| userId (CRM) | [ ] | identityMap | identityMap.[namespace][0].id |
| [ ] | [ ] | [ ] | [ ] |

---

## 8. AEP datasets

| Dataset name | Dataset ID | Schema | Ingestion method | Frequency | Notes |
|---|---|---|---|---|---|
{dataset_rows if dataset_rows else "| (none yet) | — | — | — | — | — |"}

---

## 9. Validation checklist

- [ ] Every event maps to an XDM field group; no orphan fields.
- [ ] Single collection path (Web SDK) confirmed; no duplicate legacy beacons.
- [ ] Identity namespaces populated and stitching validated.
- [ ] Primary identity descriptor set on each schema.
- [ ] Consent captured and enforced at every downstream point.
- [ ] Datasets created and profile-enabled for real-time schemas.
- [ ] Instrumentation validated in stage against this spec before launch.
- [ ] Merge policies reviewed for each sandbox.
"""

            return {
                "markdown": md,
                "sandbox": active_sandbox,
                "schema_count": len(schemas),
                "namespace_count": len(custom_ns),
                "dataset_count": len(datasets),
                "instructions": (
                    "Complete sections 2 (event taxonomy), 3 (data elements), 5 (consent), "
                    "and 7 (XDM mapping). Sections 4, 6, and 8 are pre-populated from your sandbox."
                ),
            }

        except Exception as exc:
            return {"error": str(exc)}

    # ── AJO Journey Design Canvas ────────────────────────────────────────────

    @mcp.tool()
    @track("generate_journey_canvas")
    def generate_journey_canvas(
        journey_id: str = "",
        sandbox: str = "",
    ) -> dict:
        """Generate a pre-populated AJO Journey Design Canvas document.

        Fetches existing segments, journeys, offers, collections, placements,
        ranking formulas, and merge policies from the sandbox and returns a
        filled-in Markdown canvas ready for the journey architect to complete.

        Args:
            journey_id: Optional AJO journey ID to pre-fill journey identity fields.
            sandbox: Sandbox name (defaults to active profile sandbox).
        """
        try:
            sb = sandbox or None
            active_sandbox = sandbox or "active profile sandbox"

            # ── Fetch live platform data ─────────────────────────────────────

            seg_resp = aep_get(
                "/data/core/ups/segment/definitions",
                sandbox=sb,
                params={"limit": 30},
            )
            segments = seg_resp.get("children", seg_resp.get("segments", []))

            journeys_resp = aep_get(
                "/authoring/journeys",
                sandbox=sb,
                params={"limit": 20},
            )
            journeys = journeys_resp.get("content", journeys_resp) if isinstance(journeys_resp, dict) else journeys_resp

            journey_detail = {}
            if journey_id:
                journey_detail = aep_get(f"/authoring/journeys/{journey_id}", sandbox=sb)

            offers_resp = aep_get("/data/core/dps/offers", sandbox=sb, params={"limit": 20})
            offers = offers_resp.get("items", [])

            collections_resp = aep_get("/data/core/dps/offer-collections", sandbox=sb, params={"limit": 20})
            collections = collections_resp.get("items", [])

            placements_resp = aep_get("/data/core/dps/placements", sandbox=sb, params={"limit": 20})
            placements = placements_resp.get("items", [])

            ranking_resp = aep_get("/data/core/dps/ranking-formulas", sandbox=sb, params={"limit": 10})
            rankings = ranking_resp.get("items", [])

            mp_resp = aep_get("/data/core/ups/config/mergePolicies", sandbox=sb, params={"limit": 10})
            merge_policies = mp_resp.get("children", [])

            # ── Build list blocks ────────────────────────────────────────────

            def _bullet_list(items, name_key="name", id_key="id", limit=10):
                if not items:
                    return "  _(none found in sandbox)_"
                return "\n".join(
                    f"  - **{i.get(name_key, '—')}** `{i.get(id_key, '')}`"
                    for i in items[:limit]
                )

            seg_list = _bullet_list(
                [{"name": s.get("name"), "id": s.get("id")} for s in segments], limit=10
            )
            journey_list = _bullet_list(
                [{"name": j.get("name"), "id": j.get("uid", j.get("id", ""))} for j in (journeys if isinstance(journeys, list) else [])],
                limit=8,
            )
            offer_list = _bullet_list(offers, limit=10)
            collection_list = _bullet_list(collections, limit=8)
            placement_list = _bullet_list(placements, limit=8)
            ranking_list = _bullet_list(rankings, limit=5)
            mp_list = _bullet_list(
                [{"name": m.get("name"), "id": m.get("id")} for m in merge_policies], limit=5
            )

            # Journey identity fields (if a journey_id was provided)
            jname = journey_detail.get("name", "[ journey name ]") if journey_detail else "[ journey name ]"
            jid_val = journey_id or "[ — run get_journey after creation ]"
            jstatus = journey_detail.get("status", "[ ]") if journey_detail else "[ ]"

            md = f"""# AJO Journey Design Canvas

A one-page design for an Adobe Journey Optimizer journey or campaign: who enters, what they
experience across channels, how decisioning and consent gate it, and how success is measured.

> Generated from sandbox **{active_sandbox}**. Bracketed fields `[ ]` require manual input.

---

## 1. Journey identity

| Field | Value |
|---|---|
| Journey name | {jname} |
| Objective / hypothesis | [ if we … then [metric] improves by [target] ] |
| Type | [ triggered / batch / recurring ] |
| AJO journey ID | {jid_val} |
| Status | {jstatus} |
| Owner | [ ] |
| Primary KPI & baseline | [ conversion / engagement; current value ] |
| Target sandbox | {active_sandbox} |

---

## 2. Audience & entry

**Available RT-CDP segments in this sandbox:**

{seg_list}

| Aspect | Definition |
|---|---|
| Entry audience (RT-CDP segment) | [ pick from list above ] |
| Entry event / trigger | [ event qualification / segment membership ] |
| Eligibility / consent gate | [ required consent signals — collect, personalize ] |
| Suppression rules | [ frequency caps, exclusion segments ] |
| Expected volume | [ ] |

---

## 3. Journey steps

| Step | Channel | Message / action | Wait / timing | Decision / branch | Consent check |
|---|---|---|---|---|---|
| 1 | [email] | [welcome] | [immediate] | [opened? Y/N] | [marketing] |
| 2 | [push] | [reminder] | [+48h if no open] | [ ] | [push] |
| 3 | [web / in-app] | [personalized offer] | [on next visit] | [decisioning: next-best-offer] | [personalize] |
| 4 | [ ] | [ ] | [ ] | [ ] | [ ] |

**Existing journeys for reference:**

{journey_list}

---

## 4. Decisioning / personalization

**Available offers:**

{offer_list}

**Collections:**

{collection_list}

**Placements:**

{placement_list}

**Ranking formulas:**

{ranking_list}

| Field | Value |
|---|---|
| Decision logic | [next-best-experience / offer ranking / rules / AI model] |
| Inputs (profile / computed attributes) | [ ] |
| Offer collection | [ pick from list above ] |
| Placement | [ pick from list above ] |
| Ranking formula | [ pick from list above, or rules-based ] |
| Fallback experience | [ ] |

---

## 5. Exit & guardrails

**Merge policies:**

{mp_list}

- **Goal / exit condition:** [conversion event / journey complete]
- **Frequency / fatigue rules:** [ ]
- **Hard stops:** [unsubscribe, consent withdrawal, complaint]
- **Profile merge policy used:** [ pick from list above ]

---

## 6. Measurement

| Metric | Definition | Target | Source |
|---|---|---|---|
| Entry → conversion rate | [ ] | [ ] | [CJA / AJO reporting] |
| Channel engagement (open/click) | [ ] | [ ] | [AJO / CJA] |
| Personalization lift | [vs. control / holdout] | [ ] | [Target / CJA] |
| Unsubscribe / complaint rate | [ ] | [low] | [ ] |

---

## 7. Launch checklist

- [ ] Audience segment validated and profile-enabled.
- [ ] Consent gates configured and enforced at channel and audience level.
- [ ] All messages QA'd — content, links, rendering, personalization tokens.
- [ ] Frequency/suppression and exit rules configured.
- [ ] Offers published and decision activity live.
- [ ] Measurement instrumented; control/holdout defined where used.
- [ ] Journey activated in AJO and status confirmed.
"""

            return {
                "markdown": md,
                "sandbox": active_sandbox,
                "segment_count": len(segments),
                "offer_count": len(offers),
                "collection_count": len(collections),
                "instructions": (
                    "Complete sections 1 (objective, type, owner, KPI), 2 (entry audience, trigger, consent), "
                    "3 (journey steps), 4 (decision logic inputs), 5 (exit conditions), and 6 (measurement targets). "
                    "Sections 2, 4, and 5 are pre-populated with live sandbox objects."
                ),
            }

        except Exception as exc:
            return {"error": str(exc)}
