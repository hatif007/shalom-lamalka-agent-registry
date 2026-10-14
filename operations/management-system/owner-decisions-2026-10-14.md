# Owner Decisions — 2026-10-14

**Approver:** Business owner, explicit message in ChatGPT on 2026-10-14. **Coordinator:** Growth Manager.
**Scope:** Research, planning and draft recommendations ONLY. No site publication or modifications, no analytics/tracking changes, no permissions changes and no direct agent runtime activation.

| Work ID | Owner decision | Allowed next step | Explicit restrictions | Routing |
|---|---|---|---|---|
| GROW-SEO-01 | **HOLD** | Preserve completed 11-page Website packet and exact copy variants. No draft selection or new preview. | Do not implement, publish, schedule Website Agent for this workstream, or treat variant A as approved. | Owner can reopen later. |
| GROW-SEO-03 | **APPROVE READ-ONLY** | Data Agent-style existing weekly ChatGPT report: map available `view_item`, `add_to_cart`, `begin_checkout`, `purchase`, hero/category CTA click events, event names/dimensions, consent and Wix-vs-GA4 coverage. Explicitly classify unavailable data as UNKNOWN; zero GA4 tracked purchases is NOT a Wix order count. | No analytics setup, tracking changes, Wix writes or expanded connector permissions. | Monday 2026-10-19 ~08:00 existing ChatGPT scheduled Data report; human coordinator reviews output. |
| GROW-SEO-02 | **APPROVE READ-ONLY** | SEO Agent-style existing weekly ChatGPT report: investigate true festival category URL, indexing/canonical/redirect, locale, cannibalization and source-supported inventory; compare reuse/fix/new page/no change and return GO/NO-GO research recommendation. | No new pages, URL/redirect/metadata changes, content edits, publication or forced promises. | Monday 2026-10-19 ~10:00 existing ChatGPT scheduled SEO report; human coordinator reviews output. |

## Handoff and quota discipline

- **Growth Manager** is coordinating owner decisions and the [Task Board](task-board.json). Its approved work window is Monday **12:00 Asia/Jerusalem**, but native independent agent execution is **not scheduled**.
- **Do not create duplicate agent runs.** Existing weekly ChatGPT Data and SEO automations remain the default collection windows. These tasks were already scheduled before this decision, and the decision **does not alter their prompts automatically**. If those runs omit the research-specific checks above, mark that portion `EVIDENCE_PENDING` and prepare the smallest follow-up rather than falsely claim it was dispatched.
- `APPROVED_FOR_PLANNING` on the Task Board means only read-only research authorization; it is not approval for site modifications or publication.
- `GROW-SEO-01` has higher-priority previous notes/packets referring to option A, but the **latest owner HOLD supersedes them**. Keep source unchanged as historical proposal, not active instruction.
- Preserve evidence provenance and exact source dates; today no fresh Wix/GSC/GA4 source reads were performed as part of recording these decisions.
- Next review: 2026-10-19, after two scheduled ChatGPT reporting windows, within manual Growth review.
- No native agent-to-agent dispatch was performed by this documentation update; do not mistake Registry commits or Slack routing notes for running an installed agent.
