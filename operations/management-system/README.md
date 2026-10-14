# Growth Manager — Unified Operating Calendar + Team Scorecard v1.0

**Created:** 2026-10-13 | **Orchestration owner:** Growth Manager | **Business approver:** Owner
**Canonical branch:** `main` | **Status:** `REGISTRY_READY_MANUAL_OPERATIONS`; actual recurring meetings and native agent orchestration NOT activated.

## Central management files

- [Calendar](operating-calendar.json) — daily / weekly / monthly routines, activation source, accountable coordinator, scheduled vs merely proposed status.
- [Team Scorecard](team-scorecard.json) — each agent's deliverables, measurable baseline, proposed target, owner-approval flag, review period and data evidence.
- [Task Board](task-board.json) — task status, priorities, evidence, blockers, owner approvals, handoffs and next review.
- Prior operational source: [Operating Rhythm](../operating-rhythm-v1.md).

## Decision rights & weekly meeting

Growth Manager is the **single conductor**, consolidating Data, SEO, Website and (when source is available) Festival Sales. The human owner authorizes public/business changes, new bot permissions, agent activation and business target commitments. No Skill or Registry file alone delegates tasks, writes Slack or operates Wix.

**Owner-approved weekly work windows (2026-10-13; Asia/Jerusalem):** Sunday **22:30 Website & Conversion** (manual window, first 2026-10-18); Monday **~08:00 Data** (existing flexible ChatGPT automation); Monday **~10:00 SEO** (existing flexible ChatGPT automation); Monday **12:00 Growth Manager** (manual review window, first 2026-10-19). The two ChatGPT weekly report schedules stay enabled, *not* installed-agent runtimes. **Approving a work window does not schedule or start a native custom agent.** The Sunday Website Agent and Monday Growth Manager slots are approved in the Registry but **not automated**. Daily checks are incident-triggered only; on the **first Monday of each month**, the 12:00 Growth review includes monthly strategic review without new specialist runs. Track an actual meeting or agent execution only with evidence/date/decisions.

**Weekly Growth meeting agenda — Monday 12:00 (owner-approved window; manual until activated):**
1. Check source coverage and freshness, unresolved blockers and decisions from prior week.
2. Read verified specialist reports, not unsourced narrative.
3. Review scorecard: baseline versus actual with same metric, scope, and time window.
4. Select up to 3 actions, each with owner, next review date, measurement and explicit owner approval where needed.
5. Publish only approved handoffs; missing dispatch must say `NOT_DISPATCHED`.

## Slack map

