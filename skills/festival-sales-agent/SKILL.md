# Skill: Festival Sales Agent — Booth Profitability Analysis

**Version:** 1.0  
**Runtime status:** Repository skill specification; not evidence of installation into a separate autonomous runtime.  
**Activation status:** DEFERRED until reliable booth records are supplied and validated.  
**Owner mode:** READ ONLY.

## When to use
Only after an approved and validated festival-booth dataset is available.

## Required inputs
Transaction/event date, event identifier, SKU/product, quantity, gross sales, discounts/refunds, payment fees, direct product costs, event costs, currency, and inventory reconciliation. Customer personal data should be omitted unless strictly necessary.

## Procedure
1. Verify file/source owner, date coverage, currency, timezone, duplicates, missing values, refunds, and event mapping.
2. Reconcile transaction totals to payment-system or inventory summaries where available.
3. Calculate revenue, net receipts after refunds/fees, direct gross margin, event-level contribution, units per SKU, and uncertainty only where inputs support it.
4. Keep online Wix orders separate from booth sales.
5. If records are missing or cannot be reconciled, return BLOCKED/NOT RUN with the exact gap; do not fabricate a baseline.
6. Record methodology, sample size, limitations, and evidence in the Registry.
7. Do not change payment systems, inventory, prices, or source records.

## Acceptance criteria
- Reliable booth records exist and are validated before any sales analysis.
- Reconciliation and missing-data caveats are explicit.
- No booth revenue is inferred from online sales.
- Registry validation passes.
