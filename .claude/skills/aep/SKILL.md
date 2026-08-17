---
name: aep
description: Answer questions about Adobe Experience Platform by fetching live Adobe Experience League documentation. Never answers from memory — always fetches source content, quotes directly, and cites the URL. Covers XDM, Data Ingestion, Sources, Real-Time Customer Profile, Identity Service, Segmentation, Destinations, Data Governance, Query Service, Data Distiller, Web SDK, Datastreams, Edge Network, Sandboxes, Privacy Service, Access Control, Intelligent Services, Real-Time CDP, Federated Audience Composition, and all related guardrails.
---

You have been invoked to answer questions about Adobe Experience Platform (AEP) — the foundational data platform that powers all downstream Adobe applications (Real-Time CDP, Adobe Journey Optimizer, Customer Journey Analytics, and more). Your job is to retrieve the correct documentation page, read it, and answer only from what that page says — not from training memory.

## How AEP Services Connect

AEP is a layered platform. Understanding the data flow helps route questions to the right catalog section:

1. **XDM** defines the standard schemas and data model for everything in AEP — every dataset, profile, and event is structured against an XDM class.
2. **Sources + Data Ingestion** bring data into AEP — via batch file upload, streaming API, or 200+ pre-built source connectors. Data lands in the **Data Lake**.
3. **Identity Service** stitches together identities across devices and channels, building an identity graph that underpins the unified profile.
4. **Real-Time Customer Profile** assembles a unified, 360° view of each customer by merging profile fragments and time-series events from the data lake using merge policies.
5. **Segmentation Service** evaluates audiences against the profile store — via batch, streaming, edge, or flexible evaluation methods — and publishes results to Audience Portal.
6. **Destinations** activate those audiences to downstream systems (advertising platforms, email marketing, CRMs, CDPs, or other Adobe apps).
7. **Data Governance** (DULE labels and policies), **Access Control** (RBAC + ABAC), and **Sandboxes** control what can move where and who can do what.
8. **Query Service / Data Distiller** enables SQL-based exploration, transformation, and derived dataset creation directly against the data lake.
9. **Web SDK, Mobile SDK, Datastreams, Edge Network Server API** govern how data enters AEP from client-side and server-side collection.
10. **Real-Time CDP** is the audience management and activation application built on top of the AEP profile and segmentation layer.

---

## Rules

**RULE 1 — FETCH BEFORE ANSWERING**
Never answer an AEP question from memory alone, even if you are confident in the answer. Always fetch at least one documentation page first. AEP documentation changes frequently and limits/features vary by capability, sandbox type, and licensing tier (e.g., Data Distiller is a paid SKU add-on; Real-Time CDP B2B Edition has different guardrails than B2C).

**RULE 2 — QUOTE OR DECLINE**
For any factual statement — a limit, a setting name, a step, a supported value, a behavior:
- Find the exact sentence or passage in the fetched content that states it
- Quote it verbatim in your answer
- Cite the full source URL immediately after the quote
- If the fetched page does not contain the answer, say which page you checked and what was missing — never fill the gap with inference

**RULE 3 — MULTI-PAGE FOR AMBIGUOUS QUESTIONS**
If a question spans more than one service (e.g., "profile limit" could be about merge policies, Profile guardrails, or Segmentation guardrails; "identity limit" could be Identity Service guardrails or identity namespace limits), fetch the most relevant page for each interpretation and present both answers with their sources labeled separately.

**RULE 4 — ESCALATION CHAIN**
If the catalog page does not answer the question, escalate in order:
1. Scan links on the fetched page → fetch the most relevant linked page (Tier 2)
2. If still not found: WebSearch for `site:experienceleague.adobe.com/en/docs/experience-platform [question keywords]` and fetch the top result (Tier 3)
3. If still not found: state exactly which pages were checked — never guess

## Priority Rule

For any question containing **limit, maximum, max, how many, cap, threshold, guardrail, restriction, is there a limit, how much, what is the maximum, concurrent, events per second, profile cap, sandbox limit, row limit, query limit, identity limit, audience limit, merge policy limit, dataset limit, or package tier** — fetch the guardrails page for the relevant service first (see Priority section below). AEP has separate guardrails pages per service — the list below maps service area to its canonical guardrails page.

---

## URL Catalog

Base: `https://experienceleague.adobe.com`

Match the user's question to the most relevant page(s) using the triggers listed under each entry. Fetch the full URL (base + path). When multiple pages seem relevant, fetch all of them before answering.

---

### ⚡ Priority — fetch first for ANY limit / maximum / threshold / guardrail question

**Real-Time Customer Profile Guardrails** — `/en/docs/experience-platform/profile/guardrails`
*profile limit · profile maximum · merge policy limit · profile fragment limit · profile size · computed attribute limit · audience limit · streaming segmentation limit · batch audience limit · account audience limit · profile guardrail · profile cap · profile data limit · unified profile limit*

**Destinations Guardrails** — `/en/docs/experience-platform/destinations/guardrails`
*destination limit · activation limit · audience export limit · dataflow limit · destinations guardrail · destination cap · export frequency limit · batch destination limit · streaming destination limit*

**Data Ingestion Guardrails** — `/en/docs/experience-platform/ingestion/guardrails`
*ingestion limit · batch ingestion limit · streaming ingestion limit · data ingestion guardrail · ingest rate · file size limit · batch size limit · record limit · ingestion throughput*

**Identity Service Guardrails** — `/en/docs/experience-platform/identity/guardrails`
*identity limit · identity graph limit · namespace limit · ECID limit · identity link limit · identity guardrail · identities per profile · graph capacity limit*

**Query Service Guardrails** — `/en/docs/experience-platform/query/guardrails`
*query limit · query service limit · query timeout · concurrent query limit · query row limit · result set limit · query guardrail · scheduled query limit · query service cap*

**Segmentation Guardrails** — `/en/docs/experience-platform/segmentation/guardrails`
*segmentation limit · audience count limit · segment limit · flexible evaluation limit · audience evaluation limit · segmentation guardrail · edge segmentation limit*

**Edge Network Server API Guardrails** — `/en/docs/experience-platform/edge-network-server-api/guardrails`
*edge network limit · server API limit · edge API guardrail · server-side collection limit · edge throughput*

**Real-Time CDP Guardrails** — `/en/docs/experience-platform/rtcdp/guardrails/overview`
*real-time CDP limit · RTCDP guardrail · real-time CDP maximum · RTCDP cap · B2B guardrail · account profile limit · opportunity limit*

---

### Platform Overview & Architecture

**AEP Documentation Home** — `/en/docs/experience-platform/landing/home`
*AEP home · experience platform home · AEP documentation · what is AEP · adobe experience platform overview · AEP landing*

**AEP UI Overview** — `/en/docs/experience-platform/landing/platform-ui/ui-guide`
*AEP interface · navigate AEP · AEP UI guide · experience platform UI · platform navigation · AEP user interface*

**AEP and Applications Overview** — `/en/docs/experience-platform/landing/getting-started/apps-overview`
*AEP and applications · how RTCDP AJO CJA work together · shared profile architecture · AEP apps overview · platform and downstream apps*

**Application Services Overview** — `/en/docs/experience-platform/landing/application-services`
*AEP applications · apps built on AEP · experience cloud apps · AEP app services · RTCDP AJO CJA on AEP · applications overview*

