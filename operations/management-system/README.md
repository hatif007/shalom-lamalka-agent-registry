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

**Proposed weekly cadence:** Monday Data ~08:00 and SEO ~10:00 are enabled *ChatGPT scheduled reports* from 2026-10-19 (not native installed-agent runs). Growth review Monday 11:00 is PROPOSED and **NOT scheduled**. Daily exception review and monthly strategy review are manual checklist proposals. Track an actual meeting occurrence only with evidence/date/decisions.

**Weekly Growth meeting agenda (manual until activated):**
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
