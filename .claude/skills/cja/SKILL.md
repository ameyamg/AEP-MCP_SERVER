---
name: cja
description: Answer questions about Adobe Customer Journey Analytics by fetching live Adobe Experience League documentation. Never answers from memory — always fetches source content, quotes directly, and cites the URL.
---

You have been invoked to answer questions about Adobe Customer Journey Analytics (CJA). Your job is to retrieve the correct documentation page, read it, and answer only from what that page says — not from training memory.

## Rules

**RULE 1 — FETCH BEFORE ANSWERING**
Never answer a CJA question from memory alone, even if you are confident in the answer. Always fetch at least one documentation page first. CJA documentation changes frequently and limits/features vary by package tier.

**RULE 2 — QUOTE OR DECLINE**
For any factual statement — a limit, a setting name, a step, a supported value, a behavior:
- Find the exact sentence or passage in the fetched content that states it
- Quote it verbatim in your answer
- Cite the full source URL immediately after the quote
- If the fetched page does not contain the answer, say which page you checked and what was missing — never fill the gap with inference

**RULE 3 — MULTI-PAGE FOR AMBIGUOUS QUESTIONS**
If a question could apply to more than one feature (e.g. "export" maps to both CSV download and full table cloud export), fetch the most relevant page for each interpretation and present both answers with their sources labeled separately.

**RULE 4 — ESCALATION CHAIN**
If the catalog page does not answer the question, escalate in order:
1. Scan links on the fetched page → fetch the most relevant linked page (Tier 2)
2. If still not found: WebSearch for `site:experienceleague.adobe.com/en/docs/analytics-platform [question keywords]` and fetch the top result (Tier 3)
3. If still not found: state exactly which pages were checked — never guess

## Priority Rule

For any question containing **limit, maximum, max, how many, cap, threshold, guardrail, restriction, is there a limit, how much, what is the maximum, row limit, or package tier** — fetch the Guardrails page first, then any feature-specific page. The Guardrails page is the single canonical reference for all hard and soft limits across CJA.

---

## URL Catalog

Base: `https://experienceleague.adobe.com`

Match the user's question to the most relevant page(s) using the triggers listed under each entry. Fetch the full URL (base + path). When multiple pages seem relevant, fetch all of them before answering.

---

### ⚡ Priority — fetch first for ANY limit / maximum / threshold question

**Guardrails — All CJA Limits** — `/en/docs/analytics-platform/using/technotes/guardrails`
*limit · maximum · how many · cap · threshold · guardrail · restriction · row limit · hard limit · soft limit · package tier · Foundation · Select · Prime · Ultimate · connection limit · data view limit · segment limit · derived field limit · export limit · Report Builder limit · stitching limit · audience limit · latency · data transfer limit · rows per report · file size limit · workbook limit · data block limit · scorecard tile limit · how many datasets · how many metrics · how many connections · how many dimensions*

---

### Overview

**CJA Overview** — `/en/docs/analytics-platform/using/cja-overview/cja-b2c-overview/cja-overview`
*what is CJA · CJA introduction · CJA architecture · getting started · how CJA works · customer journey analytics overview*

**AI Assistant** — `/en/docs/analytics-platform/using/cja-overview/cja-b2c-overview/ai-assistant`
*AI assistant · AI features in CJA · product knowledge AI · ask AI · intelligent features*

**Data Insights Agent** — `/en/docs/analytics-platform/using/cja-overview/cja-b2c-overview/data-analysis-ai`
*data insights agent · AI data analysis · natural language query · ask about data · AI-generated visualization*

**B2B Edition Overview** — `/en/docs/analytics-platform/using/cja-overview/cja-b2b/cja-b2b-edition`
*CJA B2B · B2B edition · account-based analytics · CJA for B2B*

---

### Upgrade & Compare with Adobe Analytics

**Comparison Overview** — `/en/docs/analytics-platform/using/compare-aa-cja/cja-aa-comparison/overview`
*compare AA to CJA · AA vs CJA · difference between Analytics and CJA · should I use CJA*

**Feature Support Comparison** — `/en/docs/analytics-platform/using/compare-aa-cja/cja-aa-comparison/cja-aa`
*CJA feature parity · what features are in CJA · AA features in CJA · feature support*

**Terminology Differences** — `/en/docs/analytics-platform/using/compare-aa-cja/cja-aa-comparison/terminology`
*CJA terminology · filter vs segment · eVar vs dimension · AA terminology in CJA · what is the CJA equivalent of*

**Data Processing Comparisons** — `/en/docs/analytics-platform/using/compare-aa-cja/cja-aa-comparison/data-processing-comparisons`
*data processing differences · attribution differences · processing rules in CJA · VISTA rules*

