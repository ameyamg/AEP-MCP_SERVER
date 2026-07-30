"""
AEP authentication and HTTP helpers.

Single-org (original behaviour):
  Set env vars AEP_ACCESS_TOKEN (or AEP_CLIENT_ID + AEP_CLIENT_SECRET),
  AEP_API_KEY, AEP_ORG_ID, AEP_SANDBOX_NAME.  All existing .env usage works
  unchanged.

Multi-org (new):
  Create orgs.json next to this file (see orgs.example.json for format).
  Select which profile is active in two ways:
    1. At startup:  AEP_PROFILE=client_a python server.py
    2. At runtime:  call set_active_profile("client_a") — or use the
                    switch_org_profile MCP tool exposed by tools/orgs.py.

  Token caches are maintained per profile, so switching orgs does not
  invalidate cached tokens for other orgs.
"""

import json
import os
import time
from pathlib import Path
from typing import Any, Optional

import httpx

AEP_BASE = "https://platform.adobe.io"
IMS_TOKEN_URL = "https://ims-na1.adobelogin.com/ims/token/v3"

# CJA API base — set CJA_BASE_URL in orgs.json per profile or override here.
# Typical value: https://cja.adobe.io  (confirm with your Adobe CSM)
_CJA_BASE_DEFAULT = "https://cja.adobe.io"

# ── Multi-org profile state ──────────────────────────────────────────────────

_profiles: dict[str, dict] = {}
_active_profile: str = ""
# Per-profile token caches: { profile_key: { "token": str, "expires_at": float } }
_token_caches: dict[str, dict[str, Any]] = {}

# Per-profile sandbox overrides for the current session.
# Key = profile name, value = full sandbox name (e.g. "aetna-hipaa-prod").
# When set, overrides the profile's default sandbox until cleared.
_sandbox_overrides: dict[str, str] = {}


def _load_profiles() -> None:
    """Load orgs.json on startup if it exists."""
    global _profiles, _active_profile
    orgs_file = Path(__file__).parent / "orgs.json"
    if not orgs_file.exists():
        return
    with orgs_file.open() as f:
        data = json.load(f)
    _profiles = data.get("profiles", {})
    default = data.get("default", "")
    env_profile = os.getenv("AEP_PROFILE", "")
    # Priority: AEP_PROFILE env var > "default" key in orgs.json > first profile
    _active_profile = (
        env_profile
        or default
        or (next(iter(_profiles)) if _profiles else "")
    )


_load_profiles()


# ── Profile management (called by tools/orgs.py and externally) ──────────────

def list_profiles() -> list[str]:
    """Return names of all configured profiles."""
    return list(_profiles.keys())


def get_active_profile() -> str:
    """Return the name of the currently active profile (empty = env-var mode)."""
    return _active_profile


def set_active_profile(name: str) -> None:
    """Switch to a named profile. Raises ValueError if the profile does not exist."""
    global _active_profile
    if name not in _profiles:
        available = list(_profiles.keys())
        raise ValueError(
            f"Profile '{name}' not found in orgs.json. "
            f"Available profiles: {available}"
        )
    _active_profile = name


def get_profile_info(name: str = "") -> dict:
    """Return non-sensitive info about a profile (no secrets)."""
    profile_name = name or _active_profile
    if not profile_name or profile_name not in _profiles:
        return {
            "mode": "env_vars",
            "org_id": os.getenv("AEP_ORG_ID", ""),
            "sandbox": os.getenv("AEP_SANDBOX_NAME", ""),
            "auth_method": "access_token" if os.getenv("AEP_ACCESS_TOKEN") else "oauth_s2s",
        }
    cfg = _profiles[profile_name]
    return {
        "mode": "profile",
        "profile": profile_name,
        "org_id": cfg.get("org_id", ""),
        "sandbox": cfg.get("sandbox", ""),
        "auth_method": "access_token" if cfg.get("access_token") else "oauth_s2s",
    }


def get_primary_namespace(sandbox_name: str = "", profile_name: str = "") -> dict:
    """Return the primary identity namespace config for the given sandbox.

    Returns a dict with 'code' (e.g. 'CRMID') and 'id' (integer namespace ID).
    Falls back to {"code": "Email", "id": 6} if not configured in the profile.
    """
    name = profile_name or _active_profile
    cfg = _profiles.get(name, {})
    sandbox = sandbox_name or get_active_sandbox(name)
    ns = cfg.get("namespaces", {}).get(sandbox, {})
    code = ns.get("primary", "Email")
    return {
        "code": code,
        "id": ns.get("primary_id", 6),
        "xdm_key": ns.get("xdm_identity_map_key", code),
    }