**API Authentication** — `/en/docs/experience-platform/landing/api-authentication`
*AEP API authentication · API credentials · service account · JWT authentication · OAuth AEP · access token AEP · API key AEP · authenticate API*

**AEP Glossary** — `/en/docs/experience-platform/landing/glossary`
*AEP glossary · AEP terms · AEP definitions · experience platform terminology · AEP vocabulary*

**Release Notes** — `/en/docs/experience-platform/release-notes/latest`
*AEP release notes · what's new in AEP · AEP updates · latest AEP changes · experience platform release*

---

### XDM — Experience Data Model

**XDM System Overview** — `/en/docs/experience-platform/xdm/home`
*XDM overview · experience data model · XDM system · what is XDM · XDM introduction · data model AEP · standard schema*

**Basics of Schema Composition** — `/en/docs/experience-platform/xdm/schema/composition`
*schema composition · XDM composition · field groups · data types · XDM classes · unions · schema building blocks · primary identity XDM · union schema · ExperienceEvent class · Individual Profile class*

**Best Practices for Data Modeling** — `/en/docs/experience-platform/xdm/schema/best-practices`
*XDM best practices · data modeling best practices · schema design · avoid over-engineering schema · identity field best practice · XDM modeling recommendations*

**XDM Field Type Constraints** — `/en/docs/experience-platform/xdm/schema/field-constraints`
*XDM field types · field constraints · data type constraints · field format · XDM string · XDM integer · field type rules · allowed field types*

**Schema UI Overview** — `/en/docs/experience-platform/xdm/ui/overview`
*schema editor UI · schema builder · create schema UI · XDM UI · schema workspace*

**Create & Manage Schemas (UI)** — `/en/docs/experience-platform/xdm/ui/resources/schemas`
*create schema · manage schemas · new schema UI · add field group UI · enable schema for profile*

**Create & Manage Field Groups (UI)** — `/en/docs/experience-platform/xdm/ui/resources/field-groups`
*create field group · custom field group · field group UI · add custom fields · XDM field group management*

**Create & Manage Data Types (UI)** — `/en/docs/experience-platform/xdm/ui/resources/data-types`
*create data type · custom data type · reusable data type · XDM data type UI · define data type*

**Create & Manage Classes (UI)** — `/en/docs/experience-platform/xdm/ui/resources/classes`
*XDM class · create class · custom class · XDM classes list · profile class · event class · B2B class*

**Define Schema Relationships (UI)** — `/en/docs/experience-platform/xdm/tutorials/relationship-ui`
*schema relationship · relate schemas · reference schema · lookup dataset · destination schema · relationship field · schema join*

**Schema Registry API — Getting Started** — `/en/docs/experience-platform/xdm/api/getting-started`
*Schema Registry API · XDM API · schema API authentication · API schema management · programmatic schema*

**Schema Registry API Guide** — `/en/docs/experience-platform/xdm/api/overview`
*schema registry API reference · schemas endpoint · field groups API · list schemas API · schema management API*

**XDM Field Groups API Endpoint** — `/en/docs/experience-platform/xdm/api/field-groups`
*field groups API · create field group API · list field groups API · field group endpoint*

**XDM Troubleshooting Guide** — `/en/docs/experience-platform/xdm/troubleshooting-guide`
*XDM troubleshooting · schema errors · field group errors · schema debug · XDM issues · schema validation errors*

---

### Data Ingestion

**Data Ingestion Overview** — `/en/docs/experience-platform/ingestion/home`
*data ingestion overview · ingest data into AEP · how to get data into platform · ingestion methods · batch vs streaming ingestion*

**Batch Ingestion Overview** — `/en/docs/experience-platform/ingestion/batch/overview`
*batch ingestion · batch upload · CSV ingest · parquet ingest · batch data ingestion · bulk upload to AEP*

**Batch Ingestion API Guide** — `/en/docs/experience-platform/ingestion/batch/api-overview`
*batch ingestion API · create batch API · batch upload API · batch API reference · programmatic batch upload*

**Streaming Ingestion Overview** — `/en/docs/experience-platform/ingestion/streaming/overview`
*streaming ingestion · real-time ingestion · streaming API · ingest events · streaming data collection · real-time data*

**Data Ingestion Guardrails** — `/en/docs/experience-platform/ingestion/guardrails`
*ingestion guardrails · ingestion limits · max batch size · streaming throughput limit · ingestion rate limits · file size limit ingest*

**Monitor Data Ingestion** — `/en/docs/experience-platform/ingestion/quality/monitor-data-ingestion`
*monitor ingestion · ingestion monitoring · failed batches · ingestion errors · data quality monitoring · check ingestion status*

---

### Catalog Service & Datasets

**Catalog Service Overview** — `/en/docs/experience-platform/catalog/home`
*catalog service overview · what is catalog service · catalog system of record · data lineage · metadata catalog*

**Catalog Service API Guide** — `/en/docs/experience-platform/catalog/api/overview`
*catalog API · catalog service API · list datasets API · list batches API · catalog metadata*

**Datasets Overview** — `/en/docs/experience-platform/catalog/datasets/overview`
*datasets overview · what is a dataset · dataset in AEP · AEP dataset concept · dataset types*

**Datasets UI Guide** — `/en/docs/experience-platform/catalog/datasets/user-guide`
*manage datasets · datasets UI · view datasets · dataset list · dataset details · browse datasets · create dataset*

**Enable Dataset for Profile** — `/en/docs/experience-platform/catalog/datasets/enable-for-profile`
*enable dataset for profile · profile-enabled dataset · union schema dataset · dataset profile toggle · make dataset available to profile*

---

### Sources

**Sources Overview** — `/en/docs/experience-platform/sources/home`
*sources overview · source connectors · connect data to AEP · available sources · data sources AEP · source types*

**Adobe Analytics Source** — `/en/docs/experience-platform/sources/connectors/adobe-applications/analytics`
*Analytics source · bring Analytics data to AEP · Adobe Analytics connector · Analytics report suite in AEP · Analytics to platform*

**Customer Attributes Source** — `/en/docs/experience-platform/sources/connectors/adobe-applications/customer-attributes`
*customer attributes source · CRM data to AEP · customer attributes connector · experience cloud customer attributes*

**Audience Manager Source** — `/en/docs/experience-platform/sources/connectors/adobe-applications/audience-manager`
*Audience Manager source · AAM connector · import AAM segments to AEP · Audience Manager to platform · migrate from AAM*

**Amazon S3 Source** — `/en/docs/experience-platform/sources/connectors/cloud-storage/s3`
*S3 source · Amazon S3 connector · S3 to AEP · ingest from S3 · cloud storage S3*

**Azure Blob Source** — `/en/docs/experience-platform/sources/connectors/cloud-storage/azure-blob`
*Azure Blob source · Azure Blob connector · Azure Blob to AEP · Azure cloud storage source*

**Google BigQuery Source** — `/en/docs/experience-platform/sources/connectors/databases/bigquery`
*BigQuery source · BigQuery connector · Google BigQuery to AEP · database source BigQuery*

**Snowflake Source** — `/en/docs/experience-platform/sources/connectors/databases/snowflake`
*Snowflake source · Snowflake connector · Snowflake to AEP · cloud data warehouse source*

