# Growth Manager — Consolidated Intake and Owner Decision Queue

**Prepared:** 2026-10-13 (Israel) | **Source of truth:** GitHub `main` following reviewed merge | **Owner:** Growth Manager
**Document status:** `READY_FOR_GROWTH_MANAGER_REVIEW`, **NOT** a completed native Growth Manager run, **NOT** approval to publish.
**Why now:** Transfer the first output from SEO, Data, Website and the Registry into one action-ready queue **without spending additional agent quota on repeating earlier work**.

## Source pack (all traceable; distinguish author evidence)

1. **Website Agent — 11-page owner submission:** [GROW-SEO-01 text-only source extract](source-extracts/grow-seo-01-owner-report-2026-10-13.md), from user-provided `GROW-SEO-01-homepage-owner-review-he.docx`. The extraction preserves all parsed 11 pages, but RTL table columns may not preserve the original page layout. **Use the clean curated interpretation below and the original DOCX to decide exact presentation details.** Owner-reported agent output; no native trace independently inspected.
2. **SEO Agent findings:** [first SEO-to-Growth handoff](../growth-seo-handoff-2026-10-13.md), GSC paired-query analysis (2026-09-13..2026-10-10, 28 settled days); test `T-022` and findings `F-008`, `F-009` in [findings registry](../../registries/findings.json). These current/prior GSC totals were independently corroborated by a separate read-only API replay on 2026-10-13.
3. **Data Agent evidence:** [acceptance log](../../registries/agent-acceptance-plan.json) and [tests](../../registries/tests.json) (`T-017`–`T-021`). Read-only Wix Catalog/order samples and GA4 property 558438175 were observed for narrow tested scopes, not a full transaction ledger or every funnel event. A specifically approved Slack message was verified in [#sales-data](https://shalomlamalka.slack.com/archives/C0C87EKC71R/p1791870672928089). Provider-level least-privilege/writes denial is not independently proven.
4. **Owner/subordinate task state:** [task board](task-board.json), [scorecard](team-scorecard.json), [operating calendar](operating-calendar.json), [found findings](../../registries/findings.json). GitHub repository `main` is current, but installed Workspace Agents are not automatically updated just because Registry files changed.
5. **Other technical findings:** `F-006` homepage alt/H1/metadata audit and `F-007` copied-looking product URL, possible missing alt/structured data; evidence is from specific dated audits. Treat as **review candidates**, not independent authority to make metadata/URL/schema changes.

## Intake outcomes — one unified queue, not one project per agent

| Priority candidate | Workstream | Existing artifact | Status | Owner/review | Main blocker |
| --- | --- | --- | --- | --- | --- |
| P1 decision | `GROW-SEO-01` Homepage hero, semantic headings, verified discovery links | Complete 11-page owner-review packet, two precise alternatives | `OWNER_REVIEW`; **no publish approval** | Website Agent proposal; SEO risk and Data readiness; Growth Manager coordinates; business owner decides | Exact CTA anchor, product/variant stock, visual Wix Preview, GA4 event coverage |
| P1 research | `GROW-SEO-02` Festival category destination feasibility | GSC query/page evidence and potential misrouted collection link | `BACKLOG / DISCOVERY_ONLY`; no new page | SEO lead, Website support; Growth Manager reviews | Verify exact live URL/canonical, locale, available inventory and cannibalization |
| P2 enabling | `GROW-SEO-03` GA4 + Wix funnel/CTA measurement coverage | Data Agent read-only tests and narrow GA4 samples | `EVIDENCE_PENDING`, `NOT_DISPATCHED` | Data Agent read-only; Growth Manager approves scoped analysis | GA4 event names/dimensions/consent/purchase comparability still unknown |
| P2 backlog | `F-006` / `F-007` accessible headings, alt images and product page metadata | Dated SEO on-page audit | Review candidates only | Website + SEO after business-impact prioritization | Template vs isolated-page diagnosis, duplicate/overlap with `GROW-SEO-01` |
| Ops gate | `OPS-002`, `OPS-003` Agent version parity and GitHub main protection | Registry records | `BLOCKED` | Owner/admin and separate runtime config checks | Website v1.1 draft vs GitHub v1.0, main protection not independently enforced |

### Suggested Top 3 Owner Decisions for Growth Manager to evaluate — not yet issued by installed agent

#### Decision 1 — GROW-SEO-01: approve *draft direction* only

**FACT from owner-submitted site review (2026-10-13):** Hero headline is an `H2`, with an `H1` later on the page; duplicated `H3` observed in text; the `קולקציית 2026` link appeared to point to `/copy-of-חצאיות-10` but its target content was **not verified**. Page layout on actual mobile/Desktop Wix Preview remains **UNKNOWN**.

**Verified SEO evidence:** Exact query `בגדים למסיבות טבע` → homepage, 23 clicks, 222 impressions, CTR 10.36%, mean position 5.42 in 2026-09-13..10-10. Query `בגדים למסיבות` is DISTINCT (5 clicks, 69 impressions, CTR 7.25%, position 5.99). Do not confuse `בגדי מסיבות` or 10-day separate reports with this 28-day window.

**Copy A — website agent's preferred version (owner's decision pending):**
- H1: **בגדים מהודו למסיבות טבע, פסטיבלים וכל רגע של חופש**
- Support: **טופים, חצאיות, וסטים, חולצות ואקססוריז צבעוניים - ליצירת לוק שמרגיש בדיוק כמוך.**
- Primary CTA: **לבחירת הלוק שלך** → new internal anchor to `בחרו את הלוק לפסטיבל`; anchor destination **UNKNOWN/not implemented**.
- Optional secondary CTA: **לטופים וגופיות** → verified public category page (size availability UNKNOWN).

