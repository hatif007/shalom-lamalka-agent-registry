# OPS-007 — Report archive end-to-end acceptance findings (2026-10-14)

**Owner authorization:** A-005 and user's explicit instruction to implement durable report storage.  
**Overall verdict:** `PARTIAL_PASS_STORAGE / BLOCKED_AUTOMATED_DELIVERY`. This is a technical test, not a business analytics report.

## What passed

1. A shared report archive contract exists at [reports/README.md](reports/README.md), with canonical path `reports/runs/YYYY-MM-DD/<role>/<report-id>.md` and a full Markdown body.
2. [A synthetic coordinator-created document](reports/runs/2026-10-14/system/ARCHIVE-SMOKE-COORDINATOR-2026-10-14.md) was written to the repository and can be retrieved from `main`. This demonstrates storage and retrieval by the coordinating ChatGPT conversation, **not a scheduled task writer**.
3. [Validator](../../scripts/validate_report_archive.py) is wired into [GitHub Actions](../../.github/workflows/registry-validation.yml); PR #13 was merged after green CI. Metadata distinguishes `FULL_GENERATED_REPORT`, `RECOVERED_EXCERPT`, `SYNTHETIC_TEST`.
4. The **existing**, separately scheduled Data (Monday ~08:00), SEO (~10:00), and Growth (~12:00) ChatGPT tasks were updated to attempt a **report-only archive write** during generation, to return their whole original authored report in the task conversation if blocked, and to avoid repeat research. Their cadence was not changed. These tasks are **not** direct executions of installed custom GPT agents.

## Scheduled-task-to-GitHub smoke test A — PARTIAL ONLY

- One-time ChatGPT scheduled task ran 2026-10-14, according to task inventory `last_run_time=2026-10-14T08:54:05Z`.
- The GitHub branch `report/archive-writer-scheduled-smoke-2026-10-14` **was created** and observed by GitHub API; its commit matched the then-current `main` head.
- The instructed full synthetic Markdown document `reports/runs/2026-10-14/system/ARCHIVE-SMOKE-SCHEDULED-2026-10-14.md` **was not present** on that branch at subsequent checks. No PR for that branch was found.
- Outcome: GitHub action *branch creation* verified, but **no original report file or PR was delivered**. Root cause is not definitively identified because the scheduled task's complete output/error text is not exposed to the available task-management tool. Do not infer permission refusal when it could be another tool or execution issue.

## Scheduled-task-to-GitHub smoke test B — NOT VERIFIED

- A second one-time low-cost scheduled task ran 2026-10-14; task inventory showed `last_run_time=2026-10-14T08:57:56Z`.
- It was asked to create **one synthetic GitHub issue** containing the test body, as a simpler one-step durable handoff.
- Multiple GitHub API checks following the run showed **no non-PR GitHub issues** in the registry at the time of verification.
- Outcome: a task run timestamp was observed, **but no issue creation was observed**. No confirmed success and no verified specific policy error.

## What is still missing

- The current task-management API can read schedules and run timestamps, but cannot return the **complete original authored task report or underlying task conversation transcript** through an available connector action.
- A complete generated report in the archive is not equivalent to a verbatim ChatGPT conversation transcript or underlying private tool logs.
- Installed Workspace Agent direct invocation and scheduled-task GitHub full-report delivery are not proven by branch creation, test fixtures, task metadata, or owner authorization.
- No Data/SEO/Growth full report has been verified as automatically committed to this new archive.
- Failed Slack sends from previous scheduled runs remain failed; they must not be represented as final reports published.

## Safe recovery and acceptance path

- First continue to use the full-body-in-task-conversation fallback; never re-run costly business-source research solely to fix storage.
- For production-ready automated archival, use a **supported authenticated execution context with durable connected-app write actions**, such as eligible ChatGPT Work task/browser workflows with GitHub, or a verified native scheduled-task-output export API/connector when supported. Such setup may require the user to open **Work mode** or connect/approve the relevant app in the UI; current tools cannot switch that mode, retrieve hidden task transcripts, or silently grant app access.
- Execute **one** new bounded synthetic storage test inside that supported runtime only after a genuine new interface is available. The acceptance gate is: scheduled task itself creates the complete Markdown report **and** an accessible GitHub PR → CI passes → PR merges → exact report file can be read from `main`; record stable link plus task evidence.
- Keep `OPS-007=EVIDENCE_PENDING` until that test and at least one non-synthetic scheduled report archive succeed; do not claim closed.
- Owner boundaries unchanged: `GROW-SEO-01=HOLD`, `GROW-SEO-02/03=READ-ONLY`, Festival Sales deferred. No site/Wix/GA4/GSC/permissions/tracking changes.