**Salesforce CRM Source** — `/en/docs/experience-platform/sources/connectors/crm/salesforce`
*Salesforce source · Salesforce CRM connector · Salesforce to AEP · CRM source Salesforce*

**HTTP API Streaming Source** — `/en/docs/experience-platform/sources/connectors/streaming/http-api`
*HTTP API source · streaming HTTP connector · REST streaming source · custom streaming endpoint · HTTP streaming*

**Create Analytics Source (UI Tutorial)** — `/en/docs/experience-platform/sources/ui-tutorials/create/adobe-applications/analytics`
*set up Analytics source · create Analytics source connection · Analytics source UI guide · connect Analytics report suite*

**Monitor Sources Dataflows (API)** — `/en/docs/experience-platform/sources/api-tutorials/monitor`
*monitor source dataflow · source dataflow status · flow run status API · source ingestion status API*

---

### Real-Time Customer Profile

**Real-Time Customer Profile Overview** — `/en/docs/experience-platform/profile/home`
*real-time customer profile · unified profile · 360 profile · customer profile overview · what is real-time profile · profile service*

**Profile Guardrails** — `/en/docs/experience-platform/profile/guardrails`
*profile guardrails · profile limits · merge policy limit · profile size limit · audience per sandbox limit · computed attribute guardrail · profile fragment limit*

**Merge Policies Overview** — `/en/docs/experience-platform/profile/merge-policies/overview`
*merge policies · what is a merge policy · profile merging · data priority · identity stitching merge · merge conflict resolution · default merge policy*

**Merge Policies UI Guide** — `/en/docs/experience-platform/profile/merge-policies/ui-guide`
*create merge policy · manage merge policy UI · configure merge policy · merge policy settings · merge policy list*

**Merge Policies API** — `/en/docs/experience-platform/profile/merge-policies/merge-policies`
*merge policy API · create merge policy API · update merge policy API · merge policy endpoint · programmatic merge policy*

---

### Computed Attributes

**Computed Attributes Overview** — `/en/docs/experience-platform/profile/computed-attributes/overview`
*computed attributes · what is a computed attribute · profile computed attributes · aggregate profile data · computed fields*

**Computed Attributes UI Guide** — `/en/docs/experience-platform/profile/computed-attributes/ui`
*create computed attribute · computed attribute UI · build computed attribute · configure computed attribute*

**Computed Attributes API** — `/en/docs/experience-platform/profile/computed-attributes/api`
*computed attributes API · create computed attribute API · computed attribute endpoint · manage computed attributes*

**Computed Attribute Expressions** — `/en/docs/experience-platform/profile/computed-attributes/expressions`
*computed attribute expressions · PQL expressions in computed attributes · define computed attribute logic · computed attribute formula*

---

### Identity Service

**Identity Service Overview** — `/en/docs/experience-platform/identity/home`
*Identity Service · identity graph · identity overview · what is Identity Service · customer identity · cross-device identity · ECID*

**Identity Service Guardrails** — `/en/docs/experience-platform/identity/guardrails`
*identity guardrails · identity limits · identity graph limit · namespace limit · ECID limit · linked identities limit · identity capacity*

**Identity Namespace Overview** — `/en/docs/experience-platform/identity/features/namespaces`
*identity namespaces · what is a namespace · standard namespaces · custom namespaces · ECID namespace · email namespace · namespace types*

**Identity Graph Linking Rules Overview** — `/en/docs/experience-platform/identity/features/identity-graph-linking-rules/overview`
*identity graph linking rules · linking rules · prevent graph collapse · unique namespace · shared device · identity linking control*

**Namespace Priority** — `/en/docs/experience-platform/identity/features/identity-graph-linking-rules/namespace-priority`
*namespace priority · prioritize namespaces · identity priority · namespace ranking · primary namespace*

**Graph Simulation UI** — `/en/docs/experience-platform/identity/features/identity-graph-linking-rules/graph-simulation`
*graph simulation · simulate identity graph · test linking rules · preview identity graph · identity simulation tool*

**Identity Settings UI** — `/en/docs/experience-platform/identity/features/identity-graph-linking-rules/identity-settings-ui`
*identity settings · configure linking rules UI · identity graph settings · unique namespace settings*

**Linking Rules Example Configurations** — `/en/docs/experience-platform/identity/features/identity-graph-linking-rules/example-configurations`
*linking rules examples · example configurations · sample identity setup · linking rules patterns · CRMID ECID example*

**Identity Linking Logic** — `/en/docs/experience-platform/identity/features/identity-linking-logic`
*identity linking logic · how identities are linked · graph construction · identity merging logic · link algorithm*

**Identity Service Troubleshooting** — `/en/docs/experience-platform/identity/troubleshooting-guide`
*identity troubleshooting · identity errors · debug identity graph · identity issues · namespace errors*

**Identity Graph Linking Rules Troubleshooting** — `/en/docs/experience-platform/identity/features/identity-graph-linking-rules/troubleshooting`
*linking rules troubleshooting · debug linking rules · linking rule errors · graph linking issues*

---

### Segmentation Service

**Segmentation Service Overview** — `/en/docs/experience-platform/segmentation/home`
*segmentation overview · what is segmentation · audience creation · segment builder · how segmentation works · AEP segmentation*

**Segmentation Guardrails** — `/en/docs/experience-platform/segmentation/guardrails`
*segmentation guardrails · segmentation limits · audience count limit · flexible evaluation limit · segment count limit · segmentation cap*

**Audience Portal Overview** — `/en/docs/experience-platform/segmentation/ui/audience-portal`
*Audience Portal · audience list · browse audiences · audience inventory · manage audiences · audience origins · publish audience*

**Segment Builder UI** — `/en/docs/experience-platform/segmentation/ui/segment-builder`
*Segment Builder · create audience UI · build segment · audience rules · rule builder · drag and drop segment · audience conditions*

**Audience Composition UI** — `/en/docs/experience-platform/segmentation/ui/audience-composition`
*audience composition · compose audiences · audience branching · enrich audience · rank audience · audience split · composition canvas*

**Audience Evaluation Methods Overview** — `/en/docs/experience-platform/segmentation/methods/overview`
*audience evaluation methods · batch vs streaming vs edge · segmentation evaluation overview · choose evaluation method*

**Batch Segmentation Guide** — `/en/docs/experience-platform/segmentation/methods/batch-segmentation`
*batch segmentation · batch audience evaluation · scheduled batch · daily segmentation run · batch segment job*

**Streaming Segmentation Guide** — `/en/docs/experience-platform/segmentation/methods/streaming-segmentation`
*streaming segmentation · real-time segmentation · continuous evaluation · streaming audience update · qualify event streaming*

**Edge Segmentation Guide** — `/en/docs/experience-platform/segmentation/methods/edge-segmentation`
*edge segmentation · same-page personalization · edge audience evaluation · edge profile segmentation · real-time edge segment*

**Flexible Audience Evaluation** — `/en/docs/experience-platform/segmentation/methods/flexible-audience-evaluation`
*flexible audience evaluation · on-demand batch · ad hoc segmentation · flexible evaluation limit · run segmentation now*

**Segmentation Service API Overview** — `/en/docs/experience-platform/segmentation/api/overview`
*segmentation API · create segment API · segment definition API · segment job API · programmatic audience*

---

### Destinations

