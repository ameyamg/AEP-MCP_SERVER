"""AEP Catalog Service — dataset and batch ingestion tools."""

from typing import Optional

from auth import aep_get, aep_post
from tools.usage_logger import track


def register(mcp) -> None:

    @mcp.tool()
    @track("list_datasets")
    def list_datasets(
        sandbox: str = "",
        limit: int = 20,
        offset: int = 0,
        name: str = "",
    ) -> dict:
        """List datasets in an AEP sandbox.

        Args:
            sandbox: Sandbox name (defaults to AEP_SANDBOX_NAME env var).
            limit: Max records to return (1–100).
            offset: Pagination offset.
            name: Optional substring filter on dataset name.
        """
        try:
            params = {"limit": limit, "start": offset}
            if name:
                params["name"] = name
            return aep_get(
                "/data/foundation/catalog/dataSets",
                sandbox=sandbox or None,
                params=params,
            )
        except Exception as exc:
            return {"error": str(exc)}

    @mcp.tool()
    @track("create_dataset")
    def create_dataset(
        name: str,
        schema_id: str,
        description: str = "",
        profile_enabled: bool = False,
        sandbox: str = "",
    ) -> dict:
        """Create a new dataset tied to an XDM schema.

        Args:
            name: Dataset display name.
            schema_id: The XDM schema $id URL to base the dataset on.
            description: Optional description.
            profile_enabled: If True, enable the dataset for Real-Time Customer
                Profile (adds the unifiedProfile tag). The schema must itself be
                Profile-enabled (union tag) for this to take effect.
            sandbox: Sandbox name.
        """
        try:
            body: dict = {
                "name": name,
                "schemaRef": {
                    "id": schema_id,
                    "contentType": "application/vnd.adobe.xed-full+json;version=1",
                },
            }
            if description:
                body["description"] = description
            if profile_enabled:
                body["tags"] = {"unifiedProfile": ["enabled:true"]}
            return aep_post(
                "/data/foundation/catalog/dataSets",
                body,
                sandbox=sandbox or None,
            )
        except Exception as exc:
            return {"error": str(exc)}

    @mcp.tool()
    @track("get_dataset")
    def get_dataset(dataset_id: str, sandbox: str = "") -> dict:
        """Get full details for a specific AEP dataset.

        Args:
            dataset_id: The catalog dataset ID.
            sandbox: Sandbox name (defaults to AEP_SANDBOX_NAME env var).
        """
        try:
            return aep_get(
                f"/data/foundation/catalog/dataSets/{dataset_id}",
                sandbox=sandbox or None,
            )
        except Exception as exc:
            return {"error": str(exc)}

    @mcp.tool()
    @track("list_batches")
    def list_batches(
        dataset_id: str = "",
        sandbox: str = "",
        status: str = "",
        limit: int = 20,
        offset: int = 0,
    ) -> dict:
        """List data ingestion batches, optionally filtered by dataset or status.

        Args:
            dataset_id: Filter by dataset ID (optional).
            sandbox: Sandbox name.
            status: Filter by batch status (success, failed, processing, etc.).
            limit: Max records to return.
            offset: Pagination offset.
        """
        try:
            params: dict = {"limit": limit, "start": offset}
            if dataset_id:
                params["dataSet"] = dataset_id
            if status:
                params["status"] = status
            return aep_get(
                "/data/foundation/catalog/batches",
                sandbox=sandbox or None,
                params=params,
            )
        except Exception as exc:
            return {"error": str(exc)}

    @mcp.tool()
    @track("get_batch")
    def get_batch(batch_id: str, sandbox: str = "") -> dict:
        """Get details for a specific data ingestion batch.

        Args:
            batch_id: The batch ID.
            sandbox: Sandbox name.
        """
        try:
            return aep_get(
                f"/data/foundation/catalog/batches/{batch_id}",
                sandbox=sandbox or None,
            )
        except Exception as exc:
            return {"error": str(exc)}

    @mcp.tool()
    @track("list_sandboxes")
    def list_sandboxes() -> dict:
        """List all sandboxes available in the IMS org."""
        try:
            return aep_get("/data/foundation/sandbox-management/sandboxes")
        except Exception as exc:
            return {"error": str(exc)}

    @mcp.tool()
    @track("get_sandbox")
    def get_sandbox(sandbox_name: str) -> dict:
        """Get details for a specific sandbox by name.

        Args:
            sandbox_name: The sandbox name.
        """
        try:
            return aep_get(f"/data/foundation/sandbox-management/sandboxes/{sandbox_name}")
        except Exception as exc:
            return {"error": str(exc)}
