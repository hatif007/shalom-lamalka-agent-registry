# SHALOM LA MALKA --- Agent Registry Specification

**Version:** 0.2\
**Status:** Owner-approved v0.2; implementation exists on the working branch; conformance remediation in progress\
**Date:** 2026-10-11\
**Operating mode:** READ ONLY by default

## 1. Purpose

Define the central registry for the Shalom La Malka agent system. The
registry documents agents, permitted data sources, evidence-backed
findings, experiments, approvals, and tests without duplicating
day-to-day discussion in `#growth-manager`.

This specification defines the registry requirements. The GitHub registry structure has been committed to the approved working branch; acceptance and semantic completeness are still under remediation. This does not mean all integrations or agent-level permissions have been configured.

## 2. Agent Registry

For each agent, record: name and purpose; responsibilities and
exclusions; status; approved sources; access mode and permitted
data/fields; prohibited actions; acceptance-test status and last
verification date; related findings and Slack links.

### Current agents

  -----------------------------------------------------------------------
  Agent             Responsibility    Sources           Current status /
                                                        constraints
  ----------------- ----------------- ----------------- -----------------
  Growth Manager    Consolidate       Verified findings Separate facts
                    evidence,         from other        from hypotheses;
                    prioritize        agents; Wix, GSC, no external
                    opportunities,    GA4 where         writes without
                    prepare growth    available         explicit approval
                    reports                             

  Data Agent        Analyze orders,   Wix Stores /      Read-only; note
                    products, sales,  Orders / Products API coverage and
                    and data quality                    order-status
                                                        exclusions; avoid
                                                        unnecessary
                                                        customer personal
                                                        data

  SEO Agent         Analyze search    Google Search     Read-only;
                    queries, pages,   Console           document date
                    clicks,                             range and data
                    impressions, CTR,                   freshness
                    and position                        

  Content &         Review product    Public            Recommendations
  Conversion Agent  pages, content,   website/content   only; no site
                    and purchase      and verified      edits or
                    journey; propose  analytics where   publishing
                    CRO experiments   available         
                    and draft copy                      

  Festival Sales    Analyze           Reliable festival Deferred until
  Agent             booth/festival    sales/cost        reliable data
                    sales and costs   records, when     exists; never
                                      available         infer festival
                                                        sales from Wix
                                                        website data
  -----------------------------------------------------------------------

## 3. Data Sources

For every source, record the system/property identifier, account owner
without exposing secrets, connection status and last verification date,
access scopes, available data types, queried date range,
freshness/processing delay, API limitations/exclusions, validation
evidence, Slack link, and status: VERIFIED, PARTIAL, BLOCKED, NOT
TESTED, or UNAVAILABLE.

  ---------------------------------------------------------------------------
  Source                  Current evidence            Status
  ----------------------- --------------------------- -----------------------
  Wix Stores / Orders /   Read-only sampling returned PARTIAL
  Products                one paid web order in the   
                          tested 30-day query. API    
                          search defaults and         
                          UTC/local date-boundary     
                          limitations were noted;     
                          this is not a complete      
                          sales ledger.               

  Google Search Console   Live                        VERIFIED for tested
                          queries/pages/performance   reads
                          data were read              
                          successfully. Record date   
                          range and settled-data      
                          limitations with each       
                          report.                     

  Google Analytics 4      Realtime screenshots show   PARTIAL / UNRESOLVED
                          `page_view`, `view_item`,   
                          `add_to_cart`, and          
                          `begin_checkout`. Wix       
                          measurement ID              
                          `G-FZGZG036SL` matches the  
                          GA4 stream shown. GSC       
                          Wizard API reports still    
                          return zero rows for        
                          queried ranges.             

  Festival booth sales    No reliable source          UNAVAILABLE / DEFERRED
                          currently available in this 
                          workflow.                   
  ---------------------------------------------------------------------------

## 4. Agent-to-Source Access Matrix

Maintain one row per agent/source pairing. A connection does not prove
every agent has direct access.

Required fields: agent; source; permitted purpose; access mode (READ
ONLY by default); permitted data/fields; prohibited data/actions;
connection/authorization status; last verified date; test result and
evidence link; known limitations.

  --------------------------------------------------------------------------------------------
  Agent          Wix                   GSC                  GA4                 Festival
                                                                                records
  -------------- --------------------- -------------------- ------------------- --------------
  Growth Manager Use verified          Use verified         Use only when       No inference
                 summaries/findings;   summaries/findings   reports are         without source
                 no writes                                  readable; note      records
                                                            discrepancy         

  Data Agent     Read orders/products  Not primary          Read only after     Deferred
                 within connector                           connection/report   
                 coverage                                   validation          

  SEO Agent      No write access       Read-only analysis   Optional context    Not applicable
                                                            only after          
                                                            validation          

  Content &      Public page/product   Optional             Use only validated  Not applicable
  Conversion     review; no edits      search-intent        analytics; no site  
  Agent                                context              changes             

  Festival Sales Do not infer booth    Not primary          Not primary         Blocked until
  Agent          sales from Wix                                                 reliable
                                                                                records exist
  --------------------------------------------------------------------------------------------

