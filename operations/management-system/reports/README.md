# Central Agent Report Archive (v1)

> **Active OPS-007 policy (2026-10-17): API trigger currently BLOCKED (HTTP 409). No four-agent native E2E pass has been established. Automated GitHub inbox promotion is intentionally paused; manual `workflow_dispatch` remains available for individually inspected, provenance-correct files. This pause does NOT disable separately configured ChatGPT Scheduled Tasks. Preserve historic synthetic files for audit, not as business findings. Do not trigger a new production report, change Wix, or automatically publish to Slack based on these technical tests.**

> **Authoritative roles and paths:** Native or separately authorized scheduled report writers use only the already-created role branch `report/inbox-<role>` with new file `reports/runs/YYYY-MM-DD/<role>/<report-id>.md`. The reviewed archive promotion workflow copies the file to `main:operations/management-system/reports/runs/YYYY-MM-DD/<role>/<report-id>.md`; the originating agent never creates branches, opens PRs or merges. This current workflow supersedes historical examples elsewhere in this document.

**Owner:** Growth Manager | **Canonical branch:** `main` | **Status:** STORAGE_CONTRACT_READY; AUTONOMOUS_CHATGPT_TASK_WRITER_NOT_YET_PROVEN
**Source of truth for completed reports:** `operations/management-system/reports/runs/YYYY-MM-DD/<role>/<report-id>.md` after the report file is committed and merged. The original ChatGPT task conversation is a **different asset**.

## Why this exists

The ChatGPT Scheduled task dashboard currently provides metadata (`last_run_time`, task title and schedule) but no full report transcript to the available orchestration tools. **Permission to read does not create a transcript-fetch API**. Archived reports must therefore be persisted *at generation time* as their full body, rather than reconstructed later from task timestamps or earlier notes.

Do not conflate:
- **Stored generated report**: the full text of a new report saved as a Markdown file by its creator; the document is the full *authored deliverable*, not a byte-perfect transcript of the ChatGPT conversation or hidden tool logs.
- **Recovered excerpt**: partial summary reconstructed from a previous conversation; permanently labelled as `RECOVERED_EXCERPT`.
- **Synthetic test**: a technical test of storage; **never** a business report or a specialist-agent run.

## Reliable file contract

Store one UTF-8 Markdown file per distinct run:

`operations/management-system/reports/runs/2026-10-19/data/GROW-SEO-03-2026-10-19.md`

The file must begin with a machine-readable JSON comment followed by the **full report body**:

```md
<!-- REPORT_ARCHIVE_V1
{"schema_version":"1.0","report_id":"GROW-SEO-03-2026-10-19","role":"data","run_date":"2026-10-19","run_mode":"CHATGPT_SCHEDULED_TASK","payload_type":"FULL_GENERATED_REPORT","task_reference":"ChatGPT scheduled task, Monday data 08:00","source_conversation_url":null,"source_evidence":["https://github.com/hatif007/shalom-lamalka-agent-registry/blob/main/operations/management-system/task-board.json"],"scope":"READ_ONLY","owner_approval":"GROW-SEO-03 APPROVE READ-ONLY 2026-10-14"}
REPORT_ARCHIVE_V1 -->
# GROW-SEO-03 — Data report (example only; NOT an actual report)
...
```

Valid `role` values: `data`, `seo`, `website`, `growth`, `system`.
Valid `payload_type` values: `FULL_GENERATED_REPORT`, `RECOVERED_EXCERPT`, `SYNTHETIC_TEST`.
Valid `run_mode` values: `CHATGPT_SCHEDULED_TASK`, `INSTALLED_AGENT_VERIFIED`, `COORDINATOR`, `TECHNICAL_SMOKE_TEST`.
`INSTALLED_AGENT_VERIFIED` **requires genuine runtime evidence**; choose ChatGPT Scheduled for ordinary scheduled tasks. `source_conversation_url` may remain `null` until an actual conversation permalink can be obtained.
Use only non-sensitive metadata and findings: **no personal customer information, email addresses, individual order details, secrets, authentication tokens or raw financial exports**. Archive is a reporting record; do not change business data, configurations, analytics, permissions or the website.

## Active role-inbox write sequence (no silent gaps)

