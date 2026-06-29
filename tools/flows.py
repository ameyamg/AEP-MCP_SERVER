"""Flow Service — source connections, destination connections, dataflows, and flow runs."""

from auth import aep_get, aep_post
from tools.usage_logger import track

_FS = "/data/foundation/flowservice"


def register(mcp) -> None:

    # ── Connections (source/destination credentials) ─────────────────────────

    @mcp.tool()
    @track("list_connections")
    def list_connections(
        sandbox: str = "",
        limit: int = 20,
        start: int = 0,
        connection_type: str = "",
    ) -> dict:
        """List Flow Service connections (source or destination credentials).

        Args:
            sandbox: Sandbox name.
            limit: Max records (1–100).
            start: Pagination offset.
            connection_type: Filter by type, e.g. 'amazon-s3', 'azure-blob', 'salesforce'.
        """
        try:
            params: dict = {"limit": limit, "start": start}
            if connection_type:
                params["property"] = f"auth.specName=={connection_type}"
            return aep_get(f"{_FS}/connections", sandbox=sandbox or None, params=params)
        except Exception as exc:
            return {"error": str(exc)}

    @mcp.tool()
    @track("get_connection")
    def get_connection(connection_id: str, sandbox: str = "") -> dict:
        """Get details for a specific Flow Service connection.

        Args:
            connection_id: Connection ID.
            sandbox: Sandbox name.
        """
        try:
            return aep_get(f"{_FS}/connections/{connection_id}", sandbox=sandbox or None)
        except Exception as exc:
            return {"error": str(exc)}

    # ── Source Connections ───────────────────────────────────────────────────

    @mcp.tool()
    @track("list_source_connections")
    def list_source_connections(
        sandbox: str = "",
        limit: int = 20,
        start: int = 0,
    ) -> dict:
        """List source connections (define which data to ingest from a connection).

        Args:
            sandbox: Sandbox name.
            limit: Max records.
            start: Pagination offset.
        """
        try:
            return aep_get(
                f"{_FS}/sourceConnections",
                sandbox=sandbox or None,
                params={"limit": limit, "start": start},
            )
        except Exception as exc:
            return {"error": str(exc)}

    @mcp.tool()
    @track("get_source_connection")
    def get_source_connection(source_connection_id: str, sandbox: str = "") -> dict:
        """Get details for a specific source connection.

        Args:
            source_connection_id: Source connection ID.
            sandbox: Sandbox name.
        """
        try:
            return aep_get(
                f"{_FS}/sourceConnections/{source_connection_id}",
                sandbox=sandbox or None,
            )
        except Exception as exc:
            return {"error": str(exc)}

    # ── Target (Destination) Connections ────────────────────────────────────

    @mcp.tool()
    @track("list_target_connections")
    def list_target_connections(
        sandbox: str = "",
        limit: int = 20,
        start: int = 0,
    ) -> dict:
        """List target connections (define where data lands — datasets or destinations).

        Args:
            sandbox: Sandbox name.
            limit: Max records.
            start: Pagination offset.
        """
        try:
            return aep_get(
                f"{_FS}/targetConnections",
                sandbox=sandbox or None,
                params={"limit": limit, "start": start},
            )
        except Exception as exc:
            return {"error": str(exc)}

    @mcp.tool()
    @track("get_target_connection")
    def get_target_connection(target_connection_id: str, sandbox: str = "") -> dict:
        """Get details for a specific target connection.

        Args:
            target_connection_id: Target connection ID.
            sandbox: Sandbox name.
        """
        try:
            return aep_get(
                f"{_FS}/targetConnections/{target_connection_id}",
                sandbox=sandbox or None,
            )
        except Exception as exc:
            return {"error": str(exc)}

    # ── Dataflows ────────────────────────────────────────────────────────────

    @mcp.tool()
    @track("list_dataflows")
    def list_dataflows(
        sandbox: str = "",
        limit: int = 20,
        start: int = 0,
        state: str = "",
    ) -> dict:
        """List dataflows (ingestion or activation pipelines).

        Args:
            sandbox: Sandbox name.
            limit: Max records.
            start: Pagination offset.
            state: Filter by state (enabled, disabled).
        """
        try:
            params: dict = {"limit": limit, "start": start}
            if state:
                params["property"] = f"state=={state}"
            return aep_get(f"{_FS}/flows", sandbox=sandbox or None, params=params)
        except Exception as exc:
            return {"error": str(exc)}

    @mcp.tool()
    @track("get_dataflow")
    def get_dataflow(dataflow_id: str, sandbox: str = "") -> dict:
        """Get details for a specific dataflow.

        Args:
            dataflow_id: Dataflow (flow) ID.
            sandbox: Sandbox name.
        """
        try:
            return aep_get(f"{_FS}/flows/{dataflow_id}", sandbox=sandbox or None)
        except Exception as exc:
            return {"error": str(exc)}

    # ── Flow Runs ────────────────────────────────────────────────────────────

    @mcp.tool()
    @track("list_flow_runs")
    def list_flow_runs(
        dataflow_id: str,
        sandbox: str = "",
        limit: int = 20,
        start: int = 0,
        status: str = "",
    ) -> dict:
        """List historical runs for a dataflow (ingestion executions).

        Args:
            dataflow_id: Parent dataflow ID.
            sandbox: Sandbox name.
            limit: Max records.
            start: Pagination offset.
            status: Filter by status (Success, Failed, Processing, etc.).
        """
        try:
            params: dict = {
                "limit": limit,
                "start": start,
                "property": f"flowId=={dataflow_id}",
            }
            if status:
                params["property"] += f",status=={status}"
            return aep_get(f"{_FS}/runs", sandbox=sandbox or None, params=params)
        except Exception as exc:
            return {"error": str(exc)}

    @mcp.tool()
    @track("get_flow_run")
    def get_flow_run(run_id: str, sandbox: str = "") -> dict:
        """Get details and status for a specific flow run.

        Args:
            run_id: Flow run ID.
            sandbox: Sandbox name.
        """
        try:
            return aep_get(f"{_FS}/runs/{run_id}", sandbox=sandbox or None)
        except Exception as exc:
            return {"error": str(exc)}

    # ── Connection Specs (available connectors) ──────────────────────────────

    @mcp.tool()
    @track("list_connection_specs")
    def list_connection_specs(sandbox: str = "", limit: int = 50) -> dict:
        """List all available connector types (S3, SFTP, Salesforce, etc.).

        Args:
            sandbox: Sandbox name.
            limit: Max records.
        """
        try:
            return aep_get(
                f"{_FS}/connectionSpecs",
                sandbox=sandbox or None,
                params={"limit": limit},
            )
        except Exception as exc:
            return {"error": str(exc)}

    @mcp.tool()
    @track("get_connection_spec")
    def get_connection_spec(spec_id: str, sandbox: str = "") -> dict:
        """Get full spec for a connector type, including required auth fields.

        Args:
            spec_id: Connection spec ID.
            sandbox: Sandbox name.
        """
        try:
            return aep_get(f"{_FS}/connectionSpecs/{spec_id}", sandbox=sandbox or None)
        except Exception as exc:
            return {"error": str(exc)}
