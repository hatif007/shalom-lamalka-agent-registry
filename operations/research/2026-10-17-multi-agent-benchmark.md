# Shalom La Malka | Multi-Agent System Benchmark | 2026-10-17

Status: independent repository-and-public-doc research; no native Workspace Agent triggered, no Wix/GA4/GSC business data read, no Slack message sent. This note is a research recommendation, not an installed-agent report. GROW-SEO-01 stays HOLD.

## Executive verdict

The project is a serious prototype with unusually good controls for a small-business agent team: four distinct installed specialist/manager roles, role-scoped GitHub inboxes, a strict synthetic-vs-real provenance schema, a reviewed report promotion workflow, source SHA validation and no automatic execution of business-changing actions. But a four-agent native end-to-end run has NOT passed. Actual API calls to the installed Data Agent have been blocked by HTTP 409. A synthetic archive test or CI success must never be presented as native-agent execution.

Strategic gap: the system protects reports much better than it currently maintains execution state or measures business outcomes. Priorities should be reliability, reproducibility, meaningful verified metrics, and controlled owner decisions, not additional agent roles.

## Repository evidence

Audited main at commit 62806a895315bffa173626ff6cd742d5a731eca4; 68 tracked files, 4 GitHub Actions workflows, 6 skill specs, 3 Python test modules.

Relevant artifacts:
- scripts/ops007_workspace_agents_e2e.py: issues native API triggers; validates distinct channels; waits for completions; verifies fresh reports in GitHub by role/date/cycle and blob SHA; passes three actual report links and SHAs to Growth Manager Pilot.
- scripts/ops007_data_api_probe.py: one Data Agent diagnostic POST with redacted support metadata.
- scripts/promote_agent_inbox.py and .github/workflows/promote-agent-inbox.yml: validate and copy role inbox reports byte-for-byte into canonical archive via reviewed Pull Request. No auto-merge.
- operations/management-system/reports/README.md: REPORT_ARCHIVE_V1 requires metadata and distinguishes SYNTHETIC_TEST, RECOVERED_EXCERPT, FULL_GENERATED_REPORT.
- operations/management-system/team-scorecard.json: actuals array is empty at review; KPI output/report targets exist but most performance targets have not been grounded.
- data-sources/ga4.json: PARTIAL_UNRESOLVED historical status. data-sources/wix.json: PARTIAL scoped reads. data-sources/google-search-console.json: VERIFIED_FOR_TESTED_READS only.

Installed-role state and external integration success cannot be inferred solely from these files. Support escalation and owner screenshots corroborate the current HTTP 409 native API blocker.

## Competitive benchmark

| Public project/example | Capability actually documented | Opportunity for this project |
| --- | --- | --- |
| OpenAI Agents SDK | Specialist-as-tool / handoffs, trace records of tool invocations and guardrails | Add per-cycle tool provenance and trace-style run journal; SDK does not directly prove or replace installed Workspace Agent invocation |
| LangGraph | Durable checkpoints, interrupts and resume, distinct retry strategies | Persist run state after each significant step; resume a partially successful cycle without reissuing non-idempotent sends |
| CrewAI Flows | Structured state, orchestration, optional persistence across steps | Keep state machine separate from natural-language Markdown reports |
| Microsoft Agent Framework | Sequential, concurrent, handoff, manager orchestration and HITL | Our model (3 specialists then Growth manager) is sensible; implement its ownership and approval rules as executable checks |
| Temporal | Durable execution across crashes, timeouts, long approvals | Valuable concept, but likely too heavyweight for this pilot until multi-day workloads exist |
| n8n Shopify-Gemini-Slack weekly template | Deterministic order KPIs -> LLM analysis -> historical sheet -> Slack, decline alert | Compute and version numeric KPIs outside the LLM; alert only on corroborated material changes |
| n8n profit-leak Shopify template | Product costs + fees + order data -> margin anomalies | Build finance completeness flags; no verified profit without cost, shipping, fees, returns |
| Shopify Sidekick / Wix Analytics Pro | Merchant-facing natural language assistant near store data | Our differentiation should be cross-source evidence, Hebrew RTL/CRO context and owner-controlled decisions, not generic chatbot answers |
| OWASP Excessive Agency | Broad agent capabilities and untrusted tool output can become security vulnerabilities | Enforce least privilege at tool level, treat reports as untrusted, require human approval for live changes |

