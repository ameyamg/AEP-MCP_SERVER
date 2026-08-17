"""AEP Segmentation Service — audience segment definitions and evaluation jobs."""

from typing import Optional

from auth import aep_get, aep_post, aep_delete
from tools.usage_logger import track


def register(mcp) -> None:

    # ── Segment Definitions ──────────────────────────────────────────────────

    @mcp.tool()
    @track("list_segments")
    def list_segments(
        sandbox: str = "",
        limit: int = 20,
        start: int = 0,
        sort: str = "updatedTime:desc",
    ) -> dict:
        """List audience segment definitions in the sandbox.

        Args:
            sandbox: Sandbox name.
            limit: Max records (1–200).
            start: Pagination offset.
            sort: Sort order (e.g. 'updatedTime:desc', 'name:asc').
        """
        try:
            return aep_get(
                "/data/core/ups/segment/definitions",
                sandbox=sandbox or None,
                params={"limit": limit, "start": start, "sortBy": sort},
            )
        except Exception as exc:
            return {"error": str(exc)}

    @mcp.tool()
    @track("get_segment")
    def get_segment(segment_id: str, sandbox: str = "") -> dict:
        """Get a specific segment definition by ID.

        Args:
            segment_id: The segment definition ID.
            sandbox: Sandbox name.
        """
        try:
            return aep_get(
                f"/data/core/ups/segment/definitions/{segment_id}",
                sandbox=sandbox or None,
            )
        except Exception as exc:
            return {"error": str(exc)}

    @mcp.tool()
    @track("create_segment")
    def create_segment(
        name: str,
        expression: str,
        description: str = "",
        sandbox: str = "",
        merge_policy_id: str = "",
    ) -> dict:
        """Create a new segment definition using PQL (Profile Query Language).

        Args:
            name: Segment display name.
            expression: PQL expression (e.g. 'workAddress.country = \"US\"').
            description: Optional description.
            sandbox: Sandbox name.
            merge_policy_id: Merge policy to use for evaluation.
        """
        try:
            body: dict = {
                "name": name,
                "profileInstanceId": "ups",
                "expression": {"type": "PQL", "format": "pql/text", "value": expression},
                "schema": {"name": "_xdm.context.profile"},
                "ttlInDays": 60,
            }
            if description:
                body["description"] = description
            if merge_policy_id:
                body["mergePolicyId"] = merge_policy_id
            return aep_post(
                "/data/core/ups/segment/definitions",
                body,
                sandbox=sandbox or None,
            )
        except Exception as exc:
            return {"error": str(exc)}

    @mcp.tool()
    @track("delete_segment")
    def delete_segment(segment_id: str, confirm: bool = False, sandbox: str = "") -> dict:
        """Delete a segment definition. Requires confirm=True to execute.

        Args:
            segment_id: The segment definition ID to delete.
            confirm: Must be True to execute. Default False returns a warning.
            sandbox: Sandbox name.
        """
        if not confirm:
            return {
                "⚠️ WARNING": "DESTRUCTIVE OPERATION — confirmation required",
                "what_will_happen": f"Segment definition '{segment_id}' will be permanently deleted. Any audiences built on it will stop evaluating.",
                "confirm_instructions": "Re-run with confirm=True to proceed.",
            }
        try:
            result = aep_delete(
                f"/data/core/ups/segment/definitions/{segment_id}",
                sandbox=sandbox or None,
            )
            return result or {"deleted": segment_id}
        except Exception as exc:
            return {"error": str(exc)}

    # ── Segment Jobs (Batch Evaluation) ─────────────────────────────────────

    @mcp.tool()
    @track("list_segment_jobs")
    def list_segment_jobs(
        sandbox: str = "",
        limit: int = 20,
        status: str = "",
    ) -> dict:
        """List batch segment evaluation jobs.

        Args:
            sandbox: Sandbox name.
            limit: Max records.
            status: Filter by job status (PROCESSING, SUCCEEDED, FAILED, etc.).
        """
        try:
            params: dict = {"limit": limit}
            if status:
                params["status"] = status
            return aep_get(
                "/data/core/ups/segment/jobs",
                sandbox=sandbox or None,
                params=params,
            )
        except Exception as exc:
            return {"error": str(exc)}

    @mcp.tool()
    @track("get_segment_job")
    def get_segment_job(job_id: str, sandbox: str = "") -> dict:
        """Get status and results of a segment evaluation job.

        Args:
            job_id: Segment job ID.
            sandbox: Sandbox name.
        """
        try:
            return aep_get(
                f"/data/core/ups/segment/jobs/{job_id}",
                sandbox=sandbox or None,
            )
        except Exception as exc:
            return {"error": str(exc)}

    @mcp.tool()
    @track("create_segment_job")
    def create_segment_job(
        segment_ids: list,
        sandbox: str = "",
    ) -> dict:
        """Trigger batch evaluation for one or more segment definitions.

        Args:
            segment_ids: List of segment definition IDs to evaluate.
            sandbox: Sandbox name.
        """
        try:
            body = {"segmentIds": segment_ids}
            return aep_post(
                "/data/core/ups/segment/jobs",
                body,
                sandbox=sandbox or None,
            )
        except Exception as exc:
            return {"error": str(exc)}

    # ── Streaming / Edge Segmentation ────────────────────────────────────────

    @mcp.tool()
    @track("list_streaming_jobs")
    def list_streaming_jobs(sandbox: str = "", limit: int = 20) -> dict:
        """List streaming segmentation jobs (continuous evaluation).

        Args:
            sandbox: Sandbox name.
            limit: Max records.
        """
        try:
            return aep_get(
                "/data/core/ups/segment/streaming/jobs",
                sandbox=sandbox or None,
                params={"limit": limit},
            )
        except Exception as exc:
            return {"error": str(exc)}
