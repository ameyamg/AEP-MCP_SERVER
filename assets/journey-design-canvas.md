# AJO Journey Design Canvas

A one-page design for an **Adobe Journey Optimizer** journey or campaign: who enters, what they
experience across channels, how decisioning and consent gate it, and how success is measured.
Replace bracketed prompts with specifics.

> **AEP MCP tips:** run `list_segments` to find entry audiences, `list_journeys` to see existing
> journeys, `list_offers` + `list_offer_activities` for decisioning objects, and `list_campaigns`
> for campaign-mode journeys. Pair with the `adobe-experience-cloud` methodology skill for
> journey orchestration strategy.

---

## 1. Journey identity

| Field | Value |
|---|---|
| Journey name | [ ] |
| Objective / hypothesis | [ if we … then [metric] improves by [target] ] |
| Type | [ triggered / batch / recurring ] |
| AJO journey ID | [ — populated by `get_journey` after creation ] |
| Owner | [ ] |
| Primary KPI & baseline | [ conversion / engagement; current value ] |
| Target sandbox | [ dev / prod ] |

---

## 2. Audience & entry

> Use `list_segments` to find the RT-CDP audience, `get_segment` for definition details.

| Aspect | Definition |
|---|---|
| Entry audience (RT-CDP segment) | [ segment name / ID ] |
| Entry event / trigger | [ event qualification / segment membership ] |
| Eligibility / consent gate | [ required consent signals — collect, personalize ] |
| Suppression rules | [ frequency caps, exclusion segments ] |
| Expected volume | [ ] |

---

## 3. Journey steps

| Step | Channel | Message / action | Wait / timing | Decision / branch | Consent check |
|---|---|---|---|---|---|
| 1 | [email] | [welcome] | [immediate] | [opened? Y/N] | [marketing] |
| 2 | [push] | [reminder] | [+48h if no open] | [ ] | [push] |
| 3 | [web / in-app] | [personalized offer] | [on next visit] | [decisioning: next-best-offer] | [personalize] |
| 4 | [ ] | [ ] | [ ] | [ ] | [ ] |

---

## 4. Decisioning / personalization

> Use `list_offers` to browse available offers, `list_offer_activities` for decision scopes,
> `list_collections` and `list_placements` for targeting configuration,
> `list_ranking_formulas` for AI/rules-based ranking.

- **Decision logic:** [next-best-experience / offer ranking / rules / AI model]
- **Inputs (profile attributes / computed attributes):** [ — use `list_computed_attributes` ]
- **Offer collection:** [ collection name / ID ]
- **Placement:** [ placement name / ID ]
- **Fallback experience:** [ ]

---

## 5. Exit & guardrails

- **Goal / exit condition:** [conversion event / journey complete]
- **Frequency / fatigue rules:** [ ]
- **Hard stops:** [unsubscribe, consent withdrawal, complaint]
- **Profile merge policy used:** [ — use `list_merge_policies` to find ID ]

---

## 6. Measurement

| Metric | Definition | Target | Source |
|---|---|---|---|
| Entry → conversion rate | [ ] | [ ] | [CJA / AJO reporting] |
| Channel engagement (open/click) | [ ] | [ ] | [AJO / CJA] |
| Personalization lift | [vs. control / holdout] | [ ] | [Target / CJA] |
| Unsubscribe / complaint rate | [ ] | [low] | [ ] |

> Use `cja_run_report` to pull CJA journey metrics. Use `get_metrics` for AEP observability
> signals (profile ingestion rate, activation success).

---

## 7. Launch checklist

- [ ] Audience segment validated and profile-enabled (`get_segment`, `get_dataset`).
- [ ] Consent gates configured and enforced at channel and audience level.
- [ ] All messages QA'd — content, links, rendering, personalization tokens.
- [ ] Frequency/suppression and exit rules configured.
- [ ] Offers published and decision activity live (`list_offer_activities`).
- [ ] Measurement instrumented; control/holdout defined where used.
- [ ] Journey activated in AJO (`get_journey` to confirm status).