**Copy B — alternative brand voice:**
- H1: **הלוק שלך למסיבה הבאה מתחיל בהודו**
- Support: **בגדים ואקססוריז צבעוניים לנשים ולגברים, לפסטיבלים, חופשות ורגעים שבא לך להרגיש בהם מלכה.**
- Primary CTA: **גלו את הלוקים** → same proposed unimplemented anchor.
- Optional secondary CTA: **לאקססוריז** → verified category (fresh stock UNKNOWN).

**Discovery tiles proposed by original document:**
- טופים וגופיות → `https://www.shalomlamalka.com/%D7%98%D7%95%D7%A4%D7%99%D7%9D-%D7%95%D7%92%D7%95%D7%A4%D7%99%D7%95%D7%AA` — observed public page; variant sizes need day-of-publication check.
- חצאיות → `https://www.shalomlamalka.com/copy-of-%D7%9E%D7%95%D7%98%D7%99-%D7%91%D7%A0%D7%A0%D7%94` — observed page; product availability mixed; unusual slug **not approval to rename**.
- וסטים → `https://www.shalomlamalka.com/%D7%95%D7%A1%D7%98%D7%99%D7%9D` — observed page; inventory at publication not established.
- אקססוריז → `https://www.shalomlamalka.com/shop-2` — observed accessories page; no claim of in-stock items.
- **חולצות לגברים** → `https://www.shalomlamalka.com/copy-of-%D7%98%D7%91%D7%A2%D7%95%D7%AA-1` — original packet recommends `HIDE` pending enough verified buyable inventory.
- **קולקציית 2026** → `https://www.shalomlamalka.com/copy-of-%D7%97%D7%A6%D7%90%D7%99%D7%95%D7%AA-10` — **DO NOT LINK** until content/title/canonical/inventory verified.

**Owner decision requested:** `APPROVE DRAFT A` / `APPROVE DRAFT B` / `REVISE` / `HOLD`. Separately decide the module tiles, H1 hierarchy and existing free-shipping-above-350-ILS banner only after current policy validation. **Do not equate approving draft with publishing.**

**Execution gates:** SEO checks query/page and cannibalization (existing festival blog), locale/canonical; Data verifies inventory and available GA4 event baselines; owner sees mobile/desktop Wix Preview (360/390/768/1440 pixels) and approves exact future site change; no URL/redirect/SEO metadata/tracking changes in this workstream. Planned post-publish KPI: same exact GSC query+page over 28 comparable settled days with guardrail on overall organic homepage traffic, brand audience and mobile UX; no causal claim.

#### Decision 2 — GROW-SEO-02: research existing category before any new landing page

**FACT:** Exact GSC `בגדים לפסטיבלים` → homepage, 4 clicks/91 impressions, CTR 4.40%, position 8.95 in 28 settled dates, compared with 0 clicks/47 impressions previously. Small sample.
**Next:** Inspect live category/collection URL, H1, indexing/canonical, redirects, Hebrew/English routes, article cannibalization and variant-level stock. Return a **GO / NO-GO** comparing existing category reuse, targeted improvements, new landing page, or no change. Do **not** create pages or redirects.

#### Decision 3 — GROW-SEO-03: measurement readiness only

**FACT:** Limited GA4/Wix read-only source probes exist. Reported GA4 window 2026-10-06..12: 11 sessions, 9 active users, 18 views, 78 events and 0 **tracked** transactions. The last figure does NOT prove Wix had zero orders.
**Next:** Data Agent should document verified `view_item`, `add_to_cart`, `begin_checkout`, `purchase`, hero CTA/category click instrumentation, consent coverage, event names, page/link dimensions and comparable Wix order statuses. **No automatic analytics setup or tracking edits.**

## Deduplication and freshness rules

- Merge `F-008` into `GROW-SEO-01` and `F-009` into `GROW-SEO-02`; do **not** launch separate duplicate campaigns.
- `F-006` heading issue belongs to homepage review; `F-007` product-page template is a separate lower-priority candidate, with no immediate independent site change.
- `F-001` is one sample Wix order query and does **not** establish business revenue; `F-002` and `F-005` are earlier GSC snapshots using different windows and should not be conflated with the verified later 28-day report.
- `F-003` recorded owner-confirmed old GA4 zero/traffic status, but later live 11-session sample exists: preserve dated evidence and do not present the older statement as current.
- `F-004` Festival Sales remains `DEFERRED` until a validated booth-sales+cost dataset exists.

## One-run instruction for Growth Manager on next available quota window

Read this source pack plus current Task Board and Scorecard **on branch `main`**. Validate the above cited evidence and select **at most 3** prioritized decisions: `APPROVE_DRAFT` / `REVISE` / `HOLD`. For each give owner, exact scope, evidence, urgency, effort, risk, dependencies, measurement/KPI, date and next required approval. Distinguish tasks already drafted from those still `NOT_DISPATCHED`; do not re-run SEO/GA4/Website audits absent critical freshness issues.

**Native Growth Manager invocation = NOT RUN; specialist dispatch = NOT RUN by writing this pack; Wix changes = 0; agent runtime permission changes = 0; website publication = 0.**
