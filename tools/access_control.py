"""Access Control — roles, permissions, users, and effective policy lookups."""

from auth import aep_get, aep_post
from tools.usage_logger import track

_AC = "/data/foundation/access-control"
_ADM = f"{_AC}/administration"


def register(mcp) -> None:

    # ── Roles ────────────────────────────────────────────────────────────────

    @mcp.tool()
    @track("list_roles")
    def list_roles(
        sandbox: str = "",
        limit: int = 50,
        start: int = 0,
    ) -> dict:
        """List attribute-based access control (ABAC) roles in the org.

        Args:
            sandbox: Sandbox name.
            limit: Max records.
            start: Pagination offset.
        """
        try:
            return aep_get(
                f"{_ADM}/roles",
                sandbox=sandbox or None,
                params={"limit": limit, "start": start},
            )
        except Exception as exc:
            return {"error": str(exc)}

    @mcp.tool()
    @track("get_role")
    def get_role(role_id: str, sandbox: str = "") -> dict:
        """Get details for a specific ABAC role, including its policies and subjects.

        Args:
            role_id: Role ID.
            sandbox: Sandbox name.
        """
        try:
            return aep_get(f"{_ADM}/roles/{role_id}", sandbox=sandbox or None)
        except Exception as exc:
            return {"error": str(exc)}

    @mcp.tool()
    @track("list_role_subjects")
    def list_role_subjects(role_id: str, sandbox: str = "") -> dict:
        """List all users and groups assigned to a role.

        Args:
            role_id: Role ID.
            sandbox: Sandbox name.
        """
        try:
            return aep_get(
                f"{_ADM}/roles/{role_id}/subjects",
                sandbox=sandbox or None,
            )
        except Exception as exc:
            return {"error": str(exc)}

    @mcp.tool()
    @track("list_role_policies")
    def list_role_policies(role_id: str, sandbox: str = "") -> dict:
        """List all policies (resource + action grants) attached to a role.

        Args:
            role_id: Role ID.
            sandbox: Sandbox name.
        """
        try:
            return aep_get(
                f"{_ADM}/roles/{role_id}/policies",
                sandbox=sandbox or None,
            )
        except Exception as exc:
            return {"error": str(exc)}

    # ── Permissions Summary ───────────────────────────────────────────────────

    @mcp.tool()
    @track("list_available_permissions")
    def list_available_permissions(sandbox: str = "") -> dict:
        """List all available AEP permissions grouped by resource category.

        Useful for understanding which permissions exist before assigning them.

        Args:
            sandbox: Sandbox name.
        """
        try:
            return aep_get(
                f"{_ADM}/permissions/summary",
                sandbox=sandbox or None,
            )
        except Exception as exc:
            return {"error": str(exc)}

    # ── Policies ─────────────────────────────────────────────────────────────

    @mcp.tool()
    @track("list_policies")
    def list_policies(
        sandbox: str = "",
        limit: int = 50,
        start: int = 0,
    ) -> dict:
        """List access control policies in the org.

        Args:
            sandbox: Sandbox name.
            limit: Max records.
            start: Pagination offset.
        """
        try:
            return aep_get(
                f"{_ADM}/policies",
                sandbox=sandbox or None,
                params={"limit": limit, "start": start},
            )
        except Exception as exc:
            return {"error": str(exc)}

    @mcp.tool()
    @track("get_policy")
    def get_policy(policy_id: str, sandbox: str = "") -> dict:
        """Get details for a specific access control policy.

        Args:
            policy_id: Policy ID.
            sandbox: Sandbox name.
        """
        try:
            return aep_get(f"{_ADM}/policies/{policy_id}", sandbox=sandbox or None)
        except Exception as exc:
            return {"error": str(exc)}

    # ── Effective Policies (what can I do?) ──────────────────────────────────

    @mcp.tool()
    @track("get_effective_policies")
    def get_effective_policies(
        resources: list,
        sandbox: str = "",
    ) -> dict:
        """Check which actions the current user can perform on specific resources.

        Returns the effective policy set — the merged result of all roles and
        policies that apply to the authenticated user.

        Args:
            resources: List of resource strings to evaluate, e.g.
                       ["/data/foundation/catalog/dataSets",
                        "/data/core/ups/segment/definitions"]
            sandbox: Sandbox name.
        """
        try:
            body = {"resources": resources}
            return aep_post(
                f"{_AC}/acl/effective-policies",
                body,
                sandbox=sandbox or None,
            )
        except Exception as exc:
            return {"error": str(exc)}

    # ── Users ─────────────────────────────────────────────────────────────────

    @mcp.tool()
    @track("list_users")
    def list_users(sandbox: str = "", limit: int = 50, start: int = 0) -> dict:
        """List users in the org and their assigned roles.

        Args:
            sandbox: Sandbox name.
            limit: Max records.
            start: Pagination offset.
        """
        try:
            return aep_get(
                f"{_ADM}/users",
                sandbox=sandbox or None,
                params={"limit": limit, "start": start},
            )
        except Exception as exc:
            return {"error": str(exc)}

    @mcp.tool()
    @track("get_user_roles")
    def get_user_roles(user_id: str, sandbox: str = "") -> dict:
        """Get all roles assigned to a specific user.

        Args:
            user_id: User ID (IMS user ID or email).
            sandbox: Sandbox name.
        """
        try:
            return aep_get(
                f"{_ADM}/users/{user_id}/roles",
                sandbox=sandbox or None,
            )
        except Exception as exc:
            return {"error": str(exc)}
