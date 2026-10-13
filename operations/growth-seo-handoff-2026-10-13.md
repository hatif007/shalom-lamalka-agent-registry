# Shalom La Malka — First SEO-to-Growth Manager Handoff

**Recorded:** 2026-10-13
**Scope:** First live SEO weekly report and independently corroborated GSC queries. **Decision status:** DRAFT RECOMMENDATIONS ONLY; no site change or experiment approved.
**Coordinator:** Growth Manager (planning/read-only). **Owner approval** required separately before changes to the live Wix site.
**Source:** Google Search Console property `https://www.shalomlamalka.com/`, `searchType=web`, GSC API (live); settled through 2026-10-10; GSC metadata date basis America/Los_Angeles.
**Comparison:** 2026-09-13..2026-10-10 inclusive versus 2026-08-16..2026-09-12 inclusive. Retrieved/replayed 2026-10-13.
**Native agent evidence class:** owner-pasted SEO Agent report matched canonical SEO skill blob `f386cd8f56f4b6286fbae2ae87be131725515fae`; native instance tool trace not independently captured here. Independent orchestration repeated GSC current/prior summary, query+page pairs, and pagination sample.

## Verified acquisition baseline

| Metric | Latest 28 settled dates | Prior 28 | Change |
| --- | ---: | ---: | ---: |
| GSC clicks | 273 | 205 | +68 (+33.2%) |
| Impressions | 3,384 | 2,751 | +633 (+23.0%) |
| CTR | 8.07% | 7.45% | +0.62 percentage points |
| Avg position (impression-weighted) | 7.04 | 7.55 | improved by about 0.50 positions |

- GSC query+page rows: **181 current** and **161 previous**, requested rowLimit=1000, hasMore=false for both. This is complete relative to the rows returned for that query, **not** evidence that anonymized queries are included.
- No GA4 conversion analysis or Wix revenue reconciliation was included in this SEO report. Revenue/margin impact is **UNKNOWN**.
- Rankings and candidate opportunity scores are **heuristics**, not projected traffic or sales. Search Console dates should not be misrepresented as Asia/Jerusalem local dates.

## Backlog for Growth Manager — TWO workstreams, not three projects

### GROW-SEO-01 — Party/nature-party homepage copy + navigation review
- **Priority:** P1. **Status:** PROPOSED_FOR_DRAFT; NOT APPROVED_FOR_PUBLISH.
- **Owner to draft:** Content & Conversion Agent; **analyst:** SEO Agent; **measurement:** Data Agent (aggregate only).
- **FACT:** Exact query `בגדים למסיבות טבע` maps to homepage in GSC. Current 23 clicks / 222 impressions / 10.36% CTR / 5.42 position; previous 8 / 139 / 5.76% / 6.75. Exact query `בגדים למסיבות` ALSO maps to homepage: current 5 / 69 / 7.25% / 5.99; prior 1 / 41 / 2.44% / 7.12.
- **Important distinction:** `בגדי מסיבות` is a separate exact query (1 / 49 / 2.04% / 9.06 current), not interchangeable with `בגדים למסיבות`.
- **HYPOTHESIS:** Clearer homepage commercial framing for nature parties and more discoverable links to relevant real inventory may help query-to-page relevance and qualified navigation. Growth from SEO content is **not proven**.
- **Next draft only:** Inspect current homepage locale and H1 structure, existing product/category inventory and intended audiences; draft **one** proposed hero line, short supporting sentence and navigation/link recommendation. Avoid keyword stuffing or creation of extra competing pages. Include exact before/after wording for owner approval.
- **Measurement:** GSC 28 *settled* dates before vs 28 after any **approved and published** change, tracking each exact query and homepage separately. Where the source coverage allows, Data Agent compares organic landing sessions and purchase funnel as an additional outcome. Record the actual publication date; seasonal demand and page mix are confounders. Do not claim causality on before-after alone.
- **Risk/guardrails:** homepage supports broad/brand intent; don't overwrite brand positioning, create cannibalizing pages, force redirects or change locale without review.
- **Next gate:** Content & Conversion draft + SEO review, then specific owner approval for implementation.

