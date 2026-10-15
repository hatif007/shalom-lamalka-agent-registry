# OPS-007 — Verified reporting handoff and QA protocol (2026-10-15)

Status: **REPAIR_PROPOSED / AUTOMATIC_DELIVERY_NOT_VERIFIED**. Approved by owner for Registry/reporting infrastructure work. This is not a claim that ChatGPT Scheduled Tasks or installed GPTs can send autonomously to Slack.

## Incident evidence

On 2026-10-15 four ChatGPT Scheduled Tasks generated Website, Data, SEO, and Growth deliverables in their respective conversations. The four attempts to write full authored reports using GitHub `create_file` were reported blocked by OpenAI safety checks; file lookups returned 404. Growth read missing files, correctly recorded EVIDENCE_PENDING, and could not consume the other original reports. No final Slack messages were verified. Synthetic storage success on 2026-10-14 does not prove production delivery.

## Required sequence and acceptance

1. Specialist generates report with date, source, exact source window and timezone, row counts/pagination, freshness and FACT/UNKNOWN. Prior history is not the same as agent operating age.
2. Archive only when GitHub tool/policy allows it, using REPORT_ARCHIVE_V1 and the complete authored body. Never retry a safety-blocked operation, swap APIs to evade a block, or call storage successful without readback. Use existing role inbox branches only under the scheduled task scope.
3. A separately authorized Registry coordinator may archive *owner-provided original complete authored reports* after quality review, with provenance distinguishing coordinator archiving from scheduled-task persistence. No synthetic business claims; no assertion that a raw ChatGPT conversation transcript was exported.
4. Growth must read the three full specialist artifacts, confirm source/role/date and independently re-query a bounded sample of decisive business metrics, or label SOURCE_NOT_RECHECKED; do not merely copy figures. Missing any source: EVIDENCE_PENDING, not invented synthesis.
5. Slack is **output only, not a proven inter-agent transport**. Only if sending is authorized in the active runtime, publish one verified final manager summary in #business-insights, with actual report URL and permalink. Specialist channels get at most one real final-only notification if independently authorized. A Slack message does not itself prove Growth consumed the source report.
6. Independent OPS-007 QA must verify source file SHA and readback, Growth citation of each specialist source, independent spot checks, CI/PR merge when applicable, Slack permalink, and separate installed GPT runtime proof. Accept independently: DATA_VALIDATED, COORDINATOR_ARCHIVED, SCHEDULED_WRITER_VERIFIED, GROWTH_HANDOFF_VERIFIED, SLACK_DELIVERY_VERIFIED, NATIVE_AGENT_VERIFIED.

## Bounded data QA performed on 2026-10-15

Independent GSC API re-query of site https://www.shalomlamalka.com/ using web search, 2026-09-15 through 2026-10-12: 271 clicks, 3373 impressions, 8.03439% CTR, position 7.10999. Prior 2026-08-18 through 2026-09-14: 214 clicks, 2776 impressions, 7.70893% CTR, position 7.46362. Exact query 'בגדים לפסטיבלים': 3 clicks, 90 impressions, position 9.07778. API settledThrough=2026-10-12, firstIncompleteDate=2026-10-13, dateBasis=America/Los_Angeles. These corroborate the *specific reported GSC values*, not live site canonical/inventory, source tool logs, or the complete SEO report.

## Safety and governance

GROW-SEO-01=HOLD; GROW-SEO-02/03=READ_ONLY; Festival Sales=DEFERRED. No Wix/GA4/GSC/tracking/order/site/content/permissions writes; never include personal order/customer data. A requested repair does not grant authority to bypass a tool refusal.

## Unresolved architectural blocker

A ChatGPT notification email links to a task conversation but is not a machine-readable report inbox. The currently exposed coordinator interfaces do not supply the full contents of arbitrary other task conversations. Until a permitted persistent-report write or supported authenticated transcript interface succeeds, fully unattended Growth intake remains **BLOCKED**. Repeating identical scheduled writer attempts is a test, not a demonstrated fix. Do not close OPS-007 until an end-to-end production pass is independently evidenced.
