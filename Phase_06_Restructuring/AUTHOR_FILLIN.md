# Author fill-in list (Phase 6) - the bracketed fields that only the authors can close

Everything below is the only remaining content-level gap in the submission set. The agent
must not fill these in: author identity, funding and repository identifiers cannot be
invented, and the scientific claims belong to the authors.

| # | Where | Field | Status |
|---|---|---|---|
| 1 | `manuscript_IJHMT.md` front matter | author names, affiliations, ORCID iDs, corresponding author | placeholder line present |
| 2 | Declarations | CRediT authorship contribution statement | skeleton sentence waits for the author list of #1 |
| 3 | Declarations | Declaration of competing interest | to state "none" or the actual interests |
| 4 | Declarations | Funding | grant names/numbers, or "no specific grant" |
| 5 | Declarations | Data availability | public repository name + DOI for the data package |
| 6 | Declarations | Declaration of Generative AI | confirm the tool name and the stated purposes, then delete the bracket if unchanged |
| 7 | `01_Literature/` (P5-1) | Cattaneo 1948 / Vernotte 1958 primary sources | no DOI-bearing Crossref record found; either supply the bibliographic details or keep the names in prose with the Gurtin-Pipkin [15] anchor, as now |
| 8 | Submission site | LaTeX compile + PDF | no TeX engine in this sandbox: compile `FINAL_REVISED_MANUSCRIPT.tex` / `FINAL_REVISED_CALCULATIONS.tex` with `elsarticle` locally and compare against the generated PDF |

`calculations_IJHMT.md` (the companion) carries no separate placeholders: its front matter
and declarations come from the same builders, so closing #1-#6 in the manuscript closes
them too.

Check that after every change the builders are re-run (`build_manuscript.py`,
`build_calculations.py`, `build_supplement.py`, `tools/md_to_tex.py`, `tools/md_to_pdf.py`)
and the gates re-pass (`tools/audit_tex.py`, `tools/check_crossrefs.py`,
`tools/check_tex_commands.py`, `tools/verify_pdf.py`, plus `-c` for the companion).