This matrix is a planning baseline, not a claim that every listed
permission has been technically configured or verified.

## 5. Findings Register

Each finding must include: unique ID; statement; classification (FACT,
HYPOTHESIS, RECOMMENDATION, UNKNOWN); evidence/source; date range and
extraction timestamp; freshness caveat; metric definition/calculation;
confidence and rationale; limitations/alternative explanations; business
impact and next step; owner/status and Slack link.

Never present a hypothesis as a proven cause or outcome. Do not combine
metrics from different date ranges as if comparable.

## 6. Experiments Register

For each experiment, record: ID and business question; hypothesis;
target audience/page/product; primary success metric and guardrails;
baseline/source/date range; proposed intervention and exact change
requested; required owner approval; start/end dates and evaluation
method; result/caveats/decision.

No experiment that changes the website, pricing, tracking, integrations,
or customer-facing content may be executed without explicit approval.

## 7. Approval Log

Record approval ID; requested action and purpose; exact scope; approver
and timestamp; systems/data affected; conditions/expiration; execution
status and evidence; deviation or rollback. Approval to plan or draft is
not approval to implement; never expand approval to unrelated changes.

## 8. Test Log and reporting rules

Every agent check, test, or sample must be documented in
`#growth-manager` or the appropriate project channel, with a reference
from the registry.

Required fields: test ID and operator; status LIVE, SYNTHETIC, BLOCKED,
or NOT RUN; purpose/source; date range and sample size; steps actually
performed; results/evidence; limitations/unresolved issues; whether
changes were made (default: no); Slack permalink.

Never claim a test ran when it did not. Separate synthetic acceptance
tests from live checks. Do not claim an agent autonomously posted a
report when a connected Slack tool was used.

## 9. Evidence & Data Freshness

Every finding and test must carry: source type (LIVE / SYNTHETIC /
MANUAL_SCREENSHOT / OTHER); observed timestamp; data start/end dates;
freshness status (CURRENT / SETTLING / STALE / UNKNOWN);
processing-delay note; confidence (HIGH / MEDIUM / LOW); limitations;
evidence link.

Realtime evidence does not prove standard reports or connector APIs are
working. A zero-row report means the query returned no rows for that
scope/range; it does not automatically prove no traffic or events
occurred.

## 10. Governance and safety

-   READ ONLY is the default.
-   No website edits, publishing, pricing changes, tracking changes,
    API-key creation, permission changes, or agent-instruction changes
    without explicit owner approval.
-   Do not expose customer PII unless necessary for an approved purpose.
-   Do not infer festival/booth sales from website data.
-   Report missing data and limitations rather than inventing values.
-   Keep detailed tests in the appropriate project channel and important
    summaries/decisions in `#growth-manager`.
-   Use `#agent-registry` for registry structure, ownership, source
    access, evidence standards, and specification changes.

## 11. Open issue: GA4 reporting discrepancy

Evidence observed: - GA4 Realtime screenshots showed `page_view`,
`view_item`, `add_to_cart`, and `begin_checkout`. - Wix Google Tag field
showed measurement ID `G-FZGZG036SL`, matching the GA4 stream. - GSC
Wizard GA4 API overview and event/date queries returned zero values/rows
for queried ranges, including 2026-09-11 through 2026-10-08 and a query
for 2026-10-11.

Interpretation: - Basic event collection in Realtime was observed. -
Historical reporting and connector/API access have not been verified as
working. - Do not mark GA4 fully verified until the discrepancy is
resolved.

## 12. Acceptance criteria

-   [ ] All five agents have clear responsibilities, constraints, and
    status.
-   [ ] Each agent/source pairing is documented in the access matrix.
-   [ ] Source status and data freshness are explicit.
-   [ ] Findings distinguish fact, hypothesis, recommendation, and
    unknown.
-   [ ] Every test has a test log and Slack evidence link.
-   [ ] Approval scope is explicit and does not imply broader
    authorization.
-   [ ] Read-only and privacy boundaries are recorded.
-   [ ] Festival sales remain deferred until reliable data is available.
-   [ ] GA4 remains PARTIAL / UNRESOLVED until the reporting discrepancy
    is resolved.

## 13. Implementation boundary

The registry files are maintained in the private GitHub repository. The current remediation changes documentation and registry records on `fix/registry-v0.2-structure` only. No database, external automation, connector permissions, agent deployment, or website settings are changed by this specification.

**Next step:** complete semantic validation of the registries and source metadata, review the resulting diff, then request owner approval before any merge to `main`. The owner has approved repository changes on the working branch; that approval does not authorize merging or external-system changes.
