# Shalom La Malka — GitHub Main Synchronization Readiness

**Prepared:** 2026-10-13, Asia/Jerusalem
**Purpose:** Make the Registry easy for all agents to resolve from ONE stable source-of-truth branch, without changing live agents, Wix, analytics or Slack.
**Historic planning decision:** This document was prepared before the owner authorized the merge. **Current status as of 2026-10-13:** PR #1 owner-authorized and merged; `main` now contains the v0.2 structure. GitHub branch protection and independently published Agent Builder ref cutover remain pending.
**Repository:** https://github.com/hatif007/shalom-lamalka-agent-registry
**Base/default:** `main`; **proposed head:** `fix/registry-v0.2-structure`.
**Observed snapshot (2026-10-13):** `main` `cf2275f9bf579ee63b08b3b9f4c967f8d914c0fd`, working branch `cd09309b203ed7345293964eda1f29b868dd9559`. Those are the **audit snapshot** SHAs, not an immutable proposed PR head (later prep commits change it).

## 1 — Evidence: what the audit verified

1. `main` is the repository default branch. Both branches exist, neither is reported protected by the GitHub branch list; the repo's rulesets list was empty when queried. Lack of required review/check enforcement is a deployment/governance concern, not an invitation to push to main.
2. Comparison `main...fix/registry-v0.2-structure` returned **ahead 103, behind 0, 47 changed paths**, common merge base `cf2275f9...`. Therefore a fast-forward ancestry is available at the audit snapshot; this does NOT mean every schema/operational claim is complete or all historic file moves are semantically identical.
3. GitHub tree listing: 18 entries on original main (including root-level JSON) versus 50 entries on working branch (34 files; remaining entries directories). The compare lists added `agents/`, `registries/`, `skills/`, `operations/`, `data-sources/`, scripts and GitHub Actions, with root-level files moved/removed.
4. `main` has only three `tests.json` entries (T-001..T-003) and four `findings.json` entries (F-001..F-004), while the working branch holds T-001..T-022 and F-001..F-009; access matrix has 7 vs 20 rows; approvals have 2 vs 2. These are counts/ID comparisons, not exhaustive field-by-field migrations.
5. Working-branch Registry validation workflow's latest run before these preparations: **SUCCESS** on `cd09309...` at https://github.com/hatif007/shalom-lamalka-agent-registry/actions/runs/38429438724. CI checks JSON/schema consistency and a *synthetic reference* action guard; it does not attest installed-agent runtime or provider-level OAuth enforcement.
6. No open pull requests were returned at the first audit, and the working-branch workflow initially had `push` only for `fix/registry-v0.2-structure`, plus `pull_request` to `main`. The sync-preparation change adds `main` to `push` validation; verify its own CI and PR CI.
7. Existing Growth Manager report said files were absent because its visible ref was `main` or another older copy, where the new path did not exist. The files **do** exist at their explicit paths on `fix/registry-v0.2-structure`.

## 2 — Compatibility map: OLD main -> PROPOSED main after merge

| Old `main` path | Canonical path after reviewed merge |
| --- | --- |
| `tests.json` | `registries/tests.json` |
| `findings.json` | `registries/findings.json` |
| `approvals.json` | `registries/approvals.json` |
| `experiments.json` | `registries/experiments.json` |
| `access-matrix.json` | `registries/access-matrix.json` |
| `data-agent.md` | `agents/data-agent.md` |
| `growth-manager.md` | `agents/growth-manager.md` |
| `seo-agent.md` | `agents/seo-agent.md` |
| `content-conversion-agent.md` | `agents/website-conversion-agent.md` (renamed fourth role; legacy `agents/content-conversion-agent.md` points to it) |
| `festival-sales-agent.md` | `agents/festival-sales-agent.md` |
| `agent-registry-spec-v0.2.md` | `SPEC/agent-registry-spec-v0.2.md` |
| `wix.json` etc. | `data-sources/wix.json` etc. |

The old root-level `data-sources` *file* is replaced by the `data-sources/` *directory*. Existing links, Builder Knowledge connections or scripts that use older paths **will require reconfiguration**. Preserve history; do not delete the working branch on cutover day.

## 3 — Pre-merge safety gates (PR review)

- [x] Ancestry/compare and tree shape checked at the initial snapshot; behind=0 and no diverged `main` commits.
- [x] Working-branch CI previously passed on `cd09309...` (pre-preparation commit).
- [x] Existing registry records and source-scope boundaries audited for the planned structural migration; no mutation of Wix, GA4, Slack or installed agents.
- [ ] Check **latest** branch head and PR diff, including renames/deletions and any new commits. Re-run compare; if `main` changes, re-evaluate conflicts.
- [ ] PR CI succeeds for the **final proposed head**, with Registry validation and reference-guard synthetic tests.
- [ ] Review that the **public repository** contains no customer PII, keys, secrets, sensitive messages, private connection URLs or dangerous writes (no comprehensive secrets scan was performed during this audit).
- [ ] Confirm `README.md` links, JSON IDs and canonical role naming. Historical `SPEC` has the older role name in its 2026-10-11 approved v0.2 table; the canonical renamed role is described in `agents/website-conversion-agent.md`.
- [ ] Configure **branch protection/ruleset for `main`**: require PR/review and passing `Validate registry structure and required fields` check, no force push/delete. This is a **recommended administrative action**, not already enforced. Exact available options and check contexts need to be verified in the GitHub UI.
- [ ] Explicit owner approval before any merge to `main`.

