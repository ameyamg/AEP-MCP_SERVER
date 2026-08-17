"""ERD generation tool — produces Mermaid erDiagram syntax from AEP XDM schemas."""

import re
import urllib.parse

from auth import aep_get
from tools.usage_logger import track

_ACCEPT_LIST = "application/vnd.adobe.xed-id+json"
_ACCEPT_FULL = "application/vnd.adobe.xed-full+json;version=1"

# Title patterns that identify auto-generated / system schemas to skip
_SKIP_PATTERNS = [
    r"^adhoc xdm schema",
    r"^ajo\b",
    r"\bajo\b.*schema",
    r"channel tracking",
    r"journey.*step.*event",
    r"feedback message event",
    r"decision event",
    r"journeyversion",
    r"^jo[a-z]",
]
_SKIP_RE = re.compile("|".join(_SKIP_PATTERNS), re.IGNORECASE)

# XDM type → Mermaid type
_TYPE_MAP = {
    "string": "string",
    "integer": "int",
    "number": "float",
    "boolean": "boolean",
    "array": "array",
    "object": "object",
}

# Top-level XDM/system fields to always exclude from display
_SKIP_FIELDS = {"_id", "timestamp", "eventType", "identityMap", "repositoryCreatedBy",
                "repositoryLastModifiedBy", "createdByBatchID", "modifiedByBatchID"}


def _safe_name(title: str) -> str:
    """Make a schema title safe for Mermaid identifiers."""
    name = re.sub(r"[^a-zA-Z0-9]", "_", title)
    name = re.sub(r"_+", "_", name).strip("_")
    return name[:50]


def _mermaid_type(field_def: dict) -> str:
    fmt = field_def.get("format", "")
    if fmt in ("date-time", "date"):
        return "datetime"
    return _TYPE_MAP.get(field_def.get("type", ""), "string")


def _is_system_schema(title: str) -> bool:
    return bool(_SKIP_RE.search(title))


def _extract_fields(
    properties: dict,
    pk_fields: set,
    fk_fields: set,
    tenant_id: str,
    max_fields: int,
) -> list[tuple[str, str, str]]:
    """Return list of (mermaid_type, field_name, marker) tuples."""
    results = []

    # Flatten tenant namespace fields one level up for display
    tenant_props = {}
    if tenant_id and tenant_id in properties:
        tenant_def = properties[tenant_id]
        tenant_props = tenant_def.get("properties", {})

    def _add(fname: str, fdef: dict, marker: str) -> None:
        if len(results) >= max_fields:
            return
        if fdef.get("type") in ("object", "array") and not marker:
            return
        results.append((_mermaid_type(fdef), fname, marker))

    # PKs first
    for fname, fdef in {**properties, **tenant_props}.items():
        if fname in _SKIP_FIELDS or fname.startswith("_") or ":" in fname:
            continue
        if fname in pk_fields:
            _add(fname, fdef, "PK")

    # FKs second
    for fname, fdef in {**properties, **tenant_props}.items():
        if fname in _SKIP_FIELDS or fname.startswith("_") or ":" in fname:
            continue
        if fname in fk_fields and fname not in pk_fields:
            _add(fname, fdef, "FK")

    # Regular fields
    for fname, fdef in {**properties, **tenant_props}.items():
        if len(results) >= max_fields:
            break
        if fname in _SKIP_FIELDS or fname.startswith("_") or ":" in fname:
            continue
        if fname in pk_fields or fname in fk_fields:
            continue
        if fdef.get("type") == "object":
            continue
        _add(fname, fdef, "")

    return results


