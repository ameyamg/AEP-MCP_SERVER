---
name: aep-mcp-server
description: >-
  Execute operations directly inside Adobe Experience Platform (AEP) and Adobe
  Journey Optimizer (AJO) using 115+ MCP tools — query real-time profiles,
  inspect or create XDM schemas and datasets, run ad-hoc SQL, build audience
  segments, orchestrate Flow Service dataflows, ingest data, manage AJO
  journeys and offer decisioning, and switch between multiple client org
  profiles at runtime. Reach for this skill whenever the work involves
  actually doing something inside AEP/AJO, not just planning it. For program
  strategy, delivery methodology, AEM content design, or data-layer
  architecture, pair with the adobe-experience-cloud methodology skill.
license: For internal Deloitte engagement use. No client-confidential content.
---

# AEP MCP Server

## Overview

This skill connects Claude directly to Adobe Experience Platform and Adobe
Journey Optimizer REST APIs through a FastMCP server. Every tool runs against
a live AEP org — reading, creating, or updating real platform objects. It
supports **multiple client org profiles** (each with their own credentials,
sandboxes, identity namespaces, and merge policies) and lets you switch
between them at any point in the conversation.

**What "good" looks like:** a consultant or engineer uses natural language to
navigate across datasets, schemas, profiles, and journeys — without leaving
Claude — while the platform state stays authoritative. The server never caches
business data; it reads and writes through AEP APIs on every call.

**Pairs with:** the `adobe-experience-cloud` methodology skill for strategy,
architecture decisions, delivery phases, and AEM/Tags/Target/Analytics
coverage that this skill does not provide.

## When to Use

Use this skill when the request involves any of:

- **Querying AEP** — look up a real-time profile by identity, browse the
  identity graph, run SQL in Query Service, preview a segment.
- **Managing schemas and datasets** — list, inspect, create, or update XDM
  schemas, field groups, descriptors, or datasets.
- **Audience segmentation** — list, create, or evaluate segment definitions;
  run batch segment jobs; check streaming job status.
- **AJO journeys and campaigns** — list or inspect journey versions, campaign
  details, offer decisioning objects (offers, activities, collections,
  rankings).
- **Data ingestion and flow service** — create source/target connections,
  build mapping sets with Data Prep expressions, launch dataflows or flow
  runs.
- **Platform operations** — data hygiene (TTL, record deletes), computed
  attributes, observability metrics, access control roles and policies.
- **Multi-org / multi-sandbox work** — switch between client org profiles and
  sandboxes at runtime without restarting the server.

**When NOT to use:**
- For program strategy, experience vision, delivery phases, or KPI definition
  → use `adobe-experience-cloud`.
- For AEM Sites/Assets, headless content fragments, or Adobe Tags/Web SDK
  architecture → use `adobe-experience-cloud`.
- For Adobe Target A/B testing or Adobe Analytics workspace design → use
  `adobe-experience-cloud`.
- For Salesforce CRM or Salesforce Data Cloud → use
  `salesforce-sales-service-cloud` or `salesforce-data-cloud-cdp`.

## Tool Domains

| Domain | What you can do |
|--------|----------------|
| **Datasets & Batches** | List, get, create datasets; inspect batch status |
| **XDM Schemas** | List, get, create schemas, field groups, descriptors, data types |
| **Real-Time Profiles** | Look up profiles by identity; traverse identity graph |
| **Identity Namespaces** | List namespaces; get details by code or ID |
| **Audience Segments** | List, get, create segment definitions; run and monitor batch jobs |
| **Query Service** | Run ad-hoc SQL; manage templates and scheduled queries |
| **AJO Journeys & Campaigns** | List, get journey versions and campaign details |
| **Offer Decisioning** | Offers, collections, placements, activities, ranking formulas |
| **Flow Service** | Source/target connections, dataflows, flow runs, connection specs |
| **Data Prep** | Mapping sets, mappings, expression validation, preview |
| **Data Hygiene** | Dataset TTL expirations, record delete orders, quota |
| **Computed Attributes** | List, get, create, update computed attributes |
| **Observability** | Platform metrics, alert subscriptions and notifications |
| **Access Control (ABAC)** | Roles, permissions, policies, effective policies |
| **CJA** | Connections, data views, filters, calculated metrics, reports |
| **Multi-Org** | List profiles, switch org, switch sandbox, reset to default |
| **RT-CDP proxy** | Adobe's official RT-CDP MCP tools via auth-proxied connection |

## Setup

New users: run `/aep-mcp-setup` for a guided wizard that collects credentials,
auto-discovers sandboxes, identity namespace IDs, and merge policies, and
writes a complete `orgs.json` profile.

Full instructions: see [ONBOARDING.md](./ONBOARDING.md).

## Delivery Assets

Use these templates during the Architect and Personalize phases of an AEC
program. They pair with the `adobe-experience-cloud` methodology skill.

- **[assets/experience-data-layer-spec.md](./assets/experience-data-layer-spec.md)**
  — Data layer and XDM collection specification: events, data elements, identity,
  consent, and XDM field mapping. Use `list_schemas`, `list_identity_namespaces`,
  and `list_descriptors` to populate the AEP-specific fields.
- **[assets/journey-design-canvas.md](./assets/journey-design-canvas.md)**
  — AJO journey design canvas: audience entry, channel steps, decisioning,
  consent gates, exit criteria, and KPIs. Use `list_segments`, `list_journeys`,
  and `list_offers` to pull live platform objects into the canvas.

## Guidelines

- **Read before write.** Use `get_*` and `list_*` tools to confirm current
  state before creating or modifying platform objects.
- **Sandbox first.** Always confirm the active sandbox (`get_current_org`)
  before running mutations. Use dev/staging sandboxes for exploratory work.
- **Credentials stay in `orgs.json`.** Never include client IDs, secrets, or
  org IDs in chat. `orgs.json` is gitignored and never committed.
- **Multi-org discipline.** When switching org profiles mid-conversation,
  confirm the switch with `get_current_org` before issuing write operations.
- **Pair with methodology.** These tools execute what the
  `adobe-experience-cloud` skill designs — use them together for full program
  delivery: strategy → architecture → implementation.
