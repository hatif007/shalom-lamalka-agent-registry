# Data Agent v2: connector-level security hardening and approval gate

**Status (2026-10-13): REFERENCE POLICY TESTED; NOT DEPLOYED INTO THE WORKSPACE AGENT RUNTIME.**  
**Agent:** `shalom-lamalka-data-analysis-v2`  
**Canonical skill:** `skills/data-agent/SKILL.md` v2.0  
**Owner-approved goal:** read-only Wix/GA4/GitHub, with precisely one task-authorized PII-free Slack report to `#sales-data` or `#agent-team`.

## Source of truth and evidence levels

1. **Behavioral policy:** The canonical Skill contains read-only and approved-Slack clauses. It is an instruction layer, NOT provider-enforced least privilege.
2. **Reference guard:** `security/data_agent_action_guard.py` is a fail-closed callable `allow(tool, args, trusted_context)` with synthetic allow/deny regression cases. CI runs the regression suite. It is *not called automatically* by ChatGPT's installed tool layer. It MUST NOT be represented as live connector enforcement.
3. **Actual platform configuration:** A Workspace Agent builder/admin must apply per-agent Action controls and Connector Action Constraints, and publish the updated agent version. Where action-level constraints cannot fully restrict input or arbitrary code, disable the broad action or replace it with a dedicated, independently hosted read-only MCP endpoint. Broad permissions on other agents/workspaces must not be changed as a shortcut.
4. **Provider credentials:** Provider-granted Wix/GA4/GitHub/Slack scopes are separate from ChatGPT action approvals. Verify the effective scopes with the provider/admin independently; do not infer scope limitations from a successful read, the Skill, or the current ChatGPT default `Allow low-risk actions`.

## Required per-agent action controls

| Source | Keep enabled for Data Agent | Disable or restrict |
| --- | --- | --- |
| Wix | Site-identity lookup; read-only product V3 query `POST /stores/v3/products/query`; read-only eCommerce orders search `POST /ecom/v1/orders/search`. Exact site ID `03b550bb-4ab1-4854-99b8-8bb153c4431e` | Arbitrary `ExecuteWixAPI`; site management; product/order/inventory/refund/cancellation writes. **Generic `CallWixSiteAPI` is mixed-capability.** Do not permit it without enforced method + URL + body constraints or a read-only provider token. |
| GA4 | `ping`, `get_account_summaries`, `run_report` limited to property `558438175` and permitted aggregate metrics | Analytics/property/settings and permission modifications; write actions not required |
| GitHub | Read-only `fetch_file` for `hatif007/shalom-lamalka-agent-registry`, `fix/registry-v0.2-structure`, `skills/data-agent/SKILL.md` | `create_file`, `update_file`, `delete_file`, commits/merges/PR mutations and arbitrary repo access |
| Slack | Read allowed channels; one `slack_send_message` to `C0C87EKC71R` or `C0C86D1C3D5` **only** after a fresh task-specific authorization to that destination. Prefer *Always ask* for message send. | All other channels/DMs, message edits/deletes/replies/schedules/channel settings. Verify actual send with message timestamp/permalink. |

**Slack exception:** Do not disable every write globally if the agent still needs approved Slack delivery. Use one narrow send action with approval and destination constraints. To enforce *one message per task* and prevent PII technically, a trusted mediator must maintain send counters and validate output/content outside the LLM. `pii_review_passed` in the reference code is merely a mediator-supplied assertion and NOT a complete PII detector.

## Preferred credential isolation

- **Wix:** use a dedicated app/API credential restricted to read-product V3 (`SCOPE.STORES.PRODUCT_READ`) and read-orders (`SCOPE.DC-STORES.READ-ORDERS`), plus other read-only catalog-discovery scopes only when required. **Do not** grant write, manager or wildcard scopes. Reconnection or separate app registration may be required; do not revoke the existing shared connection before a replacement successfully passes read-only smoke tests.
- **GA4:** restrict the agent connection to the necessary reporting property and read-only analytics roles. If the integration only exposes read actions, document that as a tool-surface limitation, not evidence that its provider principal cannot write elsewhere.
- **GitHub:** a read-only GitHub App installation or fine-grained token restricted to repository contents read and the named repository is preferable to a personal broad write-authorized connection. The orchestration administrator may keep separate repo-maintenance credentials.
- **Slack:** use a separate bot/agent principal limited to the required channels where feasible; Slack `chat:write` permits broad message-send API operations, so an independent channel/action constraint is necessary.

## Safe acceptance test plan (never run production mutations)

- Capture **builder screenshots/exported configuration** showing tool action availability, applicable Connector Action Constraints, approval settings, published version and effective app connection identity.
- Negative test **without invoking a mutating tool**: requests to change Wix/GA4, create GitHub commits, send without task approval, send twice, and send to `#business-insights` must be refused. Record *tool-call trace absent*, not just a textual refusal.
- Validate all positive reads: Wix products/orders query + cursor paging, GA4 property `558438175`; sample/coverage limits explicit.
- Independently inspect **provider scopes** and/or narrow connection permissions; test only supported safe read operations with replacement credentials.
- With a fresh explicit task authorization, send exactly one benign aggregate Slack report to one approved channel, check delivered message and permalink.
- Require evidence from the actual installed and *published* Workspace Agent. A different ChatGPT conversation using the same connectors is insufficient.
- Full enforcement PASS requires **deployed and verified** action limits or properly scoped read-only credentials, native negative-refusal evidence, and positive authorized reporting. If any control cannot be wired, record BLOCKED / PARTIAL PASS; do not suppress the gap.

## Current connected-app audit

At inspection on 2026-10-13, `Wix - Shalom La Malka`, `GitHub`, and `Slack` each inherited ChatGPT's `Allow low-risk actions`. This is an approval behavior, not a provider scope restriction and not a per-Workspace-Agent action allowlist. There is no connected tool in this orchestrator chat to inspect or edit the installed agent's builder action controls, nor to change its existing provider OAuth grants without reauthorization.

## CI coverage

`.github/workflows/registry-validation.yml` runs `python security/data_agent_action_guard.py` to assert a small allowlist and deny simulated unsafe calls. The test sends **zero live mutations, zero Slack messages, and no access tokens**. A green CI run is not proof of deployed connector enforcement.

## Relevant official documentation

- https://help.openai.com/en/articles/20001143/ (Workspace Agent actions, write approval, Connector Action Constraints)
- https://help.openai.com/en/articles/11509118-admin-controls-security-and-compliance-for-plugins-and-apps (workspace Action controls vs Permissions)
- https://dev.wix.com/docs/overview/auth-permissions/permissions (Wix permission scopes and roles)
- https://dev.wix.com/docs/build-apps/develop-your-app/auth/permissions/configure-permissions-for-your-app (Wix app requested scopes)
- https://docs.slack.dev/reference/scopes/chat.write (Slack send/write scope)