**Using AA Data in CJA** — `/en/docs/analytics-platform/using/compare-aa-cja/cja-aa-comparison/aa-data-in-cja`
*bring AA data into CJA · use Adobe Analytics data · AA report suite in CJA*

**Evolution from AA to CJA** — `/en/docs/analytics-platform/using/compare-aa-cja/aa-to-cja`
*why upgrade to CJA · AA to CJA journey · move from AA · CJA benefits*

**Guide for AA Users** — `/en/docs/analytics-platform/using/compare-aa-cja/aa-to-cja-user`
*coming from Adobe Analytics · AA user guide · transitioning from AA · analyst moving to CJA*

**Upgrade Recommendations** — `/en/docs/analytics-platform/using/compare-aa-cja/upgrade-to-cja/cja-upgrade-recommendations`
*how to upgrade to CJA · upgrade path · upgrade recommendations · best way to migrate*

**Org Readiness** — `/en/docs/analytics-platform/using/compare-aa-cja/upgrade-to-cja/cja-upgrade-org-readiness`
*organizational readiness · prepare for upgrade · team readiness · upgrade prerequisites*

**Schema Architecture (Upgrade)** — `/en/docs/analytics-platform/using/compare-aa-cja/upgrade-to-cja/schema/cja-upgrade-schema-architect`
*upgrade schema design · XDM schema for upgrade · schema planning*

**Create Schema (Upgrade)** — `/en/docs/analytics-platform/using/compare-aa-cja/upgrade-to-cja/schema/cja-upgrade-schema-create`
*create XDM schema · build schema for migration*

**Dataset Creation (Upgrade)** — `/en/docs/analytics-platform/using/compare-aa-cja/upgrade-to-cja/create-datasets/cja-upgrade-dataset`
*create dataset upgrade · AEP dataset for migration*

**Create Connection (Upgrade)** — `/en/docs/analytics-platform/using/compare-aa-cja/upgrade-to-cja/cja-upgrade-connection`
*create connection upgrade step*

**Create Data View (Upgrade)** — `/en/docs/analytics-platform/using/compare-aa-cja/upgrade-to-cja/cja-upgrade-dataview`
*create data view upgrade step*

**Validate Upgrade** — `/en/docs/analytics-platform/using/compare-aa-cja/upgrade-to-cja/cja-upgrade-validate`
*validate upgrade · confirm data is correct · verify migration*

**Historical Data via Source Connector** — `/en/docs/analytics-platform/using/compare-aa-cja/upgrade-to-cja/historical-data-source-connector/cja-upgrade-source-connector`
*historical data migration · backfill historical · Analytics source connector upgrade · bring over old AA data*

**Alternative: Source Connector Only** — `/en/docs/analytics-platform/using/compare-aa-cja/upgrade-to-cja/alternative-upgrade-methods/cja-upgrade-alternative-source-connector`
*source connector only upgrade · simplest upgrade path*

**Alternative: AppMeasurement** — `/en/docs/analytics-platform/using/compare-aa-cja/upgrade-to-cja/alternative-upgrade-methods/cja-upgrade-alternative-appmeasurement`
*AppMeasurement upgrade · upgrade without Web SDK*

---

### Data Ingestion

**Data Ingestion Overview** — `/en/docs/analytics-platform/using/cja-data-ingestion/data-ingestion`
*how to ingest data · ingestion overview · get data into CJA · ingestion methods · send data*

**Adobe Analytics Source Connector** — `/en/docs/analytics-platform/using/cja-data-ingestion/ingest-use-guides/analytics`
*ingest from Adobe Analytics · Analytics source connector · report suite data · pull in AA data*

**Web SDK** — `/en/docs/analytics-platform/using/cja-data-ingestion/ingest-use-guides/edge-network/aepwebsdk`
*Web SDK · alloy.js · browser tracking · JavaScript tracking · implement Web SDK*

**Mobile SDK** — `/en/docs/analytics-platform/using/cja-data-ingestion/ingest-use-guides/edge-network/aepmobilesdk`
*Mobile SDK · iOS tracking · Android tracking · mobile app data*

**Batch Ingestion** — `/en/docs/analytics-platform/using/cja-data-ingestion/ingest-use-guides/batch`
*batch ingestion · upload CSV · file-based ingestion · bulk data upload*

**Streaming Ingestion** — `/en/docs/analytics-platform/using/cja-data-ingestion/ingest-use-guides/streaming`
*streaming ingestion · real-time data · streaming data · live data feed*

**Sources Connectors** — `/en/docs/analytics-platform/using/cja-data-ingestion/ingest-use-guides/sources`
*source connectors · third-party data · CRM data · Salesforce · Marketo · external source*

**Edge Network Server API** — `/en/docs/analytics-platform/using/cja-data-ingestion/ingest-use-guides/edge-network/serverapi`
*server-side data · server API · Edge Network API · server-to-server tracking*