Primary source URLs:
- https://developers.openai.com/api/docs/guides/agents/sdk
- https://openai.github.io/openai-agents-python/tracing/
- https://docs.langchain.com/oss/javascript/langgraph/thinking-in-langgraph
- https://github.com/crewAIInc/crewAI/blob/main/docs/v1.15.12/en/concepts/flows.mdx
- https://learn.microsoft.com/agent-framework/workflows/orchestrations/
- https://docs.temporal.io/ai
- https://n8n.io/workflows/13872-analyze-shopify-orders-with-gemini-ai-and-send-weekly-slack-insights/
- https://n8n.io/workflows/20619-monitor-daily-shopify-profit-leaks-with-gpt-4o-google-sheets-and-slack/
- https://help.shopify.com/en/manual/ai-powered-tools/sidekick
- https://support.wix.com/en/article/wix-analytics-pro-an-overview
- https://genai.owasp.org/llmrisk/llm062025-excessive-agency/

These are documented patterns and community workflow templates; none are proved deployed here or directly comparable through measured business outcomes.

## Specific gaps and risks

P0 A. Native API availability: The trigger returned HTTP 409 even after refreshing the Workspace Agents token. The support case is escalated with real request IDs. The next meaningful success gate is accepted-and-completed native runtime, not merely 202 or working chat. Avoid additional four-agent retries until resolved.

P0 B. Four-agent E2E proof: No verified set of three fresh native specialist reports plus Growth report and genuine Slack permalink for the same cycle. CI and synthetic smoke reports must stay separate from operational acceptance.

P1 C. Partial-cycle recovery: The coordinator triggers Data, SEO and Website before waiting on all three. If a later trigger fails, earlier agents could already be running. No durable cycle checkpoint or safe resume mechanism currently exists, and rerunning dispatch creates a new cycle. Design a persisted cycle ledger with role states, attempt count, agent_trigger_run_id, source report URL/blob SHA, Slack sent status and final decision; no rerun of side effects without verification.

P1 D. Slack real delivery: Growth Pilot is supposed to send once, but coordinator ends as PARTIAL_UNTIL_SLACK_PERMALINK_VERIFIED and has no independent Slack readback. Add exact-cycle ID lookup, sender provenance, one-per-cycle delivery ledger and verified permalink. No fake coordinator substitute.

P1 E. Contracts drift: operations/management-system/reports/README.md still describes creator-side new report branches and PRs, while current accepted implementation uses pre-existing report/inbox-role branches and separate promotion. Several historic registry/calendar instructions remain interspersed with current ones; token secret references in the current workflows are WORKSPACE_AGENTS_TOKEN1 while older guide says WORKSPACE_AGENTS_TOKEN. Create one canonical current runbook and automatic stale-reference lint; keep historical notes explicitly marked historical.

P1 F. Timezone mismatch: promote-agent-inbox.yml uses cron 45 9 * * 1 in UTC. That is approximately 12:45 in Israel daylight time and 11:45 in standard time. Growth review is scheduled 12:00 Israel, so winter archive promotion may run BEFORE Growth and defer the newest Growth report until a later cycle. Better trigger on verified completion or choose a timezone-aware post-run buffer after review.

P1 G. Format validation is not truth validation: report parser verifies path, metadata, schema, HTTPS evidence strings and minimum body size. It does not prove the cited website exists, a tool actually ran, source freshness, consistency with Wix orders or completeness of cost fields. Add structured EvidenceFact fields (metric, value, unit, observation window, extracted_at, source_url, source_type, confidence and limitation). Assert synthetic/actual boundaries with tests.

