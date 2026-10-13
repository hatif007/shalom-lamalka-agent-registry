# Shalom La Malka — Content & Conversion Agent | GROW-SEO-01

**Issue:** GROW-SEO-01
**Owner-approved next step:** 2026-10-13 — prepare Content & Conversion Agent's homepage proposal.
**Authorized execution mode:** READ ONLY site review + OFFLINE DRAFT ONLY. No site edits, Wix writes, publishing, Slack sends, GitHub writes by the independent Content & Conversion Agent.
**Business coordinator:** Shalom La Malka — Growth Manager.
**Draft responsible:** Content & Conversion Agent. **Reviewers:** SEO Agent for organic search and brand/website owner for eventual implementation.
**Handoff status:** READY_FOR_AGENT_REVIEW / NOT DISPATCHED_TO_INSTALLED_AGENT / NOT APPROVED_FOR_PUBLICATION.
**Target:** https://www.shalomlamalka.com/ (homepage, Hebrew intended user journey). Preserve verified existing locale routing and brand positioning.

## Why this task

Growth Manager's first real business cycle, as identified by the owner, prioritized a low-risk homepage messaging/navigation proposal ahead of a higher-risk new festival landing page. This is an **approved content research and drafting task**, **not** approval to implement it.

Canonical evidence:
- SEO Agent's 28 **settled** days: 2026-09-13..2026-10-10, compared to 2026-08-16..2026-09-12, Google Search Console property https://www.shalomlamalka.com/, `web`. Exact query `בגדים למסיבות טבע` maps to the homepage: 23 clicks / 222 impressions / 10.36% CTR / average position 5.42 (prior 8/139/5.76%/6.75). Exact query `בגדים למסיבות`: 5/69/7.25%/5.99 (prior 1/41/2.44%/7.12). These exact queries must remain distinct; `בגדי מסיבות` is another distinct query.
- Growth Manager's separate **10-day** window 2026-10-02..2026-10-11 (source settled through 2026-10-11): `בגדים למסיבות טבע` 5 clicks, 70 impressions, 7.14% CTR, position 7.04, homepage. Do not compare this 10-day data directly against the 28-day figures or interpret as an SEO decline.
- Growth Manager owner-supplied live report: homepage already mentions parties/festivals but lacks dedicated cluster navigation; `קולקציית 2026` reportedly leads to `/copy-of-חצאיות-10` with H1 `חצאיות` and mixed assortment. The precise live URL/heading, canonical and locale behavior require agent's own read-only confirmation before being described as current fact.
- Wix Catalog V3 first 100 visible products, per Growth Manager owner-supplied report: 78 aggregate `IN_STOCK` / 22 `OUT_OF_STOCK`, additional pages. This sample is **not** complete apparel inventory or variant/size availability. Before recommending links or featured items, confirm destination and available stock; if no live inventory read permission, state UNKNOWN and do not claim availability.
- Public webpage crawl returned existing broad homepage framing such as `בגדים ואקססוריז מהודו למסיבות טבע, פסטיבלים, חופשות`, navigation for women, men and accessories, and featured products, but the third-party crawl was ~3 months old as of this request; inspect the live page before quoting exact *current* wording. Do not repeat existing copy as if it were a new proposal.
- No reliably attributed conversion uplift or purchase-revenue data, and no completed experiment.

## Exact assignment to Content & Conversion Agent

1. **READ ONLY** inspect the current Hebrew homepage and mobile and desktop presentation where feasible. Record inspection date, current on-page hero/H1, first-screen message, navigation labels/targets, availability of current CTA destinations, product modules, key purchase-friction issues, any SEO/locale/redirect ambiguity. Clearly separate directly observed from reported and unknown.
2. **Draft two strong alternative hero-copy options** in natural, authentic Hebrew preserving the brand's energetic boho/India/festival identity. For each, supply (a) proposed main heading/H1, (b) 1-2 short sentences, (c) primary CTA, (d) optional secondary CTA. Do **not** keyword-stuff, promise unproven garment features or erase brand/non-festival audiences. If current hero already contains relevant SEO language, favor a small specific improvement and justify it.
3. **Design one navigation / discovery module** tentatively titled `בחרו את הלוק לפסטיבל`: tiles or links for women, men and only product categories proven to exist and useful. List each proposed anchor, intended target URL, confirmation status (VERIFIED/UNKNOWN), what happens if mostly out of stock, and whether to hide/change the link until stock is confirmed. Do not direct shoppers to the ambiguous collection page until its content/target is checked.
4. Provide **current versus proposed copy** in a side-by-side before/after table, avoiding claims about current text if unverified. Annotate placement: hero, supporting text, CTA, navigation tile, optional content section.
5. Include **mobile-first UX and accessibility**: H1 semantics (avoid duplicate semantic headings), readable hero, tap-target CTA prominence, image alt guidance only for information-bearing images, RTL navigation, trust/customer policy copy that is factually verified; no design assets needed.
6. **Measure**: GSC query+homepage clicks as primary acquisition KPI over 28 *settled* days before versus 28 after a future separately approved publication; navigation CTA clicks, product-page views and add-to-cart *only when corresponding GA4 events and dimensions are proven available*. Specify unknown instrumentation as UNKNOWN; never request tracking changes without separate approval. Include guardrails for brand queries, homepage organic clicks, mobile usability and other business audiences.
7. **Risk review**: do not alter URLs, canonical, redirects, pricing or product stock. Avoid creating a third competing SEO page. Flag locale behavior if root URL redirects to `/en`; do not assume it is a defect. Do not claim 12–20 apparel variants are available without detailed inventory evidence.
8. Deliver a concise **owner review packet**: executive recommendation (Option A or B), confidence and risk, full copy-ready Hebrew variants, target links (with verification status), one visual section-by-section text wireframe, measurement plan and **explicit changes awaiting owner approval**.

## Scope / security

- Allowed: public page read, source/evidence review, offline draft, and returning proposed HTML copy/structure as text only.
- Not allowed: modify Wix or any website, update product/category metadata, create a new collection/URL, change redirects/SEO settings, edit prices or inventory, publish content, run an experiment, create tracking, contact customers, Slack send, or write GitHub/Registry **from the Content & Conversion Agent**.
- Growth Manager coordinates/assigns proposals conceptually but **direct agent-to-agent invocation is not currently verified**. This file in GitHub does NOT dispatch the task to the installed agent.
- Every reported factual claim must include the exact page or GSC source, date and caveat. Clearly label FACT/HYPOTHESIS/RECOMMENDATION/UNKNOWN.
- Owner's approval of the *drafting step* is not approval of the content wording, link targets or publication.

## Registry references on working branch

**Repository:** `hatif007/shalom-lamalka-agent-registry`
**Exact branch:** `fix/registry-v0.2-structure` (**not main**)
- `operations/growth-seo-handoff-2026-10-13.md`
- `operations/seo-weekly-playbook-v1.md`
- `registries/findings.json` IDs F-008, F-009
- `registries/tests.json` ID T-022
- `skills/content-conversion-agent/SKILL.md`

## Completion definition

A complete, independently reviewed **proposal package only**, with two hero/copy alternatives, actual homepage before/after comparison, verified/unknown navigation destinations, measurable KPIs and guardrails, explicit owner approval checklist, no mutations or Slack sends. If a source cannot be opened, label BLOCKED and draft only facts supported by visible information; do not fabricate a live site state.

**Next decision gate:** owner reviews draft; only after separate explicit owner approval may the team plan a scoped Wix change. Default outcome is DRAFT_READY_FOR_OWNER_REVIEW.