---

### Data Mirror

**Data Mirror Overview** — `/en/docs/analytics-platform/using/cja-data-mirror/data-mirror`
*data mirror · sync from Snowflake · sync from BigQuery · sync from Databricks · mirror external data · change data capture*

**Relational Data** — `/en/docs/analytics-platform/using/cja-data-mirror/relational`
*relational data mirror · mirror relational data · foreign key · join data*

**Model-Based Data** — `/en/docs/analytics-platform/using/cja-data-mirror/model-based`
*model-based data mirror · mirror model data*

**Configure AEP** — `/en/docs/analytics-platform/using/cja-data-mirror/configure/aep`
*configure AEP for data mirror · set up data mirror in Experience Platform*

**Configure CJA** — `/en/docs/analytics-platform/using/cja-data-mirror/configure/cja`
*configure CJA for data mirror · set up data mirror in CJA*

**Configure Data Warehouse** — `/en/docs/analytics-platform/using/cja-data-mirror/configure/datawarehouse`
*configure Snowflake data mirror · configure BigQuery data mirror · configure Databricks data mirror · enable change data capture*

**Data Mirror Considerations** — `/en/docs/analytics-platform/using/cja-data-mirror/considerations`
*data mirror limitations · data mirror considerations · data mirror best practices*

---

### Connections

**Connections Overview** — `/en/docs/analytics-platform/using/cja-connections/overview`
*connections overview · what is a connection · how connections work*

**Create Connection** — `/en/docs/analytics-platform/using/cja-connections/create-connection`
*create a connection · add datasets · event dataset · lookup dataset · profile dataset · summary dataset · dataset types · backfill dataset · connection settings*

**Manage Connections** — `/en/docs/analytics-platform/using/cja-connections/manage-connections`
*manage connections · edit connection · delete connection · connection monitoring · rows added · records skipped*

**Transform Datasets for B2B** — `/en/docs/analytics-platform/using/cja-connections/transform-datasets-b2b-lookups`
*B2B transform · transform dataset · B2B lookup · account-based connection*

**Combined Event Datasets** — `/en/docs/analytics-platform/using/cja-connections/combined-dataset`
*combined event dataset · combine datasets · union datasets · merge event datasets*

**Standard Lookups** — `/en/docs/analytics-platform/using/cja-connections/standard-lookups`
*standard lookups · device lookup · browser lookup · OS lookup · mobile device lookup · auto-added lookups*

**Audience Analysis** — `/en/docs/analytics-platform/using/cja-connections/audience-analysis/analyze-audiences`
*analyze audiences in CJA · audience analysis · AEP audience in CJA · use AEP audiences*

---

### Data Views

**Data Views Overview** — `/en/docs/analytics-platform/using/cja-dataviews/data-views`
*what is a data view · data view overview · how data views work*

**Create / Edit Data View** — `/en/docs/analytics-platform/using/cja-dataviews/create-dataview`
*create data view · edit data view · configure data view · add component · include exclude values · value bucketing · substring · no value options*

**Session Settings** — `/en/docs/analytics-platform/using/cja-dataviews/session-settings`
*session settings · define session · session timeout · custom session · session definition · session container*

**Derived Fields** — `/en/docs/analytics-platform/using/cja-dataviews/derived-fields`
*derived fields · derived field function · case when · lookup function · regex derived field · URL parse · classify · concatenate · date math · find and replace · lowercase · math function · merge fields · next or previous · split function · summarize · trim · typecast · deduplicate · marketing channel derived field · create new dimension from field · field transformation*

**Summary Data** — `/en/docs/analytics-platform/using/cja-dataviews/summary-data`
*summary data · summary dataset · aggregate data · non-event data · ad impression data · cost data*

**Component Reference** — `/en/docs/analytics-platform/using/cja-dataviews/component-reference`
*component reference · all dimensions CJA · all metrics CJA · standard components · default dimensions · default metrics*

**BI Extension** — `/en/docs/analytics-platform/using/cja-dataviews/bi-extension`
*BI extension · Power BI CJA · Tableau CJA · SQL access CJA · Looker CJA · PostgreSQL CJA · BI tool connection · query CJA with SQL*

**Data Governance** — `/en/docs/analytics-platform/using/cja-dataviews/data-governance`
*data governance · privacy labels · DULE labels · sensitive data · consent labels*

---

### Segments (formerly Filters)

> CJA renamed "filters" to "segments" in 2025. Treat both terms as equivalent when routing.

**Segments Overview** — `/en/docs/analytics-platform/using/cja-components/segments/seg-overview`
*segments overview · what are segments · CJA segments · filters overview · how segments work · segment containers · person session event container*

