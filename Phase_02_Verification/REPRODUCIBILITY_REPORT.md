# REPRODUCIBILITY REPORT — Phase 2 (2026-10-03)

## Environment of this re-check
* sandbox: 2 vCPU, ~3.9 GB RAM, Linux 6.1.158+ (glibc 2.36)
* Python 3.11.2 · numpy 2.4.6 · scipy 1.17.1 · matplotlib 3.11.2 · python-docx · openpyxl · reportlab · PyMuPDF 1.28.2
* the archived production data were produced with Python 3.13.14 · numpy 2.3.5 · scipy 1.17.1 · matplotlib 3.10.9
  (`CODE_FREEZE_v2_blockF.json`), and re-verified on 2026-10-01 with Python 3.11.2 + numpy 2.3.5
* setup recipe (also in `PAPER_PROJECT/README.md`):
  `python3 -m venv .venv && .venv/bin/pip install numpy scipy matplotlib python-docx openpyxl reportlab pymupdf && sh bootstrap_paths.sh`

## Checks performed, with the measured outcome
1. **Bit-level reproduction of a production solve.** `A_chi1_phi000_M` re-solved in this environment:
   peak wall hoop stress −8.5363872762e+05 Pa/K, relative difference from the archived value **2.7e-16** (1 ulp);
   `t*` and the wall-reconstruction error identical; the backward error of the linear solve differs only at the
   round-off floor (7.3e-25 → 6.7e-25, an 8 % difference of two numbers that are both noise).
   Evidence: `verification/FIDELITY_check.json`.
2. **Determinism of the analysis layer.** `analyze_v2.py` re-run over all 175 stored runs with the extended script:
   9 keys added, 0 removed, **1** pre-existing scalar changed (`numerics.n_runs`, 150 → 175 by construction).
   No physical quantity moved. Evidence: `verification/ANALYSIS_DIFF.md`, `verification/ANALYSIS_V2_before_phase2.json`.
3. **Verification suite re-run.** 28 cases, 27 PASS / 0 FAIL / 1 INFO, 1101 CPU-s. The V0 sequence values are
   *identical strings* to the 2026-10-01 run (1.668623219132792e-2, 4.177783115160594e-3, 1.0446010651126159e-3
   for χ = 1), i.e. the re-specified criterion is applied to the same measured numbers, not to re-derived ones.
   The 2026-10-01 record, including its FAIL for V0 under the old criterion, is preserved unchanged in
   `07_Tests/logs/` and in `Phase_02_Verification/historical/`.
4. **New production runs.** `EM` ablations (24) + `D_iso_circle_M` (1): 1696 CPU-s, 68 s/run average, each written
   as a `.json`/`.npz` pair under `09_Raw_Data/production/` and registered in `10_Processed_Data/PRODUCTION_PROVENANCE.csv`
   (RUN_ID, block, grid, model, τ, χ, φ, a, code version, input checksum, environment, output digests).
5. **Document chain.** `build_manuscript.py` / `build_calculations.py` regenerate `.md` + `.docx` from
   `ANALYSIS_V2.json`, `TEST_RESULTS.json`, `CONVERGENCE_*.json` and the frozen code constants; `tools/md_to_tex.py`
   produces the `.tex`; `tools/md_to_pdf.py` renders the 33-page preprint PDF (LaTeX compilation is not available in
   this sandbox — see finding A15); `tools/audit_tex.py` (70 checks), `check_tex_commands.py`, `check_crossrefs.py`,
   `test_md_to_tex.py` (26), `renumber_crossrefs.py` (12 edits verified) and `verify_pdf.py` (both documents) all pass.
   New guard: the builders abort if a generated table contains `n/a`, `??`, `TODO` or an empty cell.
6. **Code provenance.** `CODE_FREEZE_submission_2026_10_03b.json` (27 files) describes the code as it now stands;
   the two earlier manifests are untouched. §9.1 of the manuscript cites the chain and the 1 ulp re-solve result.

## What a reviewer can rerun, and how long it takes
`python3 08_Experiments/reproduce.py` (tests 1101 s, production matrix 112 jobs ≈ 2400 s, convergence runs,
analysis, figures, documents). Single new ablation job ≈ 60–70 s on 1 core. The 87 original runs need ≈ 20 min with
one worker; the heavy 192×96/96×144 family needs the rest.

## Known limits of this report (not hidden)
* The PDFs are produced by the project's markdown→reportlab pipeline, **not** by compiling the `.tex`; the LaTeX
  source has passed static checks only. The `.tex` will compile or not on the authors' TeX installation — recorded
  as an open item, not asserted.
* 150 of the 175 archived runs were not re-solved in this phase (only their analysis was recomputed and one job was
  re-solved as a spot check); the full re-solve of the whole matrix is the 2026-10-01 `15_Audits/RERUN_COMPARISON.md`.
* Independent expert review of the formulation and of the acceptance criteria has not been obtained (author action).
