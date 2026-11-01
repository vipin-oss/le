# Blockers and limits — checkpoint 2026-10-28 (UTC)

Items that stop or limit completion. Each has the action needed to unblock it.

| # | Blocker or limit | Effect | Action needed |
| --- | --- | --- | --- |
| B1 | Session branch and handoff branch differ. The handoff named `arena/b5e608f8-le`; this session is bound to `arena/36bc8cc8-le`. | Prior work was brought onto this branch by a fast-forward of `arena/b5e608f8-le` (`cae4c11`). Nothing was pushed to `arena/b5e608f8-le`. | Author confirms which branch is the record of truth. |
| B2 | Private source library (Drive): partial re-copy only. The connector truncates the middle of large results, so the full 118-row `SOURCE_LEDGER.csv` cannot be read in one call. | Patched 7 visible rows and added 2 (Eringen1968b, Mindlin1974) in `SOURCE_LEDGER.csv` on 2026-10-28. Corrections: Barak2023 family to VERIFIED; Eringen1966a and Green1991-GN-I to VERIFIED; Ezzat2011 changed from VERIFIED to FOUND-DOI-MISMATCH (library copy is a different paper); Eringen1968b added as DOI-MISMATCH. Middle rows of the Drive ledger are unchecked, so the repo copy may still differ. The Eq. 4.17 source conflict and the Chen–Gurtin, Hetnarski, and Gorenflo sources are still unchecked. | Re-read the Drive ledger in chunks if the connector offers paging, or have the author export the sanitized CSV into the repo. |
| B3 | Crossref API was not reachable from the bash sandbox (connection refused). The fetch tool reaches it. | Crossref checks must use the fetch tool and be recorded with their output. | Use the fetch tool for Crossref; record results in `phase5/reports/`. |
| B4 | The CI job logs could not be downloaded (results-service EOF). | Gate counts from logs (overfull boxes, near-overfull) are not repeated here. The PDF text was checked directly. | Re-check the logs from the Actions page, or rely on the published output PDF. |
| B5 | Final-size visual review of the rebuilt PDF was not performed for the new text. | R1.5 (table overrun) stays open. | Render the affected table pages and review at print size. |
| B6 | Missing primary sources (6 records in `MISSING_SOURCES.csv`). | Statements that depend on them are limitations, not facts. | Obtain the texts or keep the limitation statements. |
| B7 | Vernotte (1958) and Cattaneo (1948) were checked only against two secondary citations. | Their pages are corrected in the bibliography but not confirmed on the original. | Author checks the original or accepts the secondary check (`BIB_CHECK_2026-10-28.md`). |
| B8 | Journal policies (data, AI use, conflicts, funding, reference style) were not read. | The journal drafts are not submission-ready. | Author reads the chosen journal's policies and fills the placeholders. |
| B9 | Ledger `old_text_short` fields are paraphrases, so a verbatim anchor match is not a reliable staleness test. | Some `tex_file:line` anchors may point to moved text (WP6-20). | Manual anchor review, row by row, in WP8. |
| B10 | Equation audit: 98 displays remain CONDITIONAL (52 newly inventoried, 46 original). | WP4 is not complete. | Derive or source-check each row; record scope. |
| B11 | Brave report branch `arena/0be2770f-le` unchanged at `3cfbdad`; no B2x report to act on. | None at this checkpoint. | Re-check when a new report appears. |
