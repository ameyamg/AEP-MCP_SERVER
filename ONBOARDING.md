# AEP MCP Server — Onboarding Guide

A FastMCP server that exposes **115+ Adobe Experience Platform and AJO tools** directly inside Claude. Query datasets, inspect schemas, look up profiles, run SQL, manage segments, build journeys, configure dataflows, and more — all through natural language.

---

## What you get

| Domain | Tools |
|--------|-------|
| Datasets & Batches | list, get, create datasets; inspect batches |
| XDM Schemas | list, get, create schemas, field groups, descriptors |
| Real-Time Profiles | look up profiles by identity, browse identity graph |
| Identity Namespaces | list and inspect namespaces |
| Audience Segments | list, get, create segments; run batch jobs |
| Query Service | run ad-hoc SQL, manage templates and scheduled queries |
| AJO Journeys & Campaigns | list, inspect, get journey/campaign details |
| Offer Decisioning | offers, activities, collections, placements, rankings |
| Flow Service | sources, destinations, connections, dataflows, flow runs |
| Data Hygiene | dataset TTL, record delete orders, quota |
| Data Prep | mapping sets, expression validation, preview |
| Computed Attributes | list, get, create, update |
| Observability | metrics, alert subscriptions |
| Access Control | roles, permissions, effective policies |
| CJA | connections, data views, filters, calculated metrics, reports |
| Multi-Org | switch between org profiles and sandboxes at runtime |

---

## Prerequisites

