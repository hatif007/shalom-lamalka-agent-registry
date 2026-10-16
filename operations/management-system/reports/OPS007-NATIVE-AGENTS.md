# OPS-007 — Native Workspace Agents E2E (not a ChatGPT Scheduled Task)

This workflow uses OpenAI's **Workspace Agent API Channels** to invoke the **already installed** agents, including the **Growth Manager Pilot**. No new OpenAI Platform agents are needed.

### Owner's one-time security setup

1. On each installed Workspace Agent (Data, SEO, Website Director V2, and **Growth Manager Pilot**), add and publish an API channel. Record its `agtch_...` API trigger ID. The Pilot ID must not be confused with the original Growth Manager ID.
2. In ChatGPT Business Admin > Access tokens, create a **Workspace Agents** scoped access token, for a principal authorized to run all four shared agents. Do not create an OpenAI Platform API key.
3. Store the token **only** in GitHub repository > Settings > Secrets and variables > Actions > New repository secret named `WORKSPACE_AGENTS_TOKEN`. Do not paste it in chat, an issue, or repository code. Restrict and rotate access appropriately.
4. Confirm each installed agent's actual Tool/Skill policy allows its exact report-only GitHub Writer branch/path. The existing Data Agent v2 may still prohibit GitHub writes; if so this test will stop instead of bypassing it. Also confirm the Growth Pilot's authorized Slack send behavior.
5. GitHub > Actions > **OPS-007 Native Workspace Agents E2E** > Run workflow. Supply the four actual API channel IDs. This workflow intentionally has **no recurring schedule** until the first native acceptance succeeds and the owner chooses a cadence.

### What the workflow proves

- Triggers three installed specialists using `POST https://api.chatgpt.com/v1/workspace_agents/{agtch_id}/trigger` with a unique cycle and an idempotency key.
- Uses the beta `agent_trigger_run_id` and GET run-status endpoint to confirm the runs finished. A 202 response by itself is insufficient.
- Checks a **new exact report** under the specialist's own pre-created GitHub inbox branch, validates `REPORT_ARCHIVE_V1`, role/date/cycle, `SYNTHETIC_TEST`, and Git blob SHA.
- **Only after all three pass**, triggers Growth Manager **Pilot**, passing the three verified GitHub URLs and SHAs.
- Growth should create its own detailed report under `report/inbox-growth` and send **one** Slack message with a real report link to `#business-insights`, if its installed tool policy authorizes sending.
- This coordinator verifies the Growth report in GitHub but **does not send Slack itself**. Independently inspect the Slack channel and retain the real message permalink to conclude `FULL_E2E_PASS`.
- Failure, missing API token, permission blocks or absent reports results in `BLOCKED`; no fabricated output, no substitutes and no override of agent permissions.

The test is synthetic, without Wix, GA4, GSC or production commercial data. `GROW-SEO-01=HOLD` persists. Promotion to canonical archive remains a **separate** reviewed flow in `promote-agent-inbox.yml`.

Reference: https://developers.openai.com/workspace-agents/trigger-runs
