"""AEP XDM Schema Registry tools — schemas, classes, field groups, data types."""

import urllib.parse
from typing import Optional

from auth import aep_get, aep_post, aep_patch
from tools.usage_logger import track

# Schema Registry uses versioned Accept headers for full schema payloads.
_ACCEPT_LIST = "application/vnd.adobe.xed-id+json"
_ACCEPT_FULL = "application/vnd.adobe.xed+json;version=1"
_ACCEPT_FULL_EXT = "application/vnd.adobe.xed-full+json;version=1"


def register(mcp) -> None:

    @mcp.tool()
    @track("list_schemas")
    def list_schemas(
        container: str = "tenant",
        sandbox: str = "",
        limit: int = 20,
        start: str = "",
        full: bool = False,
    ) -> dict:
        """List XDM schemas in the Schema Registry.

        Args:
            container: 'tenant' (custom schemas) or 'global' (system schemas).
            sandbox: Sandbox name.
            limit: Max records to return.
            start: Pagination cursor (orderby value of last item).
            full: Return full schema definitions instead of just IDs/titles.
        """
        try:
            params: dict = {"limit": limit}
            if start:
                params["start"] = start
            accept = _ACCEPT_FULL if full else _ACCEPT_LIST
            return aep_get(
                f"/data/foundation/schemaregistry/{container}/schemas",
                sandbox=sandbox or None,
                params=params,
                accept=accept,
            )
        except Exception as exc:
            return {"error": str(exc)}

    @mcp.tool()
    @track("get_schema")
    def get_schema(schema_id: str, sandbox: str = "", full: bool = True) -> dict:
        """Get a specific XDM schema by its $id or meta:altId.

        Args:
            schema_id: The schema $id URL or meta:altId (will be URL-encoded).
            sandbox: Sandbox name.
            full: If True, return the full expanded schema (default True).
        """
        try:
            encoded = urllib.parse.quote(schema_id, safe="")
            accept = _ACCEPT_FULL_EXT if full else _ACCEPT_FULL
            return aep_get(
                f"/data/foundation/schemaregistry/tenant/schemas/{encoded}",
                sandbox=sandbox or None,
                accept=accept,
            )
        except Exception as exc:
            return {"error": str(exc)}

    @mcp.tool()
    @track("list_classes")
    def list_classes(
        container: str = "tenant",
        sandbox: str = "",
        limit: int = 20,
        full: bool = False,
    ) -> dict:
        """List XDM classes in the Schema Registry.

        Args:
            container: 'tenant' or 'global'.
            sandbox: Sandbox name.
            limit: Max records.
            full: Return full class definitions.
        """
        try:
            accept = _ACCEPT_FULL if full else _ACCEPT_LIST
            return aep_get(
                f"/data/foundation/schemaregistry/{container}/classes",
                sandbox=sandbox or None,
                params={"limit": limit},
                accept=accept,
            )
        except Exception as exc:
            return {"error": str(exc)}

    @mcp.tool()
    @track("list_field_groups")
    def list_field_groups(
        container: str = "tenant",
        sandbox: str = "",
        limit: int = 20,
        full: bool = False,
    ) -> dict:
        """List XDM field groups (mixins) in the Schema Registry.

        Args:
            container: 'tenant' or 'global'.
            sandbox: Sandbox name.
            limit: Max records.
            full: Return full field group definitions.
        """
        try:
            accept = _ACCEPT_FULL if full else _ACCEPT_LIST
            return aep_get(
                f"/data/foundation/schemaregistry/{container}/fieldgroups",
                sandbox=sandbox or None,
                params={"limit": limit},
                accept=accept,
            )
        except Exception as exc:
            return {"error": str(exc)}

    @mcp.tool()
    @track("get_field_group")
    def get_field_group(field_group_id: str, sandbox: str = "") -> dict:
        """Get a specific XDM field group by its $id or meta:altId.

        Args:
            field_group_id: The field group $id URL or meta:altId.
            sandbox: Sandbox name.
        """
        try:
            encoded = urllib.parse.quote(field_group_id, safe="")
            return aep_get(
                f"/data/foundation/schemaregistry/tenant/fieldgroups/{encoded}",
                sandbox=sandbox or None,
                accept=_ACCEPT_FULL_EXT,
            )
        except Exception as exc:
            return {"error": str(exc)}

    @mcp.tool()
    @track("list_data_types")
    def list_data_types(
        container: str = "tenant",
        sandbox: str = "",
        limit: int = 20,
    ) -> dict:
        """List XDM data types in the Schema Registry.

        Args:
            container: 'tenant' or 'global'.
            sandbox: Sandbox name.
            limit: Max records.
        """
        try:
            return aep_get(
                f"/data/foundation/schemaregistry/{container}/datatypes",
                sandbox=sandbox or None,
                params={"limit": limit},
                accept=_ACCEPT_LIST,
            )
        except Exception as exc:
            return {"error": str(exc)}

    @mcp.tool()
    @track("list_descriptors")
    def list_descriptors(sandbox: str = "") -> dict:
        """List schema descriptors (relationships, identities, etc.) for the tenant.

        Note: the descriptors endpoint does not accept a `limit` query param
        (returns 400 if passed), so all descriptors are returned.

        Args:
            sandbox: Sandbox name.
        """
        try:
            return aep_get(
                "/data/foundation/schemaregistry/tenant/descriptors",
                sandbox=sandbox or None,
                accept="application/vnd.adobe.xdm-v2+json",
            )
        except Exception as exc:
            return {"error": str(exc)}

    # ── Creation tools ─────────────────────────────────────────────────────────

    @mcp.tool()
    @track("create_field_group")
    def create_field_group(
        title: str,
        properties: dict,
        description: str = "",
        intended_class: str = "https://ns.adobe.com/xdm/context/profile",
        sandbox: str = "",
    ) -> dict:
        """Create a new XDM field group (mixin) in the tenant container.

        Args:
            title: Field group display name.
            properties: The JSON Schema `properties` object for the field group.
                Custom fields must be nested under the org's tenant namespace key,
                e.g. {"_myorg": {"type": "object", "properties": {...}}}.
            description: Optional description.
            intended_class: Class $id the field group is meant to extend
                (default: Individual Profile).
            sandbox: Sandbox name.
        """
        try:
            body = {
                "type": "object",
                "title": title,
                "description": description,
                "meta:intendedToExtend": [intended_class],
                "allOf": [{"properties": properties}],
            }
            return aep_post(
                "/data/foundation/schemaregistry/tenant/fieldgroups",
                body,
                sandbox=sandbox or None,
                accept=_ACCEPT_FULL,
            )
        except Exception as exc:
            return {"error": str(exc)}

    @mcp.tool()
    @track("create_schema")
    def create_schema(
        title: str,
        field_group_ids: list,
        description: str = "",
        base_class: str = "https://ns.adobe.com/xdm/context/profile",
        sandbox: str = "",
    ) -> dict:
        """Create a new XDM schema in the tenant container.

        Args:
            title: Schema display name.
            field_group_ids: List of field group $id URLs to compose into the schema.
            description: Optional description.
            base_class: Class $id the schema is built on (default: Individual Profile).
            sandbox: Sandbox name.
        """
        try:
            all_of = [{"$ref": base_class}] + [{"$ref": fg} for fg in field_group_ids]
            body = {
                "type": "object",
                "title": title,
                "description": description or title,
                "allOf": all_of,
                "meta:class": base_class,
            }
            return aep_post(
                "/data/foundation/schemaregistry/tenant/schemas",
                body,
                sandbox=sandbox or None,
                accept=_ACCEPT_FULL,
            )
        except Exception as exc:
            return {"error": str(exc)}

    @mcp.tool()
    @track("create_descriptor")
    def create_descriptor(descriptor: dict, sandbox: str = "") -> dict:
        """Create a schema descriptor (identity, relationship, etc.).

        For a primary identity descriptor, pass:
            {
              "@type": "xdm:descriptorIdentity",
              "xdm:sourceSchema": "<schema $id>",
              "xdm:sourceVersion": 1,
              "xdm:sourceProperty": "/_tenant/fieldName",
              "xdm:namespace": "Email",
              "xdm:property": "xdm:code",
              "xdm:isPrimary": true
            }

        Args:
            descriptor: The full descriptor object.
            sandbox: Sandbox name.
        """
        try:
            return aep_post(
                "/data/foundation/schemaregistry/tenant/descriptors",
                descriptor,
                sandbox=sandbox or None,
            )
        except Exception as exc:
            return {"error": str(exc)}

    @mcp.tool()
    @track("enable_schema_for_profile")
    def enable_schema_for_profile(schema_id: str, sandbox: str = "") -> dict:
        """Enable a schema for Real-Time Customer Profile (adds the union meta tag).

        Args:
            schema_id: The schema $id URL or meta:altId.
            sandbox: Sandbox name.
        """
        try:
            encoded = urllib.parse.quote(schema_id, safe="")
            patches = [
                {
                    "op": "add",
                    "path": "/meta:immutableTags",
                    "value": ["union"],
                }
            ]
            return aep_patch(
                f"/data/foundation/schemaregistry/tenant/schemas/{encoded}",
                patches,
                sandbox=sandbox or None,
                content_type="application/json",
                accept=_ACCEPT_FULL,
            )
        except Exception as exc:
            return {"error": str(exc)}
