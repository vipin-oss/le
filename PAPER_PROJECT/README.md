# PAPER_PROJECT — verified continuum study of cavity thermoelasticity in monoclinic β-Ga₂O₃

Working project (MASTER_PROMPT v2.1) that turns the handoff `COMPLETE_WORK_HANDOFF_2026-09-30.zip` into a defensible manuscript.
Status after this session: Phases 0 and 7→13 executed; Phases 1–6 not re-opened (their documents are superseded where noted); **physical validation APPLICABLE — EVIDENCE_UNAVAILABLE**; independent expert review not done; submission, authorship and the final journal are user-owned.

## Start here
1. `13_Manuscript/manuscript_IJHMT.docx` (and `.md`) — the paper; `highlights.txt`, `SUPPLEMENTARY_TABLES.xlsx`, `cover_letter.md`, `JOURNAL_FIT.md`, `MANUSCRIPT_STATS.json`.
2. `00_Project_Control/PROJECT_STATE_FINAL.md` — recovery summary; `CENTRAL_STORY.md`; `DECISION_LOG.md` (P7-D002 is the decision flagged for the user); `CHANGELOG.md`; `REJECTED_IDEAS.md`.
3. `14_Documentation/CORRECTIONS_LOG.md` — what was wrong in the handoff and what the corrected numbers are.

## Layout (MASTER_PROMPT §74)
| Folder | Content |
|---|---|
| `00_Project_Control` | master prompt, phase states 00 and 07–13, logs, status files, scripts that build them |
| `01_Literature` | verified references (Crossref), search log |
| `02_Problem_Definition` | frozen acceptance criteria v2 |
| `03_Validation` | verification-against-reference results (no physical validation) |
| `04_Theory` | formulation addendum (model, scaling identity, admissibility) |
| `05_Numerical_Method` | method v2 (Bromwich inversion), convergence and stability reports |
| `06_Source_Code` | solver and pipeline (`src/`), code-freeze hashes, diff vs handoff |
| `07_Tests` | verification suite, reports, reproduction test |
| `08_Experiments` | production matrix and drivers, convergence studies, analysis, figures |
| `09_Raw_Data` | per-run raw outputs (npz + json), convergence data |
| `10_Processed_Data` | analysis JSON/markdown, provenance table |
| `11_Figures`, `12_Tables` | figures and CSV tables used in the paper |
| `13_Manuscript` | manuscript builders and outputs |
| `15_Audits` | pre-production, pre-manuscript and final adversarial audits |
| `packages/` | `PACKAGE_PHASE_07…13.zip` (reconstructed cumulative packages), `RESEARCH_PROJECT_FINAL.zip` if created |

## Reproduce (2 vCPU, 2 GB RAM; never run two 192×96 jobs at once)
```
python 07_Tests/run_tests.py && python 07_Tests/run_tests_supplement.py && python 07_Tests/make_test_report.py     # ≈ 20 min
python 08_Experiments/run_production_v2.py heavy &  python 08_Experiments/run_production_v2.py light              # ≈ 45 min, two workers
python 08_Experiments/run_convergence.py ; python 08_Experiments/run_convergence_dirs.py 30
python 08_Experiments/analyze_v2.py && python 08_Experiments/make_figures.py && python 13_Manuscript/build_manuscript.py
python 08_Experiments/reproduce.py                                                                                 # reproduction test
```
Environment: Python 3.13.14, numpy 2.3.5, scipy 1.17.1, matplotlib 3.10.9, python-docx 1.1.2, openpyxl 3.1.5 (identical to the handoff's recorded environment).

## Read-only inputs
`/home/user/work/handoff/` (304 files, 303/303 SHA-256) is the untouched handoff; `/home/user/work/rerun/` is the first-session review area (`REVIEW_FINDINGS.md`, patch, test scripts).