## 4 — Agent/runtime cutover after a separately approved merge

1. Verify `main` contains `skills/`, `agents/`, `registries/`, `operations/`, `data-sources/`, scripts and workflow; `main` Push CI must pass.
2. Replace **hard-coded references** in the relevant Workspace Agent Skills/knowledge connections from `fix/registry-v0.2-structure` to `main`, but only via a separately reviewed Agent Builder update. Do not assert the Git merge automatically changes runtime agent configuration.
3. Validate with one safe **native read** from each active agent: Growth Manager retrieves handoff path, SEO retrieves weekly playbook, Data Agent reads canonical skill, Website Agent reads its P1 brief. Report which ref/path was used, without side effects.
4. Do not open up permissions while switching Git refs. Each agent's per-action constraints and approval requirements stay unchanged.
5. **Important drift:** GitHub `skills/website-conversion-agent/SKILL.md` describes v1.0. Owner reports the independently installed Website Agent prepared a separate **v1.1 draft** and removed its Wix/GitHub/Slack connectors. That runtime draft is **not proven to be committed to GitHub or published**. Do NOT overwrite its Skill with the repository v1.0; collect the actual v1.1 package and reconcile under a separately approved Skill update.
6. Registry's agent creation/acceptance metadata may lag owner-observed installed runtime. Update only with explicitly labeled owner-reported evidence; never convert a self-report into independent backend proof.
7. Keep 7-day read-only monitoring after cutover and retain the previous head SHA for normal `git revert` or corrective PR if necessary. No force push.

## 5 — Proposed branch strategy once cutover is fully approved

- Make `main` the **single operational source of truth** for approved policy/role definitions and owner-reviewed findings.
- Use short-lived topic branches plus PRs for modifications. `fix/registry-v0.2-structure` remains temporarily as reference; retire only after all live agents read `main` and owner approves cleanup.
- Use required CI and owner review for `skills/`, `registries/`, `operations/`, `security/` changes. Registry commits do not grant Workspace Agent tools or OAuth privileges.
- For urgent runtime corrections, publish Agent Builder changes separately from repository PRs, then record which deployed Skill/config revision was actually observed.

## 6 — Read-only verification checklist after merge (NOT RUN)

- [ ] Confirm root `README.md` is current and points to canonical files.
- [ ] Query `main` for `registries/tests.json` (T-022) and `registries/findings.json` (F-009).
- [ ] Confirm `main` Push CI success, not just working-branch CI success.
- [ ] Ask installed Growth Manager to read `operations/growth-seo-handoff-2026-10-13.md` on `main`; no edits/Slack.
- [ ] Ask Website Agent to read its current deployed Skill **without replacing** the reported v1.1 draft.
- [ ] Record final cutover status `PASSED` / `PARTIAL` / `BLOCKED`; explain all remaining provider-level permission issues.

**No `main` writes, PR merges, default-branch switches, runtime agent updates, Wix/GA4 writes, or Slack messages were authorized/performed by preparing this report.**

## 7 — Post-merge verification update (2026-10-13)

- **Owner approval:** Given in this session to complete the GitHub consolidation.
- **PR:** [#1](https://github.com/hatif007/shalom-lamalka-agent-registry/pull/1), merged; SHA `7a4b02d929af2385e5aad62d2904ca387123206a`.
- **Read from main:** independently fetched `README.md`, `registries/tests.json` (T-001..T-022, 22 records), `registries/findings.json` (F-001..F-009, 9 records), `operations/growth-seo-handoff-2026-10-13.md`, `skills/website-conversion-agent/SKILL.md`, and `.github/workflows/registry-validation.yml`.
- **CI:** [main push workflow](https://github.com/hatif007/shalom-lamalka-agent-registry/actions/runs/38435947216) succeeded after merge; PR workflow succeeded before merge. These are metadata/reference tests, not full runtime security certification.
- **Agent Builder cutover:** NOT RUN (separate installed agents; user reports daily agent quota exhausted). Do not imply the GitHub merge updates runtime agent skill references.
- **Security:** Public repository patch scanned for obvious token/private-key/email/phone patterns. Matches were synthetic emails or numeric Slack message IDs; this does not constitute a full Git-history or dedicated secret scan.
- **Branch protection:** NOT CONFIGURED. A GitHub settings action to enforce a ruleset is not provided in this connection; requires repository admin UI (Settings > Rules > Rulesets, or Branches protection) and follow-up verification.
- **Website Skill mismatch:** GitHub v1.0 remains unchanged; owner-reported installed v1.1 draft remains its own artifact, not overwritten by this merge. Reconcile by obtaining the actual v1.1 package when the user next works with Agent Builder.
- **Outcome:** GITHUB_MAIN_STRUCTURE_AND_CI_PASS; FULL_AGENT_RUNTIME_REF_CUTOVER_AND_BRANCH_PROTECTION_PENDING.

This updated record supersedes only the pre-merge authorization and post-merge unchecked items above. It does not retroactively rewrite what was true during the original readiness audit.
