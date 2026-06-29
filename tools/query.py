"""AEP Query Service — ad-hoc SQL queries and query templates."""

from auth import aep_get, aep_post, aep_delete
from tools.usage_logger import track


def register(mcp) -> None:

    # ── Queries ──────────────────────────────────────────────────────────────

    @mcp.tool()
    @track("run_query")
    def run_query(
        sql: str,
        name: str = "",
        sandbox: str = "",
        output_dataset_id: str = "",
    ) -> dict:
        """Submit an ad-hoc SQL query to AEP Query Service.

        Large result sets are written to a dataset; small ones are returned inline.

        Args:
            sql: SQL statement to execute (standard ANSI SQL against AEP datasets).
            name: Optional display name for this query.
            sandbox: Sandbox name.
            output_dataset_id: Optional dataset ID to write results into (CTAS).
        """
        try:
            body: dict = {"dbName": "prod:all", "sql": sql}
            if name:
                body["name"] = name
            if output_dataset_id:
                body["ctasParameters"] = {"datasetId": output_dataset_id}
            return aep_post(
                "/data/foundation/query/queries",
                body,
                sandbox=sandbox or None,
            )
        except Exception as exc:
            return {"error": str(exc)}

    @mcp.tool()
    @track("list_queries")
    def list_queries(
        sandbox: str = "",
        limit: int = 20,
        start: int = 0,
        order_by: str = "updated:desc",
        status: str = "",
    ) -> dict:
        """List submitted queries in Query Service.

        Args:
            sandbox: Sandbox name.
            limit: Max records (1–100).
            start: Pagination offset.
            order_by: Sort field and direction (e.g. 'updated:desc').
            status: Filter by status (IN_PROGRESS, SUCCESS, FAILED, etc.).
        """
        try:
            params: dict = {"limit": limit, "start": start, "orderby": order_by}
            if status:
                params["status"] = status
            return aep_get(
                "/data/foundation/query/queries",
                sandbox=sandbox or None,
                params=params,
            )
        except Exception as exc:
            return {"error": str(exc)}

    @mcp.tool()
    @track("get_query")
    def get_query(query_id: str, sandbox: str = "") -> dict:
        """Get status and details of a specific query.

        Args:
            query_id: Query ID returned from run_query.
            sandbox: Sandbox name.
        """
        try:
            return aep_get(
                f"/data/foundation/query/queries/{query_id}",
                sandbox=sandbox or None,
            )
        except Exception as exc:
            return {"error": str(exc)}

    @mcp.tool()
    @track("cancel_query")
    def cancel_query(query_id: str, sandbox: str = "") -> dict:
        """Cancel an in-progress query.

        Args:
            query_id: Query ID to cancel.
            sandbox: Sandbox name.
        """
        try:
            result = aep_delete(
                f"/data/foundation/query/queries/{query_id}",
                sandbox=sandbox or None,
            )
            return result or {"cancelled": query_id}
        except Exception as exc:
            return {"error": str(exc)}

    # ── Query Templates ──────────────────────────────────────────────────────

    @mcp.tool()
    @track("list_query_templates")
    def list_query_templates(
        sandbox: str = "",
        limit: int = 20,
        start: int = 0,
    ) -> dict:
        """List saved query templates.

        Args:
            sandbox: Sandbox name.
            limit: Max records.
            start: Pagination offset.
        """
        try:
            return aep_get(
                "/data/foundation/query/query-templates",
                sandbox=sandbox or None,
                params={"limit": limit, "start": start},
            )
        except Exception as exc:
            return {"error": str(exc)}

    @mcp.tool()
    @track("get_query_template")
    def get_query_template(template_id: str, sandbox: str = "") -> dict:
        """Get a specific query template by ID.

        Args:
            template_id: Query template ID.
            sandbox: Sandbox name.
        """
        try:
            return aep_get(
                f"/data/foundation/query/query-templates/{template_id}",
                sandbox=sandbox or None,
            )
        except Exception as exc:
            return {"error": str(exc)}

    @mcp.tool()
    @track("create_query_template")
    def create_query_template(
        name: str,
        sql: str,
        description: str = "",
        sandbox: str = "",
    ) -> dict:
        """Save a reusable SQL query as a named template.

        Args:
            name: Template display name.
            sql: SQL statement to save.
            description: Optional description.
            sandbox: Sandbox name.
        """
        try:
            body: dict = {"name": name, "sql": sql}
            if description:
                body["description"] = description
            return aep_post(
                "/data/foundation/query/query-templates",
                body,
                sandbox=sandbox or None,
            )
        except Exception as exc:
            return {"error": str(exc)}

    # ── Scheduled Queries ────────────────────────────────────────────────────

    @mcp.tool()
    @track("list_scheduled_queries")
    def list_scheduled_queries(sandbox: str = "", limit: int = 20) -> dict:
        """List all scheduled (recurring) query runs.

        Args:
            sandbox: Sandbox name.
            limit: Max records.
        """
        try:
            return aep_get(
                "/data/foundation/query/schedules",
                sandbox=sandbox or None,
                params={"limit": limit},
            )
        except Exception as exc:
            return {"error": str(exc)}

    @mcp.tool()
    @track("list_query_runs")
    def list_query_runs(schedule_id: str, sandbox: str = "", limit: int = 20) -> dict:
        """List individual runs for a scheduled query.

        Args:
            schedule_id: Scheduled query ID.
            sandbox: Sandbox name.
            limit: Max records.
        """
        try:
            return aep_get(
                f"/data/foundation/query/schedules/{schedule_id}/runs",
                sandbox=sandbox or None,
                params={"limit": limit},
            )
        except Exception as exc:
            return {"error": str(exc)}
