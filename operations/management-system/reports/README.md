# Central Agent Report Archive (v1)

**Owner:** Growth Manager | **Canonical branch:** \`main\` | **Status:** STORAGE_CONTRACT_READY; AUTONOMOUS_CHATGPT_TASK_WRITER_NOT_YET_PROVEN
**Source of truth for completed reports:** \`operations/management-system/reports/runs/YYYY-MM-DD/<role>/<report-id>.md\` after the report file is committed and merged. The original ChatGPT task conversation is a **different asset**.

## Why this exists

The ChatGPT Scheduled task dashboard currently provides metadata (\`last_run_time\`, task title and schedule) but no full report transcript to the available orchestration tools. **Permission to read does not create a transcript-fetch API**. Archived reports must therefore be persisted *at generation time* as their full body, rather than reconstructed later from task timestamps or earlier notes.

Do not conflate:
- **Stored generated report**: the full text of a new report saved as a Markdown file by its creator; the document is the full *authored deliverable*, not a byte-perfect transcript of the ChatGPT conversation or hidden tool logs.
- **Recovered excerpt**: partial summary reconstructed from a previous conversation; permanently labelled as \`RECOVERED_EXCERPT\`.
- **Synthetic test**: a technical test of storage; **never** a business report or a specialist-agent run.

## Reliable file contract

Store one UTF-8 Markdown file per distinct run:

\`operations/management-system/reports/runs/2026-10-19/data/GROW-SEO-03-2026-10-19.md\`

The file must begin with a machine-readable JSON comment followed by the **full report body**:

\`\`\`md
<!-- REPORT_ARCHIVE_V1
{"schema_version":"1.0","report_id":"GROW-SEO-03-2026-10-19","role":"data","run_date":"2026-10-19","run_mode":"CHATGPT_SCHEDULED_TASK","payload_type":"FULL_GENERATED_REPORT","task_reference":"ChatGPT scheduled task, Monday data 08:00","source_conversation_url":null,"source_evidence":["https://github.com/hatif007/shalom-lamalka-agent-registry/blob/main/operations/management-system/task-board.json"],"scope":"READ_ONLY","owner_approval":"GROW-SEO-03 APPROVE READ-ONLY 2026-10-14"}
REPORT_ARCHIVE_V1 -->
# GROW-SEO-03 — Data report (example only; NOT an actual report)
...
\`\`\`

Valid \`role\` values: \`data\`, \`seo\`, \`website\`, \`growth\`, \`system\`.
Valid \`payload_type\` values: \`FULL_GENERATED_REPORT\`, \`RECOVERED_EXCERPT\`, \`SYNTHETIC_TEST\`.
Valid \`run_mode\` values: \`CHATGPT_SCHEDULED_TASK\`, \`INSTALLED_AGENT_VERIFIED\`, \`COORDINATOR\`, \`TECHNICAL_SMOKE_TEST\`.
\`INSTALLED_AGENT_VERIFIED\` **requires genuine runtime evidence**; choose ChatGPT Scheduled for ordinary scheduled tasks. \`source_conversation_url\` may remain \`null\` until an actual conversation permalink can be obtained.
Use only non-sensitive metadata and findings: **no personal customer information, email addresses, individual order details, secrets, authentication tokens or raw financial exports**. Archive is a reporting record; do not change business data, configurations, analytics, permissions or the website.

## Write sequence (no silent gaps)

1. Run the scheduled research **once**, subject to existing owner decisions and connected-source permissions. Generate the **complete source-grounded report once**.
2. If GitHub write tools are available *during that run*, create **one new exact Markdown report** on a fresh \`report/<date>-<role>\` branch, using this contract. **No silent replacements or modifications to unrelated Registry files.**
3. Open a PR to \`main\`, run Registry validation/CI; merge only when the active tool permissions and repo policy allow it. If merge is blocked, include the PR link and report \`REPORT_READY_PR_PENDING\`. The committed file is the source-linked artifact after merge.
4. Post a short final-only summary in the role's **authorized** channel, **only if the installed Skill/task/tool policy allows sending**; include the actual GitHub report URL. Growth Manager collects links in \`#business-insights\` for decisions only. Do not claim Slack delivery without its actual permalink.
5. If GitHub app actions are unavailable/refused, **print the full report in the task conversation** with \`ARCHIVE_BLOCKED\`, the exact attempted action and missing connector/permission. Never invent a GitHub link. Do not re-run expensive source research to fix storage.
6. If the task can only return narrative, a separately authorized coordinator can file that **same exact report text** with a backlink and truthful provenance. A summary is not a verbatim original.

## Acceptance checks

**Archive implementation test:** writing a synthetic file to a topic branch + passing \`scripts/validate_report_archive.py\` + merging + reading back the identical file proves storage works for this coordinator only.

**Actual scheduled-task-to-repository test:** run one **low-cost synthetic scheduled ChatGPT task**, which itself writes and commits a \`SYNTHETIC_TEST\` report and returns a proven URL/PR; verify via GitHub and task history. Only that end-to-end result can mark the *scheduled writer* VERIFIED. No external business research or site mutation for this smoke test. **Failure to send from within a scheduled task leaves OPS-007 BLOCKED**, even if the coordinator can upload separately.

**Production acceptance (first Monday):** each of Data, SEO and Growth has an original full generated Markdown report with actual evidence, exact date and matching task receipt, PR/CI link, and a genuine final delivery receipt or an honest \`NOT_POSTED\`. Never classify an archived excerpt or synthetic test as a full report.

## Current business gates

- \`GROW-SEO-01=HOLD\` — no homepage preview or draft implementation.
- \`GROW-SEO-02=APPROVE READ-ONLY\` — SEO research only.
- \`GROW-SEO-03=APPROVE READ-ONLY\` — Data research only; the owner verified no orders in the prior tested week.
- Festival Sales is \`DEFERRED\`.
- Direct invocation of installed GPT agents remains unverified/unavailable in this connection.

See [Task Board](../task-board.json), [Owner Decisions](../owner-decisions-2026-10-14.md) and \`OPS-007\`.
