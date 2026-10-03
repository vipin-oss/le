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

## 2026-10-01 — continuation session (repository `vipin-oss/le`, branch `arena/01a0f67f-le`)
- Audited the delivered `le.zip` (52,189,612 B, sha256 `5e780e1f…`); verified the handoff baseline
  303/303 SHA-256. Audit record: `docs/PHASE1_AUDIT.md`.
- **P7-D002 confirmed by the user** (Bromwich single-pulse synthesis stands).
- Full re-run of tests (26 PASS / 1 FAIL / 1 exploratory), production (150/150), convergence
  (C2/C3/C4), analysis, figures, supplement, manuscript and reproduction test (11 PASS / 0 FAIL).
  All scientific outputs bit-identical to the delivered ones — see `RERUN_COMPARISON.md`.
- Regenerated: `TEST_RESULTS.json`, `TEST_REPORT.md`, `09_Raw_Data/{production,convergence}/`,
  `ANALYSIS_V2.json`, `ANALYSIS_V2_TABLES.md`, `PRODUCTION_PROVENANCE.csv`, `CONVERGENCE_*.json`,
  `VALIDATION_RESULTS.md`, `CONVERGENCE_REPORT.md`, `STABILITY_REPORT.md`, `11_Figures/`,
  `12_Tables/`, `13_Manuscript/*`, `CENTRAL_STORY.md`, `CORRECTIONS_LOG.md`, phase states 07–13.
- New: `06_Source_Code/CODE_FREEZE_v2_final.json` (addendum, R-D003);
  `bootstrap_paths.sh` (R-D004); `tools/compare_rerun.py`; `RERUN_COMPARISON.md`;
  `00_Project_Control/PROJECT_STATE_FINAL.md`; `packages/PACKAGE_PHASE_07…13.zip` and
  `packages/RESEARCH_PROJECT_FINAL.zip` (MASTER_PROMPT §67/§74).
- Code: one-line portability edit in `13_Manuscript/ms_results.py` only (R-D002; verified
  output-identical). No equation, BC, IC, parameter or solver change.
- Not re-run: `09_Raw_Data/convergence_gamma3p5/` (partial γ = 3.5 study — no regenerator script
  exists in the package); pilot re-run (reference data absent, as before).

## 2026-10-03 — provenance pass (repository `vipin-oss/le`, branch `arena/01a10176-le`)
- Audited the git connection of the paper to this repository (`docs/GIT_CONNECTION_AUDIT_2026-10-03.md`,
  `python3 tools/connection_audit.py`): worktree, HEAD and `origin/main` agree at blob level for all
  tracked files, `le.zip` is fully accounted for (committed or explicitly ignored), the read-only handoff
  baseline verifies 303/303 SHA-256, and the manuscript/companion PDF + .tex pass every static gate.
- Recomputed all four code-freeze manifests against the committed code: `v2_gate` 9/15 (exactly the six
  files the manuscript names — the paper's statement is confirmed), `v2_blockF` and `v2_final` historical,
  `submission_2026_10_02` 25/27 with the two manuscript builders stale.
- New: `06_Source_Code/CODE_FREEZE_submission_2026_10_03.json` (27/27 matching) — the manifest to deposit.
  The 2026-10-02 manifest is unchanged and kept as history.
- `13_Manuscript`: §9.1 and companion §11 now cite the 2026-10-03 manifest; both builders abort if the
  deposited manifest does not describe the code; `.md/.docx/.tex/.pdf` rebuilt (one paragraph changed per
  document, page counts unchanged, PDF bytes differ only in the embedded timestamp). No scientific content,
  no data and no source code under `06_Source_Code/src/` was modified.
- Tooling: `tools/verify_pdf.py` (running-title in the margin check, divergence report, out-of-order
  units counted separately) and `tools/connection_audit.py` (new).

## 2026-10-03 — download artifact published (branch `arena/01a10176-le`)
- Built `PAPER_PROJECT/packages/RESEARCH_PROJECT_FINAL.zip` (`make_packages.py final`: 523 files + `MANIFEST.json`,
  37,946,120 B) and recomputed all 523 manifest entries from the archive: 0 mismatches.
- Published it as `dist/RESEARCH_PROJECT_FINAL_2026-10-03.zip` (+ `.sha256`, + `dist/README.md`) on this branch,
  with release notes under tag `final-2026-10-03`, so the package has a direct download link. Release-asset
  upload was not possible from the sandbox (`uploads.github.com` unreachable), hence the `dist/` copy.
  `packages/` itself stays gitignored and regenerable; `main` and every scientific file are untouched.