**Create Segments** — `/en/docs/analytics-platform/using/cja-components/segments/seg-create`
*create a segment · create a filter · new segment · build a segment*

**Segment Builder** — `/en/docs/analytics-platform/using/cja-components/segments/seg-builder`
*segment builder · filter builder · segment rules · AND OR logic · include exclude · dimension filter · metric filter · segment conditions*

**Quick Segments** — `/en/docs/analytics-platform/using/cja-components/segments/seg-quick`
*quick segment · quick filter · inline segment · ad hoc segment · temporary filter*

**Sequential Segments** — `/en/docs/analytics-platform/using/cja-components/segments/seg-sequential-build`
*sequential segment · sequential filter · THEN operator · order of events · sequence segment · funnel segment*

**Manage Segments** — `/en/docs/analytics-platform/using/cja-components/segments/seg-manage`
*segment manager · manage segments · share segment · approve segment · tag segment · delete segment*

---

### Calculated Metrics

**Calculated Metrics Overview** — `/en/docs/analytics-platform/using/cja-components/cja-calcmetrics/calc-metr-overview`
*calculated metrics · custom metrics · what are calculated metrics · how calculated metrics work*

**Workflow / Create Options** — `/en/docs/analytics-platform/using/cja-components/cja-calcmetrics/cm-workflow/cm-workflow`
*how to create calculated metric · calculated metric workflow · new calculated metric*

**Build a Calculated Metric** — `/en/docs/analytics-platform/using/cja-components/cja-calcmetrics/cm-workflow/cm-build-metrics`
*build calculated metric · calculated metric builder · metric formula · drag and drop metric · create formula · combine metrics*

**Use Functions** — `/en/docs/analytics-platform/using/cja-components/cja-calcmetrics/cm-workflow/cm-using-functions`
*calculated metric functions · approximate count distinct · mean · variance · percentile · regression · statistical function · basic functions · advanced functions*

**Metric Type & Attribution** — `/en/docs/analytics-platform/using/cja-components/cja-calcmetrics/cm-workflow/m-metric-type-alloc`
*metric type · attribution in calculated metric · allocation model · linear attribution · participation metric · metric attribution setting*

**Segmented Metrics** — `/en/docs/analytics-platform/using/cja-components/cja-calcmetrics/cm-workflow/metrics-with-segments`
*segmented metric · filtered metric · metric with segment · metric with filter applied*

**Calculated Metrics Manager** — `/en/docs/analytics-platform/using/cja-components/cja-calcmetrics/cm-workflow/cm-manager`
*calculated metrics manager · manage calculated metrics*

**Share Calculated Metrics** — `/en/docs/analytics-platform/using/cja-components/cja-calcmetrics/cm-workflow/cm-sharing`
*share calculated metric · share metric · give access to metric*

**Approve Calculated Metrics** — `/en/docs/analytics-platform/using/cja-components/cja-calcmetrics/cm-workflow/cm-approving`
*approve metric · approved metric · certified metric*

**Tag Calculated Metrics** — `/en/docs/analytics-platform/using/cja-components/cja-calcmetrics/cm-workflow/cm-tagging`
*tag calculated metric · label metric · organize metrics*

**Copy Calculated Metrics** — `/en/docs/analytics-platform/using/cja-components/cja-calcmetrics/cm-workflow/cm-copy`
*copy calculated metric · duplicate metric · clone metric*

**Default / Template Metrics** — `/en/docs/analytics-platform/using/cja-components/cja-calcmetrics/default-calcmetrics`
*default calculated metrics · calculated metric templates · Adobe-provided metrics · out-of-the-box calculated metrics*

---

### Workspace Projects

**Workspace Home** — `/en/docs/analytics-platform/using/cja-workspace/home`
*analysis workspace · workspace overview · what is workspace · workspace home*

**Create Projects** — `/en/docs/analytics-platform/using/cja-workspace/build-workspace-project/create-projects`
*create project · new project · start analysis · new workspace project*

**Projects Overview (Freeform)** — `/en/docs/analytics-platform/using/cja-workspace/build-workspace-project/freeform-overview`
*freeform project · workspace project interface · workspace layout*

**Basic Analysis** — `/en/docs/analytics-platform/using/cja-workspace/perform-basic-analysis`
*basic analysis · beginner workspace · how to analyze in workspace*

**Advanced Analysis** — `/en/docs/analytics-platform/using/cja-workspace/perform-adv-analysis`
*advanced analysis · complex workspace · advanced workspace techniques*

**Workspace Folders — Create** — `/en/docs/analytics-platform/using/cja-workspace/build-workspace-project/workspace-folders/create-folders`
*create folder workspace · organize projects · workspace folder*

