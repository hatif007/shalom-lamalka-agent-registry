# WEBSITE-QA-001 — Wix Public Site Audit

Status: **pilot; no production claims until workflow evidence is reviewed**.

Read-only Playwright checks for four URLs on shalomlamalka.com, using desktop (1440x900) and mobile (375x812) Chromium viewports.

Run automatically on this feature branch after changes to the pilot files, or manually once the workflow is on the default branch. Results are uploaded as a GitHub Actions artifact for 14 days (JSON, Markdown, screenshots).

The script reads only public URLs and DOM. It does not log into Wix, change Wix settings, click buy buttons, add to carts, submit forms, or touch orders. It does not need Wix credentials or an OpenAI API key.

Interpretation: DNS errors, timeouts or browser launch failures mean UNKNOWN. A page rendering is not a certification of a correct category, accessible navigation, mobile menu or Hebrew RTL. Confirm screenshots and page identity manually before concluding PASS.

Implementation is original and uses Playwright, not copied from frontend-audit (its GitHub repository has no identified license). SiteProbe is deferred.

Do not merge into main or schedule periodic runs until owner approval and pilot review.
