---
name: ajo
description: Answer questions about Adobe Journey Optimizer by fetching live Adobe Experience League documentation. Never answers from memory — always fetches source content, quotes directly, and cites the URL.
---

You have been invoked to answer questions about Adobe Journey Optimizer (AJO). Your job is to retrieve the correct documentation page, read it, and answer only from what that page says — not from training memory.

## Rules

**RULE 1 — FETCH BEFORE ANSWERING**
Never answer an AJO question from memory alone, even if you are confident in the answer. Always fetch at least one documentation page first. AJO documentation changes frequently and limits/features vary by capability, sandbox type, and licensing tier.

**RULE 2 — QUOTE OR DECLINE**
For any factual statement — a limit, a setting name, a step, a supported value, a behavior:
- Find the exact sentence or passage in the fetched content that states it
- Quote it verbatim in your answer
- Cite the full source URL immediately after the quote
- If the fetched page does not contain the answer, say which page you checked and what was missing — never fill the gap with inference

**RULE 3 — MULTI-PAGE FOR AMBIGUOUS QUESTIONS**
If a question could apply to more than one feature (e.g. "decisioning" maps to both Experience Decisioning and Offer Decisioning; "limit" may live on general guardrails or a feature-specific guardrails page), fetch the most relevant page for each interpretation and present both answers with their sources labeled separately.

**RULE 4 — ESCALATION CHAIN**
If the catalog page does not answer the question, escalate in order:
1. Scan links on the fetched page → fetch the most relevant linked page (Tier 2)
2. If still not found: WebSearch for `site:experienceleague.adobe.com/en/docs/journey-optimizer [question keywords]` and fetch the top result (Tier 3)
3. If still not found: state exactly which pages were checked — never guess

## Priority Rule

For any question containing **limit, maximum, max, how many, cap, threshold, guardrail, restriction, is there a limit, how much, what is the maximum, concurrent, events per second, profile cap, or package tier** — fetch the General AJO Guardrails page first, then fetch any feature-specific guardrails page that applies (Orchestrated Campaigns, Offer Decisioning). The guardrails pages are the canonical reference for all hard and soft limits in AJO.

---

## URL Catalog

Base: `https://experienceleague.adobe.com`

Match the user's question to the most relevant page(s) using the triggers listed under each entry. Fetch the full URL (base + path). When multiple pages seem relevant, fetch all of them before answering.

---

### ⚡ Priority — fetch first for ANY limit / maximum / threshold question

**AJO Guardrails & Limitations** — `/en/docs/journey-optimizer/using/get-started/essentials/guardrails`
*limit · maximum · guardrail · threshold · cap · how many · restriction · concurrent journeys · live journeys · events per second · profile limit · journey timeout · reentrance · pause duration · paused journeys · inbound events · read audience rate · supplemental ID rate · event per profile · XDM schema limit · hard limit · soft limit · sandbox limit*

**Orchestrated Campaigns Guardrails** — `/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/guardrails`
*orchestrated campaign limit · orchestrated campaign maximum · campaign table limit · schema size · channel activity limit · orchestrated guardrail*

**Offer Decisioning Guardrails** — `/en/docs/journey-optimizer/using/offer-decisioning/get-started-decision/offer-guardrails`
*offer limit · offer maximum · placement limit · collection limit · decision limit · offer activity limit · offer capping · offer decisioning guardrail · decision management limit*

---

### Get Started & Overview

**AJO Home** — `/en/docs/journey-optimizer/using/ajo-home`
*AJO home · journey optimizer home · AJO documentation · journey optimizer documentation*

**Get Started with AJO** — `/en/docs/journey-optimizer/using/get-started/essentials/get-started`
*get started · introduction to AJO · AJO overview · what is journey optimizer · adobe journey optimizer introduction*

**Understanding AJO** — `/en/docs/journey-optimizer/using/get-started/essentials/understanding-ajo`
*understanding AJO · how AJO works · AJO architecture · AJO concepts · journey optimizer architecture*

**Key Terminology** — `/en/docs/journey-optimizer/using/get-started/essentials/terminology`
*AJO terminology · AJO glossary · journey optimizer terms · what is a journey · what is a campaign · what is a surface · AJO definitions*

**AI & Intelligent Features** — `/en/docs/journey-optimizer/using/get-started/essentials/ai-features`
*AI features in AJO · intelligent features · AI in journey optimizer · machine learning AJO · smart features*

**Journeys vs Campaigns** — `/en/docs/journey-optimizer/using/get-started/work-efficiently/journeys-vs-campaigns`
*journey vs campaign · when to use journey · when to use campaign · difference between journey and campaign · should I use journey or campaign*

**Navigate the Interface** — `/en/docs/journey-optimizer/using/get-started/work-efficiently/user-interface`
*AJO interface · navigate AJO · AJO UI · journey optimizer UI · user interface · AJO navigation*

**Troubleshooting** — `/en/docs/journey-optimizer/using/get-started/troubleshooting`
*AJO troubleshooting · journey optimizer errors · debug AJO · AJO issues · common problems*

**Roles & Quick Start** — `/en/docs/journey-optimizer/using/get-started/by-role/quick-start`
*AJO quick start · getting started by role · marketer quick start · data engineer quick start*

**Developer Quick Start** — `/en/docs/journey-optimizer/using/get-started/by-role/developer`
*developer getting started · AJO developer · API developer AJO · technical quick start*

**Channels Overview** — `/en/docs/journey-optimizer/using/channels/gs-channels`
*channels overview · what channels does AJO support · AJO channel list · communication channels · all channels*

---

### Journeys

**Get Started with Journeys** — `/en/docs/journey-optimizer/using/orchestrate-journeys/journey`
*journey overview · what is a journey · journey get started · journey introduction · journey orchestration*

**Create Your First Journey** — `/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/journey-gs`
*create journey · new journey · journey creation · how to create a journey · build a journey*

**Journey Designer / Canvas** — `/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/using-the-journey-designer`
*journey designer · journey canvas · journey builder · design journey · drag and drop journey*

**Journey Activities** — `/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/about-journey-activities`
*journey activities · journey actions · journey events · wait activity · end activity · journey palette · message activity · channel action*

**Condition Activity** — `/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/condition-activity`
*journey condition · condition activity · if/else in journey · split path · branching · journey fork · data source condition · time condition*

**Test Your Journey** — `/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/testing-the-journey`
*test journey · journey test mode · journey testing · simulate journey · test profile journey*

**Journey Properties** — `/en/docs/journey-optimizer/using/orchestrate-journeys/building-advanced-conditions-journeys/syntax/journey-properties`
*journey properties · journey context · journey metadata · journeyVersionId · journey node · journey expression context*

**Build Advanced Conditions** — `/en/docs/journey-optimizer/using/orchestrate-journeys/building-advanced-conditions-journeys/building-advanced-conditions-journeys-landing-page`
*advanced conditions · journey expressions · expression editor journey · XDM in journey · conditions syntax · journey formula*

**Journey FAQ** — `/en/docs/journey-optimizer/using/orchestrate-journeys/journey-faq`
*journey FAQ · journey frequently asked questions · journey troubleshooting · journey errors · journey questions*

---

### Campaigns

**Get Started with Campaigns** — `/en/docs/journey-optimizer/using/campaigns/get-started-with-campaigns`
*campaign overview · what is a campaign · campaign get started · types of campaigns · action campaign · API campaign · orchestrated campaign*

**Create Action Campaign** — `/en/docs/journey-optimizer/using/campaigns/action-campaigns/create-campaign`
*create campaign · new campaign · how to create a campaign · action campaign setup*