**Workspace Folders — Manage** — `/en/docs/analytics-platform/using/cja-workspace/build-workspace-project/workspace-folders/manage-folders`
*manage folders · delete folder · rename folder*

**User Preferences** — `/en/docs/analytics-platform/using/cja-workspace/user-preferences`
*user preferences · workspace preferences · default panel · default visualization · density setting · color palette workspace*

**Share Projects** — `/en/docs/analytics-platform/using/cja-workspace/curate-share/share-projects`
*share project · share workspace · give access · send project link · project permissions*

**Curate Projects** — `/en/docs/analytics-platform/using/cja-workspace/curate-share/curate`
*curate project · hide components · component curation · limit what recipients see*

**Scheduled Projects** — `/en/docs/analytics-platform/using/cja-components/scheduled-projects-manager`
*schedule project · scheduled report · email project · recurring project · automate report delivery*

---

### Visualizations

**Visualizations Overview** — `/en/docs/analytics-platform/using/cja-workspace/visualizations/freeform-analysis-visualizations`
*visualizations overview · what visualizations are available · chart types · visualization types*

**Area** — `/en/docs/analytics-platform/using/cja-workspace/visualizations/area`
*area chart · stacked area*

**Bar** — `/en/docs/analytics-platform/using/cja-workspace/visualizations/bar`
*bar chart · column chart · stacked bar*

**Bullet** — `/en/docs/analytics-platform/using/cja-workspace/visualizations/bullet-graph`
*bullet chart · bullet graph · KPI gauge · target visualization*

**Cohort Table** — `/en/docs/analytics-platform/using/cja-workspace/visualizations/cohort-table/cohort-analysis`
*cohort table · cohort analysis · retention cohort · repeat visitor cohort*

**Combo Chart** — `/en/docs/analytics-platform/using/cja-workspace/visualizations/combo-charts`
*combo chart · combined chart · bar and line · dual axis chart*

**Donut** — `/en/docs/analytics-platform/using/cja-workspace/visualizations/donut`
*donut chart · pie chart · part of whole*

**Fallout** — `/en/docs/analytics-platform/using/cja-workspace/visualizations/fallout/fallout-flow`
*fallout · funnel visualization · drop-off · conversion funnel · fallout report*

**Flow** — `/en/docs/analytics-platform/using/cja-workspace/visualizations/flow/flow`
*flow visualization · customer journey flow · path analysis · next page flow · previous page · flow diagram*

**Freeform Table** — `/en/docs/analytics-platform/using/cja-workspace/visualizations/freeform-table/freeform-table`
*freeform table · data table · breakdown table · cross-tab*

**Histogram** — `/en/docs/analytics-platform/using/cja-workspace/visualizations/histogram`
*histogram · distribution chart · frequency distribution*

**Horizontal Bar** — `/en/docs/analytics-platform/using/cja-workspace/visualizations/horizontal-bar`
*horizontal bar · ranked bar*

**Journey Canvas** — `/en/docs/analytics-platform/using/cja-workspace/visualizations/journey-canvas/journey-canvas`
*journey canvas · customer journey visualization · flexible journey · map customer path · non-linear journey · journey nodes*

**Key Metric Summary** — `/en/docs/analytics-platform/using/cja-workspace/visualizations/key-metric`
*key metric summary · KPI card · metric comparison · sparkline summary*

**Line** — `/en/docs/analytics-platform/using/cja-workspace/visualizations/line`
*line chart · trend line · time series chart*

**Scatter** — `/en/docs/analytics-platform/using/cja-workspace/visualizations/scatterplot`
*scatter plot · scatter chart · correlation chart*

**Summary Number / Change** — `/en/docs/analytics-platform/using/cja-workspace/visualizations/summary-number-change`
*summary number · summary change · big number · single metric display · percent change*

**Treemap** — `/en/docs/analytics-platform/using/cja-workspace/visualizations/treemap`
*treemap · proportional area chart*

**Venn** — `/en/docs/analytics-platform/using/cja-workspace/visualizations/venn`
*venn diagram · segment overlap · overlap visualization*

---

### Panels

**Panels Overview** — `/en/docs/analytics-platform/using/cja-workspace/panels/panels`
*panels overview · what are panels · CJA panels · workspace panels · panel types*

**Blank Panel** — `/en/docs/analytics-platform/using/cja-workspace/panels/blank-panel`
*blank panel · empty panel*

**Attribution Panel** — `/en/docs/analytics-platform/using/cja-workspace/panels/attribution`
*attribution panel · attribution model · last touch · first touch · linear attribution · time decay · position-based · algorithmic attribution · compare attribution models · credit*

**Experimentation Panel** — `/en/docs/analytics-platform/using/cja-workspace/panels/experimentation`
*experimentation panel · A/B test · experiment analysis · statistical significance · lift · confidence interval · test variant · control group*

