"""Multi-org / multi-sandbox profile management."""

import auth
from tools.usage_logger import track


def register(mcp) -> None:

    @mcp.tool()
    @track("list_org_profiles")
    def list_org_profiles() -> dict:
        """List all org profiles configured in orgs.json and show which is active.

        Returns profile names and the currently active one. Credentials are
        never returned — only org IDs and sandbox names.
        """
        profiles = auth.list_profiles()
        active = auth.get_active_profile()
        details = {
            name: auth.get_profile_info(name)
            for name in profiles
        }
        return {
            "active_profile": active or "(env-var mode — no orgs.json)",
            "profiles": details,
        }

    @mcp.tool()
    @track("switch_org_profile")
    def switch_org_profile(profile_name: str) -> dict:
        """Switch the active AEP org so all subsequent tool calls use that org's credentials.

        Token caches are maintained per org — switching back to a previously used
        org reuses its cached token if it has not expired.

        Args:
            profile_name: Name of the profile to activate (must exist in orgs.json).
        """
        try:
            previous = auth.get_active_profile()
            auth.set_active_profile(profile_name)
            info = auth.get_profile_info(profile_name)
            return {
                "status": "switched",
                "previous_profile": previous or "(env-var mode)",
                "active_profile": profile_name,
                "org_id": info["org_id"],
                "sandbox": info["sandbox"],
                "auth_method": info["auth_method"],
            }
        except ValueError as exc:
            return {"error": str(exc)}

    @mcp.tool()
    @track("get_current_org")
    def get_current_org() -> dict:
        """Show which org profile and sandbox are currently active.

        Returns the active profile name, IMS org ID, effective sandbox,
        available sandboxes, and auth method.
        """
        active = auth.get_active_profile()
        info = auth.get_profile_info(active)
        sandboxes = auth.list_sandboxes(active)
        effective_sandbox = auth.get_active_sandbox(active)
        return {
            "active_profile": active or "(env-var mode)",
            "effective_sandbox": effective_sandbox,
            "available_sandboxes": sandboxes or {"default": info.get("sandbox", "")},
            **{k: v for k, v in info.items() if k != "sandbox"},
        }

    @mcp.tool()
    @track("switch_sandbox")
    def switch_sandbox(sandbox: str) -> dict:
        """Switch the active sandbox for the current org for the rest of this session.

        Accepts a short alias ('dev', 'prod') or a full sandbox name.
        All subsequent tool calls will use this sandbox until reset_sandbox is called
        or the session ends.

        Args:
            sandbox: Alias ('dev', 'prod') or full sandbox name (e.g. 'my-org-prod').
        """
        try:
            active = auth.get_active_profile()
            previous = auth.get_active_sandbox(active)
            resolved = auth.set_sandbox_override(sandbox, active)
            return {
                "status": "switched",
                "profile": active,
                "previous_sandbox": previous,
                "active_sandbox": resolved,
            }
        except Exception as exc:
            return {"error": str(exc)}

    @mcp.tool()
    @track("reset_sandbox")
    def reset_sandbox() -> dict:
        """Reset the active sandbox back to the profile default.

        Use this after finishing prod operations to return to the default sandbox.
        """
        active = auth.get_active_profile()
        previous = auth.get_active_sandbox(active)
        auth.clear_sandbox_override(active)
        default = auth.get_active_sandbox(active)
        return {
            "status": "reset",
            "profile": active,
            "previous_sandbox": previous,
            "active_sandbox": default,
        }