**Campaign Properties** — `/en/docs/journey-optimizer/using/campaigns/action-campaigns/campaign-properties`
*campaign properties · campaign settings · campaign name · campaign tags · campaign description*

**Campaign Content** — `/en/docs/journey-optimizer/using/campaigns/action-campaigns/campaign-content`
*campaign content · add content to campaign · campaign message · campaign channel action*

**Review & Activate Campaign** — `/en/docs/journey-optimizer/using/campaigns/action-campaigns/review-activate-campaign`
*activate campaign · publish campaign · launch campaign · review campaign · campaign activation*

**Campaign Schedule** — `/en/docs/journey-optimizer/using/campaigns/action-campaigns/campaign-schedule`
*campaign schedule · schedule campaign · campaign timing · campaign recurrence · campaign start date · one-time campaign · recurring campaign*

**Campaign Audience** — `/en/docs/journey-optimizer/using/campaigns/action-campaigns/campaign-audience`
*campaign audience · target audience campaign · campaign segment · who to target campaign*

**API-Triggered Campaigns** — `/en/docs/journey-optimizer/using/campaigns/api-triggered-campaigns/api-triggered-campaigns`
*API-triggered campaign · transactional campaign · API campaign · trigger campaign via API · batch campaign API*

**API Campaign Properties** — `/en/docs/journey-optimizer/using/campaigns/api-triggered-campaigns/api-triggered-campaign-properties`
*API campaign properties · API campaign settings · contextual attributes API campaign*

**API Campaign Content** — `/en/docs/journey-optimizer/using/campaigns/api-triggered-campaigns/api-triggered-campaign-content`
*API campaign content · API campaign message · personalize API campaign*

**Review & Activate API Campaign** — `/en/docs/journey-optimizer/using/campaigns/api-triggered-campaigns/review-activate-api-triggered-campaign`
*activate API campaign · publish API campaign · API campaign activation*

**Orchestrated Campaigns Overview** — `/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/gs-orchestrated-campaigns`
*orchestrated campaigns · what are orchestrated campaigns · multi-step campaigns · orchestrated campaign overview · workflow campaign*

**Orchestrated Campaigns Landing** — `/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/orchestrated-campaigns-landing-page`
*orchestrated campaign documentation · orchestrated campaigns section*

**Orchestrated Campaigns FAQ** — `/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/orchestrated-campaigns-faq`
*orchestrated campaigns FAQ · orchestrated campaign questions · orchestrated campaign troubleshooting*

**Orchestrate Activities** — `/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/launch/orchestrate-activities`
*orchestrate activities · add activities to campaign · campaign workflow builder · campaign canvas activities*

**Create Orchestrated Campaign** — `/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/launch/create-orchestrated-campaign`
*create orchestrated campaign · new orchestrated campaign · orchestrated campaign setup · schedule orchestrated campaign*

**Design Campaign Activities** — `/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/design-campaigns/design-campaigns-landing-page`
*design campaign activities · campaign activity types · targeting activities · flow control · channel activities in campaigns*

**Orchestrated Campaign Reporting** — `/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/launch/reporting-campaigns`
*orchestrated campaign reports · campaign performance · orchestrated campaign analytics*

---

### Email Channel

**Email Channel** — `/en/docs/journey-optimizer/using/channels/email/email-landing-page`
*email channel · AJO email · email messaging · send email AJO · email overview*

**Create Email** — `/en/docs/journey-optimizer/using/channels/email/create-email`
*create email · new email · add email to journey · add email to campaign · email message creation*

**Design Email (Email Designer)** — `/en/docs/journey-optimizer/using/channels/email/design-email/design-email-landing-page`
*email designer · design email · email template · email layout · drag and drop email · HTML email · email builder · email content · email visual editor*

**Email Opt-Out** — `/en/docs/journey-optimizer/using/channels/email/email-opt-out`
*email opt-out · unsubscribe email · list unsubscribe · one-click unsubscribe · suppress email · email preference · opt-out management*

**Configure Email** — `/en/docs/journey-optimizer/using/channels/email/configure-email/configure-email-landing-page`
*configure email channel · email channel configuration · email settings · BCC email · email tracking · email header · CC field*

**Deliverability** — `/en/docs/journey-optimizer/using/monitor/deliverability/deliverability`
*deliverability · email deliverability · inbox placement · email reputation · spam · bounce · hard bounce · soft bounce*

---

### Push Notifications Channel

**Push Notifications Landing** — `/en/docs/journey-optimizer/using/channels/push/push-landing-page`
*push notification · push channel · mobile push · push overview · AJO push*

**Get Started with Push** — `/en/docs/journey-optimizer/using/channels/push/get-started-push`
*get started push · push introduction · push overview · push notifications overview*

**Push Flow & Architecture** — `/en/docs/journey-optimizer/using/channels/push/push-config/push-gs`
*push flow · push architecture · how push works · push services · APNs · FCM · push token*

**Push Notification Configuration** — `/en/docs/journey-optimizer/using/channels/push/push-config/push-configuration`
*configure push · push credentials · push certificate · push API key · iOS push config · Android push config · APNs certificate · FCM key*

**Configure Push Channel** — `/en/docs/journey-optimizer/using/channels/push/push-config/push-config-landing-page`
*push channel setup · push configuration landing · push channel prerequisites · mobile SDK push*

**Create Push Notification** — `/en/docs/journey-optimizer/using/channels/push/create-push`
*create push notification · new push · add push to journey · add push to campaign · push message creation · rapid delivery push*

**Design Push Notification** — `/en/docs/journey-optimizer/using/channels/push/design-push`
*design push · push content · push title · push body · push image · push buttons · iOS push design · Android push design · rich push*

**Send Push Notification** — `/en/docs/journey-optimizer/using/channels/push/send-push`
*send push · validate push · preview push notification · push delivery*

---

### SMS / MMS / RCS Channel

**SMS/MMS/RCS Landing** — `/en/docs/journey-optimizer/using/channels/sms/sms-landing-page`
*SMS · MMS · RCS · text message · SMS channel · mobile messaging · AJO SMS*

**Get Started with SMS** — `/en/docs/journey-optimizer/using/channels/sms/get-started-sms`
*get started SMS · SMS overview · SMS introduction · text messaging overview · SMS use cases*

**Configure SMS Channel** — `/en/docs/journey-optimizer/using/channels/sms/configure-sms/sms-configuration`
*configure SMS · SMS channel configuration · SMS provider setup · SMS channel surface*

**SMS Configuration Surface** — `/en/docs/journey-optimizer/using/channels/sms/configure-sms/sms-configuration-surface`
*SMS surface · SMS channel preset · SMS configuration settings · SMS sender number*

**Configure Custom SMS Provider** — `/en/docs/journey-optimizer/using/channels/sms/configure-sms/sms-configuration-custom`
*custom SMS provider · third party SMS · custom provider configuration · Sinch · Twilio*

**Configure Infobip** — `/en/docs/journey-optimizer/using/channels/sms/configure-sms/sms-configuration-infobip`
*Infobip SMS · configure Infobip · Infobip provider · Infobip AJO integration*

**SMS Webhook** — `/en/docs/journey-optimizer/using/channels/sms/configure-sms/sms-webhook`
*SMS webhook · SMS inbound · SMS reply · SMS opt-out webhook · SMS feedback*

**SMS Subdomains** — `/en/docs/journey-optimizer/using/channels/sms/sms-subdomains`
*SMS subdomain · URL shortening SMS · SMS link tracking · subdomain for SMS*

**Create SMS/MMS Message** — `/en/docs/journey-optimizer/using/channels/sms/create-sms`
*create SMS · new text message · add SMS to journey · SMS content · MMS message · write SMS*

