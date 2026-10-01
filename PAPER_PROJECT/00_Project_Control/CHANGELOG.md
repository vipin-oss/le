# CHANGELOG — PAPER_PROJECT

## 2026-10-01
- Downloaded the handoff and verified it (303/303 SHA-256) into `/home/user/work/handoff/`.
- Review area `/home/user/work/rerun/`: tests, logs, `REVIEW_FINDINGS.md`, `rotate_Q_beta_fix.diff`, `fixed_src/cg_model.py`. The patch is NOT applied to project code; the working copy `rerun/proj/` is still unfixed.
- Removed the stray `handoff/PROJECT_CRYSTAL_GEOMETRY_01/src/__pycache__` (created by my own execution; not in the original zip).
- Created `/home/user/PAPER_PROJECT/00_Project_Control/`: MASTER_PROMPT.md (copy of the handoff file, SHA-256 `c18fd525…dac0`), MASTER_PROMPT_VERSION, MASTER_PROMPT_DATE, PROJECT_STATE_PHASE_00.md, INPUT_INVENTORY.md, PROJECT_CONSTRAINTS.md, TOOL_AVAILABILITY.md, DECISION_LOG.md, CHANGELOG.md; plus `/home/user/PAPER_PROJECT/README.md`.
- No scientific equations, parameters, code, BCs, ICs or acceptance criteria were changed.

## 2026-10-01 (Phases 7–10)
- New code in `06_Source_Code/src/`: `cg_bromwich.py`, `cg_ref1d.py`, `cg_pipeline.py`; `cg_model.py` (rotate_Q_beta sign fix), `cg_solver.py` (`inertia_scale`, `refine`) — diffs vs handoff in `06_Source_Code/DIFF_VS_HANDOFF.txt`.
- New tests `07_Tests/run_tests.py` (+ diagnostics); new scripts `08_Experiments/*`; documents `04_Theory/FORMULATION_ADDENDUM.md`, `05_Numerical_Method/NUMERICAL_METHOD_V2.md`, `02_Problem_Definition/ACCEPTANCE_CRITERIA_V2_FROZEN.md`, `01_Literature/*` (verified references, search log).
- No change to equations, constitutive laws, BCs, ICs, geometry, material parameters (alpha, cp, tau sets as before; new sensitivity sets are labelled).

## 2026-10-01 (Phases 11–13)
- Production (150 runs, `09_Raw_Data/production/`), convergence C2/C3, analysis `ANALYSIS_V2.json`/`ANALYSIS_V2_TABLES.md`, tables (`12_Tables/`), figures (`11_Figures/`), provenance (`PRODUCTION_PROVENANCE.csv`), code-freeze addendum (`CODE_FREEZE_v2_blockF.json`).
- Manuscript (`13_Manuscript/manuscript_IJHMT.docx/.md`), highlights, cover letter draft, supplementary workbook, journal-fit record; audits (`15_Audits/`), reproduction test (11 PASS), CORRECTIONS_LOG, CENTRAL_STORY, EVIDENCE_LOG, phase states 07–13, status files, REJECTED_IDEAS update.
- `cg_pipeline.run_config`: optional `pulse` argument and `gamma_grid` (defaults unchanged; baseline results bit-identical).