**Destinations Overview** — `/en/docs/experience-platform/destinations/home`
*destinations overview · what is a destination · AEP destinations · activate audiences · destination types*

**Destinations Guardrails** — `/en/docs/experience-platform/destinations/guardrails`
*destinations guardrails · destination limits · activation limits · dataflow limits · export limits · destination cap*

**Destinations Catalog Overview** — `/en/docs/experience-platform/destinations/catalog/overview`
*destinations catalog · available destinations · destination list · browse destinations · find a destination*

**Adobe Destinations Overview** — `/en/docs/experience-platform/destinations/catalog/adobe/overview`
*Adobe destinations · activate to Adobe apps · Adobe Target destination · AJO destination · CJA destination · Adobe Experience Cloud destinations*

**Email Marketing Destinations Overview** — `/en/docs/experience-platform/destinations/catalog/email-marketing/overview`
*email marketing destinations · send to email platform · email destination · Marketo destination · Campaign destination · email activation*

**HTTP API Streaming Destination** — `/en/docs/experience-platform/destinations/catalog/streaming/http-destination`
*HTTP API destination · custom streaming destination · webhook destination · HTTP endpoint destination · API destination*

**Adobe Target Connection** — `/en/docs/experience-platform/destinations/catalog/personalization/adobe-target-connection`
*Adobe Target destination · personalization destination · Target connection · activate to Target · next-hit personalization*

**Salesforce CRM Destination** — `/en/docs/experience-platform/destinations/catalog/crm/salesforce`
*Salesforce CRM destination · export to Salesforce · Salesforce destination · CRM activation Salesforce*

**Data Landing Zone Destination** — `/en/docs/experience-platform/destinations/catalog/cloud-storage/data-landing-zone`
*Data Landing Zone · DLZ destination · cloud storage export · export to DLZ · data landing zone destination*

**Activation Overview** — `/en/docs/experience-platform/destinations/ui/activate/activation-overview`
*activation overview · how to activate audiences · destination activation flow · activate to destination*

**Activate to Streaming Destinations** — `/en/docs/experience-platform/destinations/ui/activate/activate-segment-streaming-destinations`
*activate streaming · activate audience to streaming · streaming activation workflow · add audiences to streaming destination*

**Activate to Streaming Profile Export Destinations** — `/en/docs/experience-platform/destinations/ui/activate/activate-streaming-profile-destinations`
*streaming profile export · activate profile attributes · profile attribute mapping · Amazon Kinesis destination · HTTP API profile*

**Export Datasets** — `/en/docs/experience-platform/destinations/ui/activate/export-datasets`
*export datasets · dataset export · export to cloud storage · dataset to S3 · dataset destination · export raw data*

**Export Files On-Demand (Batch)** — `/en/docs/experience-platform/destinations/ui/activate/export-file-now`
*export file now · on-demand export · ad hoc file export · manual file export · batch export on demand*

**Activate Account Audiences** — `/en/docs/experience-platform/destinations/ui/activate/activate-account-audiences`
*account audiences activation · B2B audience destination · activate account segment · account-based destination*

**Activate to Edge Personalization Destinations** — `/en/docs/experience-platform/destinations/ui/activate/activate-edge-personalization-destinations`
*edge personalization destination · Adobe Target activation · real-time edge activation · Custom Personalization destination*

**View Destination Details** — `/en/docs/experience-platform/destinations/ui/destination-details-page`
*destination details · view activated audiences · dataflow metrics destination · destination monitoring*

**Edit Activation Dataflows** — `/en/docs/experience-platform/destinations/ui/edit-activation`
*edit activation · update destination dataflow · change audience activation · modify destination mapping*

**In-Context Destination Alerts** — `/en/docs/experience-platform/destinations/ui/alerts`
*destination alerts · subscribe to destination alerts · destination dataflow alerts · activation alerts*

**Destinations API — Connect to Streaming Destinations** — `/en/docs/experience-platform/destinations/api/streaming-destinations`
*destinations API · Flow Service destinations · create destination connection · activate via API · programmatic activation · streaming destination API*

---

### Data Prep

**Data Prep Overview** — `/en/docs/experience-platform/data-prep/home`
*Data Prep overview · map data · transform data · data transformation · what is Data Prep · data preparation AEP*

**Mapping Sets** — `/en/docs/experience-platform/data-prep/mapping-set`
*mapping set · create mapping · field mapping · map source to XDM · data mapping · mapping configuration*

**Data Prep Functions** — `/en/docs/experience-platform/data-prep/functions`
*Data Prep functions · transformation functions · map functions · concat · string functions · date functions · math functions*

**Calculated Fields** — `/en/docs/experience-platform/data-prep/calculated-fields`
*calculated fields · computed fields in mapping · derive field data prep · transform field value*

**Data Prep API Overview** — `/en/docs/experience-platform/data-prep/api/overview`
*Data Prep API · mapping API · programmatic mapping · create mapping API · mapping set endpoint*

**Data Prep UI — Mapping** — `/en/docs/experience-platform/data-prep/ui/mapping`
*Data Prep UI · mapping UI · map fields in UI · data prep interface · source to XDM mapping UI*

---

### Query Service & Data Distiller

**Query Service Overview** — `/en/docs/experience-platform/query/home`
*Query Service overview · SQL on AEP · query experience platform data · ad hoc queries · what is Query Service*

**Query Service Guardrails** — `/en/docs/experience-platform/query/guardrails`
*query guardrails · query limits · query timeout · concurrent query limit · query row output limit · Query Service cap*

**Query Editor UI Guide** — `/en/docs/experience-platform/query/ui/user-guide`
*query editor · Query Service UI · write SQL · run SQL query · query editor interface · SQL query UI*

**Connect Clients to Query Service** — `/en/docs/experience-platform/query/clients/overview`
*connect to Query Service · PSQL client · Tableau Query Service · Power BI Query Service · external client · third-party SQL client*

**SQL Syntax Guide** — `/en/docs/experience-platform/query/sql/syntax`
*SQL syntax · supported SQL · Query Service SQL reference · SQL statements · SELECT syntax AEP · SQL dialect*

**Best Practices for Writing Queries** — `/en/docs/experience-platform/query/best-practices/writing-queries`
*query best practices · write efficient queries · SQL optimization · query performance tips · Query Service tips*

**Query Service API — Getting Started** — `/en/docs/experience-platform/query/api/getting-started`
*Query Service API · run query API · schedule query API · query API authentication · programmatic query*

**Data Distiller Overview** — `/en/docs/experience-platform/query/data-distiller/overview`
*Data Distiller · what is Data Distiller · Data Distiller SKU · batch query processing · post-ingestion transformation · Data Distiller overview*

**Derived Datasets Overview** — `/en/docs/experience-platform/query/data-distiller/derived-datasets/overview`
*derived datasets · create derived dataset · derived attribute dataset · SQL-based derived dataset · augment profile with derived dataset*

**Create Derived Datasets with SQL** — `/en/docs/experience-platform/query/data-distiller/derived-datasets/create-derived-datasets-with-sql`
*create derived datasets SQL · build derived dataset · SQL derived dataset tutorial · derived dataset query*

**AI/ML Feature Pipelines** — `/en/docs/experience-platform/query/data-distiller/ml-feature-pipelines/overview`
*ML feature pipelines · machine learning features · Data Distiller ML · Python notebook Data Distiller · feature engineering*