def register(mcp) -> None:

    @mcp.tool()
    @track("generate_schema_erd")
    def generate_schema_erd(
        schema_ids: str = "",
        profile_only: bool = True,
        max_fields: int = 15,
        sandbox: str = "",
    ) -> dict:
        """Generate a Mermaid ERD diagram from AEP XDM schemas.

        Returns Mermaid erDiagram syntax Claude can render directly.
        Skips auto-generated AJO, adhoc, and system schemas automatically.

        Args:
            schema_ids: Comma-separated schema $id or altId values for specific schemas.
                        Leave empty to auto-discover schemas in the sandbox.
            profile_only: When True (default), only includes Real-Time Profile-enabled schemas.
                          Set to False to include ExperienceEvent and Lookup schemas too.
            max_fields: Max fields shown per entity box (default 15). PK/FK always included.
            sandbox: Sandbox name (defaults to active profile sandbox).
        """
        try:
            sb = sandbox or None
            schemas_data: list[dict] = []

            if schema_ids.strip():
                # Fetch specific schemas by ID
                for sid in [s.strip() for s in schema_ids.split(",") if s.strip()]:
                    enc = urllib.parse.quote(sid, safe="")
                    s = aep_get(
                        f"/data/foundation/schemaregistry/tenant/schemas/{enc}",
                        sandbox=sb,
                        accept=_ACCEPT_FULL,
                    )
                    if "properties" in s:
                        schemas_data.append(s)
            else:
                # Auto-discover from sandbox
                resp = aep_get(
                    "/data/foundation/schemaregistry/tenant/schemas",
                    sandbox=sb,
                    params={"limit": 100},
                    accept=_ACCEPT_LIST,
                )
                for entry in resp.get("results", []):
                    title = entry.get("title", "")
                    if _is_system_schema(title):
                        continue

                    sid = entry.get("$id") or entry.get("meta:altId", "")
                    if not sid:
                        continue

                    enc = urllib.parse.quote(sid, safe="")
                    full = aep_get(
                        f"/data/foundation/schemaregistry/tenant/schemas/{enc}",
                        sandbox=sb,
                        accept=_ACCEPT_FULL,
                    )
                    if "error" in full or "properties" not in full:
                        continue

                    if profile_only:
                        tags = full.get("meta:immutableTags", [])
                        if not any("union" in t for t in tags):
                            continue

                    schemas_data.append(full)

            if not schemas_data:
                return {
                    "error": "No schemas found. Try profile_only=False to include non-profile schemas, "
                             "or pass specific schema_ids."
                }

            # Fetch descriptors for identities and relationships
            desc_resp = aep_get(
                "/data/foundation/schemaregistry/tenant/descriptors",
                sandbox=sb,
                params={"limit": 500},
            )
            descriptors = desc_resp.get("results", [])

            # Build identity map: schema $id → set of identity field names (PKs)
            pk_map: dict[str, set] = {}
            for d in descriptors:
                if d.get("@type") == "xdm:descriptorIdentity":
                    src = d.get("xdm:sourceSchema", "")
                    field = d.get("xdm:sourceProperty", "").lstrip("/").split("/")[-1]
                    pk_map.setdefault(src, set()).add(field)

            # Relationship descriptors
            rel_descs = [d for d in descriptors if d.get("@type") == "xdm:descriptorRelationship"]

            # Build FK map: schema $id → set of FK field names
            fk_map: dict[str, set] = {}
            for d in rel_descs:
                src = d.get("xdm:sourceSchema", "")
                field = d.get("xdm:sourceProperty", "").lstrip("/").split("/")[-1]
                fk_map.setdefault(src, set()).add(field)

            # Map schema $id → safe Mermaid name (for relationship lines)
            id_to_name = {
                s.get("$id", ""): _safe_name(s.get("title", "Unknown"))
                for s in schemas_data
            }

            # Generate Mermaid
            lines = ["erDiagram"]

            for schema in schemas_data:
                schema_id = schema.get("$id", "")
                title = schema.get("title", schema_id)
                entity = _safe_name(title)
                properties = schema.get("properties", {})
                tenant_id = schema.get("meta:tenantNamespace", "").lstrip("_")
                tenant_key = f"_{tenant_id}" if tenant_id else ""

                fields = _extract_fields(
                    properties,
                    pk_map.get(schema_id, set()),
                    fk_map.get(schema_id, set()),
                    tenant_key,
                    max_fields,
                )

                lines.append(f"    {entity} {{")
                if fields:
                    for ftype, fname, marker in fields:
                        suffix = f" {marker}" if marker else ""
                        lines.append(f"        {ftype} {fname}{suffix}")
                else:
                    lines.append(f"        string id PK")
                lines.append("    }")

            # Add relationship lines
            included_ids = set(id_to_name.keys())
            for d in rel_descs:
                src_id = d.get("xdm:sourceSchema", "")
                dst_id = d.get("xdm:destinationSchema", "")
                label = d.get("xdm:label", "relates_to").replace(" ", "_")
                if src_id in included_ids and dst_id in included_ids:
                    lines.append(
                        f'    {id_to_name[src_id]} }}o--|| {id_to_name[dst_id]} : "{label}"'
                    )

            return {
                "mermaid": "\n".join(lines),
                "schema_count": len(schemas_data),
                "schemas_included": [s.get("title", s.get("$id", "")) for s in schemas_data],
                "tip": "Ask Claude to render this as a Mermaid diagram, or paste the 'mermaid' value into mermaid.live",
            }

        except Exception as exc:
            return {"error": str(exc)}