def get_merge_policy(sandbox_name: str = "", role: str = "primary", profile_name: str = "") -> str:
    """Return the configured merge policy ID for the given sandbox and role.

    Args:
        sandbox_name: Full sandbox name. Defaults to the currently active sandbox.
        role:         'primary' (default) or 'secondary'.
        profile_name: Profile to look up. Defaults to the active profile.

    Returns the merge policy ID string, or "" if not configured.
    """
    name = profile_name or _active_profile
    cfg = _profiles.get(name, {})
    sandbox = sandbox_name or get_active_sandbox(name)
    policies = cfg.get("merge_policies", {}).get(sandbox, {})
    return policies.get(role, "")


def list_sandboxes(profile_name: str = "") -> dict[str, str]:
    """Return the sandboxes dict for a profile, or {} if none defined."""
    name = profile_name or _active_profile
    cfg = _profiles.get(name, {})
    return cfg.get("sandboxes", {})


def get_active_sandbox(profile_name: str = "") -> str:
    """Return the effective sandbox for the given (or active) profile.

    Priority: session override > profile default.
    """
    name = profile_name or _active_profile
    if name in _sandbox_overrides:
        return _sandbox_overrides[name]
    cfg = _profiles.get(name, {})
    return cfg.get("sandbox") or os.environ.get("AEP_SANDBOX_NAME", "")


def set_sandbox_override(sandbox_alias_or_name: str, profile_name: str = "") -> str:
    """Set a session-level sandbox override for the active (or named) profile.

    Accepts either a named alias from the profile's 'sandboxes' dict (e.g. 'prod')
    or a full sandbox name (e.g. 'my-org-prod').
    Returns the resolved full sandbox name.
    """
    name = profile_name or _active_profile
    sandboxes = list_sandboxes(name)
    # Resolve alias → full name if possible, otherwise treat as a literal sandbox name
    resolved = sandboxes.get(sandbox_alias_or_name, sandbox_alias_or_name)
    _sandbox_overrides[name] = resolved
    return resolved


def clear_sandbox_override(profile_name: str = "") -> None:
    """Remove the session sandbox override, reverting to the profile default."""
    name = profile_name or _active_profile
    _sandbox_overrides.pop(name, None)


def _active_cfg() -> dict:
    """Return the config dict for the currently active profile, or {} for env-var mode."""
    if _active_profile and _active_profile in _profiles:
        return _profiles[_active_profile]
    return {}


# ── Token management ─────────────────────────────────────────────────────────

def get_access_token() -> str:
    """Return a valid IMS bearer token for the active org profile."""
    cfg = _active_cfg()
    cache_key = _active_profile or "__env__"

    # Static / pre-generated bearer token (Option A)
    direct = cfg.get("access_token") or os.getenv("AEP_ACCESS_TOKEN", "")
    if direct:
        return direct

    # OAuth Server-to-Server with per-profile caching (Option B)
    now = time.time()
    entry = _token_caches.get(cache_key, {"token": None, "expires_at": 0.0})
    if entry["token"] and now < entry["expires_at"] - 60:
        return entry["token"]  # type: ignore[return-value]

    client_id = cfg.get("client_id") or os.environ["AEP_CLIENT_ID"]
    client_secret = cfg.get("client_secret") or os.environ["AEP_CLIENT_SECRET"]

    resp = httpx.post(
        IMS_TOKEN_URL,
        data={
            "grant_type": "client_credentials",
            "client_id": client_id,
            "client_secret": client_secret,
            "scope": (
                "AdobeID,openid,read_organizations,"
                "additional_info.projectedProductContext,"
                "additional_info.roles,adobeio_api"
            ),
        },
        timeout=15,
    )
    resp.raise_for_status()
    data = resp.json()
    _token_caches[cache_key] = {
        "token": data["access_token"],
        "expires_at": now + data.get("expires_in", 3600),
    }
    return data["access_token"]


# ── Request helpers ───────────────────────────────────────────────────────────

