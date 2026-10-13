# Shalom La Malka — Agent Operating Rhythm v1.0

**Approved by owner:** 2026-10-13  
**Phase:** business operations after infrastructure verification  
**Source of truth:** This is an operations plan, NOT an amendment to tool/OAuth permissions, a published Workspace Agent configuration, or an authorization to publish/edit site content.  
**Default:** READ ONLY; respect the dedicated agent's canonical SKILL.md and the current access matrix.

## Business objective

Generate qualified organic traffic and profitable website purchases using data-backed opportunities, prioritized actions, and measured follow-through — not activity metrics or reports for their own sake.

## Roles and current activation gates

| Role | Purpose and default deliverable | Operating status as of 2026-10-13 |
| --- | --- | --- |
| Growth Manager | Collect validated findings, rank impact/confidence/effort/risk, propose 3 priority business actions and owners | Coordination only; independent agent runtime not fully accepted. No autonomous delegation or external writes yet. |
| Data Agent v2 | Read-only Wix/GA4 source quality, traffic and purchase-funnel overview, order/product sampling, and three evidence-backed recommendations | OPERATIONAL PASS FOR VERIFIED READ-ONLY WORKFLOWS. One pre-authorized Slack report per task only under its canonical exception. |
| SEO Agent | GSC queries/pages/clusters, search opportunity research and technical SEO audit; 3 prioritized opportunities | LIVE GSC source reads verified 2026-10-13. Weekly **ChatGPT** SEO report scheduled from 2026-10-19; separate installed SEO Agent acceptance and native scheduling still pending. |
| Content & Conversion Agent | Read-only product/customer journey review and draft copy/experiment hypotheses | Draft/recommendations only; no autonomous publishing or experiment activation. |
| Festival Sales Agent | Event-level booth sales/product mix/margin | DEFERRED until reliable event sales+cost records; never infer booth performance from Wix online orders. |

## Operating cadence

| Cadence | Process | Responsible | Output and escalation |
| --- | --- | --- | --- |
| Daily (later activation) | Monitor meaningful anomalies, source access and data lag, not normal volatility from low traffic | Data + SEO once verified | Escalate only material issues; no automatic external messaging before approval. |
| **Weekly — first live routine** | GA4 last 7 **complete local dates** vs previous 7; read-only Wix Catalog V3/orders query with exact sample/filter/pagination disclosure | ChatGPT scheduled read-only Data Agent-style workflow | Concise Hebrew report: max 3 facts, max 3 prioritized recommendations, owners, target metric, exact source/time/range/coverage. |
| Weekly — SEO (now active in ChatGPT) | Latest 28 settled GSC dates vs prior 28; validated query+landing-page opportunities | ChatGPT scheduled GSC read-only report; independent SEO Agent activation remains separate | Max 3 prioritized opportunities with confidence, impact, next steps and KPIs; no Wix edits or published copy. |
| Weekly review | Merge validated Data/SEO outputs; choose actions with owner approval where required | Growth Manager or owner pending runtime acceptance | Small decision register: issue, evidence, action, owner, due date, measurable outcome. |
| Monthly (activation after first weekly cycle) | Compare trends, assess completed experiments, retire weak ideas, prioritize next month | Growth Manager | 3 strategic priorities, evidence and resources needed. |

## Activated schedule: Data Agent-style weekly report

- **Scheduler:** ChatGPT task automation in the current conversation/workspace; **NOT** direct execution of the installed `shalom-lamalka-data-analysis-v2` agent instance. No evidence is implied of native scheduled agent execution.
- **First recurrence:** Monday **2026-10-19 morning, approximately 08:00 Asia/Jerusalem** (flexible timing; exact delivery may vary).
- **Recurrence:** weekly Mondays. A separate ChatGPT-based weekly SEO report was activated on 2026-10-13 as recorded in the next section; neither schedule invokes an installed custom agent.
- **Wix:** site `03b550bb-4ab1-4854-99b8-8bb153c4431e`, Catalog V3 product read and eCommerce orders search only. Orders status filters and unavailable `INITIALIZED` must be explained. No raw customer records or customer PII in report.
- **GA4:** property `558438175` (Asia/Jerusalem / ILS). Week comparison uses complete dates; do not mistake GA4 tracked 0 purchases for a comprehensive Wix order ledger.
- **Result format:** FACT/HYPOTHESIS/UNKNOWN, source/time/range, caveats, max three recommendations ranked impact/confidence/effort, how to measure, no marketing promises unsupported by evidence.
- **Permission boundary:** no Wix/GA4 business mutations, product/content/checkout changes, GitHub/Registry writes, automatic Slack sends, customer contact, publishing, or permission edits; missing connector becomes BLOCKED (do not guess).
- **Delivery:** scheduled ChatGPT report only. Any Slack delivery by the installed Data Agent must receive separate task-specific authorization to `#sales-data` or `#agent-team`; this operations plan is not blanket Slack authorization.

## Activated schedule: SEO weekly opportunity report

- **Scheduler:** ChatGPT task automation in the current workspace, not native invocation of an installed SEO Agent.
- **First recurrence:** Monday **2026-10-19 morning, approximately 10:00 Asia/Jerusalem**, flexible within the scheduling window; weekly Mondays thereafter.
- **Source:** GSC Wizard read-only property `https://www.shalomlamalka.com/`. Verified live 2026-10-13: 273 clicks, 3,384 impressions, CTR 8.07%, mean position 7.04 in settled 2026-09-13 through 2026-10-10; reporting metadata settledThrough=2026-10-10.
- **Deliverable:** 28 settled days versus prior 28, up to three evidence-backed commercially relevant search opportunities, query+page pairs, recommendations and measurable KPIs, clearly marked hypotheses.
- **Initial candidate landing-page pairings:** Homepage for `בגדים למסיבות טבע`, `בגדים לפסטיבלים`, and `בגדי מסיבות` (verified in GSC query+page read).
- **Full playbook:** `operations/seo-weekly-playbook-v1.md`.
- **Controls:** No Wix/content/SEO metadata mutations, no sitemap submissions, no GitHub write by the scheduled SEO task, no Slack sends and no autonomous cross-agent dispatch. If GSC source is inaccessible on a scheduled run, report BLOCKED; do not fabricate results.
- **Runtime gate:** The separately installed SEO Agent remains PENDING for native instance verification; this automation does not assert its activation.

## First weekly cycle — action checklist

1. **Monday Oct 19** — receive read-only week-to-week Data report, with error handling for connector unavailability.
2. Review metric coverage and distinguish no data from no activity; avoid claims of statistically significant shifts on 11-session-scale baseline.
3. Receive scheduled ChatGPT SEO report after the Data report; independently verify the installed SEO Agent's own tool access before enabling native autonomous operation or Slack sending.
4. Growth Manager/owner select **up to 3 specific actions** with owner, due date and success metric; do not execute protected actions without task-specific approval.
5. At next cycle, check whether a previous action measurably changed results; never attribute causality from coincident shifts alone.

## Security and evidence

- Data Agent Skill v2.0: `skills/data-agent/SKILL.md`.
- Agent status and source limitations: `registries/agent-acceptance-plan.json`, `registries/access-matrix.json`.
- Reference allow/deny guard: `security/data_agent_action_guard.py` is CI-tested, but **not a live installed-agent mediator**.
- This document is authored by an explicitly authorized GitHub maintenance/orchestration process, NOT by the read-only Data Agent runtime.
- No `main` merge, Wix or GA4 write, OAuth change or Slack message is authorized by creating this record.