P1 H. Business scorecard not closed: team-scorecard actuals is empty, and various output quotas are not impact metrics. Model end-to-end quality across order counts, revenue source reconciliations, conversion measurement coverage, SEO query-page opportunity, owner approvals and measured post-action outcomes. Numbers absent from validated sources must remain UNKNOWN, not zero.

P1 I. Error taxonomy and spend discipline: distinguish 409 provider unavailable, 401/403 authentication, 429 rate/limits, permissions/approval suspended, missing report, stale evidence and Slack send blocked. Retry only transient categories with bounded budget and idempotency; no retries to brute-force 409 or owner approval. Avoid daily jobs for a low-traffic store unless material exceptions occur.

P2 J. Current main branch protection not re-audited. Historical README stated main was unprotected at last observation; do not call it unprotected today without a fresh administrative check. Promote PR review and CI from convention to enforceable rule if appropriate.

## Preferred target architecture

Owner/approved source reads -> deterministic privacy, freshness, budget gate -> persisted unique cycle ledger -> native installed specialist API calls -> individual role-inbox Markdown + optional verified structured facts -> metadata/sha/source gate -> real installed Growth Manager Pilot -> Growth readback -> real Slack send -> independent Slack verification -> reviewed archive promotion -> next-week decision/outcome comparison.

The deterministic coordinator may validate and transfer artifacts but must never fabricate native specialist reports or send a message pretending to be Growth Pilot.

## Proposed work plan while API 409 support is pending

1. GitHub-only reliability sprint: agree on cycle states (NOT_STARTED, ACCEPTED, RUNNING, REPORT_VERIFIED, BLOCKED, APPROVAL_REQUIRED, SLACK_VERIFIED, ARCHIVED), design a checkpoint format and test interrupted-cycle replay with no live API.
2. Align current runbook, role-inbox staging paths, secret name, ownership and UTC/Israel scheduling semantics. Keep all owner decisions.
3. Add negative CI fixtures for duplicate role IDs, mismatched report metadata, fabricated SHA, blank evidence, wrong source date, missing historical KPI and duplicate Slack cycle.
4. Define deterministic weekly facts.json schema next to reports, with explicit UNKNOWN and source windows. Historical data is only baseline after validated read-only extraction.
5. Upon API unblock: prove ONE installed Data Agent can complete a synthetic, author-origin report with proper readback; then three specialists; then Growth + independent Slack permalink. Promote only after complete.
6. Later: 1 modest read-only production weekly run, then 3 measured recommendations maximum with owner approval. No publication/website edits without a separate, scoped authorized change process.

## Business opportunities, later stages

- Weekly Hebrew evidence cockpit: Wix order ledger (subject to verified coverage) + GA4 observed funnel (NOT revenue authority) + settled GSC windows + mobile/RTL website issues; no assumption that booth sales equal Wix sales.
- Material exception detector rather than a noisy daily digest: major verified category link defect, repeatable checkout data mismatch, absent shipping/COGS needed for contribution, significant settled GSC change. Require minimum comparable sample and supporting sources.
- Experiment registry: propose -> baseline -> review -> explicit owner approval -> separate implementation -> QA/rollback -> measure -> close. Keep GROW-SEO-01 HOLD.
- Later a read-only Slack question interface grounded in latest verified reports and run ledger. Not a priority before reporting and cost are proven.
- Keep four roles for now; do not expand to festival agent or ads agent until accessible evidence and business need justify it.

## Audit limits

This review checked the repository files through the connected GitHub integration and public technical/vendor documentation. No live Wix, GA4, GSC, installed agent execution, token scope, production Slack permissions, branch rulesets or payment plans were verified in this review. Competitive examples are illustrative architecture patterns, not proof of cost savings or efficacy for Shalom La Malka.