**SMS Cost Optimization** — `/en/docs/journey-optimizer/using/channels/sms/sms-cost-optimization`
*SMS cost · SMS character limit · SMS encoding · SMS segments · Unicode SMS · GSM SMS · reduce SMS cost*

---

### In-App Messages Channel

**In-App Channel Landing** — `/en/docs/journey-optimizer/using/channels/in-app/in-app-landing-page`
*in-app message · in-app channel · in-app notification · mobile in-app · web in-app · AJO in-app*

**Get Started with In-App** — `/en/docs/journey-optimizer/using/channels/in-app/get-started-in-app`
*in-app overview · in-app introduction · in-app messaging get started · in-app use cases*

**In-App Configuration** — `/en/docs/journey-optimizer/using/channels/in-app/inapp-configuration`
*configure in-app · in-app prerequisites · in-app setup · in-app channel configuration · in-app surface*

**Create In-App Message (Mobile)** — `/en/docs/journey-optimizer/using/channels/in-app/create-in-app`
*create in-app · new in-app message · add in-app to journey · mobile in-app creation · in-app trigger*

**Configure Web In-App** — `/en/docs/journey-optimizer/using/channels/in-app/create-in-app-web`
*web in-app · in-app web configuration · web in-app trigger · web SDK in-app · manual trigger in-app*

**Design In-App Content** — `/en/docs/journey-optimizer/using/channels/in-app/design-in-app`
*design in-app · in-app layout · in-app image · in-app buttons · in-app modal · in-app banner · in-app fullscreen · in-app content*

---

### Web Channel

**Web Channel Landing** — `/en/docs/journey-optimizer/using/channels/web/web-landing-page`
*web channel · web personalization · AJO web · website personalization · web experience*

**Get Started with Web** — `/en/docs/journey-optimizer/using/channels/web/get-started-web`
*web channel overview · web personalization overview · web experience get started · AJO web introduction*

**Configure Web Channel** — `/en/docs/journey-optimizer/using/channels/web/configure-web-channel/configure-web-channel-landing-page`
*configure web channel · web channel setup · web configuration landing*

**Web Channel Prerequisites** — `/en/docs/journey-optimizer/using/channels/web/configure-web-channel/web-prerequisites`
*web channel prerequisites · web SDK requirement · browser extension · web channel requirements · alloy.js*

**Web Configuration** — `/en/docs/journey-optimizer/using/channels/web/configure-web-channel/web-configuration`
*web configuration · web channel surface · web property · web page URL · single page · multi-page*

**Web Subdomains** — `/en/docs/journey-optimizer/using/channels/web/configure-web-channel/web-delegated-subdomains`
*web subdomain · web channel subdomain · web content subdomain configuration*

**Create Web Experiences** — `/en/docs/journey-optimizer/using/channels/web/create-web`
*create web experience · new web experience · web personalization creation · web journey · web campaign*

**Non-Visual Editor** — `/en/docs/journey-optimizer/using/channels/web/author-web-pages/web-non-visual-editor`
*web non-visual editor · web code editor · edit web without browser extension · web modifications code*

**Author Single-Page Applications** — `/en/docs/journey-optimizer/using/channels/web/author-web-pages/web-spa`
*SPA · single-page application · web SPA · react personalization · angular personalization · SPA views*

**Monitor Web Experiences** — `/en/docs/journey-optimizer/using/channels/web/author-web-pages/monitor-web-experiences`
*monitor web experience · web experience report · web clicks · web impressions · web engagement*

---

### Code-Based Experience Channel

**Get Started with Code-Based** — `/en/docs/journey-optimizer/using/channels/code-based-experience/get-started-code-based`
*code-based experience · code-based channel · code based personalization · developer channel · JSON surface · HTML surface · API surface*

**Configure Code-Based Channel** — `/en/docs/journey-optimizer/using/channels/code-based-experience/configure-code-based-channel/configure-code-based-channel-landing-page`
*configure code-based · code-based configuration · code-based surface · code-based prerequisites · code-based SDK*

**Create Code-Based Experiences** — `/en/docs/journey-optimizer/using/channels/code-based-experience/create-code-based-experiences/create-code-based-experiences-landing-page`
*create code-based experience · code-based journey · code-based campaign · add code-based to journey*

---

### Content Cards Channel

**Content Cards Landing** — `/en/docs/journey-optimizer/using/channels/content-card/content-card-landing-page`
*content card · content cards · in-app inbox · persistent in-app · card feed · content card overview*

**Get Started with Content Cards** — `/en/docs/journey-optimizer/using/channels/content-card/configure/content-card-lp`
*content card get started · content card introduction · content card prerequisites · content card setup*

**Content Card Config Prerequisites** — `/en/docs/journey-optimizer/using/channels/content-card/configure/content-card-configuration-prereq`
*content card configuration · content card prerequisites · content card setup · content card channel config*

**Content Card SDK Configuration** — `/en/docs/journey-optimizer/using/channels/content-card/configure/content-card-configuration-sdk`
*content card SDK · web SDK content card · content card web configuration · content card implementation*

**Create Content Card** — `/en/docs/journey-optimizer/using/channels/content-card/create-content-card`
*create content card · new content card · add content card to journey · content card campaign · content card message*

**Design Content Card** — `/en/docs/journey-optimizer/using/channels/content-card/design-content-card`
*design content card · content card layout · content card image · content card buttons · content card personalization*

---

### Direct Mail Channel

**Get Started with Direct Mail** — `/en/docs/journey-optimizer/using/channels/direct-mail/get-started-direct-mail`
*direct mail · direct mail channel · physical mail · postal mail · direct mail overview · print channel*

**Direct Mail Configuration** — `/en/docs/journey-optimizer/using/channels/direct-mail/direct-mail-configuration`
*configure direct mail · direct mail provider · direct mail file routing · direct mail extraction file · DM configuration*

**Create Direct Mail** — `/en/docs/journey-optimizer/using/channels/direct-mail/create-direct-mail`
*create direct mail · new direct mail · direct mail message creation · direct mail content · direct mail file*

**Test & Send Direct Mail** — `/en/docs/journey-optimizer/using/channels/direct-mail/test-send-direct-mail`
*send direct mail · test direct mail · validate direct mail · direct mail delivery · preview direct mail*

---

### WhatsApp Channel

**Get Started with WhatsApp** — `/en/docs/journey-optimizer/using/channels/whatsapp/get-started-whatsapp`
*WhatsApp · WhatsApp channel · WhatsApp messaging · AJO WhatsApp · WhatsApp overview*

**WhatsApp Configuration** — `/en/docs/journey-optimizer/using/channels/whatsapp/whatsapp-configuration`
*configure WhatsApp · WhatsApp setup · WhatsApp business API · WhatsApp channel configuration · Meta WhatsApp*

**Create WhatsApp Message** — `/en/docs/journey-optimizer/using/channels/whatsapp/create-whatsapp`
*create WhatsApp message · new WhatsApp · add WhatsApp to journey · WhatsApp message content*

**Send WhatsApp Message** — `/en/docs/journey-optimizer/using/channels/whatsapp/send-whatsapp`
*send WhatsApp · deliver WhatsApp · validate WhatsApp message · WhatsApp delivery*

---

### LINE Channel

**LINE Configuration** — `/en/docs/journey-optimizer/using/channels/line/line-configuration`
*LINE channel · configure LINE · LINE messaging · LINE provider setup · AJO LINE*

**Create LINE Message** — `/en/docs/journey-optimizer/using/channels/line/create-line`
*create LINE message · LINE message content · add LINE to journey · new LINE message*