1. Require a specific owner-approved run and an installed-agent runtime that can execute it. Check role-level tool constraints, the existing `report/inbox-<role>` branch, valid scope and data privacy before requesting any report. During the OPS-007 API 409 freeze, do not infer a run from a scheduled task configuration, local GitHub Actions job, or archived file.
2. If the run is expressly authorized, the **originating agent** produces exactly one original UTF-8 Markdown report, with truthful `REPORT_ARCHIVE_V1` metadata and `source_evidence`. For a purely synthetic OPS-007 test use `TECHNICAL_SMOKE_TEST` and `SYNTHETIC_TEST`. Never label the same test a business report or verified production output.
3. The report writer may create only `reports/runs/YYYY-MM-DD/<role>/<report-id>.md` on its PRE-EXISTING role branch `report/inbox-<role>`, provided tool-level permissions allow it. Never create another branch, write `main`, overwrite prior reports, open or merge PRs, or modify other roles' files. Read back the exact new file and verify its Git blob SHA. If any step fails, mark `ARCHIVE_BLOCKED` with the real cause.
4. A separately authorized review operator may run `.github/workflows/promote-agent-inbox.yml` manually **after** inspecting the original reports and their runtime provenance; it stages byte-for-byte copies under `operations/management-system/reports/runs/YYYY-MM-DD/<role>/<report-id>.md` on a dedicated archive branch, opens a reviewable PR and never auto-merges. The weekly cron is paused pending OPS-007 native E2E acceptance. Only after merge/readback does the report exist in the canonical `main` archive.
5. Growth Manager Pilot must read the three separate verified specialist reports before preparing its own original report. Any authorized Slack send must be separately allowed, deduplicated by exact cycle, and independently verified by a real permalink. A GitHub coordinator never impersonates a native role or substitutes its own report/message for the role's output.
6. The originating agent should include the complete authored report in its own conversation when feasible, especially when archiving fails, and preserve `UNKNOWN` for unsupported business claims. Avoid costly repeat research solely to fix storage. No customer PII, credentials or raw transaction data.

**Historical notes below document prior Scheduled Task trials and are not authority to override the above current role-inbox/write policy.**

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

## Accepted scheduled one-step writer architecture — 2026-10-14

**Historical attempts A/B:** the scheduled task succeeded in creating a topic branch but did not save a file; a synthetic issue handoff was not observed. **New reduced-action smoke C: PASS.** A one-time ChatGPT Scheduled Task directly created a [full synthetic Markdown file](runs/2026-10-14/system/ARCHIVE-E2E-SCHEDULED-2026-10-14.md) on an already-existing topic branch. The coordinator **read back exact file contents**, [PR #15](https://github.com/hatif007/shalom-lamalka-agent-registry/pull/15) passed Registry CI and was merged; a subsequent read of `main` returned the identical blob. **This proves technical scheduled-task file persistence, not a production business report or full ChatGPT conversation transcript.**

**Dedicated permanent report-only inbox branches (created and verified):** `report/inbox-data`, `report/inbox-seo`, `report/inbox-website`, and `report/inbox-growth`.

**New authorized write sequence:** each existing weekly *ChatGPT Scheduled Task*, after producing its full report once, performs **one GitHub `create_file` call on its own PRE-CREATED inbox branch** to `reports/runs/YYYY-MM-DD/<role>/<report-id>.md` using this metadata schema, no branch/PR/issue creation in the scheduled context. This route was tested with a small synthetic file; genuine full report persistence still requires first scheduled weekly evidence. Tasks must also return their full authored Markdown report in their task conversation, even if a write fails. An authorized GitHub operator checks source quality, opens a PR, gets CI pass and merges to `main`, then optionally posts only final verified findings to Slack. No automated CI merge or automatically archived *transcript* is implied.

**Role-specific write policies:** the separate ChatGPT Scheduled Data *task* has its own report-only inbox workflow. The historical installed Data Agent v2 prohibited all GitHub/Registry writes; repository Skill v2.1 adds an **explicitly owner-approved, synthetic OPS-007 native-test exception** for at most one new `reports/runs/YYYY-MM-DD/data/OPS007-NATIVE-<run-id>-data.md` on the existing `report/inbox-data` branch. **The installed Workspace Data Agent does not inherit that updated Skill from a GitHub merge; its active Skill and higher-priority Instructions must be updated and confirmed separately before native E2E.** This exception never authorizes Wix/GA4/GSC changes or production GitHub report writes. Other installed roles also require actual role-scoped Writer tool permissions and active Skill compliance. A report archived in a private GitHub repository is the **full authored deliverable**, not ChatGPT raw conversation metadata, tool-call logs, or a native agent invocation trace.

**Growth source fallback:** before running any new source queries, inspect relevant existing files in `report/inbox-data`, `report/inbox-seo` and `report/inbox-website` and `main`. If an original specialist report is missing/unverified, write `EVIDENCE_PENDING` rather than inventing a report or rerunning the specialist. Avoid treating `SYNTHETIC_TEST` as evidence of sales/SEO outcomes. The coordinator performs the branch-to-`main` PR/CI review outside scheduled task execution.