**SQL Insights Overview** — `/en/docs/experience-platform/query/data-distiller/sql-insights/overview`
*SQL Insights · custom reporting insights · bespoke reporting model · Data Distiller reporting · query accelerated insights*

**Send Accelerated Queries** — `/en/docs/experience-platform/query/data-distiller/sql-insights/send-accelerated-queries`
*accelerated queries · query accelerated store · fast queries · Data Distiller accelerated store · stateless queries*

**Reporting Insights Data Model** — `/en/docs/experience-platform/query/data-distiller/sql-insights/reporting-insights-data-model`
*reporting insights data model · Real-Time CDP insights data model · custom dashboard SQL · sql insights reporting model*

**Data Distiller Top Tips** — `/en/docs/experience-platform/query/data-distiller/top-tips-to-maximize-value`
*Data Distiller tips · maximize Data Distiller · best practices Data Distiller · Data Distiller optimization*

---

### Data Governance

**Data Governance Overview** — `/en/docs/experience-platform/data-governance/home`
*data governance overview · DULE · data usage labeling · governance framework · data governance AEP · data usage policies*

**Data Usage Labels Overview** — `/en/docs/experience-platform/data-governance/labels/overview`
*data labels · usage labels · DULE labels · data usage labeling · label types · core labels · contract labels · sensitive labels*

**Labels User Guide** — `/en/docs/experience-platform/data-governance/labels/user-guide`
*apply labels · manage labels UI · label dataset · label field · labels workspace · data usage labels UI*

**Dataset Labels API** — `/en/docs/experience-platform/data-governance/labels/dataset-api`
*labels API · dataset labels API · apply labels API · label endpoint · programmatic labeling*

**Data Usage Policies Overview** — `/en/docs/experience-platform/data-governance/policies/overview`
*data usage policies · marketing actions · DULE policies · policy creation · policy types · what is a data policy*

**Data Usage Policies User Guide** — `/en/docs/experience-platform/data-governance/policies/user-guide`
*create policy · manage policies UI · policy builder · enable policy · configure marketing action*

**Data Governance Enforcement Overview** — `/en/docs/experience-platform/data-governance/enforcement/overview`
*policy enforcement · governance enforcement · block activation · auto enforcement · consent enforcement*

**Automatic Policy Enforcement** — `/en/docs/experience-platform/data-governance/enforcement/auto-enforcement`
*auto enforcement · automatic governance · destination policy check · activation policy enforcement*

**Data Governance API Overview** — `/en/docs/experience-platform/data-governance/api/overview`
*governance API · policy API · labels API · marketing actions API · governance programmatic*

---

### Access Control

**Access Control Overview** — `/en/docs/experience-platform/access-control/home`
*access control overview · RBAC · roles and permissions · what is access control · user permissions AEP · manage access*

**Attribute-Based Access Control Overview** — `/en/docs/experience-platform/access-control/abac/overview`
*ABAC · attribute-based access control · field-level access · data label access control · granular access control*

**ABAC Roles (UI)** — `/en/docs/experience-platform/access-control/abac/ui/roles`
*create roles · manage roles UI · ABAC roles · role permissions · assign users to role · role management*

**ABAC Labels (UI)** — `/en/docs/experience-platform/access-control/abac/ui/labels`
*access control labels · ABAC labels · restrict field access · label-based access · field-level restriction*

**ABAC API Overview** — `/en/docs/experience-platform/access-control/abac/api/overview`
*ABAC API · access control API · roles API · permissions API · programmatic access control*

**Access Control API Overview** — `/en/docs/experience-platform/access-control/api/overview`
*access control API · permissions API · roles and permissions API · access control management API*

---

### Sandboxes

**Sandbox Overview** — `/en/docs/experience-platform/sandbox/home`
*sandbox overview · what is a sandbox · sandbox types · production sandbox · development sandbox · sandbox AEP*

**Sandbox UI Overview** — `/en/docs/experience-platform/sandbox/ui/overview`
*sandbox UI · manage sandboxes · switch sandbox · create sandbox · sandbox list · sandbox management UI*

**Sandbox API Overview** — `/en/docs/experience-platform/sandbox/api/overview`
*sandbox API · create sandbox API · sandbox management API · list sandboxes API · programmatic sandbox*

**Sandbox Tooling** — `/en/docs/experience-platform/sandbox/sandbox-tooling`
*sandbox tooling · copy objects between sandboxes · sandbox package · export import sandbox config · sandbox promotion*

**Backup Object Configuration** — `/en/docs/experience-platform/sandbox/use-cases/backup-object-configuration`
*backup sandbox · backup configuration · sandbox object backup · save sandbox state*

**Promote Sandbox to Production** — `/en/docs/experience-platform/sandbox/use-cases/promote-sandbox-to-production`
*promote sandbox · sandbox to production · production promotion · sandbox migration · dev to prod sandbox*

---

### Privacy Service

**Privacy Service Overview** — `/en/docs/experience-platform/privacy/home`
*Privacy Service overview · GDPR AEP · CCPA AEP · privacy requests · data subject requests · delete personal data · access personal data*

**Privacy Service UI Overview** — `/en/docs/experience-platform/privacy/ui/overview`
*Privacy Service UI · privacy request UI · submit privacy job · manage privacy requests*

**Privacy Service User Guide** — `/en/docs/experience-platform/privacy/ui/user-guide`
*create privacy job · privacy job UI · submit access request · submit delete request · privacy management UI*

**Privacy Service API Guide** — `/en/docs/experience-platform/privacy/api/overview`
*Privacy Service API · privacy job API · GDPR API · create privacy request API · programmatic privacy*

**Privacy for Experience Cloud Apps** — `/en/docs/experience-platform/privacy/experience-cloud-apps`
*privacy for Adobe apps · Privacy Service app coverage · Analytics privacy · Target privacy · AAM privacy*

**Privacy Service JavaScript Library** — `/en/docs/experience-platform/privacy/js-library`
*privacy JS library · opt-out · consent management JS · privacy JavaScript · client-side privacy*

---

### Web SDK

**Web SDK Overview** — `/en/docs/experience-platform/web-sdk/home`
*Web SDK overview · AEP Web SDK · Alloy · what is Web SDK · client-side data collection · JavaScript SDK*

**Install Web SDK** — `/en/docs/experience-platform/web-sdk/install/overview`
*install Web SDK · Web SDK installation · add Alloy · configure Web SDK · Web SDK setup*

**Web SDK Commands** — `/en/docs/experience-platform/web-sdk/commands/overview`
*Web SDK commands · sendEvent · configure · setConsent · getIdentity · Web SDK API · Alloy commands*

**Web SDK Identity** — `/en/docs/experience-platform/web-sdk/identity/overview`
*Web SDK identity · ECID Web SDK · first-party cookies · identity in Web SDK · visitor ID Web SDK*

**Web SDK Personalization** — `/en/docs/experience-platform/web-sdk/personalization/overview`
*Web SDK personalization · render offers · Target via Web SDK · Offer Decisioning Web SDK · personalize with Web SDK*

**Web SDK Consent** — `/en/docs/experience-platform/web-sdk/consent/overview`
*Web SDK consent · consent management Web SDK · IAB TCF Web SDK · opt-in opt-out Web SDK*

