# Skill: SEO Agent — Search Opportunity Detection

**Version:** 1.0  
**Runtime status:** Repository skill specification; not evidence of installation into a separate autonomous runtime.  
**Owner mode:** READ ONLY.

## When to use
Use for Search Console query/page analysis, technical SEO audits, and opportunity hypotheses.

## Procedure
1. Confirm the exact GSC property and search type.
2. Use settled date ranges where possible; record the exact start/end and settled-through date.
3. Preserve query/page dimensions, clicks, impressions, CTR, position, filters, and pagination.
4. Use page-level evidence to connect a query opportunity to the actual landing page before recommending page edits.
5. Separate observed facts from hypotheses. A query with impressions is not proof of a poor snippet or conversion opportunity.
6. Audit pages read-only. Consider locale, canonical, redirects, decorative images, and accessibility before interpreting crawler flags.
7. Never edit or publish website content, metadata, redirects, or settings.
8. Record evidence and caveats in the Registry and send only material summaries to `#growth-outcomes`.

## Required outputs
Source, property, exact date range, settled-through date, query/page sample size, metrics, evidence, hypothesis, confidence, limitations, next step.

## Acceptance criteria
- Live GSC response is reproducible.
- Query opportunities are mapped to pages when possible.
- Synthetic tests are clearly marked synthetic.
- No site changes occur.
- Registry validation passes.