**Freeform Panel** — `/en/docs/analytics-platform/using/cja-workspace/panels/freeform-panel`
*freeform panel · default panel*

**Media Average Minute Audience** — `/en/docs/analytics-platform/using/cja-workspace/panels/average-minute-audience-panel`
*average minute audience · media minute audience · AMA panel · streaming video audience*

**Media Concurrent Viewers** — `/en/docs/analytics-platform/using/cja-workspace/panels/media-concurrent-viewers`
*concurrent viewers · live viewers · simultaneous viewers · peak viewers*

**Media Playback Time Spent** — `/en/docs/analytics-platform/using/cja-workspace/panels/media-playback-time-spent`
*playback time spent · media time spent · time watched · video engagement time*

**Next / Previous Item** — `/en/docs/analytics-platform/using/cja-workspace/panels/next-previous`
*next item panel · previous item panel · page flow panel*

**Quick Insights** — `/en/docs/analytics-platform/using/cja-workspace/panels/quickinsight`
*quick insights panel · beginner panel · guided panel*

---

### Guided Analysis

**Guided Analysis Overview** — `/en/docs/analytics-platform/using/guided-analysis/overview`
*guided analysis · product analytics · self-service analysis · what is guided analysis*

**Active Growth** — `/en/docs/analytics-platform/using/guided-analysis/active-growth`
*active growth · active users · new repeat returning churned users · user growth*

**Conversion Trends** — `/en/docs/analytics-platform/using/guided-analysis/conversion-trends`
*conversion trends · funnel trends over time · conversion rate trends*

**Engagement** — `/en/docs/analytics-platform/using/guided-analysis/engagement`
*engagement analysis · feature engagement · breadth vs depth · feature usage*

**First Use Impact** — `/en/docs/analytics-platform/using/guided-analysis/first-use-impact`
*first use impact · first time feature use · feature adoption impact*

**Frequency** — `/en/docs/analytics-platform/using/guided-analysis/frequency`
*frequency analysis · usage frequency · how often users do something*

**Funnel** — `/en/docs/analytics-platform/using/guided-analysis/funnel`
*guided funnel · funnel analysis · conversion funnel guided · drop-off guided*

**Net Growth** — `/en/docs/analytics-platform/using/guided-analysis/net-growth`
*net growth · net user growth · gained vs lost users · new minus churned*

**Release Impact** — `/en/docs/analytics-platform/using/guided-analysis/release-impact`
*release impact · feature release analysis · before after release · measure release*

**Retention** — `/en/docs/analytics-platform/using/guided-analysis/retention`
*retention guided analysis · user retention · returning users · retention rate*

**Timeline** — `/en/docs/analytics-platform/using/guided-analysis/timeline`
*timeline guided analysis · individual user events · user session timeline · event sequence*

**Trends** — `/en/docs/analytics-platform/using/guided-analysis/trends`
*trends analysis · usage trends · event trends over time*

---

### Report Builder

**Report Builder Overview** — `/en/docs/analytics-platform/using/cja-reportbuilder/rb-overview`
*report builder · CJA in Excel · Excel add-in · report builder overview*

**Setup / Install** — `/en/docs/analytics-platform/using/cja-reportbuilder/report-builder-setup`
*install report builder · set up report builder · report builder installation*

**Report Builder Hub** — `/en/docs/analytics-platform/using/cja-reportbuilder/report-builder-hub`
*report builder hub · report builder interface · data block list*

**Select a Data View** — `/en/docs/analytics-platform/using/cja-reportbuilder/select-data-view`
*select data view report builder · change data view Excel*

**Create a Data Block** — `/en/docs/analytics-platform/using/cja-reportbuilder/create-a-data-block`
*create data block · new data block · add data to Excel · build request*

**Manage Data Blocks** — `/en/docs/analytics-platform/using/cja-reportbuilder/manage-reportbuilder`
*manage data blocks · edit data block · update data block · refresh data block*

**Select Date Range** — `/en/docs/analytics-platform/using/cja-reportbuilder/select-date-range`
*date range report builder · change dates report builder · rolling dates Excel*

**Work with Segments** — `/en/docs/analytics-platform/using/cja-reportbuilder/work-with-filters`
*segments in report builder · filters in report builder · add segment Excel*

**Settings** — `/en/docs/analytics-platform/using/cja-reportbuilder/report-builder-settings`
*report builder settings · offline mode · report builder preferences*

**Schedule Workbooks** — `/en/docs/analytics-platform/using/cja-reportbuilder/schedule-reportbuilder`
*schedule report builder · schedule Excel workbook · automated workbook · email workbook*

---

### Stitching

**Stitching Overview** — `/en/docs/analytics-platform/using/stitching/overview`
*stitching overview · what is stitching · identity stitching · cross-device analysis · cross-channel stitching · person ID stitching*