def get_headers(sandbox: Optional[str] = None, extra: Optional[dict] = None) -> dict:
    """Build standard AEP API request headers for the active profile."""
    cfg = _active_cfg()
    api_key = cfg.get("api_key") or cfg.get("client_id") or os.environ["AEP_API_KEY"]
    org_id = cfg.get("org_id") or os.environ["AEP_ORG_ID"]

    # Sandbox resolution priority:
    # 1. Explicit sandbox arg passed by the tool (e.g. user said "run in prod")
    # 2. Session-level override set via switch_sandbox tool
    # 3. Profile default sandbox
    effective_sandbox = sandbox or get_active_sandbox()

    headers = {
        "Authorization": f"Bearer {get_access_token()}",
        "x-api-key": api_key,
        "x-gw-ims-org-id": org_id,
        "x-sandbox-name": effective_sandbox,
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    if extra:
        headers.update(extra)
    return headers


def aep_get(
    path: str,
    *,
    sandbox: Optional[str] = None,
    params: Optional[dict] = None,
    accept: Optional[str] = None,
) -> Any:
    """GET request against the AEP API."""
    extra = {"Accept": accept} if accept else None
    resp = httpx.get(
        f"{AEP_BASE}{path}",
        headers=get_headers(sandbox, extra),
        params={k: v for k, v in (params or {}).items() if v is not None},
        timeout=30,
    )
    resp.raise_for_status()
    return resp.json()


def aep_post(
    path: str,
    body: dict,
    *,
    sandbox: Optional[str] = None,
    accept: Optional[str] = None,
) -> Any:
    """POST request against the AEP API."""
    extra = {"Accept": accept} if accept else None
    resp = httpx.post(
        f"{AEP_BASE}{path}",
        headers=get_headers(sandbox, extra),
        json=body,
        timeout=30,
    )
    resp.raise_for_status()
    return resp.json()


def aep_patch(
    path: str,
    patches: list,
    *,
    sandbox: Optional[str] = None,
    content_type: str = "application/json-patch+json",
    accept: Optional[str] = None,
) -> Any:
    """PATCH request against the AEP API using JSON Patch.

    Defaults to Content-Type application/json-patch+json. Some services (e.g. the
    Schema Registry) require Content-Type application/json plus a versioned Accept
    header — pass content_type/accept to override.
    """
    extra = {"Accept": accept} if accept else None
    headers = get_headers(sandbox, extra)
    headers["Content-Type"] = content_type
    resp = httpx.patch(
        f"{AEP_BASE}{path}",
        headers=headers,
        json=patches,
        timeout=30,
    )
    resp.raise_for_status()
    return resp.json() if resp.content else None


def aep_delete(path: str, *, sandbox: Optional[str] = None) -> Optional[dict]:
    """DELETE request against the AEP API."""
    resp = httpx.delete(
        f"{AEP_BASE}{path}",
        headers=get_headers(sandbox),
        timeout=30,
    )
    resp.raise_for_status()
    return resp.json() if resp.content else None


# ── CJA helpers ───────────────────────────────────────────────────────────────
# CJA uses the same IMS token and org header but a different base URL.
# No x-sandbox-name — CJA scopes requests via dataviewId query param instead.

def get_cja_base() -> str:
    """Return the CJA API base URL for the active profile, or the module default."""
    cfg = _active_cfg()
    return cfg.get("cja_base_url") or os.getenv("CJA_BASE_URL") or _CJA_BASE_DEFAULT


def get_cja_headers(extra: Optional[dict] = None) -> dict:
    """Build CJA API request headers (no x-sandbox-name)."""
    cfg = _active_cfg()
    api_key = cfg.get("api_key") or cfg.get("client_id") or os.environ["AEP_API_KEY"]
    org_id = cfg.get("org_id") or os.environ["AEP_ORG_ID"]
    headers = {
        "Authorization": f"Bearer {get_access_token()}",
        "x-api-key": api_key,
        "x-gw-ims-org-id": org_id,
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    if extra:
        headers.update(extra)
    return headers


def cja_get(path: str, *, params: Optional[dict] = None) -> Any:
    """GET request against the CJA API."""
    resp = httpx.get(
        f"{get_cja_base()}{path}",
        headers=get_cja_headers(),
        params={k: v for k, v in (params or {}).items() if v is not None},
        timeout=30,
    )
    resp.raise_for_status()
    return resp.json()


def cja_post(path: str, body: dict) -> Any:
    """POST request against the CJA API."""
    resp = httpx.post(
        f"{get_cja_base()}{path}",
        headers=get_cja_headers(),
        json=body,
        timeout=30,
    )
    resp.raise_for_status()
    return resp.json()


def cja_put(path: str, body: dict) -> Any:
    """PUT request against the CJA API."""
    resp = httpx.put(
        f"{get_cja_base()}{path}",
        headers=get_cja_headers(),
        json=body,
        timeout=30,
    )
    resp.raise_for_status()
    return resp.json()


def cja_delete(path: str) -> Optional[dict]:
    """DELETE request against the CJA API."""
    resp = httpx.delete(
        f"{get_cja_base()}{path}",
        headers=get_cja_headers(),
        timeout=30,
    )
    resp.raise_for_status()
    return resp.json() if resp.content else None
