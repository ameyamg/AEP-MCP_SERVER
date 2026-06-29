"""Data Hygiene — dataset expirations (TTL) and record-level delete orders."""

from auth import aep_get, aep_post, aep_delete
from tools.usage_logger import track

_HYG = "/data/core/hygiene"


def register(mcp) -> None:

    # ── Dataset Expirations (TTL) ────────────────────────────────────────────

    @mcp.tool()
    @track("list_dataset_expirations")
    def list_dataset_expirations(
        sandbox: str = "",
        status: str = "",
        limit: int = 20,
        page: int = 1,
    ) -> dict:
        """List dataset expiration (TTL) schedules.

        Args:
            sandbox: Sandbox name.
            status: Filter by status (PENDING, COMPLETED, ERROR, CANCELLED).
            limit: Max records per page.
            page: Page number (1-based).
        """
        try:
            params: dict = {"limit": limit, "page": page}
            if status:
                params["status"] = status
            return aep_get(f"{_HYG}/ttl", sandbox=sandbox or None, params=params)
        except Exception as exc:
            return {"error": str(exc)}

    @mcp.tool()
    @track("get_dataset_expiration")
    def get_dataset_expiration(ttl_id: str, sandbox: str = "") -> dict:
        """Get details for a specific dataset expiration (TTL) schedule.

        Args:
            ttl_id: Dataset expiration ID (returned from list or create).
            sandbox: Sandbox name.
        """
        try:
            return aep_get(f"{_HYG}/ttl/{ttl_id}", sandbox=sandbox or None)
        except Exception as exc:
            return {"error": str(exc)}

    @mcp.tool()
    @track("create_dataset_expiration")
    def create_dataset_expiration(
        dataset_id: str,
        expire_on: str,
        sandbox: str = "",
        description: str = "",
    ) -> dict:
        """Schedule a dataset for automatic deletion on a future date.

        Args:
            dataset_id: AEP catalog dataset ID to expire.
            expire_on: ISO-8601 expiry date (e.g. '2025-12-31').
            sandbox: Sandbox name.
            description: Optional reason / description.
        """
        try:
            body: dict = {"datasetId": dataset_id, "expiry": expire_on}
            if description:
                body["description"] = description
            return aep_post(f"{_HYG}/ttl", body, sandbox=sandbox or None)
        except Exception as exc:
            return {"error": str(exc)}

    @mcp.tool()
    @track("cancel_dataset_expiration")
    def cancel_dataset_expiration(ttl_id: str, sandbox: str = "") -> dict:
        """Cancel a pending dataset expiration before it executes.

        Args:
            ttl_id: Dataset expiration ID to cancel.
            sandbox: Sandbox name.
        """
        try:
            result = aep_delete(f"{_HYG}/ttl/{ttl_id}", sandbox=sandbox or None)
            return result or {"cancelled": ttl_id}
        except Exception as exc:
            return {"error": str(exc)}

    # ── Record Delete Orders ─────────────────────────────────────────────────

    @mcp.tool()
    @track("list_record_delete_orders")
    def list_record_delete_orders(
        sandbox: str = "",
        status: str = "",
        limit: int = 20,
        page: int = 1,
    ) -> dict:
        """List record-level delete work orders (GDPR / privacy deletes).

        Args:
            sandbox: Sandbox name.
            status: Filter by status (PENDING, PROCESSING, COMPLETED, ERROR).
            limit: Max records per page.
            page: Page number (1-based).
        """
        try:
            params: dict = {"limit": limit, "page": page}
            if status:
                params["status"] = status
            return aep_get(f"{_HYG}/workorder", sandbox=sandbox or None, params=params)
        except Exception as exc:
            return {"error": str(exc)}

    @mcp.tool()
    @track("get_record_delete_order")
    def get_record_delete_order(work_order_id: str, sandbox: str = "") -> dict:
        """Get details and status for a specific record delete work order.

        Args:
            work_order_id: Work order ID.
            sandbox: Sandbox name.
        """
        try:
            return aep_get(
                f"{_HYG}/workorder/{work_order_id}",
                sandbox=sandbox or None,
            )
        except Exception as exc:
            return {"error": str(exc)}

    @mcp.tool()
    @track("create_record_delete_order")
    def create_record_delete_order(
        dataset_id: str,
        identities: list,
        sandbox: str = "",
        description: str = "",
    ) -> dict:
        """Submit a record delete work order to remove specific identities from a dataset.

        Args:
            dataset_id: Target dataset ID.
            identities: List of identity dicts, each with 'namespace' (code) and 'id'.
                        Example: [{"namespace": "Email", "id": "user@example.com"}]
            sandbox: Sandbox name.
            description: Optional description / legal basis.
        """
        try:
            body: dict = {
                "datasetId": dataset_id,
                "identities": [
                    {"namespace": {"code": ident["namespace"]}, "id": ident["id"]}
                    for ident in identities
                ],
            }
            if description:
                body["description"] = description
            return aep_post(f"{_HYG}/workorder", body, sandbox=sandbox or None)
        except Exception as exc:
            return {"error": str(exc)}

    # ── Quota ────────────────────────────────────────────────────────────────

    @mcp.tool()
    @track("get_hygiene_quota")
    def get_hygiene_quota(sandbox: str = "") -> dict:
        """Get data hygiene quota usage (number of delete orders / dataset TTLs allowed).

        Args:
            sandbox: Sandbox name.
        """
        try:
            return aep_get(f"{_HYG}/quota", sandbox=sandbox or None)
        except Exception as exc:
            return {"error": str(exc)}
