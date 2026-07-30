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

### 2. Configure credentials

```bash
cp orgs.example.json orgs.json
```

Open `orgs.json` and fill in your values — see the inline comments in `orgs.example.json` for guidance on every field. The minimum required fields per profile are:

```json
{
  "default": "my_org",
  "profiles": {
    "my_org": {
      "client_id": "<from Adobe Developer Console>",
      "client_secret": "<from Adobe Developer Console>",
      "api_key": "<same as client_id>",
      "org_id": "<XXXX@AdobeOrg>",
      "sandbox": "<your-sandbox-name>"
    }
  }
}
```

**`orgs.json` is gitignored — it will never be committed.**

Alternatively, use environment variables (`.env` file):
```
AEP_CLIENT_ID=...
AEP_CLIENT_SECRET=...
AEP_API_KEY=...
AEP_ORG_ID=...
AEP_SANDBOX_NAME=...
```

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

## Guided setup wizard

If you prefer a step-by-step interactive setup, open Claude Code in the repo directory and run:

```
/aep-mcp-setup
```

The wizard will collect your credentials, auto-discover your sandboxes, identity namespace IDs, and merge policy IDs, and write a complete `orgs.json` for you.

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

## Finding required values

### Sandbox names
In the AEP UI, click the sandbox switcher in the top-right corner, or run `list_sandboxes` after connecting.

### Identity namespace code and ID
Run `list_identity_namespaces` after connecting. Find your primary identity namespace (e.g. `Email`, `ECID`, or a custom one like `CRMID`) and note its `id` (integer) and `code` (string). Add these to `orgs.json` under `namespaces`.

### Merge policy IDs
Run `list_merge_policies` after connecting. Note the UUID of your default (or Edge-activated) merge policy and add it to `orgs.json` under `merge_policies`.

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
