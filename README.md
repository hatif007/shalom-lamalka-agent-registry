# Shalom La Malka — Agent Registry

**Status:** Initial registry package prepared for owner upload  
**Operating mode:** READ ONLY by default  
**Specification:** `SPEC/agent-registry-spec-v0.2.md`

## Purpose
Central, structured record of agents, data sources, access boundaries, findings, experiments, approvals, and test evidence.

## Governance
- No external writes, site edits, integrations, permission changes, agent deployment, or automation without explicit owner approval.
- Every check/test/sample must be logged to Slack with the actual action, source/date range/volume, LIVE/SYNTHETIC/BLOCKED/NOT RUN status, results/limitations, and whether any changes were made.
- Never present synthetic data as live evidence.
- Separate confirmed facts, hypotheses, recommendations, and unknowns.
- Do not store unnecessary customer personal data.
- Festival booth sales are not inferred from Wix website sales.

## Folder guide
- `agents/`: roles and constraints
- `data-sources/`: availability and access notes
- `registries/`: structured records for findings, experiments, approvals, and test logs
- `SPEC/`: approved v0.2 specification

## Current implementation status
This package is prepared for manual upload. It has not been uploaded to GitHub by ChatGPT, and no repository settings or external systems have been changed.
