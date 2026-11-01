# `paper_v2/` — the review manuscript (current state)

**Start at `../README.md`** (workspace index) or `arena_deliverables/README_FOR_CLAUDE.md` (deep log).
This page only tells you what this directory holds and how to build the paper.

## The paper

- Sources: `manuscript_v2/master/` — `main.tex` plus `sections/` (17), `appendices/` (A–F), `frontmatter/`,
  `tables/source/` and one bibliography (`references_local.bib`).
- Build: `cd manuscript_v2/master && pdflatex main && bibtex main && pdflatex main && pdflatex main`
  (or `make`; see `manuscript_v2/master/BUILD.md`). Overleaf runs the same sequence.
- Figures: 16 PDFs are shipped inside the submission zip; in this workspace they live **outside** the repository
  (18 source PDFs exist; 2 are declared provisional in Appendix D and are deliberately not shipped).

## Last measured build (2026-11-01, 17:13 UTC)

| Quantity | Value |
|---|---|
| Pages / words | 142 / 64,932 |
| Sections / appendices | 17 / 6 (A–F) |
| Numbered equations | 136 (all labelled; inventoried in `arena_deliverables/P1_audit/equation_inventory.csv`) |
| Figures / tables | 16 (1–16) / 55 (1–55) |
| Cited works | 107 of 144 `.bib` entries |
| Unresolved refs / missing cites / leaked LaTeX | 0 / 0 / 0 |

Audit: 26 checks, 21 PASS, 5 REPORT, **0 FAIL** — `arena_deliverables/P1_audit/PAGE_LEVEL_AUDIT_2026-11-01.md`.

## Directory map

| Path | What it is |
|---|---|
| `manuscript_v2/master/` | the paper (build inputs) |
| `manuscript_v2/CHANGELOG_v2.md` | every change, dated, with its reason |
| `manuscript_v2/REVIEW_CYCLES.md` | three editorial cycles, each author→reviewer→editor→author |
| `arena_deliverables/README_FOR_CLAUDE.md` | ★ cold-start log: rules, provenance of every number, open items |
| `arena_deliverables/P1_audit/` | page-level audit: `audit_pages.py`, `check_page_audit.py`, `check_refs.py`, CSV results, report |
| `arena_deliverables/submission/` | the shipped zip (sources + figures + build docs) |
| `arena_deliverables/check_readme_paths.py` | gate: makes sure these READMEs stay true (paths exist, numbers match) |
| `versions/v1.1_source_snapshot/` | frozen v1.1, never edited |
| `versions/v1.2_edits_2026-11-01/` | pre-edit copy of every file edited on 2026-11-01 |
| `working_notes/` | retained working collections that are deliberately **not** part of the paper |
| `BLUEPRINT_v3.1.md` | the plan (§10: phases P0–P7 and their exit conditions) |
| `claim_register.csv`, `verification_register.csv`, `atlas_targets.csv`, `benchmark_registry.csv` | evidence registers |
| `P1_DEFECT_REGISTER.md` | defects found, with status |

## Open items

Register coverage (29 of 136 equations), 18 unpointed register rows, overfull-box warnings (compile log only),
journal choice, external review, atlas case results (0 of 40). Details and the full list: `../README.md` §5.