**Send LINE Message** — `/en/docs/journey-optimizer/using/channels/line/send-line`
*send LINE message · deliver LINE · validate LINE message · LINE delivery*

---

### iOS Live Activities Channel

**Get Started with Live Activities** — `/en/docs/journey-optimizer/using/channels/live-activity/get-started-mobile-live`
*live activities · iOS live activity · lock screen notification · dynamic island · live updates · live activity overview*

**Configure Live Activities** — `/en/docs/journey-optimizer/using/channels/live-activity/configure/mobile-live-configuration`
*configure live activities · live activity setup · live activity channel configuration · live activity prerequisites*

**Create Live Activity** — `/en/docs/journey-optimizer/using/channels/live-activity/create-mobile-live`
*create live activity · new live activity · live activity campaign · start live activity · update live activity · end live activity*

**Live Activity FAQ** — `/en/docs/journey-optimizer/using/channels/live-activity/mobile-live-faq`
*live activity FAQ · live activity questions · live activity limitations · live activity troubleshooting*

**Troubleshoot Live Activities** — `/en/docs/journey-optimizer/using/channels/live-activity/troubleshoot-mobile-live`
*troubleshoot live activity · live activity errors · debug live activity · live activity not showing*

---

### Experience Decisioning (Decisioning)

**Experience Decisioning Landing** — `/en/docs/journey-optimizer/using/decisioning/experience-decisioning/experience-decisioning-landing-page`
*experience decisioning · decisioning · AJO decisioning · offer decisioning new · decision items · personalized offers decisioning*

**Get Started with Decisioning** — `/en/docs/journey-optimizer/using/decisioning/experience-decisioning/gs-experience-decisioning`
*get started decisioning · decisioning overview · decisioning introduction · how decisioning works · decision catalog*

**Decision Items** — `/en/docs/journey-optimizer/using/decisioning/experience-decisioning/manage-decision-items/items`
*decision items · create decision item · manage decision items · offer catalog · decision item attributes · eligibility rules for items*

**Decision Policy Get Started** — `/en/docs/journey-optimizer/using/decisioning/experience-decisioning/decision-policies/create-decision`
*decision policy · what is a decision policy · decision policy overview · create decision policy · add decision policy*

**Create Decision Policy** — `/en/docs/journey-optimizer/using/decisioning/experience-decisioning/decision-policies/create-decision-policy`
*create decision policy · decision policy setup · configure decision policy · selection strategy · decision policy channel*

**Context Data for Decisioning** — `/en/docs/journey-optimizer/using/decisioning/experience-decisioning/selection/context-data`
*context data decisioning · use context in decision · runtime context decisioning · profile attributes decisioning · event context decisioning*

**AEP Data for Decisioning** — `/en/docs/journey-optimizer/using/decisioning/experience-decisioning/aep-data/aep-data-exd`
*AEP data in decisioning · platform data decisioning · lookup data decisioning · AEP dataset decision items*

**Report on Decisioning** — `/en/docs/journey-optimizer/using/decisioning/experience-decisioning/cja-reporting`
*decisioning reports · decisioning analytics · CJA decisioning report · measure decisioning · decisioning performance*

**Decisioning Use Case** — `/en/docs/journey-optimizer/using/decisioning/experience-decisioning/experience-decisioning-uc`
*decisioning use case · decisioning example · code-based decisioning · content experiment decisioning · decisioning tutorial*

---

### Offer Decisioning / Decision Management

**Get Started with Offer Decisioning** — `/en/docs/journey-optimizer/using/offer-decisioning/get-started-decision/starting-offer-decisioning`
*offer decisioning · decision management · offer management · offer library · personalized offers · AJO offers · offer engine*

**Key Steps to Create an Offer** — `/en/docs/journey-optimizer/using/offer-decisioning/get-started-decision/key-steps`
*create offer steps · offer creation workflow · how to create an offer · offer setup process · offer components*

**Offers E2E Tutorial** — `/en/docs/journey-optimizer/using/offer-decisioning/get-started-decision/offers-e2e`
*offer end to end · offer tutorial · personalized offer in email · offer example · offer walkthrough*

**Add Constraints to Offer** — `/en/docs/journey-optimizer/using/offer-decisioning/managing-offers-in-the-offer-library/configure-offers/add-constraints`
*offer constraints · offer capping · offer eligibility · offer rules · offer frequency cap · offer expiry date · offer date constraint*

**Configure Offer Selection in Decisions** — `/en/docs/journey-optimizer/using/offer-decisioning/create-manage-activities/configure-offer-selection`
*offer selection · decision offer selection · ranking in decision · offer ranking · configure offer activity*

**Create Simulations** — `/en/docs/journey-optimizer/using/offer-decisioning/create-manage-activities/simulation`
*offer simulation · simulate offers · test offers · offer preview · offer decision test · which offers are selected*

**Batch Decisioning** — `/en/docs/journey-optimizer/using/offer-decisioning/batch-delivery`
*batch decisioning · batch offer · offer to audience · deliver offers to all profiles · offline offer decisioning*

**Rankings Get Started** — `/en/docs/journey-optimizer/using/offer-decisioning/rankings/get-started-rankings`
*offer ranking · rank offers · offer priority · ranking formula · rank by score · offer eligibility ranking*

**Create AI Ranking Models** — `/en/docs/journey-optimizer/using/offer-decisioning/rankings/ai-models/create-ranking-strategies`
*AI ranking · auto-optimization · offer AI model · machine learning ranking · predictive ranking · auto-optimize offer*

**Offer Decisioning API** — `/en/docs/journey-optimizer/using/offer-decisioning/api-reference/offer-delivery-api/decisioning-api`
*offer API · decisioning API · deliver offers API · Edge Decisioning API · batch decisioning API · offer delivery API*

---

### Content Templates & Fragments

**Content Templates Landing** — `/en/docs/journey-optimizer/using/content-management/content-templates/content-templates-landing-page`
*content templates · template overview · AJO templates · reusable content*

**About Content Templates** — `/en/docs/journey-optimizer/using/content-management/content-templates/content-templates`
*what are content templates · content template overview · email template · SMS template · push template · in-app template*

**Access Content Templates** — `/en/docs/journey-optimizer/using/content-management/content-templates/access-content-templates`
*access templates · browse templates · template library · find content template*

**Create Content Templates** — `/en/docs/journey-optimizer/using/content-management/content-templates/create-content-templates`
*create content template · new template · save as template · build content template*

**Content Locking** — `/en/docs/journey-optimizer/using/content-management/content-templates/content-locking`
*content locking · lock template · locked content · prevent editing template · template governance · template protection*

**Test Content Templates** — `/en/docs/journey-optimizer/using/content-management/content-templates/test-content-templates`
*test template · preview template · validate content template · template preview*

**Use Content Templates** — `/en/docs/journey-optimizer/using/content-management/content-templates/use-content-templates`
*use template · apply template · select template · template in journey · template in campaign*

**Fragments Landing** — `/en/docs/journey-optimizer/using/content-management/fragments/fragments-landing-page`
*fragments · content fragments · reusable content blocks · fragment overview*

**About Fragments** — `/en/docs/journey-optimizer/using/content-management/fragments/fragments`
*what are fragments · visual fragment · expression fragment · fragment types · reusable blocks*

**Create Fragments** — `/en/docs/journey-optimizer/using/content-management/fragments/create-fragments`
*create fragment · new fragment · build fragment · design fragment · expression fragment creation*

**Save as Fragment** — `/en/docs/journey-optimizer/using/content-management/fragments/save-fragments`
*save as fragment · convert to fragment · make reusable · save selection as fragment*