**Web SDK FAQ** — `/en/docs/experience-platform/web-sdk/faq`
*Web SDK FAQ · Web SDK questions · Alloy FAQ · common Web SDK issues · Web SDK limitations*

**Web SDK Use Cases** — `/en/docs/experience-platform/web-sdk/use-cases/top-use-cases`
*Web SDK use cases · top Web SDK use cases · collect behavioral data · single-page app SDK · send data to multiple solutions*

**Web SDK Release Notes** — `/en/docs/experience-platform/web-sdk/release-notes`
*Web SDK release notes · Web SDK updates · Alloy version · Web SDK changelog*

---

### Datastreams

**Datastreams Overview** — `/en/docs/experience-platform/datastreams/overview`
*datastreams overview · what is a datastream · datastream concept · Edge Network datastream · configure data routing*

**Create and Configure Datastreams** — `/en/docs/experience-platform/datastreams/configure`
*create datastream · configure datastream · datastream settings · enable services in datastream · AEP service in datastream*

**Dynamic Datastream Configurations** — `/en/docs/experience-platform/datastreams/configure-dynamic-datastream`
*dynamic datastream · datastream rules · route data by rules · conditional datastream · dynamic routing*

**Data Prep for Data Collection** — `/en/docs/experience-platform/datastreams/data-prep`
*Data Prep in datastream · map data at Edge · transform at collection · XDM mapping Edge · datastream data prep*

**Datastream Overrides** — `/en/docs/experience-platform/datastreams/overrides`
*datastream overrides · override datastream settings · runtime override · Web SDK override · Mobile SDK override*

**Bot Detection for Datastreams** — `/en/docs/experience-platform/datastreams/bot-detection`
*bot detection · filter bots · bot filtering datastream · IP bot exclusion · bot traffic detection*

**Dynamic Datastream Configuration Patterns** — `/en/docs/experience-platform/datastreams/dynamic-datastream/configuration-patterns`
*dynamic datastream patterns · configuration pattern examples · dynamic routing patterns · conditional routing examples*

---

### Edge Network Server API

**Edge Network Server API Overview** — `/en/docs/experience-platform/edge-network-server-api/overview`
*Edge Network Server API · server-side collection · server-side event forwarding · server API overview · Edge Network API*

**Edge Network API Guardrails** — `/en/docs/experience-platform/edge-network-server-api/guardrails`
*Edge Network guardrails · server API limits · Edge API throughput · server API performance · Edge Network limits*

**Edge Network API Authentication** — `/en/docs/experience-platform/edge-network-server-api/authentication`
*Edge Network authentication · server API auth · Edge API credentials · authenticate server API*

**Interactive Data Collection (Interact Endpoint)** — `/en/docs/experience-platform/edge-network-server-api/data-collection/interactive-data-collection`
*interact endpoint · interactive collection · Edge Network POST · single event API · respond with content*

**Edge Network API Troubleshooting** — `/en/docs/experience-platform/edge-network-server-api/troubleshooting`
*Edge Network API troubleshooting · server API errors · debug Edge API · server API issues*

---

### Real-Time CDP

**Real-Time CDP Home** — `/en/docs/experience-platform/rtcdp/home`
*Real-Time CDP · RTCDP home · Real-Time Customer Data Platform · what is RTCDP · RTCDP documentation*

**Real-Time CDP Overview** — `/en/docs/experience-platform/rtcdp/intro/rtcdp-intro/overview`
*RTCDP overview · Real-Time CDP overview · how RTCDP works · RTCDP architecture · RTCDP concepts*

**Real-Time CDP Guardrails** — `/en/docs/experience-platform/rtcdp/guardrails/overview`
*RTCDP guardrails · Real-Time CDP limits · RTCDP limits · RTCDP cap · RTCDP maximum*

**Real-Time CDP B2B Edition Overview** — `/en/docs/experience-platform/rtcdp/intro/rtcdpb2b-intro/b2b-overview`
*RTCDP B2B · Real-Time CDP B2B · B2B edition · account-based marketing AEP · B2B CDP · B2B overview*

**RTCDP B2B Tutorial** — `/en/docs/experience-platform/rtcdp/intro/rtcdpb2b-intro/b2b-tutorial`
*RTCDP B2B getting started · B2B tutorial · set up B2B RTCDP · B2B data model tutorial*

**RTCDP B2B Use Case** — `/en/docs/experience-platform/rtcdp/intro/rtcdpb2b-intro/b2b-use-case`
*RTCDP B2B use case · B2B marketing use case · account-based use case · opportunity targeting*

**Account Profile Overview (B2B)** — `/en/docs/experience-platform/rtcdp/account/account-profile-overview`
*account profiles · B2B account profile · account data · manage accounts RTCDP · company profile*

**B2B Segmentation Use Cases** — `/en/docs/experience-platform/rtcdp/segmentation/b2b`
*B2B segmentation · segment accounts · segment by opportunity · B2B audience · account audience · B2B segment use case*

**Browse Profiles in RTCDP** — `/en/docs/experience-platform/rtcdp/profile/profile-browse`
*browse profiles RTCDP · view customer profiles · profile lookup · find profile RTCDP*

**RTCDP B2B Architecture Upgrade** — `/en/docs/experience-platform/rtcdp/intro/rtcdpb2b-intro/b2b-architecture-upgrade`
*B2B architecture upgrade · RTCDP B2B changes · B2B edition upgrade · new B2B architecture*

---

### Intelligent Services

**Intelligent Services Overview** — `/en/docs/experience-platform/intelligent-services/home`
*Intelligent Services overview · AI services AEP · Attribution AI · Customer AI · Intelligent Services introduction*

**Attribution AI Overview** — `/en/docs/experience-platform/intelligent-services/attribution-ai/overview`
*Attribution AI · marketing attribution · channel attribution · touchpoint attribution · AI attribution model*

**Attribution AI User Guide** — `/en/docs/experience-platform/intelligent-services/attribution-ai/user-guide`
*Attribution AI setup · configure Attribution AI · Attribution AI UI · create Attribution AI instance*

**Customer AI Overview** — `/en/docs/experience-platform/intelligent-services/customer-ai/overview`
*Customer AI · propensity scoring · churn prediction · conversion prediction · AI score · customer propensity*

**Configure Customer AI** — `/en/docs/experience-platform/intelligent-services/customer-ai/user-guide/configure`
*configure Customer AI · Customer AI setup · create Customer AI instance · Customer AI UI · propensity model setup*

**Intelligent Services Data Requirements** — `/en/docs/experience-platform/intelligent-services/data-requirements`
*Intelligent Services data · data requirements · input schema · Consumer ExperienceEvent schema · Attribution AI data · Customer AI data*

---

### Data Access & Catalog

**Data Access Overview** — `/en/docs/experience-platform/data-access/home`
*Data Access overview · access ingested data · read dataset files · data access API · explore data lake*

**Data Access API Guide** — `/en/docs/experience-platform/data-access/api`
*Data Access API · download dataset files · list dataset batches · data file access · read data files API*

**View Dataset Data Tutorial** — `/en/docs/experience-platform/data-access/tutorials/dataset-data`
*view dataset data · read dataset · access batch data · download parquet files · dataset data tutorial*

**Catalog Service API Overview** — `/en/docs/experience-platform/catalog/api/overview`
*Catalog API · catalog service API · metadata API · list datasets API · list batches API · catalog endpoint*

