# Shalom La Malka — Agent Registry

**Status:** Registry v0.2 approved; repository structure committed; conformance remediation in progress
**Operating mode:** READ ONLY by default
**Specification:** `SPEC/agent-registry-spec-v0.2.md`
**Default branch:** `main` (do not update directly as part of this work)
**Working branch:** `fix/registry-v0.2-structure`

## Purpose
Central, structured record of agents, data sources, access boundaries, findings, experiments, approvals, and test evidence.

## Repository structure
- `agents/`: roles, constraints, sources, and validation status for the five agents
- `data-sources/`: source status, access notes, known limitations, and evidence gaps
- `registries/`: access matrix, approvals, tests, findings, and experiments
- `SPEC/`: approved Registry v0.2 specification

## Governance
- READ ONLY is the default.
- No external writes, website edits, publishing, pricing changes, integration changes, permission changes, agent deployment, or automation without explicit owner approval.
- Every check/test/sample must be logged to the appropriate Slack channel with the actual action, source/date range/volume, LIVE/SYNTHETIC/BLOCKED/NOT RUN status, results/limitations, whether changes were made, and a permalink.
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
- Registry conformance: remediation in progress; do not treat the registry as fully accepted until required fields and evidence gaps have been reviewed.
- GA4: `PARTIAL / UNRESOLVED`; realtime evidence does not establish historical reporting/API correctness.
- Festival sales: `UNAVAILABLE / DEFERRED` until reliable booth records are provided.

## Change boundary
This registry documents permissions and tests; it does not grant permissions. Website, integration, tracking, permission, deployment, and automation changes require separate explicit approval. Changes in this remediation are limited to the Git repository and the working branch; no merge to `main` is authorized by this note.
