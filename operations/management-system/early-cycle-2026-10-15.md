# OPS-008 | One-time advance of four-role reporting cycle — 2026-10-15

**Owner instruction received 2026-10-14:** Bring the first full operational run and OPS-007 acceptance from 18–19 October to **tomorrow morning, Thursday 15 October 2026**, just once. All times `Asia/Jerusalem`.

**Run mode:** Four separate **ChatGPT Scheduled Tasks**, not confirmed invocations of independently installed GPT agents. Read-only in Wix, GA4, GSC, website and permissions. GitHub report-only write to four authenticated pre-existing inbox branches is authorized; no data/SEO/website content writes.

## 2026-10-15 one-time schedule (owner-authorized)

| Window | Task | Canonical report branch | Expected full report file |
| --- | --- | --- | --- |
| 06:30 | Website — advance | `report/inbox-website` | `operations/management-system/reports/runs/2026-10-15/website/WEBSITE-REVIEW-2026-10-15.md` |
| 07:15 | Data — advance | `report/inbox-data` | `operations/management-system/reports/runs/2026-10-15/data/GROW-SEO-03-2026-10-15.md` |
| 08:15 | SEO — advance | `report/inbox-seo` | `operations/management-system/reports/runs/2026-10-15/seo/GROW-SEO-02-2026-10-15.md` |
| 09:45 | Growth — advance | `report/inbox-growth` | `operations/management-system/reports/runs/2026-10-15/growth/GROWTH-WEEKLY-2026-10-15.md` |
| 11:30 | OPS-007 acceptance — advance | inspect four role branches | final PASS/PARTIAL/BLOCKED evidence-backed report; PR/CI/readback if tools allow |

Each one-time task: full original source-based Markdown report, `REPORT_ARCHIVE_V1` metadata, at most **one** `GitHub create_file` on its **already existing** role inbox branch, no new branch/Issue/PR/merge in the producing task; task also prints the complete report in its own conversation. Only final, verified PII-free findings to authorized Slack role channel if tool and runtime policy permit. If blocked, `ARCHIVE_BLOCKED` / `NOT_POSTED`. Do **not** invent receipts or rerun research to fix publication.

On 2026-10-14, the coordinating operator independently confirmed **all four role inbox branches existed** through the connected GitHub API. That is a prerequisite, not proof of new reports.

## Avoid duplicate reporting

The four existing enabled recurring ChatGPT tasks were retained, but their next weekly occurrence was shifted to:
- **Website:** Sunday 2026-10-25 at 22:30.
- **Data:** Monday 2026-10-26 at approximately 08:00.
- **SEO:** Monday 2026-10-26 at approximately 10:00.
- **Growth Manager:** Monday 2026-10-26 at 12:00.

Thus **no second regular four-role cycle on 2026-10-18/19**. The normal weekday/time cadence is unchanged after this exceptional advance. The pre-existing first acceptance task for Monday 19 October was **retimed**, not duplicated, to 2026-10-15 at 11:30.

## QA closure gates

For **each role** independently require:
1. A real 2026-10-15 ChatGPT scheduled run receipt.
2. The source-supported **full** original generated report stored in the expected branch file, with `payload_type=FULL_GENERATED_REPORT`; not `SYNTHETIC_TEST`, not `RECOVERED_EXCERPT`; no PII.
3. GitHub PR/CI success and merged readback to `main` when the review environment allows; otherwise `PR_PENDING` with actual file link.
4. Genuine Slack final-only message permalink in the designated channel, or `NOT_POSTED` with actual blocker.
5. Honest distinction from installed ChatGPT custom GPT runtime, which is still not directly invocable through the current connector.
6. ChatGPT full *authored report* is different from raw *conversation transcript*. No unsupported API for transcript extraction can be assumed from Owner permission.

If all documented OPS-007 requirements pass, allow a separately authorized Registry closure PR. Otherwise keep `EVIDENCE_PENDING` or `BLOCKED`, state precisely which requirement failed and evidence. No manufactured `CLOSED`. `GROW-SEO-01=HOLD`, `GROW-SEO-02/03=APPROVE READ-ONLY`, Festival Sales `DEFERRED`.

**As of preparation on 2026-10-14:** `SCHEDULED / NOT YET RUN`. No genuine 2026-10-15 report exists yet. No Slack completion was claimed by this planning record.