---

### Dataflows & Monitoring

**Dataflows Overview** — `/en/docs/experience-platform/dataflows/home`
*dataflows overview · what is a dataflow · data movement · dataflow concept · sources dataflow · destinations dataflow*

**Monitoring Dashboard Overview** — `/en/docs/experience-platform/dataflows/ui/monitor`
*monitoring dashboard · monitor data flow · track ingestion · end-to-end monitoring · data journey monitoring*

**Monitor Data Lake Ingestion** — `/en/docs/experience-platform/dataflows/ui/monitor-sources`
*monitor sources · monitor data lake ingestion · sources monitoring · ingestion monitoring UI · source dataflow status*

**Monitor Streaming Profile Ingestion** — `/en/docs/experience-platform/dataflows/ui/monitor-streaming-profile`
*monitor streaming profile · profile ingestion monitoring · streaming profile status · profile update monitoring*

**Monitor Audiences Dataflows** — `/en/docs/experience-platform/dataflows/ui/monitor-audiences`
*monitor audiences · audience dataflow monitoring · audience evaluation status · segment job monitoring*

**Monitor Dataflows via API** — `/en/docs/experience-platform/dataflows/api/monitor`
*monitor dataflows API · Flow Service monitoring · flow run status API · dataflow metrics API*

---

### Observability & Alerts

**Observability Insights Overview** — `/en/docs/experience-platform/observability/home`
*Observability Insights · platform metrics · AEP observability · operational insights · platform activity monitoring*

**Observability API Overview** — `/en/docs/experience-platform/observability/api/overview`
*Observability API · metrics API · observability insights API · platform metrics endpoint*

**Alerts Overview** — `/en/docs/experience-platform/observability/alerts/overview`
*alerts overview · what is an alert · AEP alerts · event-based alerts · configure alerts · alert notifications*

**Alerts UI Guide** — `/en/docs/experience-platform/observability/alerts/ui`
*manage alerts UI · enable alert · alert history · alert subscriptions UI · view alerts*

**Subscribe to I/O Event Notifications** — `/en/docs/experience-platform/observability/alerts/subscribe`
*subscribe to alerts · I/O event notifications · webhook alert · automation alert · alert webhook*

**Standard Alert Rules** — `/en/docs/experience-platform/observability/alerts/rules`
*alert rules · standard alerts · predefined alerts · available alert types · alert rule reference*

---

### Dashboards

**Dashboards Overview** — `/en/docs/experience-platform/dashboards/home`
*dashboards overview · AEP dashboards · platform dashboards · overview dashboard · custom dashboard*

**Profiles Dashboard** — `/en/docs/experience-platform/dashboards/guides/profiles`
*profiles dashboard · profile metrics · audience size · profile widgets · profile overview dashboard*

**Audiences Dashboard** — `/en/docs/experience-platform/dashboards/guides/audiences`
*audiences dashboard · audience metrics · segment size · audience overlap · audience growth · audience dashboard widgets*

**Destinations Dashboard** — `/en/docs/experience-platform/dashboards/guides/destinations`
*destinations dashboard · activation metrics · destination widgets · activated audiences · destination monitoring dashboard*

**License Usage Dashboard** — `/en/docs/experience-platform/dashboards/guides/license-usage`
*license usage · license consumption · license dashboard · entitlement monitoring · sandbox license usage · license cap*

**Account Profiles Dashboard** — `/en/docs/experience-platform/dashboards/guides/account-profiles`
*account profiles dashboard · B2B dashboard · account metrics · B2B profile dashboard*

---

### Tags & Event Forwarding (Data Collection)

**Tags Overview** — `/en/docs/experience-platform/tags/home`
*Tags overview · Adobe Tags · Launch · tag management · TMS · AEP Tags · data collection tags*

**Tag Rules** — `/en/docs/experience-platform/tags/ui/rules`
*tag rules · create tag rule · event trigger rule · data element · action · tag rule configuration*

**Tag Extensions Overview** — `/en/docs/experience-platform/tags/ui/extensions/overview`
*tag extensions · install extension · available extensions · AEP Web SDK extension · Analytics extension*

**Tags API Overview** — `/en/docs/experience-platform/tags/api/overview`
*Tags API · Launch API · programmatic tag management · Reactor API · tag library API*

**Event Forwarding Overview** — `/en/docs/experience-platform/tags/event-forwarding/overview`
*event forwarding · server-side forwarding · Edge network forwarding · forward events · server-side tagging*

**Event Forwarding Getting Started** — `/en/docs/experience-platform/tags/event-forwarding/getting-started`
*event forwarding setup · configure event forwarding · create event forwarding property · getting started event forwarding*

---

### Data Lifecycle / Hygiene

**Data Lifecycle Overview** — `/en/docs/experience-platform/data-lifecycle/home`
*data lifecycle management · data hygiene · TTL · dataset expiration · record delete · data deletion AEP*

**Data Lifecycle UI Overview** — `/en/docs/experience-platform/data-lifecycle/ui/overview`
*data lifecycle UI · manage hygiene UI · hygiene requests UI · data lifecycle workspace*

**Dataset Expiration (TTL)** — `/en/docs/experience-platform/data-lifecycle/ui/dataset-expiration`
*dataset TTL · dataset expiration · auto-delete dataset · scheduled dataset deletion · dataset lifetime*

**Record Delete** — `/en/docs/experience-platform/data-lifecycle/ui/record-delete`
*record delete · delete profile records · hygiene record delete · GDPR delete · identity-based delete*

**Data Lifecycle API Overview** — `/en/docs/experience-platform/data-lifecycle/api/overview`
*data hygiene API · TTL API · record delete API · hygiene job API · dataset expiration API*

---

### Federated Audience Composition

**FAC Documentation Home** — `/en/docs/federated-audience-composition/using/landing`
*Federated Audience Composition home · FAC documentation · federated audiences · external data warehouse audiences*

**FAC Overview** — `/en/docs/federated-audience-composition/using/overview`
*Federated Audience Composition overview · what is FAC · federate from data warehouse · no data copy · Snowflake audience · Redshift audience · BigQuery audience*

**Work with Audiences (FAC)** — `/en/docs/federated-audience-composition/using/start/audiences`
*FAC audience workflow · publish federated audience · federated audience to AEP · audience from warehouse*

**Get Started with Compositions (FAC)** — `/en/docs/federated-audience-composition/using/compositions/home`
*FAC compositions · composition canvas · build federated composition · what is a composition FAC*

**Create Compositions (FAC)** — `/en/docs/federated-audience-composition/using/compositions/create-composition`
*create FAC composition · new composition · FAC canvas · build audience from warehouse*

**Activities in Compositions (FAC)** — `/en/docs/federated-audience-composition/using/compositions/activities`
*FAC activities · targeting activities · flow control activities · query activity · split activity · union activity*

**Configure Destinations (FAC)** — `/en/docs/federated-audience-composition/using/config/destinations`
*FAC destinations · federated audience enrichment · enrich AEP audience · FAC to AEP · federated enrichment configuration*

**FAC FAQ** — `/en/docs/federated-audience-composition/using/faq`
*FAC FAQ · federated audience composition questions · FAC limitations · FAC requirements · data warehouse requirements*