**Customizable Fragments** — `/en/docs/journey-optimizer/using/content-management/fragments/customizable-fragments`
*customizable fragment · editable fragment · customize fragment · override fragment field · fragment variable*

**Manage Fragments** — `/en/docs/journey-optimizer/using/content-management/fragments/manage-fragments`
*manage fragments · edit fragment · delete fragment · archive fragment · publish fragment · fragment status*

---

### Personalization

**Personalization Landing** — `/en/docs/journey-optimizer/using/content-management/personalization/personalization-landing-page`
*personalization overview · AJO personalization · dynamic personalization · personalize content*

**Personalize Content** — `/en/docs/journey-optimizer/using/content-management/personalization/personalize`
*personalize message · add personalization · how to personalize · personalization in AJO · first name personalization*

**Build Expressions** — `/en/docs/journey-optimizer/using/content-management/personalization/personalization-build-expressions`
*expression editor · personalization editor · build personalization expression · expression builder*

**Personalization Syntax** — `/en/docs/journey-optimizer/using/content-management/personalization/personalization-syntax`
*personalization syntax · Handlebars syntax · expression syntax · if helper · each helper · capitalize · uppercase · profile attribute syntax*

**Use Expression Fragments** — `/en/docs/journey-optimizer/using/content-management/personalization/use-expression-fragments`
*expression fragments in personalization · use fragment in expression editor · reusable expression*

**AEP Data Personalization** — `/en/docs/journey-optimizer/using/content-management/personalization/aep-data-perso`
*AEP data personalization · platform data in message · dataset lookup personalization · AEP attribute personalization*

**Helper Functions** — `/en/docs/journey-optimizer/using/content-management/personalization/functions/functions-landing-page`
*helper functions · personalization functions · string functions · date functions · math functions · array functions · toUpperCase · toLowercase · formatDate · isEmpty*

**Personalization Use Cases** — `/en/docs/journey-optimizer/using/content-management/personalization/personalization-use-cases/personalization-use-cases-landing-page`
*personalization examples · personalization use cases · personalize with offer ranking · use context in personalization · email personalization example*

---

### Dynamic Content

**Dynamic Content Landing** — `/en/docs/journey-optimizer/using/content-management/dynamic/dynamic-landing-page`
*dynamic content · conditional content · variants by audience · content variants · rule-based content*

**Get Started with Dynamic Content** — `/en/docs/journey-optimizer/using/content-management/dynamic/get-started-dynamic-content`
*dynamic content overview · conditional content overview · get started dynamic · variants introduction*

**Create Conditions** — `/en/docs/journey-optimizer/using/content-management/dynamic/create-conditions`
*create conditions · condition rules · conditional rule · build condition · condition editor · audience condition · profile condition*

**Add Dynamic Content** — `/en/docs/journey-optimizer/using/content-management/dynamic/dynamic-content`
*add dynamic content · apply condition · show if condition · content variant · dynamic email · conditional message*

---

### AI Assistant for Content Generation

**AI Assistant Landing** — `/en/docs/journey-optimizer/using/content-management/ai-assistant/ai-assistant-landing-page`
*AI assistant · content generation AI · generative AI AJO · AI content · AI writing · AI images*

**Get Started with AI Assistant** — `/en/docs/journey-optimizer/using/content-management/ai-assistant/gs-generative`
*AI assistant overview · generative AI overview · get started AI content · Azure OpenAI AJO · Firefly AJO*

**AI Prompting Guide** — `/en/docs/journey-optimizer/using/content-management/ai-assistant/ai-assistant-prompting-guide`
*AI prompting · write prompts AI · CO-STAR framework · AI prompt guide · better AI content prompts · prompt tips*

**Generate Full Content** — `/en/docs/journey-optimizer/using/content-management/ai-assistant/generative-full-content`
*generate full email · AI full content · complete email AI · AI generate entire message · AI email generation*

**Generate Images** — `/en/docs/journey-optimizer/using/content-management/ai-assistant/generative-image`
*generate images AI · AI image generation · AI visual content · Firefly images · AI image email*

**Generate Push with AI** — `/en/docs/journey-optimizer/using/content-management/ai-assistant/generative-push`
*AI push notification · generate push content · AI write push · push content generation*

**Generate Landing Page with AI** — `/en/docs/journey-optimizer/using/content-management/ai-assistant/generative-lp`
*AI landing page · generate landing page content · AI landing page generation*

**Content Experiment with AI** — `/en/docs/journey-optimizer/using/content-management/ai-assistant/generative-experimentation`
*AI experiment · AI A/B test · AI content variation · generate experiment variants AI*

**AI Personalization Expressions** — `/en/docs/journey-optimizer/using/content-management/ai-assistant/generative-personalization-expressions`
*AI personalization expressions · generate expression AI · explain expression AI · fix expression AI · AI in expression editor*

**Brand Management** — `/en/docs/journey-optimizer/using/content-management/ai-assistant/brands/brands`
*brand management · brand guidelines AI · brand voice · manage brand · upload brand guidelines · brand alignment AI*

---

### Content Experiments & Optimization

**Get Started with Content Experiments** — `/en/docs/journey-optimizer/using/content-management/content-experiment/get-started-experiment`
*content experiment · A/B test · AB testing · content test · experiment overview · randomized trial*

**Create Content Experiment** — `/en/docs/journey-optimizer/using/content-management/content-experiment/content-experiment`
*create content experiment · new experiment · create A/B test · experiment variants · experiment setup*

**Get Started with Message Optimization** — `/en/docs/journey-optimizer/using/content-management/message-optimization/gs-message-optimization`
*message optimization · send-time optimization · STO · winning variant · experiment winner · optimize content*

**Optimization via Experimentation** — `/en/docs/journey-optimizer/using/content-management/message-optimization/optimization-experimentation`
*optimization experimentation · use experiment for optimization · winning treatment · auto-send winning variant*

---

### Multilingual Content

**Multilingual Content Landing** — `/en/docs/journey-optimizer/using/content-management/content-multilingual/content-multilingual-landing-page`
*multilingual content · multi-language · localization · translation AJO · multilingual messaging*

**Get Started Multilingual** — `/en/docs/journey-optimizer/using/content-management/content-multilingual/multilingual-gs`
*get started multilingual · multilingual overview · multilingual introduction · language translation permissions*

**Create Locales** — `/en/docs/journey-optimizer/using/content-management/content-multilingual/multilingual-locale`
*create locale · language locale · add locale · locale settings · manage language locales*

**Add Language Providers** — `/en/docs/journey-optimizer/using/content-management/content-multilingual/multilingual-provider`
*translation provider · language provider · add translation service · translation API · language service provider*

**Manual Translation** — `/en/docs/journey-optimizer/using/content-management/content-multilingual/multilingual-manual`
*manual translation · translate manually · multilingual manual · export for translation · import translation*

**Automated Translation** — `/en/docs/journey-optimizer/using/content-management/content-multilingual/multilingual-automated`
*automated translation · auto-translate · machine translation · automatic translation workflow · translate automatically*

---

### Landing Pages

**Get Started with Landing Pages** — `/en/docs/journey-optimizer/using/content-management/landing-pages/get-started-lp`
*landing page · AJO landing page · landing page overview · landing page introduction · subscription page*

**Create Landing Pages** — `/en/docs/journey-optimizer/using/content-management/landing-pages/create-lp`
*create landing page · new landing page · build landing page · landing page setup*

**Design Landing Pages** — `/en/docs/journey-optimizer/using/content-management/landing-pages/landing-pages-design/design-lp`
*design landing page · landing page template · landing page editor · customize landing page · landing page layout*

