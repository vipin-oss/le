# `paper_v2/` — the review paper (current state)

**Start at `../README.md`** (workspace index) or `arena_deliverables/README_FOR_CLAUDE.md` (deep log).
This page says what this directory holds and how to rebuild the paper.

## The paper

*Waves in Thermoelastic and Multiphysics Continua: Generalized Heat Conduction, Coupled Fields and
Interface Phenomena* — a review, 173 pages in its final build, 38 sections, 10 appendices (A–J),
declarations. The section *Wider material classes* is part of it.

| Quantity | Value |
|---|---|
| Pages (final paper) | 173 |
| Pages (`main.pdf` snapshot in this repository) | 164 |
| Sections / appendices | 38 / 10 (A–J) |
| Numbered equations | 90 |
| Figures / tables | 40 / 25 |
| References | 337 |
| Section files | 49 |

These numbers are measured, not remembered: `arena_deliverables/P6_post_merge/measure_final_pdf.py`
writes them to `arena_deliverables/P6_post_merge/final_paper_numbers.csv` from the in-repo
`main.pdf` snapshot and `paper_sources.zip`. Re-run it after any rebuild.

## Build

```bash
# Overleaf: upload paper_sources.zip and compile with pdfLaTeX
# locally:
unzip -q paper_sources.zip -d src && cd src
pdflatex main && bibtex main && pdflatex main && pdflatex main
```

`paper_sources.zip` is the authoritative source tree: 49 section files, the tables directory, the
tikz figure sources and `refs*.bib`; it is byte-identical to `overleaf_package.zip`, kept under the
older name. `main.pdf` is the snapshot build the measured numbers describe.

## What is where

| Path | What it is |
|---|---|
| `main.pdf` | the in-repo build snapshot (164 pages; the final paper is 173) |
| `paper_sources.zip` | the paper as source — the thing to upload (same file as `overleaf_package.zip`) |
| `arena_deliverables/P8_coverage/refs_P8.csv` | the reference set behind the coverage audit |
| `arena_deliverables/P10_verification/refs_P10.bib` | the two references verified in P10 |
| `arena_deliverables/P13_books/refs_P13.bib` | the six books read in P13 for the section *Wider material classes* |
| `arena_deliverables/P5_merge/` | the merge package that produced the current text: `REPORT.md`, 11 paste-ready snippets, 12 conflict rows, the verified ledger |
| `arena_deliverables/P6_post_merge/` | the audit of that merge: `post_merge_claims.csv`, `pdfs_needed_final.csv`, `STATUS.md`, `final_paper_numbers.csv` |
| `arena_deliverables/P1_audit/` | page-level audit of the **v1.2 snapshot** (142 pages): scripts, CSV results, narrative report |
| `arena_deliverables/P17_submission/` | submission support for the review version: independent referee report, seven bibliographic completions (pages_fix.csv), abstract claim table, supplement plan with page counts, pre-submission e-mail, cover letter, new-versus-existing statement, the 41-figure and 25-table list, and its own gate |
| `arena_deliverables/P18_checks/` | source checks behind the referee report: the Green-Lindsay relaxation-time inequality (what is recorded, what is not, and the one page that settles it), the Nowacki entry and its ISBN, and the Chen 2001 / Dreyer-Struchtrup 1993 availability check, with an evidence table and its own gate |
| `arena_deliverables/P19_patches/` | patch tables for the seven P19 items on the 153-page review build: article numbers for the seven page-less references, the fifteen given-name-first author entries, journal-name uniformisation with ISSN titles, the abstract-against-Table-4 discrepancy table, the twenty-one caption cross-references with their printed numbers, the fourteen DOI-less references with an editor paragraph, the Green-Lindsay ordering record, and its own gate |
| `arena_deliverables/check_readme_paths.py` | gate: these READMEs stay true (paths exist, numbers match the PDF) |
| `claim_register.csv`, `verification_register.csv`, `benchmark_registry.csv`, `atlas_targets.csv` | the evidence registers |
| `atlas_targets.csv`, `missing_sources_priority.csv`, `refs_catalogue_check.csv` | what is still missing, and how the catalogue was checked |
| `manuscript_v2/` | **older snapshot (v1.1/v1.2), not the current paper** — kept because the audit trail cites it |
| `versions/v1.1_source_snapshot/`, `versions/v1.2_edits_2026-11-01/` | frozen v1.1 and the pre-edit copies of every 2026-11-01 edit |
| `working_notes/` | retained working collections deliberately **not** part of the paper |
| `BLUEPRINT_v3.1.md`, `P1_DEFECT_REGISTER.md` | the plan and the defect record |

## Open items

The claim ledger `claim_register.csv` holds **224 rows** — 78 supported, 38 partly, 5 not supported as
worded, 103 with no source in hand — and 81 of them rest on a page-level read. The new text is audited
separately in `arena_deliverables/P6_post_merge/post_merge_claims.csv` (63 rows).

Register coverage (11 of 136 inventoried equations carry a status); two post-merge defects (a
cross-reference printing "(A)" in Appendix A, and Tables 21–23 floating after the reference list);
sources still to be read (`arena_deliverables/P6_post_merge/pdfs_needed_final.csv`); journal choice,
external review and atlas case results (0 of 40). The full list, with what each one blocks, is
`arena_deliverables/P6_post_merge/STATUS.md`.
