"""Data Prep — mapping sets, individual mappings, built-in functions, and expression validation."""

from auth import aep_get, aep_post
from tools.usage_logger import track

_DP = "/data/foundation/conversion"


def register(mcp) -> None:

    # ── Mapping Sets ─────────────────────────────────────────────────────────

    @mcp.tool()
    @track("list_mapping_sets")
    def list_mapping_sets(
        sandbox: str = "",
        limit: int = 20,
        start: int = 0,
        name: str = "",
    ) -> dict:
        """List Data Prep mapping sets.

        Args:
            sandbox: Sandbox name.
            limit: Max records.
            start: Pagination offset.
            name: Optional substring filter on mapping set name.
        """
        try:
            params: dict = {"limit": limit, "start": start}
            if name:
                params["name"] = name
            return aep_get(f"{_DP}/mappingSets", sandbox=sandbox or None, params=params)
        except Exception as exc:
            return {"error": str(exc)}

    @mcp.tool()
    @track("get_mapping_set")
    def get_mapping_set(mapping_set_id: str, sandbox: str = "") -> dict:
        """Get full details for a specific mapping set.

        Args:
            mapping_set_id: Mapping set ID.
            sandbox: Sandbox name.
        """
        try:
            return aep_get(
                f"{_DP}/mappingSets/{mapping_set_id}",
                sandbox=sandbox or None,
            )
        except Exception as exc:
            return {"error": str(exc)}

    @mcp.tool()
    @track("create_mapping_set")
    def create_mapping_set(
        name: str,
        input_schema: dict,
        output_schema: dict,
        mappings: list,
        sandbox: str = "",
    ) -> dict:
        """Create a new Data Prep mapping set.

        Args:
            name: Display name for the mapping set.
            input_schema: JSON Schema object for the source data shape.
            output_schema: JSON Schema object for the target XDM shape.
            mappings: List of mapping objects, each with 'sourceType', 'source',
                      'destination'. Example:
                      [{"sourceType": "ATTRIBUTE", "source": "$.firstName",
                        "destination": "person.name.firstName"}]
            sandbox: Sandbox name.
        """
        try:
            body = {
                "name": name,
                "inputSchema": input_schema,
                "outputSchema": output_schema,
                "mappings": mappings,
            }
            return aep_post(f"{_DP}/mappingSets", body, sandbox=sandbox or None)
        except Exception as exc:
            return {"error": str(exc)}

    # ── Individual Mappings ──────────────────────────────────────────────────

    @mcp.tool()
    @track("list_mappings")
    def list_mappings(
        mapping_set_id: str,
        sandbox: str = "",
        limit: int = 100,
        start: int = 0,
    ) -> dict:
        """List all field mappings within a mapping set.

        Args:
            mapping_set_id: Parent mapping set ID.
            sandbox: Sandbox name.
            limit: Max records.
            start: Pagination offset.
        """
        try:
            return aep_get(
                f"{_DP}/mappingSets/{mapping_set_id}/mappings",
                sandbox=sandbox or None,
                params={"limit": limit, "start": start},
            )
        except Exception as exc:
            return {"error": str(exc)}

    @mcp.tool()
    @track("get_mapping")
    def get_mapping(mapping_set_id: str, mapping_id: str, sandbox: str = "") -> dict:
        """Get details for a specific field mapping within a mapping set.

        Args:
            mapping_set_id: Parent mapping set ID.
            mapping_id: Individual mapping ID.
            sandbox: Sandbox name.
        """
        try:
            return aep_get(
                f"{_DP}/mappingSets/{mapping_set_id}/mappings/{mapping_id}",
                sandbox=sandbox or None,
            )
        except Exception as exc:
            return {"error": str(exc)}

    # ── Built-in Functions ───────────────────────────────────────────────────

    @mcp.tool()
    @track("list_data_prep_functions")
    def list_data_prep_functions(
        sandbox: str = "",
        limit: int = 100,
        start: int = 0,
    ) -> dict:
        """List all built-in Data Prep transformation functions.

        Returns function names, categories, signatures, and descriptions.

        Args:
            sandbox: Sandbox name.
            limit: Max records.
            start: Pagination offset.
        """
        try:
            return aep_get(
                f"{_DP}/functions",
                sandbox=sandbox or None,
                params={"limit": limit, "start": start},
            )
        except Exception as exc:
            return {"error": str(exc)}

    # ── Expression Validation ────────────────────────────────────────────────

    @mcp.tool()
    @track("validate_mapping_expression")
    def validate_mapping_expression(
        expression: str,
        input_schema: dict,
        sandbox: str = "",
    ) -> dict:
        """Validate a Data Prep mapping expression against an input schema.

        Use this to check expressions like 'toUpperCase($.email)' before saving.

        Args:
            expression: Data Prep expression string to validate.
            input_schema: JSON Schema of the source record.
            sandbox: Sandbox name.
        """
        try:
            body = {
                "expression": expression,
                "inputSchema": input_schema,
            }
            return aep_post(f"{_DP}/validate", body, sandbox=sandbox or None)
        except Exception as exc:
            return {"error": str(exc)}

    # ── Mapping Set Previews ─────────────────────────────────────────────────

    @mcp.tool()
    @track("preview_mapping_set")
    def preview_mapping_set(
        mapping_set_id: str,
        sample_data: dict,
        sandbox: str = "",
    ) -> dict:
        """Preview the output of a mapping set applied to a sample source record.

        Args:
            mapping_set_id: Mapping set to test.
            sample_data: A single source record dict to run through the mapping.
            sandbox: Sandbox name.
        """
        try:
            body = {"data": [sample_data], "mappingSetId": mapping_set_id}
            return aep_post(f"{_DP}/preview", body, sandbox=sandbox or None)
        except Exception as exc:
            return {"error": str(exc)}