**Landing Page Forms** — `/en/docs/journey-optimizer/using/content-management/landing-pages/lp-forms`
*landing page form · opt-in form · subscription form · form fields landing page · form components*

**LP Subdomains** — `/en/docs/journey-optimizer/using/content-management/landing-pages/lp-configuration/lp-subdomains`
*landing page subdomain · landing page domain · configure LP subdomain · LP URL*

**LP Presets** — `/en/docs/journey-optimizer/using/content-management/landing-pages/lp-configuration/lp-presets`
*landing page preset · landing page configuration · LP preset · landing page channel surface*

**Subscription Lists** — `/en/docs/journey-optimizer/using/content-management/landing-pages/subscription-list`
*subscription list · email subscription · subscribe · manage subscriptions · opt-in list*

**Landing Page Use Cases** — `/en/docs/journey-optimizer/using/content-management/landing-pages/lp-use-cases`
*landing page use cases · LP examples · opt-in use case · subscription use case · unsubscribe landing page*

---

### Cross-Solution Content Integrations

**Content Integrations Overview** — `/en/docs/journey-optimizer/using/content-management/combine/combine-landing-page`
*content integrations · AJO integrations content · combine solutions · cross-solution content*

**Content Integration List** — `/en/docs/journey-optimizer/using/content-management/combine/content-integrations`
*supported content integrations · integration list · which integrations · AJO content partners*

**Assets (Asset Essentials)** — `/en/docs/journey-optimizer/using/content-management/combine/assets`
*AEM Assets Essentials · asset library · image library · digital assets AJO · use images from assets*

**Adobe Stock** — `/en/docs/journey-optimizer/using/content-management/combine/stock`
*Adobe Stock · stock images · licensed images · stock photo AJO · use stock images*

**Adobe Express** — `/en/docs/journey-optimizer/using/content-management/combine/express`
*Adobe Express · image editing · design in Express · Express integration · create images Express*

**AEM Content Fragments** — `/en/docs/journey-optimizer/using/content-management/combine/aem/aem-fragments`
*AEM fragments · AEM content fragments · Experience Manager fragments · use AEM content in AJO*

**AEM Dynamic Media** — `/en/docs/journey-optimizer/using/content-management/combine/aem-dynamic`
*AEM Dynamic Media · dynamic media integration · Experience Manager Dynamic Media · dynamic images AJO*

**GenStudio Integration** — `/en/docs/journey-optimizer/using/content-management/combine/genstudio`
*GenStudio · GenStudio for Performance Marketing · GenStudio AJO · export template GenStudio · import from GenStudio*

**MCP Clients (Beta)** — `/en/docs/journey-optimizer/using/content-management/combine/ajo-mcp`
*MCP · model context protocol · AJO MCP · AI assistant MCP · inspect AJO from AI · troubleshoot via MCP*

---

### Testing, Preview & Approval

**Test, Validate & Approve Landing** — `/en/docs/journey-optimizer/using/test/test-landing-page`
*test AJO · validate message · approve message · testing overview · preview test approval*

**Preview & Test Content Landing** — `/en/docs/journey-optimizer/using/test/preview-test/preview-test-landing-page`
*preview content · test content · preview and test · message preview*

**Preview and Test** — `/en/docs/journey-optimizer/using/test/preview-test/preview-test`
*preview message · test message · use test profiles · preview email · preview push · preview SMS*

**Simulate Content Variations** — `/en/docs/journey-optimizer/using/test/preview-test/simulate-sample-input`
*simulate content · simulate variations · sample input · test with sample data · simulate personalization*

**Send Proofs** — `/en/docs/journey-optimizer/using/test/preview-test/proofs`
*send proof · email proof · proof delivery · test send · send to seed address · proof rendering*

**Get Started with Approval** — `/en/docs/journey-optimizer/using/test/approve/gs-approval`
*approval workflow · get started approvals · approve journey · approve campaign · approval overview*

**Approve Journeys & Campaigns** — `/en/docs/journey-optimizer/using/test/approve/approve-landing-page`
*approve journey · approve campaign · approval policies · create approval policy · require approval*

**Review & Approve Request** — `/en/docs/journey-optimizer/using/test/approve/review-approve-request`
*review approval request · approve request · reject request · reviewer role · approve or reject*

---

### Audiences, Profiles & Identities

**Audiences Landing** — `/en/docs/journey-optimizer/using/audiences-profiles-identities/audiences/audiences-landing-page`
*audiences overview · AJO audiences · audience management · audience section*

**About Audiences** — `/en/docs/journey-optimizer/using/audiences-profiles-identities/audiences/about-audiences`
*what are audiences · audience types · AEP audiences in AJO · audience composition · streaming audiences · batch audiences · audience qualification*

**Create Audiences** — `/en/docs/journey-optimizer/using/audiences-profiles-identities/audiences/create/create-landing-page`
*create audience · segment builder · new audience · build audience · audience rule · create segment*

**Target Audiences in Journeys** — `/en/docs/journey-optimizer/using/audiences-profiles-identities/audiences/target-audiences`
*target audience · read audience journey · audience-based journey · how to use audience in journey · select audience*

**Enrichment Attributes** — `/en/docs/journey-optimizer/using/audiences-profiles-identities/audiences/enrichment-attributes`
*enrichment attributes · audience enrichment · enrich audience · audience composition attributes · use enrichment in personalization*

**Profiles Landing** — `/en/docs/journey-optimizer/using/audiences-profiles-identities/profiles/profiles-landing-page`
*profile overview · AJO profiles · customer profile · real-time profile*

**Get Started with Profiles** — `/en/docs/journey-optimizer/using/audiences-profiles-identities/profiles/get-started-profiles`
*get started profiles · profile introduction · unified customer profile · profile attributes · profile data*

**Test Profiles** — `/en/docs/journey-optimizer/using/audiences-profiles-identities/profiles/creating-test-profiles`
*test profiles · create test profile · test profile creation · seed profile · profile for testing*

**Computed Attributes** — `/en/docs/journey-optimizer/using/audiences-profiles-identities/profiles/computed-attributes`
*computed attributes · calculated attributes · derived attributes · profile computed · event aggregation attribute*

**Get Started with Identity** — `/en/docs/journey-optimizer/using/audiences-profiles-identities/get-started-identity`
*identity · identity graph · identity namespace · cross-device identity · profile identity linking · ECID*

**License Usage** — `/en/docs/journey-optimizer/using/audiences-profiles-identities/license-usage`
*license usage · engageable profiles · license limit · profile count · AJO license · usage dashboard*

---

### Reporting & Analytics

**Get Started with Reporting** — `/en/docs/journey-optimizer/using/reporting/gs-reports`
*reporting overview · AJO reports · analytics AJO · performance reporting · reporting get started*

**Live Reports** — `/en/docs/journey-optimizer/using/reporting/live-report/live-report`
*live report · real-time report · last 24 hours · live performance · live metrics*

**All-Time Reports with CJA** — `/en/docs/journey-optimizer/using/reporting/channel-report/report-gs-cja`
*all-time report · CJA reports · updated reporting experience · global report · new reporting*

**Manage CJA Reports** — `/en/docs/journey-optimizer/using/reporting/channel-report/report-cja-manage`
*manage reports · customize reports · export report · report filters · create report · scheduled report*

**Work with CJA in AJO** — `/en/docs/journey-optimizer/using/reporting/channel-report/cja-ajo`
*CJA integration · AJO CJA · customer journey analytics journey optimizer · CJA data view AJO*

**Journey Live Report** — `/en/docs/journey-optimizer/using/reporting/live-report/journey-live-report`
*journey live report · journey real-time report · journey performance live · journey metrics live*