### GROW-SEO-02 — Festival-category landing page feasibility
- **Priority:** P1 for **analysis**, not immediate technical change. **Status:** DISCOVERY_ONLY; NOT APPROVED_FOR_PUBLISH.
- **Owner to investigate:** SEO Agent + Content & Conversion; **owner review:** Growth Manager.
- **FACT:** Exact query `בגדים לפסטיבלים` maps to homepage in GSC. Current 4 clicks / 91 impressions / 4.40% CTR / 8.95 position; prior 0 / 47 / 0% / 9.13. Small sample: no reliable conversion estimate.
- **Reported page finding — needs separate direct confirmation:** The native SEO report describes homepage link 'קולקציית 2026' leading to a `copy-of-...` URL titled 'חצאיות' while presenting multiple product types. Do NOT treat the precise page structure, canonical, redirects, language or product stock as independently verified by this GSC replay.
- **HYPOTHESIS:** Search intent for festival attire may not be well represented by the available catalog architecture. A suitable existing category page *might* help; not necessarily a new page.
- **Next analysis only:** Read the actual URL/canonical, 301/302 behavior, current title/H1, language routing, internal linking, products/inventory and competing URLs. Recommend **reuse/fix existing category vs new dedicated landing page vs no change** with an SEO risk comparison. Draft (do not implement) a proposed URL, page title/H1/content outline and link targets only after corroboration.
- **Measurement:** Track query+page pairs, page impressions/clicks/rank for 28–56 *settled* dates after any owner-approved launch, using the true live URL. Monitor cannibalization and redirects. No estimated revenue without conversion tracking.
- **Risks/guardrails:** changing slugs/URL can break links, canonical and indexing; preserving existing URLs via reviewed redirects is mandatory if a move is approved.
- **Next gate:** feasibility report to owner before any modification.

### GROW-SEO-03 — Data-quality measurement support, not separate SEO content project
- **Priority:** P2 enabling measurement.
- **Owner:** Data Agent read-only.
- **Request:** Verify GA4 organic traffic and purchase-funnel event availability, Wix order sample/status/pagination coverage and alignment of reporting windows. Record where metrics are blocked/unknown.
- **Guardrails:** GA4 recorded zero conversions does not establish Wix zero orders; website orders do not equal festival booth sales. No new tracking or conversion configuration is authorized.

## Decision register / responsible next steps

| Ref | Next deliverable | Responsible agent | When to review | Current status |
| --- | --- | --- | --- | --- |
| GROW-SEO-01 | Homepage copy+navigation proposal (before/after text + risks) | Content & Conversion, SEO support | Next weekly Growth Manager review | READY_FOR_DRAFT |
| GROW-SEO-02 | Festival page feasibility with canonical/redirect/inventory evidence | SEO + Content & Conversion | Next weekly Growth Manager review | DISCOVERY_ONLY |
| GROW-SEO-03 | Organic-conversion measurement coverage note | Data Agent | Next Data weekly report | READ_ONLY_REQUEST_PROPOSED |

No tasks have been dispatched directly to separate agent runtimes by writing this file. Native autonomous delegation/orchestration remains unverified. No Slack message, Wix edit, content publication, analytics configuration change or permission change was performed.

## Growth Manager decision format

Provide no more than 3 items per review. For each: FACT, HYPOTHESIS, RECOMMENDATION, impact (qualitative, no invented revenue), confidence, effort, risk/reversibility, task owner, dependencies, approval gate, success metric and review date. Recommend **two** workstreams above; keep `בגדים למסיבות` as a subtopic of the party cluster rather than opening a third project.

## Source / reference

- Canonical SEO Skill: `skills/seo-agent/SKILL.md`; SEO cadence: `operations/seo-weekly-playbook-v1.md`.
- Current operator-authored acceptance/replay test: Registry `registries/tests.json` T-022; related findings F-008/F-009.
- 2026-10-13 live API validation from the orchestration connection returned the exact overall and per-query values; no site write calls made.
