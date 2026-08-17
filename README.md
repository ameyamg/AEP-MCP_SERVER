# AEP MCP Server

Two MCP servers that give Claude (and any MCP-compatible client) natural-language access to Adobe Experience Platform, Adobe Journey Optimizer, and Real-Time CDP.

| Server | File | Tools | Description |
|--------|------|-------|-------------|
| **AEP** (custom-built) | `server.py` | 137+ | Full AEP/AJO API coverage built with FastMCP |
| **RT-CDP** (Adobe official proxy) | `rtcdp_proxy.py` | 18 | Proxies Adobe's official `rtcdp-mcp.adobe.io` server |

---

## Quick Start

### 1. Install dependencies

```bash
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Configure credentials

Copy the example and fill in your credentials from **Adobe Developer Console → Project → OAuth Server-to-Server**:

```bash
cp orgs.example.json orgs.json
# edit orgs.json with your client_id, client_secret, org_id, sandbox
```

Or use environment variables (single-org fallback):

```bash
cp .env.example .env
# edit .env
```

### 3. Register with Claude Code

Copy `.mcp.json.example` to `.mcp.json` and update the paths:

```bash
cp .mcp.json.example .mcp.json
# edit .mcp.json — update /path/to/aep-mcp-server to your actual path
```

Or add manually to `.claude/mcp_servers.json`:

```json
{
  "aep": {
    "command": "/path/to/aep-mcp-server/.venv/bin/python",
    "args": ["/path/to/aep-mcp-server/server.py"]
  },
  "rtcdp": {
    "command": "/path/to/aep-mcp-server/.venv/bin/python",
    "args": ["/path/to/aep-mcp-server/rtcdp_proxy.py"]
  }
}
```

> Use the **absolute path to the venv Python** (`.venv/bin/python`) so the MCP client finds the right interpreter regardless of the system `python3` or any active conda environment.

### 4. Install the pre-commit hook (recommended)

Blocks accidental credential commits:

```bash
python3 scripts/install_hooks.py
```

### 5. Run

```bash
python3 server.py                        # AEP server, default org profile
AEP_PROFILE=MyClient python3 server.py  # start with a specific profile
```

---

## Multi-Org Configuration

`orgs.json` supports multiple named profiles — useful when working across different Adobe orgs or sandboxes:

```json
{
  "default": "ClientA",
  "profiles": {
    "ClientA": {
      "client_id": "...",
      "client_secret": "...",
      "api_key": "...",
      "org_id": "XXXX@AdobeOrg",
      "sandbox": "prod",
      "sandboxes": {
        "dev": "my-sandbox-dev",
        "prod": "my-sandbox-prod"
      }
    },
    "ClientB": {
      "client_id": "...",
      "client_secret": "...",
      "api_key": "...",
      "org_id": "YYYY@AdobeOrg",
      "sandbox": "prod"
    }
  }
}
```

Switch orgs at runtime with the `switch_org_profile` tool or by setting `AEP_PROFILE` at startup. Token caches are maintained per profile.

---

## Server 1 — AEP MCP (`server.py`)

Built with [FastMCP](https://github.com/jlowin/fastmcp). All tools accept an optional `sandbox` parameter; if omitted, the active profile's default sandbox is used.

### Datasets & Batches
`list_datasets` · `get_dataset` · `create_dataset` · `get_batch` · `list_batches` · `get_sandbox` · `list_sandboxes` · `reset_sandbox`

### XDM Schema Registry
`list_schemas` · `get_schema` · `create_schema` · `enable_schema_for_profile` · `list_field_groups` · `get_field_group` · `create_field_group` · `list_classes` · `list_data_types` · `list_descriptors` · `create_descriptor`

### Real-Time Customer Profile & Identity
`get_profile_by_identity` · `get_identity_cluster` · `list_identity_namespaces` · `get_identity_namespace` · `list_merge_policies` · `list_profile_export_jobs` · `get_profile_export_job`

### Segmentation / Audiences
`list_segments` · `get_segment` · `create_segment` · `delete_segment` · `list_segment_jobs` · `get_segment_job` · `create_segment_job` · `list_streaming_jobs`

### Query Service
`list_queries` · `get_query` · `run_query` · `cancel_query` · `list_query_runs` · `list_query_templates` · `get_query_template` · `create_query_template` · `list_scheduled_queries`

### AJO — Journeys & Campaigns
`list_journeys` · `get_journey` · `list_journey_versions` · `list_campaigns` · `get_campaign`

### AJO — Offer Decisioning
`list_offers` · `get_offer` · `list_placements` · `list_collections` · `list_offer_activities` · `get_offer_activity` · `list_ranking_formulas` · `create_eligibility_rule`

### Flow Service (Sources & Destinations)
`list_connections` · `get_connection` · `list_connection_specs` · `get_connection_spec` · `list_dataflows` · `get_dataflow` · `list_flow_runs` · `get_flow_run` · `list_source_connections` · `get_source_connection` · `list_target_connections` · `get_target_connection`

### Observability Insights & Alerts
`get_metrics` · `list_alert_subscriptions` · `get_alert_subscription` · `get_alerts_by_feature` · `list_alert_notifications` · `subscribe_alert`

### Data Hygiene
`list_dataset_expirations` · `get_dataset_expiration` · `create_dataset_expiration` · `cancel_dataset_expiration` · `list_record_delete_orders` · `get_record_delete_order` · `create_record_delete_order` · `get_hygiene_quota`

### Data Prep (Mapping)
`list_mapping_sets` · `get_mapping_set` · `create_mapping_set` · `preview_mapping_set` · `list_mappings` · `get_mapping` · `validate_mapping_expression` · `list_data_prep_functions`

### Computed Attributes
`list_computed_attributes` · `get_computed_attribute` · `create_computed_attribute` · `update_computed_attribute`

### Access Control (ABAC)
`list_roles` · `get_role` · `list_role_subjects` · `list_role_policies` · `list_policies` · `get_policy` · `get_effective_policies` · `list_available_permissions` · `list_users` · `get_user_roles`

### Customer Journey Analytics (CJA)
CJA tools use a Data View ID instead of a sandbox.

`cja_list_connections` · `cja_get_connection` · `cja_list_data_views` · `cja_get_data_view` · `cja_list_dimensions` · `cja_list_metrics` · `cja_list_projects` · `cja_get_project` · `cja_create_project` · `cja_update_project` · `cja_delete_project` · `cja_list_filters` · `cja_get_filter` · `cja_create_filter` · `cja_update_filter` · `cja_delete_filter` · `cja_list_calculated_metrics` · `cja_get_calculated_metric` · `cja_create_calculated_metric` · `cja_update_calculated_metric` · `cja_delete_calculated_metric` · `cja_list_annotations` · `cja_create_annotation` · `cja_delete_annotation` · `cja_run_report`

### Org & Multi-Org Management
`list_org_profiles` · `get_current_org` · `switch_org_profile` · `switch_sandbox`

---

## Server 2 — RT-CDP Proxy (`rtcdp_proxy.py`)

A lightweight stdio→HTTPS proxy that forwards tool calls to **Adobe's official Real-Time CDP MCP server** at `rtcdp-mcp.adobe.io`. Auth headers are sourced from the active `orgs.json` profile, so `switch_org_profile` works across both servers.

Configure the upstream URL via `.env` (optional — defaults to Adobe's endpoint):

```
RTCDP_MCP_URL=https://rtcdp-mcp.adobe.io/mcp
```

> **Note:** Adobe's RT-CDP MCP server is a gated feature. Contact your Adobe representative for access.

### Tools (proxied from Adobe)
`search_audiences` · `preview_audience_membership` · `inspect_audience_evaluation_jobs` · `inspect_audience_export_jobs` · `search_destination_connectors` · `search_destination_accounts` · `search_destination_flows` · `search_destination_input_connections` · `search_destination_output_connections` · `search_source_connectors` · `search_source_accounts` · `search_source_flows` · `search_source_input_connections` · `search_source_output_connections` · `search_identity_namespaces` · `search_merge_policies` · `search_organizations` · `inspect_flow_runs`

---

## Project Layout

```
server.py                  # AEP FastMCP entrypoint
rtcdp_proxy.py             # RT-CDP stdio→HTTPS proxy
auth.py                    # Auth + HTTP helpers; multi-org profile state
orgs.json                  # Your credentials — GITIGNORED, never commit
orgs.example.json          # Template for orgs.json
.env / .env.example        # Fallback single-org config
requirements.txt
hooks/pre-commit           # Blocks credential commits
scripts/install_hooks.py   # Installs the pre-commit hook
tools/
  datasets.py              # Catalog Service: datasets, batches, sandboxes
  schemas.py               # Schema Registry: XDM schemas, classes, field groups
  profiles.py              # Real-Time Customer Profile, identity, merge policies
  segments.py              # Segmentation: definitions, jobs, streaming
  query.py                 # Query Service: ad-hoc SQL, templates, scheduled
  ajo.py                   # AJO: journeys, campaigns, offers, eligibility rules
  cja.py                   # Customer Journey Analytics
  flows.py                 # Flow Service: connections, dataflows, flow runs
  observability.py         # Observability Insights: metrics, alerts
  data_hygiene.py          # Data Hygiene: dataset TTL, record deletes
  data_prep.py             # Data Prep: mapping sets, expression validation
  computed_attributes.py   # Computed Attributes
  access_control.py        # ABAC: roles, permissions, effective policies
  orgs.py                  # Multi-org: list/switch profiles and sandboxes
  usage_logger.py          # @track decorator — logs tool calls to CSV
```

---

## Adding a New Tool Module

1. Create `tools/new_domain.py` with a `register(mcp)` function
2. Add to `server.py`: import it and call `new_domain.register(mcp)`
3. Follow the tool pattern in `CLAUDE.md`

## Auth Flow

`auth.py` checks `orgs.json` profiles first, then falls back to `.env` environment variables.

- **OAuth S2S** (recommended): set `client_id` + `client_secret` — token auto-refreshes before expiry
- **Static token** (dev/testing): set `access_token` — no auto-refresh

## Requirements

```
mcp[cli]>=1.3.0
httpx>=0.27.0
python-dotenv>=1.0.0
```