**Journey Report (All-Time)** — `/en/docs/journey-optimizer/using/reporting/channel-report/journey-reporting/journey-global-report-cja`
*journey report · journey analytics · journey performance report · journey email report · journey SMS report · journey push report*

**Journey Reports Landing** — `/en/docs/journey-optimizer/using/reporting/channel-report/journey-reporting/journey-reporting-landing-page`
*journey reports section · journey reporting overview*

**Journey Step Sharing** — `/en/docs/journey-optimizer/using/reporting/reports/sharing-overview`
*journey step sharing · journey data AEP · share journey data · journey events AEP dataset · export journey data*

**Campaign Live Report** — `/en/docs/journey-optimizer/using/reporting/live-report/campaign-live-report`
*campaign live report · campaign real-time metrics · campaign performance live*

**Campaign Report (All-Time)** — `/en/docs/journey-optimizer/using/reporting/channel-report/campaign-reporting/campaign-global-report-cja`
*campaign report · campaign analytics · campaign performance · campaign email report · campaign SMS report*

**Landing Page Live Report** — `/en/docs/journey-optimizer/using/reporting/live-report/lp-report-live`
*landing page live report · LP live metrics · landing page performance live*

**Landing Page Report** — `/en/docs/journey-optimizer/using/reporting/channel-report/lp-report-global-cja`
*landing page report · LP analytics · landing page performance all-time · LP metrics*

**Subscription Live Report** — `/en/docs/journey-optimizer/using/reporting/live-report/subscription-report-live`
*subscription live report · subscription metrics live · subscription list report live*

**Subscription Report** — `/en/docs/journey-optimizer/using/reporting/channel-report/subscription-report-global-cja`
*subscription report · subscription analytics · subscription list performance · opt-in report*

---

### Channel Configuration

**Get Started with Configuration** — `/en/docs/journey-optimizer/using/configuration/get-started-configuration`
*channel configuration · AJO configuration · configure channels · channel setup overview · channel surface*

**Channel Surfaces / Configurations** — `/en/docs/journey-optimizer/using/configuration/channel-surfaces`
*channel surface · channel configuration · create channel surface · channel preset · configure email surface · configure SMS surface · configure push surface*

**Mobile Setup Guide** — `/en/docs/journey-optimizer/using/configuration/guided-setup/set-mobile-config`
*mobile setup · guided setup mobile · configure mobile · mobile SDK setup · mobile channel setup*

**IP Warmup Get Started** — `/en/docs/journey-optimizer/using/configuration/implement-ip-warmup-plan/ip-warmup-gs`
*IP warmup · warm up IPs · IP warming plan · new IP reputation · deliverability warmup*

**IP Warmup Deliverability Guide** — `/en/docs/journey-optimizer/using/configuration/implement-ip-warmup-plan/ip-warmup-deliverability-guide`
*IP warmup guide · warmup schedule · ramp up sending · warmup phases*

**Seed Lists** — `/en/docs/journey-optimizer/using/configuration/seed-lists`
*seed list · seed address · test delivery · seed email · BCC seed · monitor deliverability seed*

**Archiving Support** — `/en/docs/journey-optimizer/using/configuration/archiving-support`
*archiving · archive messages · message archiving · email archiving · BCC archiving · compliance archiving*

**Primary Email Address** — `/en/docs/journey-optimizer/using/configuration/primary-email-addresses`
*primary email address · execution address · profile email field · change email field · email address field*

**CC Email Field** — `/en/docs/journey-optimizer/using/configuration/cc-email-field`
*CC email · carbon copy · visible CC · email CC field · add CC to email*

**Business Rules / Frequency Rules** — `/en/docs/journey-optimizer/using/configuration/frequency-rules`
*frequency rules · business rules · frequency capping · message frequency · communication limit · how often can I contact · daily cap · weekly cap · monthly cap*

---

### Subdomain Delegation & Deliverability

**Subdomain Delegation Landing** — `/en/docs/journey-optimizer/using/configuration/delegate-subdomains/delegate-subdomains-landing-page`
*subdomain delegation · delegate subdomain · email subdomain · configure subdomain · subdomain setup*

**About Subdomain Delegation** — `/en/docs/journey-optimizer/using/configuration/delegate-subdomains/about-subdomain-delegation`
*subdomain delegation overview · full delegation · CNAME delegation · subdomain types · why delegate subdomain*

**Full Delegation** — `/en/docs/journey-optimizer/using/configuration/delegate-subdomains/delegate-subdomain`
*full subdomain delegation · delegate email subdomain · Adobe manage DNS · full DNS delegation*

**Custom CNAME Delegation** — `/en/docs/journey-optimizer/using/configuration/delegate-subdomains/delegate-custom-subdomain`
*CNAME delegation · custom subdomain · customer-owned certificate · CNAME setup*

**DMARC Record** — `/en/docs/journey-optimizer/using/configuration/delegate-subdomains/dmarc-record`
*DMARC · DMARC record · email authentication · DMARC policy · SPF DKIM DMARC*

**Google TXT Record** — `/en/docs/journey-optimizer/using/configuration/delegate-subdomains/google-txt`
*Google TXT record · Gmail sender · Google postmaster · TXT verification · Gmail deliverability*

**PTR Records** — `/en/docs/journey-optimizer/using/configuration/delegate-subdomains/ptr-records`
*PTR records · reverse DNS · PTR record management · rDNS · reverse lookup*

**IP Pools** — `/en/docs/journey-optimizer/using/configuration/delegate-subdomains/ip-pools`
*IP pools · create IP pool · assign IPs · IP address pool · dedicated IP · shared IP*

**Suppression List** — `/en/docs/journey-optimizer/using/configuration/monitor-reputation/manage-suppression-list`
*suppression list · suppressed email · blocked email · manage suppression · remove from suppression · add to suppression · hard bounce list*

**Email Retries** — `/en/docs/journey-optimizer/using/configuration/monitor-reputation/retries`
*email retries · retry after bounce · soft bounce retry · retry settings · bounce handling*

**Allowed List** — `/en/docs/journey-optimizer/using/configuration/monitor-reputation/allow-list`
*allowed list · allowlist · safe sender · test allowed list · restrict sending · allow specific addresses*

---

### Conflict Management & Prioritization

**Conflicts Detection** — `/en/docs/journey-optimizer/using/conflict-prioritization/conflicts`
*conflict detection · journey conflict · campaign conflict · overlapping journeys · AJO conflicts · detect conflicts · simultaneous campaigns*

**Priority Scores** — `/en/docs/journey-optimizer/using/conflict-prioritization/priority-scores`
*priority score · journey priority · campaign priority · message priority · set priority · prioritize messages*

**Capping Rules Landing** — `/en/docs/journey-optimizer/using/conflict-prioritization/capping-rules/capping-rules-landing-page`
*capping rules · frequency cap · message cap · contact frequency · rule set overview*

**Journey Capping** — `/en/docs/journey-optimizer/using/conflict-prioritization/capping-rules/journey-capping`
*journey capping · limit journey entries · entry cap · journey frequency limit · cap journeys*

**Channel Capping** — `/en/docs/journey-optimizer/using/conflict-prioritization/capping-rules/channel-capping`
*channel capping · channel frequency limit · cap by channel · email frequency cap · push frequency cap · SMS cap*

**Quiet Hours** — `/en/docs/journey-optimizer/using/conflict-prioritization/capping-rules/quiet-hours`
*quiet hours · do not disturb · DND hours · send time restrictions · quiet period · no send window*

**Rule Sets** — `/en/docs/journey-optimizer/using/conflict-prioritization/capping-rules/rule-sets`
*rule sets · capping rule sets · create rule set · assign rule set · business rules set*

