# Owner Decision Inbox — Shalom La Malka

**Last consolidated:** 2026-10-14 | **Coordinator:** Growth Manager | **Canonical location:** GitHub `main`
**Slack channel chosen by owner:** [#business-insights](https://shalomlamalka.slack.com/archives/C0C8PNALALR) (`C0C8PNALALR`) — **PRESERVE / DO NOT ARCHIVE**.
**Use:** Public-facing task metadata only; do not include customer PII, private channel contents, raw order records or unpublished confidential financial details.

## Owner action required — no new business approval implied

| Task | What is actually pending | Who must act | Next review | Source / boundary |
| --- | --- | --- | --- | --- |
| `OPS-002` | Website Agent v1.1 was reported saved as **draft**; confirm actual installed configuration and decide the safe update/publish step before changing runtime. | Owner, with Growth Manager coordination | 2026-10-19 | [Task Board](task-board.json), [Acceptance](../../registries/agent-acceptance-plan.json). **No implicit permission to publish or re-enable removed Wix/GitHub/Slack connectors.** |
| `OPS-003` | Protect GitHub `main` using branch ruleset / required PR checks; tool connection does not expose admin change. | GitHub repo admin / owner | 2026-10-19 | [Task Board](task-board.json). Previously broad Git maintenance permission granted; this is still a manual technical step, not a new business decision request. |
| `OPS-004` | Optional workspace-admin **archive action** for redundant `#content-conversion`, `#new-channel`; `#social` only if not wanted. Connected Slack tools do not support archive/delete. | Slack workspace admin / owner | 2026-10-19 | [Slack audit](slack-channel-cleanup-audit-2026-10-13.md). **`#business-insights` was formerly a candidate for archive; owner's new instruction on 2026-10-14 supersedes this. Keep it.** No channels archived yet. |

## Already decided — DO NOT re-request

| Task | Decision and status | Next event |
| --- | --- | --- |
| `GROW-SEO-01` | **HOLD** (owner, 2026-10-14). Homepage copy alternatives/source packet preserved, but no preview, workstream dispatch, edits or publication. | Only reopen after explicit new owner instruction; no reminder framed as pending approval. |
| `GROW-SEO-03` | **APPROVED READ-ONLY** (owner, 2026-10-14). GA4/Wix measurement-coverage research allowed, no tracking/config changes. | Existing Monday 2026-10-19 ~08:00 ChatGPT Data report; if gaps remain, mark evidence pending. |
| `GROW-SEO-02` | **APPROVED READ-ONLY** (owner, 2026-10-14). Festival-page feasibility research allowed, no content/URL changes. | Existing Monday 2026-10-19 ~10:00 ChatGPT SEO report; if gaps remain, mark evidence pending. |

## Future decisions — NOT requesting approval before evidence exists

- **SEO/Wix implementation:** After evidence-backed `GROW-SEO-02` GO/NO-GO and owner-ready exact page/URL change plan, separately request approval for that precise change. **No site changes now.**
- **Measurement/tracking:** After `GROW-SEO-03` event audit, only if a specific change is needed prepare a separately scoped tracking approval. **No analytics write now.**
- **Business numeric targets:** [Team Scorecard](team-scorecard.json) goals remain **unapproved**; establish comparable source baseline before asking owner for concrete conversion/revenue targets. These are **not** current urgent decisions.
- **Festival Sales Agent:** `F-004` is **DEFERRED_PENDING_DATA**. If the owner wants to activate the Festival workstream, ask for validated booth sales/cost records; never infer festival margin from Wix online orders.
- **Lower-priority technical findings:** `F-007` is a backlog review candidate, not an urgent owner approval; `F-006` is within paused homepage `GROW-SEO-01`.

## Standing publication rule — owner instruction 2026-10-14

- **Purpose:** Prevent lost owner decisions. The **GitHub Task Board + explicit owner decision files are the durable source of truth**; the **single consolidated Slack message in `#business-insights` is the owner-facing index**. Do not flood other channels with duplicate approval requests.
- On every **actual** Growth Manager decision review or when an owner decision changes, the authorized operator should **update the GitHub queue, then post ONE compact consolidated decision summary** to `#business-insights` with timestamp, task IDs, exact requested decision, status, assignee, due/review date, source links and permission gate.
- Keep 3 distinct sections in each digest: **OWNER ACTION NEEDED**, **ALREADY DECIDED / HOLD**, **WAITING ON EVIDENCE**. Do not mark research approvals as approval to implement or make paused work look urgent.
- One agent finding that has **no owner decision gate** remains in the evidence registry, not in the owner's urgent queue. Collapse duplicates.
- **No autonomous recurring Slack poster was created by this document.** Installed read-only agent runtime Slack sending must be separately authorized by its actual Skill/connection. A completed manual Slack send must include its permalink/evidence, not merely a planned path.
- The previous Slack cleanup audit's suggestion to archive `#business-insights` is **OBSOLETE as of this instruction**. The owner has explicitly chosen that channel for the decision queue.

## Traceability

- [Owner's October 14 decisions](owner-decisions-2026-10-14.md)
- [Task Board](task-board.json)
- [Growth Manager consolidated evidence](growth-manager-consolidated-intake-2026-10-13.md)
- [Operating Calendar](operating-calendar.json)
- [Channel cleanup audit](slack-channel-cleanup-audit-2026-10-13.md)

## Verified one-time Slack delivery — 2026-10-14

The owner-authorized first consolidated summary was [sent successfully to #business-insights](https://shalomlamalka.slack.com/archives/C0C8PNALALR/p1791963255855629) after the authenticated user joined that public channel. This is a **verified single message**, not evidence of installed Growth Manager autonomous Slack posting, a recurring notifier or completion of the listed owner actions. Further updates require an actual review and authorized send path.