**Field-Based Stitching** — `/en/docs/analytics-platform/using/stitching/fbs`
*field-based stitching · FBS · persistent ID transient ID · custom ID stitching*

**Graph-Based Stitching** — `/en/docs/analytics-platform/using/stitching/gbs`
*graph-based stitching · GBS · identity graph stitching · device graph*

**Enable Stitching (UI)** — `/en/docs/analytics-platform/using/stitching/use-stitching-ui`
*enable stitching · turn on stitching · configure stitching · set up stitching*

**Validate Stitching** — `/en/docs/analytics-platform/using/stitching/validate`
*validate stitching · verify stitching works · stitching data quality*

**Stitching FAQ** — `/en/docs/analytics-platform/using/stitching/faq`
*stitching FAQ · stitching questions · stitching latency · stitching limits · how long does stitching take*

---

### Dashboards / Scorecards

**Dashboards Home** — `/en/docs/analytics-platform/using/cja-dashboards/home`
*analytics dashboards · mobile scorecard · CJA dashboards · executive dashboard*

**Curator Resources** — `/en/docs/analytics-platform/using/cja-dashboards/curator`
*scorecard curator · build scorecard · curator guide*

**Create Scorecard** — `/en/docs/analytics-platform/using/cja-dashboards/create-scorecard`
*create scorecard · build executive scorecard · scorecard tiles · add metric to scorecard*

**Set Up Execs** — `/en/docs/analytics-platform/using/cja-dashboards/set-up-execs`
*set up executive · onboard executive · share scorecard with exec*

**Executive User Guide** — `/en/docs/analytics-platform/using/cja-dashboards/executive`
*use the dashboard app · read a scorecard · executive user guide*

---

### Exports

**Export to Cloud Overview** — `/en/docs/analytics-platform/using/cja-workspace/export/export-cloud`
*export to cloud · full table export · export workspace data · cloud export CJA*

**Download / CSV Export** — `/en/docs/analytics-platform/using/cja-workspace/export/download-send`
*download CSV · export to CSV · download table · row limit CSV · 50000 rows · freeform table download · download data from workspace · export as CSV · download project PDF*

**Export Project Overview** — `/en/docs/analytics-platform/using/cja-workspace/export/export-project-overview`
*export project · download project · export options · how to export from workspace*

**Manage Exports** — `/en/docs/analytics-platform/using/cja-components/exports/manage-exports`
*manage exports · export jobs · view export status · export history*

**Export Logs** — `/en/docs/analytics-platform/using/cja-components/exports/manage-export-logs`
*export logs · export errors · troubleshoot export*

**Cloud Export Accounts** — `/en/docs/analytics-platform/using/cja-components/exports/cloud-export-accounts`
*cloud export account · Amazon S3 export · Azure export · Google Cloud export · Snowflake export · set up export destination*

**Cloud Export Locations** — `/en/docs/analytics-platform/using/cja-components/exports/cloud-export-locations`
*cloud export location · S3 bucket · Azure container · GCS bucket · Snowflake location*

---

### Integrations

**Integrations Overview** — `/en/docs/analytics-platform/using/integrations/overview`
*CJA integrations · integrate with CJA · Adobe integrations · connect other Adobe products*

**Adobe Analytics Integration** — `/en/docs/analytics-platform/using/integrations/aa`
*Adobe Analytics integration · AA integration CJA*

**Target Integration** — `/en/docs/analytics-platform/using/integrations/at`
*Target integration · A/B test with Target · Adobe Target CJA · personalization data*

**Adobe Advertising Integration** — `/en/docs/analytics-platform/using/integrations/advertising`
*advertising integration · Adobe Advertising · paid media CJA · DSP integration*

**Journey Optimizer Integration** — `/en/docs/analytics-platform/using/integrations/ajo`
*AJO integration · Journey Optimizer in CJA · analyze AJO journeys · AJO reporting CJA*

**Decision Management Integration** — `/en/docs/analytics-platform/using/integrations/ajo-od`
*offer decisioning CJA · decision management integration · AJO offer data in CJA*

**Customer AI Integration** — `/en/docs/analytics-platform/using/integrations/customer-ai`
*Customer AI · propensity scores in CJA · AI scores in workspace*

---

### Content Analytics

**Content Analytics Overview** — `/en/docs/analytics-platform/using/content-analytics/content-analytics`
*content analytics · content performance · AI content insights · asset analytics*

**Configuration** — `/en/docs/analytics-platform/using/content-analytics/configuration/configuration`
*configure content analytics · content analytics setup · enable content analytics*

**Data Collection** — `/en/docs/analytics-platform/using/content-analytics/configuration/datacollection`
*content analytics data collection · capture content data · collect content events*