**Journey Ranking Formulas** — `/en/docs/journey-optimizer/using/conflict-prioritization/journey-arbitration/journey-ranking-formulas`
*journey ranking formula · arbitration formula · journey arbitration · rank journeys · which journey wins*

**Journey AI Models** — `/en/docs/journey-optimizer/using/conflict-prioritization/journey-arbitration/journey-ai-models`
*journey AI model · AI arbitration · machine learning arbitration · AI journey ranking*

---

### Connect Systems: APIs & External Systems

**Integrations Overview** — `/en/docs/journey-optimizer/using/connect-systems/ajo-integrations`
*AJO integrations · integrations overview · connect AJO · AJO connected systems*

**AJO APIs Overview** — `/en/docs/journey-optimizer/using/connect-systems/ajo-apis`
*AJO API · journey optimizer API · REST API AJO · API overview · which APIs does AJO have*

**External Systems Landing** — `/en/docs/journey-optimizer/using/connect-systems/external-systems/external-systems-landing-page`
*external systems · connect external · external data source · custom action · third-party integration*

**External Systems** — `/en/docs/journey-optimizer/using/connect-systems/external-systems/external-systems`
*external systems overview · external data · call external system · custom action external · real-time data AJO*

**API Capping** — `/en/docs/journey-optimizer/using/connect-systems/external-systems/capping`
*API capping · capping for external calls · limit API calls · throttle external system · max calls per second*

**API Throttling** — `/en/docs/journey-optimizer/using/connect-systems/external-systems/throttling`
*API throttling · throttle external calls · throttling configuration · rate limit external API · manage API calls*

**Get Started with Sources** — `/en/docs/journey-optimizer/using/connect-systems/get-started-sources`
*data sources · source connectors · ingest data · data ingestion AJO · connect data source*

---

### Connect Systems: Adobe Solutions & Sandboxes

**Adobe Solutions Landing** — `/en/docs/journey-optimizer/using/connect-systems/adobe-solutions/adobe-solutions-landing-page`
*Adobe solutions integration · Adobe integrations · connect Adobe products · Campaign integration · Marketo integration*

**Campaign Standard Integration** — `/en/docs/journey-optimizer/using/connect-systems/adobe-solutions/acs-action`
*Campaign Standard · ACS action · Adobe Campaign Standard · integrate Campaign Standard · ACS AJO*

**Campaign v7/v8 Integration** — `/en/docs/journey-optimizer/using/connect-systems/adobe-solutions/acc-action`
*Campaign Classic · Campaign v7 · Campaign v8 · Adobe Campaign · integrate ACC · ACC AJO*

**Marketo Engage Integration** — `/en/docs/journey-optimizer/using/connect-systems/adobe-solutions/marketo-engage`
*Marketo · Marketo Engage · AJO Marketo integration · connect Marketo*

**Sandboxes** — `/en/docs/journey-optimizer/using/connect-systems/sandbox/sandboxes`
*sandboxes · AJO sandbox · sandbox management · development sandbox · production sandbox · sandbox overview*

**Copy Objects Across Sandboxes** — `/en/docs/journey-optimizer/using/connect-systems/sandbox/copy-objects-to-sandbox`
*copy objects sandbox · migrate sandbox · copy journey to sandbox · copy campaign sandbox · sandbox packages · sandbox migration*

---

### Access Control & Permissions

**Permissions Overview** — `/en/docs/journey-optimizer/using/access-control/permissions-overview`
*permissions overview · access control overview · AJO permissions · who can do what · roles permissions*

**Permissions** — `/en/docs/journey-optimizer/using/access-control/permissions`
*manage permissions · configure permissions · user permissions · assign permissions · AJO access control*

**Out-of-the-Box Product Profiles** — `/en/docs/journey-optimizer/using/access-control/ootb-product-profiles`
*product profiles · default roles · built-in profiles · OOTB roles · predefined roles · journey administrator · campaign manager*

**Out-of-the-Box Permissions** — `/en/docs/journey-optimizer/using/access-control/ootb-permissions`
*OOTB permissions · built-in permissions · default permissions · permission list · all permissions*

**High/Low Level Permissions** — `/en/docs/journey-optimizer/using/access-control/high-low-permissions`
*high level permissions · low level permissions · permission levels · view vs manage · read vs write*

**Attribute-Based Access Control** — `/en/docs/journey-optimizer/using/access-control/attribute-based-access`
*attribute-based access control · ABAC · field-level access · data access label · restrict data access · sensitive data*

**Object-Level Access** — `/en/docs/journey-optimizer/using/access-control/object-based-access`
*object level access · OLA · restrict object · share object · object-based access · who can see this journey*

---

### Privacy & Data Governance

**Privacy Get Started** — `/en/docs/journey-optimizer/using/privacy/get-started-privacy`
*privacy AJO · data privacy · GDPR AJO · privacy management · privacy overview · PII*

**Privacy Requests** — `/en/docs/journey-optimizer/using/privacy/requests`
*privacy request · GDPR request · data subject request · delete personal data · access personal data · CCPA request*

**Audit Logs** — `/en/docs/journey-optimizer/using/privacy/audit-logs`
*audit logs · activity log · who did what · audit trail · user activity · change history AJO*

**Data Hygiene** — `/en/docs/journey-optimizer/using/privacy/data-hygiene`
*data hygiene · data lifecycle · delete records · dataset expiry · record delete · data cleanup*

**Data Governance Policies** — `/en/docs/journey-optimizer/using/privacy/action-privacy`
*data governance · usage policies · data labels · marketing actions · restrict channel · consent policy enforcement*

**Customer Managed Keys** — `/en/docs/journey-optimizer/using/privacy/cmk`
*customer managed keys · CMK · bring your own key · BYOK · encryption key management · data encryption*

**Consent Management Landing** — `/en/docs/journey-optimizer/using/privacy/consent/consent-landing-page`
*consent management · consent overview · manage consent · consent framework*

**Opt-Out Management** — `/en/docs/journey-optimizer/using/privacy/consent/opt-out`
*opt-out · opt out management · unsubscribe · suppress contact · honor opt-out · consent opt-out · global opt-out*

**Consent** — `/en/docs/journey-optimizer/using/privacy/consent/consent`
*consent · consent policy · consent service · enforce consent · marketing consent · channel consent*

**Preference Center** — `/en/docs/journey-optimizer/using/privacy/consent/preference-center`
*preference center · communication preferences · manage preferences · subscription preferences · contact preferences page*

---

### Data Management

**Get Started with Data** — `/en/docs/journey-optimizer/using/data-management/gs-data`
*data management · AJO data · data overview · XDM data · platform data*

**Get Started with Schemas** — `/en/docs/journey-optimizer/using/data-management/get-started-schemas`
*schemas AJO · XDM schemas · AJO schema · data schema · schema explorer*

**Datasets** — `/en/docs/journey-optimizer/using/data-management/datasets/datasets-landing-page`
*datasets AJO · AJO dataset · platform dataset · data ingestion dataset · view dataset*

**Lookup AEP Data** — `/en/docs/journey-optimizer/using/data-management/lookup-aep-data`
*lookup data · AEP data lookup · enrich journey with data · dataset lookup in journey · external dataset*

**Get Started with Queries** — `/en/docs/journey-optimizer/using/data-management/get-started-queries`
*query AJO data · query service · SQL AJO · query dataset · analyze data SQL*

---

### Tier 3 Fallback

If the catalog and Tier 2 page-link following both fail, run this WebSearch and fetch the top result:

`site:experienceleague.adobe.com/en/docs/journey-optimizer [question keywords]`
