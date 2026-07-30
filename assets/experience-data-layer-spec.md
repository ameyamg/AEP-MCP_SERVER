# Experience Data-Layer Specification

The contract that makes measurement and personalization trustworthy: what events fire, what data they
carry, how it maps to **XDM**, how it's collected via **Adobe Tags / Web SDK**, and how identity and
consent are handled. Fill collaboratively across analytics, data, and engineering.

> **AEP MCP tips:** run `list_schemas` to find your XDM schemas, `list_identity_namespaces` to find
> namespace codes and IDs, and `list_descriptors` to see which fields are marked as primary identities.
> Pair this spec with the `adobe-experience-cloud` methodology skill for architecture guidance.

---

## 1. Collection approach

| Field | Value |
|---|---|
| Collection method | [ Web SDK (alloy) / Adobe Tags ] |
| Data layer | [ Adobe Client Data Layer / custom ] |
| Properties in scope | [ sites / apps ] |
| Datastream / edge config | [ ] |
| AEP sandbox (dev) | [ ] |
| AEP sandbox (prod) | [ ] |
| Environments | [ dev / stage / prod ] |

---

## 2. Event taxonomy

| Event | Trigger | Page/scope | Key data elements | XDM field group | XDM schema | Notes |
|---|---|---|---|---|---|---|
| pageView | [page load] | [all] | [pageName, section, locale] | [web.webPageDetails] | [ ] | [ ] |
| productView | [PDP load] | [product] | [productId, price, category] | [commerce / custom] | [ ] | [ ] |
| addToCart | [click] | [product/cart] | [productId, qty] | [commerce.productListAdds] | [ ] | [ ] |
| formSubmit | [submit] | [lead] | [formId, consent] | [custom] | [ ] | [ ] |
| [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |

---

## 3. Data elements

| Data element | Source (DOM / data layer / var) | Type | Example | Required |
|---|---|---|---|---|
| pageName | [data layer] | string | [home] | Yes |
| productId | [data layer] | string | [SKU123] | Conditional |
| userAuthState | [data layer] | enum | [auth / anon] | Yes |
| [ ] | [ ] | [ ] | [ ] | [ ] |

---

## 4. Identity

> Use `list_identity_namespaces` to find namespace codes and integer IDs. Use `list_descriptors` to
> confirm which schema field carries the primary identity descriptor.

| Identity | Namespace code | Namespace ID | Source | Primary? | XDM path | Notes |
|---|---|---|---|---|---|---|
| ECID | ECID | (auto) | Web SDK | No | identityMap.ECID | device identity |
| Email (hashed) | Email | [ ] | [auth / form] | [ ] | identityMap.Email | use for stitching |
| CRM ID | [custom] | [ ] | [auth] | [ ] | identityMap.[custom] | [ ] |

---

## 5. Consent

- **Consent mechanism:** [CMP / Adobe Consent Service]
- **Consent signals captured:** [collect, personalize, share/ads]
- **XDM consent field group:** [field group name / schema path]
- **Enforcement points:** [collection, AEP audiences, AJO journeys, activation destinations]
- **Default state (pre-consent):** [ ]

---

## 6. XDM mapping summary

> Use `get_schema` with the schema ID to see full field paths. Use `list_field_groups` to find
> reusable standard or custom field groups.

| Data element | XDM schema | Field group | Field path |
|---|---|---|---|
| pageName | [ ] | web.webPageDetails | web.webPageDetails.name |
| productId | [ ] | [ ] | [ ] |
| userId (CRM) | [ ] | identityMap | identityMap.[namespace][0].id |
| [ ] | [ ] | [ ] | [ ] |

---

## 7. AEP dataset and ingestion plan

> Use `list_datasets` to find existing datasets. Use `list_schemas` + `get_schema` to confirm
> schema compatibility. For batch sources, use `list_connection_specs` to find the right connector.

| Event / source | Dataset name | Schema | Ingestion method | Frequency | Notes |
|---|---|---|---|---|---|
| Web events | [ ] | [ ] | [Web SDK streaming / batch] | [real-time] | [ ] |
| CRM records | [ ] | [ ] | [Flow Service batch] | [daily] | [ ] |
| [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |

---

## 8. Validation checklist

- [ ] Every event maps to an XDM field group; no orphan fields.
- [ ] Single collection path (Web SDK) confirmed; no duplicate legacy beacons.
- [ ] Identity namespaces populated (`list_identity_namespaces`) and stitching validated.
- [ ] Primary identity descriptor set on each schema (`list_descriptors`).
- [ ] Consent captured and enforced at every downstream point.
- [ ] Datasets created and profile-enabled for real-time schemas (`list_datasets`).
- [ ] Instrumentation validated in stage against this spec before launch.
- [ ] Merge policies reviewed for each sandbox (`list_merge_policies`).
