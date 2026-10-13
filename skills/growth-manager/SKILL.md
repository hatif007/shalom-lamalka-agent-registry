# Skill: Growth Manager — Evidence Synthesis & Prioritization

**Version:** 1.0  
**Runtime status:** Repository skill specification; not evidence of installation into a separate autonomous runtime.  
**Owner mode:** READ ONLY.

## When to use
Use when combining Wix, Google Search Console, GA4, or specialist-agent findings into business priorities and concise outcome summaries.

## Procedure
1. Check source availability and exact property/site identity before querying.
2. Use only data actually returned in the current run or linked, validated Registry evidence.
3. For every metric preserve source, exact date range, extraction time, definition, data freshness, filters, sample size, and known limitations.
4. Label each statement FACT, HYPOTHESIS, RECOMMENDATION, or UNKNOWN.
5. Prioritize by expected business impact, evidence confidence, effort, risk, and reversibility. Do not invent expected revenue impact.
6. Keep Wix online sales separate from festival-booth sales. Never infer one from the other.
7. Treat GA4 zero metrics consistently with owner-confirmed no traffic and healthy synchronization; do not mislabel this as a sync failure. Revisit only when meaningful traffic or a concrete need exists.
8. Record tests and findings in `registries/tests.json` and `registries/findings.json`, link source evidence, and validate JSON/Registry schema.
9. Send a short, material-only outcome to `#growth-outcomes`; technical scope and caveats go to `#agent-registry`. Never claim posting unless confirmed.
10. Do not change site, content, prices, orders, analytics, permissions, credentials, integrations, or campaigns.

## Required finding fields
ID, classification, statement, source, source type, date range, extraction timestamp, metric definition, confidence and rationale, freshness, limitations, alternative explanations, business impact, next step, owner, status, evidence permalink.

## Acceptance criteria
- Facts are traceable to live output or linked evidence.
- Recommendations are not represented as changes or measured outcomes.
- No unsupported sales/revenue inference.
- Registry update is read back and GitHub Actions validation succeeds.
- Slack delivery is separately verified.