- Python 3.10+
- Access to at least one Adobe Experience Platform org
- An **Adobe Developer Console** project with the **Experience Platform API** product added and an **OAuth Server-to-Server** credential created
  → [developer.adobe.com/console/projects](https://developer.adobe.com/console/projects)
- Claude Code (CLI or IDE extension)

---

## Quick setup (5 minutes)

### 1. Clone and install

```bash
git clone https://github.com/amghanekar-deloitte/AEP-MCP_SERVER.git
cd AEP-MCP_SERVER
pip install -r requirements.txt
```

### 2. Configure credentials — required fields only

```bash
cp orgs.example.json orgs.json
```

You only need to fill in **5 fields** to connect. Everything else (sandbox aliases, namespace IDs, merge policy IDs) is auto-discoverable once you're connected.

```json
{
  "default": "my_org",
  "profiles": {
    "my_org": {
      "client_id": "<from Adobe Developer Console>",
      "client_secret": "<from Adobe Developer Console>",
      "api_key": "<same as client_id>",
      "org_id": "<XXXX@AdobeOrg>",
      "sandbox": "<any valid sandbox name, e.g. prod>"
    }
  }
}
```

All credentials come from **Adobe Developer Console → your project → OAuth Server-to-Server**.

**`orgs.json` is gitignored — it will never be committed.**

### 3. Register with Claude Code

Add to `.claude/mcp_servers.json` (create if it doesn't exist):

```json
{
  "aep": {
    "command": "python",
    "args": ["/absolute/path/to/AEP-MCP_SERVER/server.py"]
  }
}
```

Run `pwd` in the repo directory to get the absolute path.

### 4. Restart Claude Code

Run `/mcp` in Claude Code to reload servers. You should see `aep` listed as connected.

---

## Auto-discovering optional values

Once you're connected with the 5 required fields, you can have Claude populate the rest of `orgs.json` automatically. Ask Claude:

> *"Discover my sandboxes and update orgs.json"*
> *"Find my identity namespaces for the prod sandbox and add them to orgs.json"*
> *"List my merge policies for all sandboxes and update the profile"*

Or use the tools directly and paste the values in manually:

| What to discover | Tool to run | Field in orgs.json |
|---|---|---|
| Available sandbox names | `list_sandboxes` | `sandboxes.dev`, `sandboxes.prod` |
| Primary identity namespace code + ID | `list_identity_namespaces` | `namespaces.<sandbox>.primary`, `primary_id` |
| Default merge policy UUID | `list_merge_policies` | `merge_policies.<sandbox>.primary` |

You can always edit `orgs.json` manually to correct or refine any discovered value.

---

## Guided setup wizard (all-in-one)

For a fully interactive setup that collects credentials AND auto-discovers all optional values in one session, open Claude Code in the repo directory and run:

```
/aep-mcp-setup
```

The wizard walks you through credentials → sandboxes → namespaces → merge policies and writes a complete `orgs.json` in one go.

---

## Multi-org and multi-sandbox usage

The server supports multiple org profiles in `orgs.json`. Switch between them at runtime with Claude:

> *"Switch to the client_b profile"*
> *"Switch to the prod sandbox"*
> *"Which org am I currently in?"*

Useful tools:
- `list_org_profiles` — see all configured profiles
- `switch_org_profile` — switch active org
- `get_current_org` — show active org and sandbox
- `switch_sandbox` — switch sandbox within current org (accepts alias or full name)
- `reset_sandbox` — return to profile default

---

## Optional: RT-CDP proxy

To also expose Adobe's official Real-Time CDP MCP tools, add a second entry to `.claude/mcp_servers.json`:

```json
{
  "aep": {
    "command": "python",
    "args": ["/absolute/path/to/AEP-MCP_SERVER/server.py"]
  },
  "rtcdp": {
    "command": "python",
    "args": ["/absolute/path/to/AEP-MCP_SERVER/rtcdp_proxy.py"]
  }
}
```

Set `RTCDP_MCP_URL` in your `.env` if the upstream URL differs from the default (`https://rtcdp-mcp.adobe.io/mcp`).

---

## Security notes

- `orgs.json` and `.env` are both gitignored — **never commit them**
- Credentials use OAuth Server-to-Server (auto-refreshing tokens) — no manual token rotation needed
- All tool calls stay local; no data is sent anywhere except to Adobe's APIs

---

## Troubleshooting

| Symptom | Fix |
|---------|-----|
| `ModuleNotFoundError: mcp` | Run `pip install -r requirements.txt` |
| `401 Unauthorized` | Check `client_id`, `client_secret`, `org_id` in `orgs.json`; verify the Experience Platform API product is added in Developer Console |
| `403 Forbidden` | Your technical account may lack the required product profile permissions in AEP Admin Console |
| Wrong sandbox returned | Set `sandbox` in your profile or `AEP_SANDBOX_NAME` env var |
| Token not refreshing | Make sure you're using OAuth S2S (not a static `access_token`) |

---

## Program delivery methodology

This server handles **API execution** — actually doing things in AEP/AJO. For program strategy,
architecture decisions, AEM content design, data-layer architecture, Adobe Tags/Web SDK, Adobe
Target, and delivery phasing, use the Deloitte enterprise **`adobe-experience-cloud`** skill
alongside this server. The two are designed to work together:

> `adobe-experience-cloud` skill → strategy + architecture → **AEP MCP Server tools** → execution

---

## Delivery asset templates

Use these templates during the Architect and Personalize phases. They are pre-wired with references
to the MCP tools that populate each section.

### Data-layer and XDM collection spec
[`assets/experience-data-layer-spec.md`](./assets/experience-data-layer-spec.md)

The contract between engineering, analytics, and data teams: event taxonomy, data elements, XDM
field mapping, identity namespaces, consent, and AEP dataset plan. Relevant MCP tools are called
out inline (`list_schemas`, `list_identity_namespaces`, `list_descriptors`, etc.).

### AJO journey design canvas
[`assets/journey-design-canvas.md`](./assets/journey-design-canvas.md)

One-page journey design: audience entry, channel steps, decisioning, consent gates, exit criteria,
and KPIs. MCP tools for pulling live objects are called out inline (`list_segments`, `list_offers`,
`list_offer_activities`, `cja_run_report`, etc.).

**Usage:** copy the template file, fill in your engagement specifics, and ask Claude to populate
the AEP-specific fields (schema IDs, segment IDs, namespace codes) using the connected MCP tools.

---

## Questions or issues?

Open an issue at [github.com/amghanekar-deloitte/AEP-MCP_SERVER/issues](https://github.com/amghanekar-deloitte/AEP-MCP_SERVER/issues).
