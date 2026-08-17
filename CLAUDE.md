# AEP MCP Server

FastMCP Python server that wraps Adobe Experience Platform (AEP) and Adobe Journey Optimizer (AJO) REST APIs as MCP tools for Claude.

## Running

```bash
python server.py          # uses default org profile from orgs.json
AEP_PROFILE=MyClient python server.py  # start with a specific org
```

## Register with Claude Code

Add to `.claude/mcp_servers.json`:
```json
{
  "aep": {
    "command": "python",
    "args": ["/Users/amghanekar/aep-mcp-server/server.py"]
  }
}
```

## Project Layout

```
server.py                  # FastMCP entrypoint — imports and registers all tool modules
auth.py                    # Auth + HTTP helpers (aep_get/post/patch/delete); multi-org state
orgs.json                  # Org profiles with credentials — GITIGNORED, never commit
orgs.example.json          # Template for orgs.json
.env / .env.example        # Fallback single-org config (used when no orgs.json)
requirements.txt
tools/
  __init__.py
  datasets.py              # Catalog Service: datasets, batches, sandboxes
  schemas.py               # Schema Registry: XDM schemas, classes, field groups, data types
  profiles.py              # Real-Time Customer Profile, identity namespaces, identity graph
  segments.py              # Segmentation: definitions, batch jobs, streaming
  query.py                 # Query Service: ad-hoc SQL, templates, scheduled queries
  ajo.py                   # AJO: journeys, campaigns, offers, offer decisioning
  flows.py                 # Flow Service: connections, dataflows, flow runs, connector specs
  observability.py         # Observability Insights: metrics, alert subscriptions
  data_hygiene.py          # Data Hygiene: dataset TTL, record deletes, quota
  data_prep.py             # Data Prep: mapping sets, functions, expression validation
  computed_attributes.py   # Computed Attributes
  access_control.py        # ABAC: roles, permissions, policies, effective policies
  architect.py             # Architect-phase templates: data-layer spec, journey canvas
  orgs.py                  # Multi-org tools: list_org_profiles, switch_org_profile, get_current_org
  usage_logger.py          # @track decorator — logs tool calls to AEP_USAGE_LOG (CSV)
```

## Tool Pattern

Every tool module exports a single `register(mcp)` function. Tools follow this exact shape — don't deviate:

```python
@mcp.tool()
@track("tool_name")
def tool_name(param: str, sandbox: str = "") -> dict:
    """One-line summary.

    Args:
        param: Description.
        sandbox: Sandbox name (defaults to AEP_SANDBOX_NAME env var).
    """
    try:
        return aep_get("/path", sandbox=sandbox or None, params={"key": param})
    except Exception as exc:
        return {"error": str(exc)}
```

Key rules:
- Always wrap in try/except returning `{"error": str(exc)}`
- `sandbox=sandbox or None` — pass `None` to let auth.py use the profile default
- Import only what you need from `auth`: `aep_get`, `aep_post`, `aep_patch`, `aep_delete`
- Register new modules in `server.py` (import + `module.register(mcp)`)

## Adding a New Tool Module

1. Create `tools/new_domain.py` with a `register(mcp)` function
2. Add to `server.py` imports and call `new_domain.register(mcp)`
3. No other files need changing

## Multi-Org Configuration

Credentials live in `orgs.json` (gitignored — copy `orgs.example.json` to get started). Each profile maps to one Adobe org. To add a new org, add a profile entry to `orgs.json`:

```json
"NewClient": {
  "client_id": "...",
  "client_secret": "...",
  "api_key": "...",
  "org_id": "XXXX@AdobeOrg",
  "sandbox": "prod"
}
```

Credentials come from Adobe Developer Console → Project → OAuth Server-to-Server.

## Auth Flow

`auth.py` checks `orgs.json` profiles first, falls back to env vars (`.env`).

- **OAuth S2S** (recommended): set `client_id` + `client_secret` — token auto-refreshes before expiry, per-profile cache
- **Static token** (dev/testing): set `access_token` — no auto-refresh

## Adobe Documentation Skills

Four Claude Code skills are bundled in `.claude/skills/` and available automatically when working in this repo:

| Slash command | Covers |
|---|---|
| `/aep` | XDM, Data Ingestion, Sources, Real-Time Customer Profile, Identity, Segmentation, Destinations, Query Service, Data Governance, Web SDK, Sandboxes |
| `/ajo` | Journeys, Campaigns, Offers, Offer Decisioning, Messages, Channels |
| `/cja` | Customer Journey Analytics, Data Views, Workspace reports, Calculated Metrics |
| `/rtcdp` | Destinations, Audience Activation, B2B/B2P, Data Governance |

Each skill fetches live content from Adobe Experience League and quotes with citations — it never answers from memory. Use these whenever you need to look up API behaviour, limits, or best practices before implementing.

## Dependencies

```
mcp[cli]>=1.3.0
httpx>=0.27.0
python-dotenv>=1.0.0
```

Install: `pip install -r requirements.txt`
