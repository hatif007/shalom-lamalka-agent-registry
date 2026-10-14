# Acceptance — four-agent weekly system and report delivery (2026-10-14)

**Owner instruction:** Perform end-to-end acceptance; owner granted standing autonomous approval to inspect agent configurations, task reports and technical report infrastructure. **Reviewer:** coordinating assistant (independent checks). **Scope:** scheduled ChatGPT tasks, GitHub role/Registry files, archive, Slack. **No changes to Wix, GA4, GSC, live site, order data, tracking or permission grants.**

**Overall verdict: `PARTIAL — FOUR_SCHEDULES_PASS / SYNTHETIC_SCHEDULED_FILE_WRITE_PASS / REAL_WEEKLY_REPORT_PENDING / NATIVE_RUNTIME_AND_TRANSCRIPT_BLOCKED`.**

## Acceptance matrix

| Test | Result | Evidence/meaning |
| --- | --- | --- |
| `T01` Four distinct role definitions | **PASS — repository specification only** | `skills/data-agent/SKILL.md` (v2.0), `skills/seo-agent/SKILL.md` (v1.0), `skills/website-conversion-agent/SKILL.md` (v1.0), `skills/growth-manager/SKILL.md` (v1.0). Each specifies duties, evidence and no public/business changes. A repo file is not runtime installation evidence. |
| `T02` Actual installed runtime version and loaded Skill for EACH of four | **BLOCKED** | `registries/agent-acceptance-plan.json` reports `runtime_instance_verified=false`, `skill_loaded_in_instance_verified=false` for every active agent. Data has owner-/operator-reported v2 runtime tests, but source-read trace and installed Skill weren't independently verified here. Website v1.1 remains a reported unpublished draft; repo still v1.0. No native installed-agent configure/invoke tool exposed to coordinator. |
| `T03` Four recurring ChatGPT report tasks enabled, distinct and appropriate | **PASS — configuration** | Actual task inventory: Sunday Website 22:30, Monday Data ~08:00, SEO ~10:00, Growth 12:00 (Asia/Jerusalem). Prompts require correct source read, no homepage work, read-only/final-only reporting. Previous duplicate Growth automations disabled. See [calendar](operating-calendar.json). |
| `T04` First complete scheduled 4-stage weekly cycle | **PENDING BY DATE** | First Website Sunday **2026-10-18** and Data/SEO/Growth Monday **2026-10-19** have not occurred as of 2026-10-14. Today's one-time individual ChatGPT reports are NOT the first full recurring cycle, nor direct installed-agent runs. |
| `T05` Report archive storage with provenance validator and CI | **PASS — coordinator only** | [Archive contract](reports/README.md), [synthetic coordinator fixture](reports/runs/2026-10-14/system/ARCHIVE-SMOKE-COORDINATOR-2026-10-14.md), [schema check](../../scripts/validate_report_archive.py), merged PR #13. This verifies repository storage/readback, not scheduled writer or ChatGPT conversation export. |
| `T06` Automated report-file write FROM Scheduled ChatGPT task to GitHub | **PASS — SYNTHETIC ONLY** | Smoke C: scheduled ChatGPT task created exact [synthetic full Markdown file](reports/runs/2026-10-14/system/ARCHIVE-E2E-SCHEDULED-2026-10-14.md) on pre-created branch; blob SHA `9260139ee333763249da76fab2b92c54627a0057`. [PR #15](https://github.com/hatif007/shalom-lamalka-agent-registry/pull/15) CI PASS, merged; identical blob reread from `main`. Does **NOT** prove a genuine specialist report saved yet. Earlier branch-only/issue failures remain in historical acceptance record. |
| `T07` Full ChatGPT task *conversation transcript* accessible through connected automation API | **BLOCKED** | Available task controls expose task schedule and last run, not full task conversation or native transcript bytes. There is no exposed authenticated ChatGPT task transcript fetch/export action to this chat. Full authored report is not a verbatim conversation transcript, including tool logs. An owner authorization does not add a missing API. |
| `T08` Slack final-only delivery and message permalink | **PARTIAL** | Authenticated coordinator has previously successfully posted final management summaries to [#business-insights](https://shalomlamalka.slack.com/archives/C0C8PNALALR). Recent specialist channel reads showed no new 2026-10-14 task-origin final Data/SEO/Website report. The scheduled tasks' ability to send remains unverified and previously reported blocked in original task conversations. |
| `T09` Governance boundaries and permissions | **PASS for repository/task instructions; runtime NOT TESTED** | `GROW-SEO-01=HOLD`, `GROW-SEO-02/03=APPROVE READ-ONLY`, Festival Sales deferred. No live site or analytics writes in this acceptance. GitHub `main` branch protection remains outside connector admin access (`OPS-003`). |
| `T10` Calendar matches actual schedules | **FIXED IN PR — CI to verify** | Corrected `CAL-WEBSITE-WEEKLY` from `MANUAL_ONLY` to `CHATGPT_AUTOMATION_ENABLED` / `SCHEDULED_FIRST_RUN_PENDING`; updated `scripts/validate_management.py` to require verified Website task identity but preserve `autonomous_agent_run=false`. |

## Four-role contract inspection

| Domain | Repository Skill | Current weekly ChatGPT task | Required installed-runtime test |
| --- | --- | --- | --- |
| Data | GA4/Wix source validation; event/sample/pagination evidence, no business writes; installed Data v2 GitHub writes specifically forbidden | Monday ~08:00 ChatGPT report, full Markdown returned in conversation and attempt at separately scoped REPORT_ONLY archive | Inspect installed v2 Skill + actual autonomous read trace; do not infer from coordinator tools or ChatGPT scheduled task |
| SEO | GSC query/page mapping, canonical/locale and read-only feasibility | Monday ~10:00 report, GROW-SEO-02 approved research only | Inspect installed configuration and native GSC read evidence |
| Website | CRO/site/RTL improvement packet; owner review before any implementation | Sunday 22:30 infrastructure exceptions only, not homepage hero/Preview | Confirm whether v1.1 was actually Published and matches approved constraints (GitHub v1.0 cannot prove it) |
| Growth Manager | Read evidence, synthesize at most 3 priorities, owner approval gates | Monday 12:00 existing evidence synthesis, no duplicated Data/SEO pulls | Inspect actual GPT instructions and an installed-runtime run/session trace |

## Correct run acceptance and transcript boundary

The accepted pipeline is `scheduled task run receipt -> complete authored output -> archive as FULL_GENERATED_REPORT with exact source -> GitHub CI/PR -> readback -> final Slack permalink -> Growth owner inbox`. Every arrow requires a real receipt, never an intended prompt.

A native transcript pipeline (`ChatGPT Previous Runs conversation -> authenticated export/get transcript bytes -> secure private archive -> readback`) is **not available to the current tool set**. An authenticated ChatGPT Work UI session can be used for a real UI-based export if the user switches to Work mode; do not use unsupported private endpoints or fake conversation URLs. Existing recovered excerpts remain `RECOVERED_EXCERPT`.

## Next acceptance gate

1. **DONE:** smoke C exact synthetic file created by scheduled task on pre-created branch, reviewed, CI passed, merged via PR #15, identical blob reread from `main`. Dedicated inbox branches now exist for `data`, `seo`, `website`, `growth`; all four weekly ChatGPT task prompts were changed to ONE `create_file` call on their pre-existing branch.
2. **PENDING:** the first genuine full Data/SEO/Website/Growth reports in these inbox branches have not yet been observed; owner-approved original ChatGPT conversation transcripts cannot be fetched via this API. Keep `OPS-007=EVIDENCE_PENDING` until a real `FULL_GENERATED_REPORT` is written and independently verified.
3. On 2026-10-19 run separate already-scheduled first-cycle QA (created 2026-10-14 for ~15:00), verify each role's real run receipt, merged full report, source evidence and Slack if allowed, without confusing task output with installed agent runtime.

**Owner approval needed:** none for further evidence reads or Registry/report-only maintenance. Runtime connector installation or ChatGPT UI Work activation needs an actual supported technical surface; user's standing approval does not create one.

## Supplemental synthetic write proof

[File after main merge](reports/runs/2026-10-14/system/ARCHIVE-E2E-SCHEDULED-2026-10-14.md) · [PR #15](https://github.com/hatif007/shalom-lamalka-agent-registry/pull/15) · [CI pass](https://github.com/hatif007/shalom-lamalka-agent-registry/actions/runs/38541374368). This validates the path `ChatGPT Scheduled Task → pre-existing GitHub branch → exact full authored file → coordinator PR → CI PASS → main → readback`. It does **not** yet validate real weekly report generation, automatic Slack final delivery, independently installed agent invocation or exact full ChatGPT raw conversation transcript extraction.
