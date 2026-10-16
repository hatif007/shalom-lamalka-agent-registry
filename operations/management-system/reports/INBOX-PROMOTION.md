# OPS-007 | Agent inbox to canonical archive

**Purpose:** resolve the GitHub Writer path restriction without broadening any installed agent's write permissions.

## Separate locations (both intentional)

- **Agent staging:** `report/inbox-ROLE:reports/runs/YYYY-MM-DD/ROLE/REPORT_ID.md`. The existing GitHub Writer allowlist permits each agent's ROLE path only.
- **Canonical archive:** `main:operations/management-system/reports/runs/YYYY-MM-DD/ROLE/REPORT_ID.md`. Only files promoted and merged here count as canonical.
- **Allowed roles:** data, seo, website, growth. Each role uses its own pre-existing inbox branch.

The workflow `.github/workflows/promote-agent-inbox.yml` is available by manual dispatch and a 30-minute schedule. It fetches the four existing inbox branches, validates paths and the REPORT_ARCHIVE_V1 header, and copies **identical bytes** into a dedicated archive branch. It never overwrites conflicting content and never merges automatically. It opens a reviewable pull request to `main` only if new valid reports exist. Each promotion is auditable using the workflow log's source branch, source commit, SHA-256, path and the PR diff. `scripts/validate_report_archive.py` continues to validate the canonical location.

**Permissions:** GitHub Actions requires repository settings allowing Actions to create PRs, with `contents:write` and `pull-requests:write`. If unavailable, record the permission blocker; do not bypass.

**Safety and provenance:** A `SYNTHETIC_TEST` remains synthetic after promotion. Neither copying bytes nor a GitHub commit proves installed-agent runtime. Do not invent `runtime_run_id`. The source report may contain untrusted content; promotion never executes it. A report copy does not authorize any Wix, GA4, GSC, price, inventory, order or customer changes.

**Important:** Promotion does **not** invoke Workspace Agents. Trigger the installed specialists through their own explicitly configured API Channels (or manually). Only after three fresh, independently evidenced reports should Growth Manager Pilot run and deliver a final Slack message via its own configured tool. Coordinator Slack messages must not impersonate Growth.

## Verification

Run `python -m unittest discover -s tests -p 'test_promote_agent_inbox.py'` and `python scripts/validate_report_archive.py`. Review the PR and confirm no automatic merge before treating a report as canonical.

**Existing smoke source:** `report/inbox-growth:reports/runs/2026-10-16/growth/OPS007-AUTONOMOUS-V4-2026-10-16.md` is a prior synthetic test suitable for a single staged-to-canonical acceptance check. It does not prove a complete four-agent E2E run.