- Central coordination: #agent-team (C0C86D1C3D5).
- Registry/test evidence: #agent-registry (C0C8E1RMD8S).
- Verified outcome summaries: #growth-outcomes (C0C8GDL7H0S).
- Existing Data channel: #sales-data (C0C87EKC71R); task-specific message authorization only.
- **New Website Agent channel:** [#website-conversion-agent](https://shalomlamalka.slack.com/archives/C0C91GU8M3N) (C0C91GU8M3N), created 2026-10-13. Initial owner-approved channel introduction [posted](https://shalomlamalka.slack.com/archives/C0C91GU8M3N/p1791913059618809).
- Legacy #content-conversion (C0C88CJ26BX) remains in place. **Do not delete or silently rename without owner direction.**

New channel creation or introductory message does NOT authorize the installed Website Agent to send Slack or modify its read-only Skill. A human may post; agent runtime requires separately granted action permissions.

## Task workflow & scope

`BACKLOG -> EVIDENCE_PENDING -> DRAFT_READY -> OWNER_REVIEW -> APPROVED_FOR_PLANNING -> RESULT_REVIEW -> CLOSED` with `BLOCKED` / `REJECTED` alternatives. These are coordination states, not authority grants. `APPROVED_FOR_PLANNING` is NOT `APPROVED_TO_PUBLISH`; actual implementation authorization must identify exact action and system separately.

## KPI design

Business outcome targets stay **UNSET** until comparable Wix/GA4/GSC baselines, product availability and owner-approved numerical ambition exist. Process/output targets (e.g. 1 website approval packet/week, 3 weekly decisions maximum, 1 verified weekly Data report) are **PROPOSED ONLY** and are not retrospectively marked achieved by a scheduled job.

Initial SEO baseline: GSC `web` 28 settled days 2026-09-13..2026-10-10: 273 clicks, 3,384 impressions, CTR 8.0674%. Coverage is historical. Website packet `GROW-SEO-01` exists owner-submitted; not published.

Festival Sales Agent is deferred until validated booth sales/cost records exist.

## Registry update method

At each meeting, Growth Manager prepares a **proposed patch** to the calendar/scorecard/task board with source, recorded actuals, proof, timestamp and owner decision. A separately authorized GitHub maintainer opens a topic-branch PR and runs CI; installed read-only agents do not write Registry. Do NOT invent meeting completion, live source access, approval, numbers or autonomous handoff.

**Security:** All site changes, Slack agent messaging, provider-scope changes, agent activation and business writes remain separately controlled. **GitHub main branch protection is still not observed enforced** and requires admin action.

## OpenAI quota-aware working policy — owner approved 2026-10-13

- Reserve **one Website deep-audit work window per week** on Sunday 22:30; do not keep this agent active continuously or launch daily duplicate crawls. Website Agent v1.1 was owner-reported as an unpublished draft; no new scheduler, connector or runtime invocation was authorized by changing this Registry calendar.
- Keep the **two existing ChatGPT weekly report automations** on Monday ~08:00 (Data) and ~10:00 (SEO). These are not direct scheduled executions of installed custom agents.
- Monday **12:00 Growth Manager** consumes the assembled Data/SEO/Website evidence and makes up to three accountable prioritization decisions. **Do not rerun** SEO/Data analyses in Growth just to repeat work.
- Daily operating rhythm is exception-driven/manual. First-Monday monthly review reuses the standard Growth review; no extra agent-wide batch.
- If OpenAI usage quota, connector access or source data is unavailable, mark `BLOCKED` or `DEFERRED` with exact reason; do not retry endlessly or misrepresent a scheduled slot as a completed task.
- Night scheduling helps sequence work **but does not create extra quota**. No promises of resource savings or native autonomous delivery until measured.

## Existing agent work consolidated — 2026-10-13

The first integrated handoff for Growth Manager is [**Growth Manager Consolidated Intake and Owner Decision Queue**](growth-manager-consolidated-intake-2026-10-13.md). Its raw input includes the owner's complete **11-page GROW-SEO-01 DOCX text extract** (not an exact rendering of RTL tables): [original source text](source-extracts/grow-seo-01-owner-report-2026-10-13.md), specialist GSC evidence, Data Agent scoped reports, registry findings and existing Task Board. Prioritization is **suggested**, not yet executed by the installed Growth Manager; no site publication or autonomous agent dispatch occurred.

**Slack hygiene:** The authenticated user's [Slack channel audit](slack-channel-cleanup-audit-2026-10-13.md) originally identified three archive candidates (`#content-conversion`, `#new-channel`, `#business-insights`) and optional `#social`; **as of 2026-10-14, the owner expressly designated `#business-insights` the canonical owner-decision inbox, so it MUST NOT be archived**. The user granted full channel cleanup authorization, but the Slack connector exposes **no channel archive/delete action**, so **0 channels were archived/deleted**. Human Slack admin UI action remains required. Keep all active, private approval and default channels.

## Owner decision override — 2026-10-14

The [latest owner decision record](owner-decisions-2026-10-14.md) **supersedes previous draft recommendations**: `GROW-SEO-01=HOLD`, `GROW-SEO-03=APPROVE READ-ONLY`, `GROW-SEO-02=APPROVE READ-ONLY`. No homepage Preview, publication or implementation is authorized. Route research requests via the existing weekly Data (~08:00) and SEO (~10:00) ChatGPT reports if their existing prompts cover the checks; **no prompt updates, new automations or separate installed-agent dispatch were performed**. Growth Manager reviews results on the manual Monday 12:00 window. Source extract and earlier recommended hero A are archival suggestions only, NOT owner approval.

## Owner decision findings inbox — approved 2026-10-14

The owner requested that **all items awaiting their decision be consolidated into [#business-insights](https://shalomlamalka.slack.com/archives/C0C8PNALALR)**. The durable [Owner Decision Inbox](owner-decision-inbox-2026-10-14.md) classifies actual owner action needs versus already approved read-only work and owner-HOLD items. The Slack channel is now **PRESERVED, NOT an archive candidate**. Growth Manager owns deduplication and routing. In each actual authorized review, update the GitHub record and post **one consolidated Slack digest** with task IDs, status, exact action/approval needed, review date and evidence. **This is a workflow rule, not a new background automation nor universal agent Slack authorization.** Do not post customer data, private approvals content or repeated items already decided.

## Owner-authorized direct inter-agent coordination — 2026-10-14

Owner approval [A-004](../../registries/approvals.json) authorizes the coordinator to use a supported **direct invocation/chat interface for the installed agents**, initiate already-approved read-only research, review intermediate evidence, challenge weak results and request corrections, and return only verified conclusions to the right channel. **This is permission, not technical activation:** no compatible ChatGPT native installed-agent invoke/chat tool is exposed in the current connection. [OPS-005](task-board.json) tracks the integration acceptance blocker; an ordinary Slack ping is not proof an agent started. No new background schedule, agent installation or connector scope mutation has been performed.

Acceptance before declaring live: verify the exact installed agent/session, read-only source and permissions, actual execution trace, iterative feedback/correction evidence, final output link, and measured usage/quota. Keep Data interim QA out of `#sales-data` until validated final results. Continue using `#business-insights` for owner-only decisions, not routine QA. No changes to Wix, GA4, tracking, permissions or publication without separate specific approval.

## Durable report archive & task delivery — 2026-10-14

The owner authorized original-report retrieval and durable storage in A-005 / OPS-007. A [central report archive](reports/README.md) is now implemented in GitHub `main`, with [a fail-closed provenance validator](../../scripts/validate_report_archive.py) executed by Registry CI. A **coordinator-created SYNTHETIC fixture** confirms the repository can store and read the file type; it is not a scheduled agent report.

The **three existing Monday ChatGPT scheduled tasks** (Data ~08:00, SEO ~10:00, Growth 12:00) have updated prompts that ask for full authored report persistence to `reports/runs/YYYY-MM-DD/{data,seo,growth}/` using report-only GitHub PRs, with full text also returned in the task conversation when archival is blocked. Their schedules and task ownership remain unchanged, and they do not directly invoke installed custom GPTs.

The **first one-time scheduled write test** ran 2026-10-14 and did create an authenticated GitHub branch `report/archive-writer-scheduled-smoke-2026-10-14`, but **no report file nor PR** was observed following completion. Therefore scheduled-task archival is **NOT VERIFIED** and should not be called operational. An alternate single-step issue-inbox test was requested to isolate GitHub action availability. Do not misrepresent a branch-only action as successful end-to-end delivery. A synthetic file, extracted excerpt, or chat summary is not a byte-perfect task transcript.

A native ChatGPT scheduled-task transcript download/list action is not exposed by the connected toolset. Even with owner's full authorization, permissions cannot create unsupported capabilities. To restore historical full reports, use an actually supported authenticated task-conversation export or source conversation access, with an explicit `RECOVERED_EXCERPT` distinction when only part of the original is available. **No repeated expensive Data/SEO source reads for archival repair.**
