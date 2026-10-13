# Shalom La Malka — Agent Registry

**Status:** Registry v0.2 structure and schema checks passing on working branch; proposed main-branch synchronization awaiting owner approval
**Operating mode:** READ ONLY by default
**Specification:** `SPEC/agent-registry-spec-v0.2.md`
**Default branch:** `main` (currently legacy layout; no direct writes or merge without separate owner approval)
**Working branch:** `fix/registry-v0.2-structure`

## Purpose
Central, structured record of agents, data sources, access boundaries, findings, experiments, approvals, and test evidence.

## Repository structure
- `agents/`: five planned business roles and their constraints; installed Workspace Agent status must be confirmed separately
- `data-sources/`: source status, access notes, known limitations, and evidence gaps
- `registries/`: access matrix, approvals, tests, findings, and experiments
- `SPEC/`: approved Registry v0.2 specification

## Governance
- READ ONLY is the default.
- No external writes, website edits, publishing, pricing changes, integration changes, permission changes, agent deployment, or automation without explicit owner approval.
- Record each material check/test/sample in the appropriate Registry record with actual action, scope, evidence, freshness, LIVE/SYNTHETIC/BLOCKED/NOT RUN status, and side effects. Slack reporting is allowed **only where separately authorized for that agent/task**; do not assume a universal right to send Slack.
- Never present synthetic data as live evidence.
- Separate confirmed facts, hypotheses, recommendations, and unknowns.
- Do not store unnecessary customer personal data.
- Festival booth sales are not inferred from Wix website sales.
- A connected repository or API does not prove every agent has direct access to it.

## Evidence and freshness
Source statuses and access claims must be limited to tested scope. Include the observation timestamp, queried date range, data freshness/processing delay, test outcome, limitations, and evidence link where known. Use `UNKNOWN` or `NOT_RECORDED` rather than inventing missing metadata.

## Current validation status
- Repository layout: organized and committed on the working branch.
- JSON syntax: all nine JSON files under `data-sources/` and `registries/` passed a local PowerShell parse check on 2026-10-12. This verifies syntax only, not semantic completeness.
- Registry automated schema consistency: GitHub Actions success on the working branch; this is not proof that all live agent tool constraints, business integrations or provider permissions have been verified.
- GA4: historical Registry source-status flag remains `PARTIAL_UNRESOLVED` pending deliberate evidence reconciliation; later scoped live GA4 reporting was observed but does not by itself prove every integration or conversion event works.
- Festival sales: `UNAVAILABLE / DEFERRED` until reliable booth records are provided.

## Change boundary
This registry documents permissions and tests; it does not grant permissions. Website, integration, tracking, permission, deployment, and automation changes require separate explicit approval. Changes in this remediation are limited to the Git repository and the working branch; no merge to `main` is authorized by this note.


## Slack reporting channels
- **Outcome summary:** [#growth-outcomes](https://shalomlamalka.slack.com/archives/C0C8GDL7H0S). Post only concise, material outcomes and evidence-backed insights. Format: `YYYY-MM-DD | Agent/domain | Report/change | Outcome | Link`.
- **Technical evidence and test log:** [#agent-registry](https://shalomlamalka.slack.com/archives/C0C8E1RMD8S). Record test scope, source/date range/volume, LIVE/SYNTHETIC/BLOCKED/NOT RUN, results, limitations, changes made, and permalink.
- Clearly distinguish recommendations from changes actually made and measured outcomes. Never claim impact that has not been measured. If there is no material result, do not post a summary just to create activity.
- Creating the outcome channel does not itself configure automatic delivery. End-to-end Slack reporting must be tested before it is described as automated.

## Main synchronization (prepared 2026-10-13)

The current `main` default branch still contains the old root-level registry layout, and does **not** contain the working-branch Skills, Operations or full registries. An owner-reviewed PR is required before `main` can become the canonical operational source for agents. See [the audited migration plan](operations/github-main-sync-readiness-2026-10-13.md). No merge is authorized by this note.

**Future canonical locations after an approved merge:** `registries/tests.json`, `registries/findings.json`, `registries/access-matrix.json`, `skills/*/SKILL.md`, `operations/*.md`. Before then, specify the working branch `fix/registry-v0.2-structure` explicitly when reading these files.

**Fourth role:** `Shalom La Malka — Website & Conversion Agent` (renamed from Content & Conversion Agent). GitHub skill `skills/website-conversion-agent/SKILL.md` still represents repository v1.0; the user reports that the separately installed runtime produced a v1.1 **draft**, not yet independently checked for repository or publication parity. Never overwrite installed v1.1 with v1.0 merely because the GitHub ref is available.

**Security:** The local Python reference action guard and GitHub CI demonstrate synthetic cases only. They do not automatically intercept live agent calls or enforce provider OAuth scopes. Also, GitHub branch protection/rulesets are not currently observed as enabled; enable reviewed PR/check requirements before operational reliance on main.
