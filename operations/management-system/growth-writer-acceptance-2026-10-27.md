# Growth Report Writer — backend acceptance specification

**State:** NOT IMPLEMENTED / NOT DEPLOYED in this proposal.

- Purpose-built authenticated `create_growth_report` equivalent; not generic GitHub write.
- Server-side fixed repo `hatif007/shalom-lamalka-agent-registry`, branch `report/inbox-growth`, role `growth`, new file `reports/runs/YYYY-MM-DD/growth/GROWTH-YYYYMMDD-<unique>.md`.
- Reject wrong role, branch, repo, path, duplicate ID, overwrite, missing owner authorization, unsupported run mode or payload, fake evidence and secrets.
- Explicit payload metadata: `FULL_GENERATED_REPORT` for approved production work. Synthetic tests must be separately authorized and classified `SYNTHETIC_TEST` regardless of `run_mode`.
- Verify server authorization is cycle-bound and consumed at most once; no retries after ambiguous or failed writes.
- Preserve exact `REPORT_ARCHIVE_V1` with source evidence and complete original Markdown body.
- Readback exact path, full body, URL, Git blob SHA; preserve commit SHA when provided.
- No site changes, customer data writes, code writes, PR creation or auto-merge.
- Independent checks needed for Workspace installed agent, schedule association, Slack send permissions and tool confirmation prompts.

The existing DATA Writer cannot substitute for this service. Do not enable generic GitHub writes to work around missing backend.
