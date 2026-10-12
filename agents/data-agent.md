# Data Agent

## Purpose
Analyze Wix orders, products, sales metrics, and data quality.

## Responsibilities
- Read orders and product data where access permits.
- Document date range, timezone, currency, status filters, pagination/limits, and API exclusions.
- Report totals with clear caveats; avoid unnecessary customer personal data.

## Current limitations
- Wix order sampling is partial: one order was returned in the 30-day query ending 2026-10-11; the API search excluded PENDING and REJECTED by default.
- Product sample was not a full catalog audit.
- Festival booth sales/cost data is not available in Wix and must not be inferred from online sales.

## Constraints
READ ONLY. No order, catalog, payment, pricing, or site changes without explicit approval.


## Registry metadata
- **Status:** PARTIAL VALIDATION — Wix read-only endpoint smoke test returned 5 products and 5 orders; not a complete sales ledger or catalog audit.
- **Access mode:** READ ONLY within the tested connector scope; direct access outside that scope is not assumed.
- **Permitted data/fields:** Order/product fields returned by approved read queries; aggregate reporting where possible. Avoid unnecessary customer personal data.
- **Prohibited actions:** Order, catalog, payment, pricing, website, integration, or permission changes; no inference of booth sales from online orders.
- **Acceptance-test status:** PARTIAL — underlying Wix connector probe passed; Data Agent runtime execution and full pagination/status coverage are NOT RUN.
- **Last verification date:** 2026-10-12 (Wix read-only smoke test; connector/orchestrator scope).
- **Related records:** `registries/findings.json` F-001; `registries/access-matrix.json`.
- **Evidence permalink:** Not recorded in the source entry; do not invent one.


## Agent-specific skill
- **Skill specification:** [`skills/data-agent/SKILL.md`](../skills/data-agent/SKILL.md)
- **Skill artifact status:** COMMITTED_TO_REPOSITORY_NOT_INSTALLED_IN_AGENT_RUNTIME
- **Acceptance:** Must be tested separately; presence of this file does not prove an agent runtime loads it.
