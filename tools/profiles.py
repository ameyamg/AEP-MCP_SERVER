"""Real-Time Customer Profile and Identity Namespace tools."""

from typing import Optional

from auth import aep_get
from tools.usage_logger import track


def register(mcp) -> None:

    # ── Identity Namespaces ──────────────────────────────────────────────────

    @mcp.tool()
    @track("list_identity_namespaces")
    def list_identity_namespaces(sandbox: str = "") -> dict:
        """List all identity namespaces (standard and custom) in the org.

        Args:
            sandbox: Sandbox name.
        """
        try:
            return aep_get(
                "/data/core/idnamespace/identities",
                sandbox=sandbox or None,
            )
        except Exception as exc:
            return {"error": str(exc)}

    @mcp.tool()
    @track("get_identity_namespace")
    def get_identity_namespace(namespace_code: str, sandbox: str = "") -> dict:
        """Get details for a specific identity namespace by its code.

        Args:
            namespace_code: The namespace code (e.g. 'Email', 'ECID', 'CRMID').
            sandbox: Sandbox name.
        """
        try:
            return aep_get(
                f"/data/core/idnamespace/identities/{namespace_code}",
                sandbox=sandbox or None,
            )
        except Exception as exc:
            return {"error": str(exc)}

    # ── Identity Graph ───────────────────────────────────────────────────────

    @mcp.tool()
    @track("get_identity_cluster")
    def get_identity_cluster(
        identity_id: str,
        namespace_code: str,
        sandbox: str = "",
    ) -> dict:
        """Get all identities in the same identity cluster as the given identity.

        Args:
            identity_id: The identity value (e.g. an email address or ECID).
            namespace_code: The namespace code for the identity (e.g. 'Email').
            sandbox: Sandbox name.
        """
        try:
            return aep_get(
                "/data/core/identity/cluster/members",
                sandbox=sandbox or None,
                params={"nsCode": namespace_code, "id": identity_id},
            )
        except Exception as exc:
            return {"error": str(exc)}

    # ── Real-Time Customer Profile ───────────────────────────────────────────

    @mcp.tool()
    @track("get_profile_by_identity")
    def get_profile_by_identity(
        entity_id: str,
        entity_id_ns: str,
        schema_name: str = "_xdm.context.profile",
        sandbox: str = "",
        merge_policy_id: str = "",
    ) -> dict:
        """Look up a Real-Time Customer Profile by identity.

        Args:
            entity_id: The identity value (e.g. email address or ECID).
            entity_id_ns: The identity namespace code (e.g. 'Email', 'ECID').
            schema_name: XDM schema class for the entity (default: _xdm.context.profile).
            sandbox: Sandbox name.
            merge_policy_id: Optional merge policy ID to apply.
        """
        try:
            params: dict = {
                "schema.name": schema_name,
                "entityId": entity_id,
                "entityIdNS": entity_id_ns,
            }
            if merge_policy_id:
                params["mergePolicyId"] = merge_policy_id
            return aep_get(
                "/data/core/ups/access/entities",
                sandbox=sandbox or None,
                params=params,
            )
        except Exception as exc:
            return {"error": str(exc)}

    @mcp.tool()
    @track("list_merge_policies")
    def list_merge_policies(sandbox: str = "", limit: int = 20) -> dict:
        """List profile merge policies defined in the sandbox.

        Args:
            sandbox: Sandbox name.
            limit: Max records.
        """
        try:
            return aep_get(
                "/data/core/ups/config/mergePolicies",
                sandbox=sandbox or None,
                params={"limit": limit},
            )
        except Exception as exc:
            return {"error": str(exc)}

    @mcp.tool()
    @track("list_profile_export_jobs")
    def list_profile_export_jobs(sandbox: str = "", limit: int = 20) -> dict:
        """List profile export jobs.

        Args:
            sandbox: Sandbox name.
            limit: Max records.
        """
        try:
            return aep_get(
                "/data/core/ups/export/jobs",
                sandbox=sandbox or None,
                params={"limit": limit},
            )
        except Exception as exc:
            return {"error": str(exc)}

    @mcp.tool()
    @track("get_profile_export_job")
    def get_profile_export_job(job_id: str, sandbox: str = "") -> dict:
        """Get status and details of a profile export job.

        Args:
            job_id: Export job ID.
            sandbox: Sandbox name.
        """
        try:
            return aep_get(
                f"/data/core/ups/export/jobs/{job_id}",
                sandbox=sandbox or None,
            )
        except Exception as exc:
            return {"error": str(exc)}