**AI Assistant in FAC** — `/en/docs/federated-audience-composition/using/start/ai-assistant`
*AI Assistant FAC · autonomous composition · AI-generated composition · AI creates FAC · natural language composition*

**FAC Release Notes** — `/en/docs/federated-audience-composition/using/release-notes/latest`
*FAC release notes · federated audience composition updates · FAC new features · FAC changelog*

---

### Use Case Playbooks

**Playbooks Overview** — `/en/docs/experience-platform/use-case-playbooks/playbooks/overview`
*playbooks overview · what is a playbook · use case playbooks · AEP playbooks · accelerate AEP · get started quickly*

**Get Started with Playbooks** — `/en/docs/experience-platform/use-case-playbooks/playbooks/get-started`
*playbooks get started · access playbooks · playbook permissions · playbook setup · enable playbooks*

**Navigate Playbooks** — `/en/docs/experience-platform/use-case-playbooks/playbooks/navigate`
*navigate playbooks · find playbooks · browse playbooks · playbook gallery*

**Choose a Playbook** — `/en/docs/experience-platform/use-case-playbooks/playbooks/choose`
*choose playbook · select playbook · filter playbooks · playbook selection · industry playbook · funnel stage playbook*

**Create, Share, and Reuse Instances** — `/en/docs/experience-platform/use-case-playbooks/playbooks/create-share-reuse`
*create playbook instance · playbook instance · share playbook · reuse playbook · generate assets from playbook*

**Data Awareness in Playbooks** — `/en/docs/experience-platform/use-case-playbooks/playbooks/data-awareness`
*playbook data awareness · move playbook assets · sandbox promotion playbooks · dev to prod playbook*

**Author Playbooks (AI Assistant)** — `/en/docs/experience-platform/use-case-playbooks/playbooks/author`
*author playbook · create custom playbook · AI Assistant playbook · playbook authoring framework*

**Available Playbooks List** — `/en/docs/experience-platform/use-case-playbooks/playbooks/playbooks-list`
*available playbooks · playbook catalog · RTCDP playbooks · AJO playbooks · list of playbooks*

---

### AI Assistant (AEP)

**AI Assistant Overview (Legacy)** — `/en/docs/experience-platform/ai-assistant/home`
*AI Assistant AEP · AI Assistant legacy · what is AI Assistant · AI Assistant overview · conversational AI AEP*

**AI Assistant UI Guide** — `/en/docs/experience-platform/ai-assistant/ui-guide`
*AI Assistant UI · launch AI Assistant · use AI Assistant · AI Assistant interface · how to use AI Assistant*

**Access AI Assistant** — `/en/docs/experience-platform/ai-assistant/access`
*AI Assistant access · AI Assistant permissions · enable AI Assistant · AI Assistant prerequisites*

**Question Guide for AI Assistant** — `/en/docs/experience-platform/ai-assistant/questions`
*AI Assistant questions · what to ask AI Assistant · question phrasing · AI Assistant prompts · sample questions*

**AI Assistant FAQ** — `/en/docs/experience-platform/ai-assistant/faq`
*AI Assistant FAQ · AI Assistant limitations · data freshness AI Assistant · AI Assistant questions*

**AI Assistant Privacy & Governance** — `/en/docs/experience-platform/ai-assistant/privacy`
*AI Assistant privacy · AI data handling · governance AI Assistant · AI security · personal data AI Assistant*

**Audience Forecasting with AI Assistant** — `/en/docs/experience-platform/ai-assistant/new-features/audience-forecasting`
*audience forecasting AI · AI audience size prediction · audience growth monitoring · significant changes AI*

---

### Data Collection Overview

**Data Collection Overview** — `/en/docs/experience-platform/collection/home`
*data collection overview · AEP data collection · client-side collection · server-side collection · Web SDK · Tags · Edge Network*

**Mobile SDK Documentation** — `/en/docs/mobile`
*Mobile SDK · AEP Mobile SDK · iOS SDK · Android SDK · mobile data collection · mobile app tracking · Places Service*

---

### Platform Assurance

**Assurance Overview** — `/en/docs/experience-platform/assurance/home`
*Platform Assurance · Adobe Assurance · Griffon · inspect SDK data · debug mobile implementation · validate data collection · Assurance overview*

**Assurance User Access** — `/en/docs/experience-platform/assurance/user-access`
*Assurance access · Assurance permissions · enable Assurance · get started Assurance*

**Using Assurance Tutorial** — `/en/docs/experience-platform/assurance/tutorials/using-assurance`
*how to use Assurance · Assurance tutorial · connect to Assurance · Assurance session*

---

### Platform Debugger

**Platform Debugger Overview** — `/en/docs/experience-platform/debugger/home`
*Platform Debugger · AEP Debugger · Experience Cloud Debugger · debug web SDK · debug Tags · validate implementation · browser extension debugger*

---

### Unified Tags

**Unified Tags Overview** — `/en/docs/experience-platform/administrative-tags/overview`
*Unified Tags · administrative tags · metadata tags · tag objects · categorize objects · AEP tagging · business object tags*

---

### Data Science Workspace

**Data Science Workspace Overview** — `/en/docs/experience-platform/data-science-workspace/home`
*Data Science Workspace · DSW · machine learning AEP · build ML model · AI recipes · Jupyter notebooks · JupyterLab*

**Data Science Workspace Walkthrough** — `/en/docs/experience-platform/data-science-workspace/walkthrough`
*Data Science Workspace walkthrough · end to end ML · build train score model · DSW tutorial*

**Train and Evaluate a Model (UI)** — `/en/docs/experience-platform/data-science-workspace/models-recipes/train-evaluate-model-ui`
*train model UI · evaluate model · DSW model training · ML model evaluation*

---

### Audience Manager Expanded Activation

**Expanded Activation Overview** — `/en/docs/experience-platform/expanded-activation/overview`
*Audience Manager Expanded Activation · AAM expanded activation · migrate AAM audiences · AAM to platform destinations · Expanded Activation*

**Expanded Activation Administration** — `/en/docs/experience-platform/expanded-activation/administration`
*configure Expanded Activation · Expanded Activation setup · account configuration · hashed email data source*

**Activate Audiences (Expanded Activation)** — `/en/docs/experience-platform/expanded-activation/activate-audiences`
*activate audiences Expanded Activation · AAM audience activation · send AAM audiences to destinations*

---

### Audit Logs

**Audit Logs Overview** — `/en/docs/experience-platform/landing/governance-privacy-security/audit-logs/overview`
*audit logs · activity audit · audit trail · user activity logs · platform audit · who did what · change history*

---

### Run and Operate

**Run and Operate Overview** — `/en/docs/experience-platform/run-and-operate/overview`
*run and operate · batch job monitoring · operational tools · troubleshoot batch failures · job schedules health checks*

**Job Schedules** — `/en/docs/experience-platform/run-and-operate/job-schedules/job-schedules`
*job schedules · scheduled batch operations · monitor scheduled jobs · ingestion profiling segmentation activation schedule*

**Job Schedules — Anti-Patterns** — `/en/docs/experience-platform/run-and-operate/job-schedules/job-schedules-anti-patterns`
*job schedule issues · configuration anti-patterns · common job schedule errors · avoid schedule problems*

**Health Checks** — `/en/docs/experience-platform/run-and-operate/health-checks`
*health checks · schema health · identity configuration health · detect configuration issues · proactive monitoring*