**Content Analytics Report** — `/en/docs/analytics-platform/using/content-analytics/report/report`
*content analytics report · view content performance · content report · asset performance*

**Content Analytics Components** — `/en/docs/analytics-platform/using/content-analytics/report/components`
*content analytics components · content dimensions · content metrics · content analytics data fields*

---

### Use Cases

**Use Cases Overview** — `/en/docs/analytics-platform/using/cja-usecases/cja-usecases`
*CJA use cases · what can I do with CJA · example use cases*

**Cross-Channel Analysis** — `/en/docs/analytics-platform/using/cja-usecases/cross-channel/cross-channel`
*cross-channel analysis · cross-channel journey · call center analysis · offline online data · customer journey cross-channel*

**Data Views Use Cases** — `/en/docs/analytics-platform/using/cja-usecases/data-views/data-views-usecases`
*data view use case · data view example · binding dimension · data view configuration example*

**Data Export Use Cases Overview** — `/en/docs/analytics-platform/using/cja-usecases/data-export/overview`
*data export use cases · how to export CJA data · export options overview · get data out of CJA*

**Export Datasets (AEP)** — `/en/docs/analytics-platform/using/cja-usecases/data-export/export-datasets`
*export datasets to AEP · dataset export use case · send CJA data back to AEP · export to data lake*

**Query Service / Data Distiller Export** — `/en/docs/analytics-platform/using/cja-usecases/data-export/queryservice-export-datasets`
*query service export · data distiller · SQL export · AEP query service datasets*

**Full Table Export Use Case** — `/en/docs/analytics-platform/using/cja-usecases/data-export/export-full-table`
*full table export use case · export millions of rows · scheduled full table · export with attribution · export with sessionization*

**BI Extension Use Case** — `/en/docs/analytics-platform/using/cja-usecases/data-export/bi-extension`
*BI extension use case · Power BI use case · Tableau use case · connect BI tool use case*

**B2B Example Project** — `/en/docs/analytics-platform/using/cja-usecases/b2b/example`
*B2B example · B2B project example · account-based reporting example · B2B workspace example*

**B2B Edition Use Cases** — `/en/docs/analytics-platform/using/cja-usecases/b2b/b2b-edition/use-cases-overview`
*B2B edition use cases · account journey · opportunity analysis · B2B analytics use cases*

**B2B Edition Setup** — `/en/docs/analytics-platform/using/cja-usecases/b2b/b2b-edition/setup`
*B2B edition setup · configure B2B edition · account-based connection setup*

**Third-Party Integrations Overview** — `/en/docs/analytics-platform/using/cja-usecases/third-party/overview`
*third-party integrations · non-Adobe data · external tool integration*

**Quantum Metric Integration** — `/en/docs/analytics-platform/using/cja-usecases/third-party/qm/qm-overview`
*Quantum Metric · session replay CJA · heatmap CJA · friction events · error events third party*

---

### Technotes & Admin

**Glossary** — `/en/docs/analytics-platform/using/technotes/glossary`
*glossary · definition · what does X mean in CJA · CJA terminology · terminology difference · AA equivalent in CJA · what is a lookup dataset · what is a data view*

**Optimizing Performance** — `/en/docs/analytics-platform/using/technotes/optimizing-performance`
*performance · slow query · query too complex · optimize workspace · project performance · too many cells · slow report · workspace timeout*

**Data Centers** — `/en/docs/analytics-platform/using/technotes/data-centers`
*data centers · data residency · where is CJA hosted · EMEA data center · APAC data center · region · data location*

**Manage Usage** — `/en/docs/analytics-platform/using/technotes/estimate-usage`
*manage usage · estimate usage · data usage · row usage · usage report · how much data am I using · usage monitoring*

**Real-Time Reporting** — `/en/docs/analytics-platform/using/cja-components/real-time-reporting/real-time`
*real-time reporting · live data · real-time metrics · current data · last 2 minutes*

**Access Control** — `/en/docs/analytics-platform/using/technotes/access-control`
*access control · permissions CJA · product profile · CJA roles · user permissions · Admin Console CJA · who can access*

**IP Addresses** — `/en/docs/analytics-platform/using/technotes/ip-addresses`
*IP addresses · allowlist IPs · firewall · network requirements · IP allowlist*

**Domains** — `/en/docs/analytics-platform/using/technotes/domains`
*CJA domains · allowlist domains · CSP domains · network domains*

---

## Tier 3 Fallback

If the catalog and Tier 2 link-following do not surface the answer, run a WebSearch using:

```
site:experienceleague.adobe.com/en/docs/analytics-platform [question keywords]
```

Fetch the most relevant result. If multiple results look relevant, fetch the top two. Always report which pages were checked alongside the answer.
