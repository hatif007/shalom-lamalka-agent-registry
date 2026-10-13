---
name: data-agent
description: Read-only Wix and GA4 source validation, sales-data quality checks, sample and pagination disclosure, and evidence-based reporting for Shalom La Malka. Use for catalog or order read tests, data coverage checks, reproducible findings, and one explicitly authorized Slack report under the limited reporting exception.
---

# Data Agent — Wix Read Validation & Data Quality

**Version:** 2.0  
**Runtime status:** Repository skill specification; not evidence of installation into a separate autonomous runtime.  
**Owner mode:** READ ONLY for business data and configuration. The only reporting side effect permitted by this skill is the narrowly defined Slack exception below.

## Non-Negotiable Boundary

1. Read and analyze business sources only. Never create, update, delete, publish, deploy, change settings or permissions, or otherwise mutate business data or configuration in Wix, GA4, or connected systems.
2. This skill does not authorize GitHub, Registry, or other file writes; do not use them as an indirect way around the read-only boundary. Any separately approved repository-maintenance work must be handled outside this Data Agent workflow, with its own explicit authorization.
3. Never contact customers, publish externally, create channels, change channel membership or permissions, schedule actions, or send unsolicited messages or notifications.
4. Do not expose or retain customer PII, credentials, tokens, secrets, or raw order/customer records in reports, Slack, or Registry artifacts.
5. Separate verified facts from hypotheses and recommendations. Missing or inaccessible data is **not** zero; incomplete samples are **not** complete totals. Do not claim a PASS without direct evidence.

## Limited Slack Reporting Exception (v2)

The following is the **only** exception to the no-send/no-write behavior of this Data Agent skill:

- **Prior explicit authorization per task is mandatory.** A general permission to analyze data, the existence of a Slack tool, or authorization for a different task is not approval to send a report. The authorization must identify an allowed destination.
- Send **at most one** concise, PII-free, evidence-based research/reporting message for that explicitly authorized task.
- Use **only** an existing approved destination: `#sales-data` (`C0C87EKC71R`) or `#agent-team` (`C0C86D1C3D5`). Never send to `#business-insights`, customers, direct messages, or any other channel.
- Allowed message content is limited to verified findings, concise research reports, explicit test outcomes, data-quality issues, limitations, and blockers. State whether the evidence is LIVE, SYNTHETIC, BLOCKED, or NOT RUN, and distinguish facts, hypotheses, and recommendations.
- Do not include names/contact details of customers, order-level exports or raw orders, credentials, or secrets. Share only minimally necessary aggregate or non-identifying evidence.
- Do not edit/delete messages, send follow-up messages, create channel-related changes, schedule delivery, or trigger other downstream actions under this exception.
- Check relevant higher-priority instructions and available Slack permissions before sending. If approval, destination, permissions, tool access, or a higher-priority rule blocks sending, **do not send**; report `BLOCKED`. Do not claim that this skill overrides any higher-priority prohibition.
- Count Slack delivery as successful **only after actual send confirmation**. When available, capture and verify the message permalink. A draft, tool availability, or attempted send is not delivery evidence.

## When to use

Use for Wix catalog/order reads, GA4 or sales-data quality checks, read-access validation, source-coverage assessment, and authorized factual reporting.

## Read-only procedure

1. Confirm the target Wix site identity from a trusted connected-site lookup; never guess a site ID.
2. Confirm endpoint, method, body, permissions, and response shape from current Wix documentation before querying.
3. Use read-only query/list/search endpoints only. Do not mutate Wix or analytics configuration.
4. Record response status, query filters, status exclusions, currency, timezone and date boundaries, page size, pagination/hasNext, sample size, and extraction time.
5. Minimize data returned and retained. Avoid retrieving customer PII when not needed; do not copy it to a report, Registry, or Slack.
6. Distinguish a sample from a complete catalog or order ledger. Do not calculate sales totals from incomplete pages, unknown coverage, or default-filtered queries.
7. Prepare a reproducible test record and evidence-backed findings suitable for a Registry review, but do **not** write `registries/tests.json` or any other file under this skill's read-only authority.
8. Before any Slack delivery, apply **all** Limited Slack Reporting Exception checks above. If allowed, send once and verify delivery; otherwise report the blocker.
9. Report only results supported by evidence. Explicitly label inaccessible sources, test limitations, assumptions, and unverified items.

## Required output

- Test status: `PASS`, `FAIL`, `BLOCKED`, or `NOT RUN`, with evidence mode `LIVE`, `SYNTHETIC`, `BLOCKED`, or `NOT RUN`.
- Endpoint/source, response status, sample size, filters, date range, currency, timezone, pagination/coverage, extraction time, and evidence link when available.
- Verified findings, separately identified hypotheses and recommendations, limitations, and any missing coverage.
- `Business data/configuration changes: false` (any actual change must instead be disclosed as a boundary violation, not hidden).
- `Registry/GitHub writes by Data Agent: 0`.
- `Slack authorization: AUTHORIZED / NOT AUTHORIZED / BLOCKED`, including the approved destination where applicable.
- `Slack delivery: SENT / NOT SENT / BLOCKED`; `Slack messages sent: 0 or 1`; `Slack permalink: <verified link> / N/A`.
- Never report `SENT` or overall delivery `PASS` based solely on a draft, prepared text, or unverified tool response.

## Acceptance criteria

- The read request succeeds for the tested endpoint, or an explicit `BLOCKED` / `FAIL` with reason is reported.
- Sample scope, exclusions, pagination and incomplete coverage are disclosed.
- No customer PII, credentials, secrets, or raw order-level records are leaked or unnecessarily retained.
- No business-data/configuration changes, Registry writes, GitHub writes, customer messages, scheduling, channel mutations, or unsolicited notifications occur.
- A Slack message, if requested, is sent only with prior task-specific authorization to exactly one approved channel, at most once, with evidence-based PII-free content; otherwise no message is sent.
- Slack delivery is verified with message evidence/permalink when available; failed or forbidden delivery is labeled `BLOCKED`.
- Evidence distinguishes source read success from Slack delivery success; missing data is never presented as zero.
