# Shalom La Malka — Agent Registry

**Status:** Registry v0.2 merged to `main` via owner-approved PR #1 on 2026-10-13; main CI passed. Full Agent Builder cutover and repository branch protection remain separate gates.
**Operating mode:** READ ONLY by default
**Specification:** `SPEC/agent-registry-spec-v0.2.md`
**Default/canonical repository branch:** `main` (Registry v0.2 structure; commit `7a4b02d929af2385e5aad62d2904ca387123206a` at cutover)
**Historical preparation branch:** `fix/registry-v0.2-structure` (retained for compatibility and rollback; do not use for new canonical references)

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
- Repository layout: consolidated in `main` via [PR #1](https://github.com/hatif007/shalom-lamalka-agent-registry/pull/1); previously staged in a separate working branch.
- JSON syntax: all nine JSON files under `data-sources/` and `registries/` passed a local PowerShell parse check on 2026-10-12. This verifies syntax only, not semantic completeness.
- Registry automated schema consistency: [main push CI passed](https://github.com/hatif007/shalom-lamalka-agent-registry/actions/runs/38435947216), including reference guard synthetic tests. This does NOT prove live connector OAuth scopes, deployed agent runtime isolation or end-to-end data coverage.
- GA4: historical Registry source-status flag remains `PARTIAL_UNRESOLVED` pending deliberate evidence reconciliation; later scoped live GA4 reporting was observed but does not by itself prove every integration or conversion event works.
- Festival sales: `UNAVAILABLE / DEFERRED` until reliable booth records are provided.

## Change boundary
This registry documents permissions and tests; it does not grant permissions. Website, integration, tracking, permission, deployment, and automation changes require separate explicit approval. Changes in this remediation are limited to the Git repository and the working branch; no merge to `main` is authorized by this note.


## Slack reporting channels
- **Outcome summary:** [#growth-outcomes](https://shalomlamalka.slack.com/archives/C0C8GDL7H0S). Post only concise, material outcomes and evidence-backed insights. Format: `YYYY-MM-DD | Agent/domain | Report/change | Outcome | Link`.
- **Technical evidence and test log:** [#agent-registry](https://shalomlamalka.slack.com/archives/C0C8E1RMD8S). Record test scope, source/date range/volume, LIVE/SYNTHETIC/BLOCKED/NOT RUN, results, limitations, changes made, and permalink.
- Clearly distinguish recommendations from changes actually made and measured outcomes. Never claim impact that has not been measured. If there is no material result, do not post a summary just to create activity.
- Creating the outcome channel does not itself configure automatic delivery. End-to-end Slack reporting must be tested before it is described as automated.

## Canonical main synchronization (completed 2026-10-13)

- **Merge:** [PR #1](https://github.com/hatif007/shalom-lamalka-agent-registry/pull/1), merge commit `7a4b02d929af2385e5aad62d2904ca387123206a`, owner-authorized; root-level historical layout replaced with `registries/`, `agents/`, `skills/`, `operations/`, `data-sources/`.
- **Validation:** [main push GitHub Actions success](https://github.com/hatif007/shalom-lamalka-agent-registry/actions/runs/38435947216) — registry metadata and synthetic guard only.
- **Canonical source:** `main`. Older `fix/registry-v0.2-structure` references in dated reports are historical; update each **installed** Agent Builder instance to use `main` only with separately approved runtime changes.
- **Fourth role:** Shalom La Malka — Website & Conversion Agent. Owner reports a created instance with a v1.1 **draft** and public web read-only review; canonical repository Skill remains **v1.0**. Do NOT replace the runtime draft v1.1 with GitHub v1.0 without reconciling the actual package.
- **Unfinished governance:** `main` still unprotected and no rulesets were observed; admin must configure required PR/check reviews. The GitHub connector used here does not expose that settings-write action.
- **Integrity:** A checked PR patch showed no obvious credential/token/private key patterns; it is **not** a comprehensive secret scan or a guarantee about full Git history.
- **Non-goals:** no Wix edits, no Slack posts, no Agent Builder changes, no OAuth scope changes, no claim that agent-to-agent task dispatch is activated.

See [main cutover audit/runbook](operations/github-main-sync-readiness-2026-10-13.md) for historic diff and remaining action gates.

## Unified Growth management system (2026-10-13)

**Growth Manager is the conductor of all five roles.** The [Operations Management System](operations/management-system/README.md) holds the [Operating Calendar](operations/management-system/operating-calendar.json), [Team Scorecard](operations/management-system/team-scorecard.json), and [Task Board](operations/management-system/task-board.json). These are the source-of-truth for *proposed* daily/weekly/monthly cadences and targets, independently from installed agent execution.

New dedicated Slack channel: [#website-conversion-agent](https://shalomlamalka.slack.com/archives/C0C91GU8M3N), created with a human-authorized introduction; the legacy #content-conversion remains available. No installed-agent Slack sending is enabled by creating this channel. Only the separate ChatGPT Data & SEO weekly tasks are currently scheduled; no scheduled native custom-agent meeting is claimed. **Owner-approved official work windows (Asia/Jerusalem):** Sunday 22:30 Website (manual, not automated), Monday ~08:00 Data (existing scheduled ChatGPT task), Monday ~10:00 SEO (existing scheduled ChatGPT task), Monday 12:00 Growth Manager (manual, not automated). First Monday 12:00 doubles as monthly review; no daily automated runs. See the calendar for execution states and quota-aware rules.
