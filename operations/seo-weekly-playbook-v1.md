# Shalom La Malka — SEO Weekly Playbook v1.0

**Owner authorization:** 2026-10-13 — activation of the next weekly operating stage.
**Run mode:** Scheduled ChatGPT reporting with a live GSC Wizard read connector where available. **Not** activation/proof of the separately installed SEO Agent runtime.
**Google Search Console property:** `https://www.shalomlamalka.com/`
**Status:** GSC read connector validated LIVE on 2026-10-13; native SEO Agent acceptance remains PENDING.
**Cadence:** Weekly, Monday morning around 10:00 Asia/Jerusalem (flexible). First due: 2026-10-19.
**Audience:** Owner and Growth Manager (when agent orchestration is authorized). No automatic Slack delivery.

## Business objective

Identify and prioritize commercially relevant organic-search opportunities, improve qualified acquisition and eventual sales, and avoid meaningless activity counts. Report a maximum of **three** actionable opportunities weekly.

## Data integrity

1. Read-only GSC performance from the verified property, searchType=`web`.
2. Use the latest **28 settled GSC dates** vs the preceding 28 dates; include both exact windows. Ask GSC metadata for `settledThrough` on each run, since the daily data lag varies.
3. Record exact property, data source (API vs warehouse), timezone/date basis, extraction date, search type, query/page dimensions, row limits, pagination, anonymization and data limitations.
4. Gather total clicks, impressions, CTR and impression-weighted mean position, plus top queries/pages and changes.
5. For each candidate, corroborate the **query+page** pairing using an actual GSC dimension-pair query before suggesting on-page work. Do not assume the homepage is the proper intended target without inspecting page intent.
6. Separate branded and irrelevant ambiguous queries from commercial demand. Examine high-impression, low-CTR or mid-ranking non-brand terms, but never treat low CTR as automatic evidence of a broken snippet.
7. Rankings, scores and potentialClicks are heuristic hypotheses, **not** traffic/revenue forecasts; quantify the evidence and small-sample uncertainty.
8. Do not confuse SEO acquisition with GA4 tracked transactions, Wix sales, or conversion causality; seek Data Agent analysis as a separate evidence source.

## Weekly output format

- **Performance pulse:** last settled 28 days vs prior 28, exact dates and 4 core metrics; flag materially meaningful changes, avoid fragile conclusions from small samples.
- **Top three opportunities:** query, matching landing page, clicks/impressions/CTR/position, factual observation, ranked priority, hypothesis, proposed action, expected mechanism, confidence, effort/risk, KPI and measurement window.
- **Escalation:** clearly state if a recommendation needs owner approval, technical/admin access, or specialist handoff to Content & Conversion.
- **Tracking:** recommend keeping a decision register (owner, action, due date, baseline metric, review date) maintained by a separately authorized Registry operator; this read-only task must not write GitHub.
- **Missing data:** `BLOCKED` / `UNKNOWN` / `NOT_RUN`, never zero unless measured zero.

## Initial verified source baseline (2026-10-13)

GSC Wizard source: live GSC API (`dataSource=api`), `searchType=web`, latest settled date `2026-10-10`; 28-day range **2026-09-13 through 2026-10-10**. Metadata uses America/Los_Angeles date basis for settlement; do not silently reinterpret it as Israel local-day close.

- Clicks: **273**
- Impressions: **3,384**
- CTR: **8.0674%**
- Impression-weighted mean position: **7.0446**

Three candidates independently joined to homepage `https://www.shalomlamalka.com/` using paired GSC `query,page` reads, each with exactly one reported pairing in the queried range:

| Query | Clicks | Impressions | CTR | Position | Proven GSC landing page |
| --- | ---: | ---: | ---: | ---: | --- |
| בגדים למסיבות טבע | 23 | 222 | 10.36% | 5.42 | Homepage |
| בגדים לפסטיבלים | 4 | 91 | 4.40% | 8.95 | Homepage |
| בגדי מסיבות | 1 | 49 | 2.04% | 9.06 | Homepage |

Interpretation: high-priority **candidates for review**, not authorization to change homepage or a promise of upside. The visible Wix page and commercial intent should be reviewed before prescribing a title/content/category alteration. Different similarly worded queries (e.g. `בגדים למסיבות`) must not be conflated with `בגדי מסיבות`.

## Security & delivery

- **STRICT READ ONLY.** Do not publish/edit metadata, content, products, robots/sitemap, redirects, tracking or permissions. No customer contact, Slack send or GitHub/Registry writes from this routine.
- GSC Wizard includes administrative/write methods; only verified read methods are authorized here, and tool availability is not permission to use mutations.
- If the scheduled ChatGPT run cannot access GSC, mark data source `BLOCKED`; do not reuse this baseline as fresh data.
- Do not assert that an independently installed SEO Agent was invoked, validated, scheduled, or authorized to report to Slack from this schedule. Its builder/runtime activation gate is separate.
- Growth Manager may review completed reports and propose tasks; cross-agent autonomous delegation is **not** enabled by this operations document.
