"""Computed Attributes — profile-level aggregated attributes derived from event data."""

from auth import aep_get, aep_post, aep_patch
from tools.usage_logger import track

_CA = "/data/core/ups/config/computedAttributes"


def register(mcp) -> None:

    @mcp.tool()
    @track("list_computed_attributes")
    def list_computed_attributes(
        sandbox: str = "",
        limit: int = 20,
        start: int = 0,
        status: str = "",
    ) -> dict:
        """List computed attribute definitions in the sandbox.

        Computed attributes are profile-level aggregations derived from
        ExperienceEvent data (e.g. 'total purchase amount last 30 days').

        Args:
            sandbox: Sandbox name.
            limit: Max records.
            start: Pagination offset.
            status: Filter by status (NEW, PROCESSING, PROCESSED, FAILED, DISABLED).
        """
        try:
            params: dict = {"limit": limit, "start": start}
            if status:
                params["status"] = status
            return aep_get(_CA, sandbox=sandbox or None, params=params)
        except Exception as exc:
            return {"error": str(exc)}

    @mcp.tool()
    @track("get_computed_attribute")
    def get_computed_attribute(attribute_id: str, sandbox: str = "") -> dict:
        """Get a specific computed attribute definition.

        Args:
            attribute_id: Computed attribute ID.
            sandbox: Sandbox name.
        """
        try:
            return aep_get(f"{_CA}/{attribute_id}", sandbox=sandbox or None)
        except Exception as exc:
            return {"error": str(exc)}

    @mcp.tool()
    @track("create_computed_attribute")
    def create_computed_attribute(
        name: str,
        display_name: str,
        description: str,
        expression: str,
        duration_unit: str,
        duration_value: int,
        sandbox: str = "",
    ) -> dict:
        """Create a new computed attribute definition.

        Args:
            name: Internal name (alphanumeric, no spaces).
            display_name: Human-readable label.
            description: Purpose / documentation string.
            expression: PQL expression that aggregates ExperienceEvent fields.
                        Example: 'sum(commerce.order.priceTotal)'
            duration_unit: Lookback window unit — DAYS, WEEKS, or MONTHS.
            duration_value: Number of units in the lookback window.
            sandbox: Sandbox name.
        """
        try:
            body = {
                "name": name,
                "displayName": display_name,
                "description": description,
                "expression": {
                    "type": "PQL",
                    "format": "pql/text",
                    "value": expression,
                },
                "duration": {
                    "unit": duration_unit,
                    "value": duration_value,
                },
            }
            return aep_post(_CA, body, sandbox=sandbox or None)
        except Exception as exc:
            return {"error": str(exc)}

    @mcp.tool()
    @track("update_computed_attribute")
    def update_computed_attribute(
        attribute_id: str,
        patches: list,
        sandbox: str = "",
    ) -> dict:
        """Update a computed attribute using JSON Patch operations.

        Args:
            attribute_id: Computed attribute ID.
            patches: List of JSON Patch operations, e.g.
                     [{"op": "replace", "path": "/description", "value": "New desc"}]
            sandbox: Sandbox name.
        """
        try:
            return aep_patch(f"{_CA}/{attribute_id}", patches, sandbox=sandbox or None)
        except Exception as exc:
            return {"error": str(exc)}
