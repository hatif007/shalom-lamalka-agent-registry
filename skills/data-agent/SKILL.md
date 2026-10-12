# Skill: Data Agent — Wix Read Validation & Data Quality

**Version:** 1.0  
**Runtime status:** Repository skill specification; not evidence of installation into a separate autonomous runtime.  
**Owner mode:** READ ONLY.

## When to use
Use for Wix catalog/order reads, sales-data quality checks, and source-coverage validation.

## Procedure
1. Confirm target Wix site identity from a trusted connected-site lookup; never guess a site ID.
2. Confirm endpoint, method, body, permissions, and response shape from Wix documentation before querying.
3. Use read-only query/list/search endpoints only. Do not mutate Wix.
4. Record HTTP result, query filters, status exclusions, currency, timezone/date boundaries, page size, pagination/hasNext, and extraction time.
5. Minimize data returned and retained; do not copy customer PII into Registry or Slack.
6. Distinguish a sample from a complete catalog or order ledger. Do not calculate sales totals from an incomplete page or default-filtered query.
7. Record a reproducible test and limitations in `registries/tests.json`; record findings only when useful and evidence-backed.
8. Validate JSON and confirm the committed file is present. Report success only after verification.

## Required outputs
- Test status and LIVE/SYNTHETIC/BLOCKED/NOT RUN mode.
- Endpoint/source, sample size, filters, date range, currency, timezone, pagination, response status.
- Results, limitations, changes made (must be false for read-only tests), evidence link.

## Acceptance criteria
- Read request succeeds for the tested endpoint.
- Sample scope and incomplete coverage are explicit.
- No customer personal data is unnecessarily retained.
- No writes occur.
- Registry validation passes.
