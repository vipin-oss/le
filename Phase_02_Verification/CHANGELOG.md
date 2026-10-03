# CHANGELOG — Phase 2 (Verification) · 2026-10-03

Closes audit findings **A1, A2, A5, A8, A9, A10** (see `FINDINGS_LEDGER.json`; A15 recorded as unresolvable in this
sandbox). No previous phase's files were modified; `Phase_01_Audit/` is untouched and remains the audit of record.

## Added
- `09_Raw_Data/production/` : 25 new runs (`E{1..4}_*_phi{000..150}_M`, `D_iso_circle_M`) as .json/.npz pairs.
- `12_Tables/ablations_E_M.csv` : production-resolution mechanism ablations (6 orientations × 4 variants + baseline).
- `10_Processed_Data/PRODUCTION_PROVENANCE.csv` regenerated (175 runs).
- `06_Source_Code/CODE_FREEZE_submission_2026_10_03b.json` (27/27 current). Earlier manifests unchanged.
- `Phase_02_Verification/`: REPORT.md, VERIFICATION_REPORT.md, REPRODUCIBILITY_REPORT.md, FINDINGS_LEDGER.json,
  bromwich_window_audit.py, diff_analysis.py, finalize.sh, finalize2.sh, patch_*.py, historical/, verification/, manifest.txt.

## Changed (all regeneration-safe; the .md/.docx/.tex/.pdf are products of the builders)
- `07_Tests/run_tests.py` : V0 criterion re-specified (order ≥ 1.9 for χ=1,2 **and** < 5e-3 at the production grid);
  new case `V0b_metric_consistency_convergence_order`; coarse-grid value recorded as information.
- `08_Experiments/production_matrix.py` : block `EM` (grid M) + `D_iso_circle_M`; documented in the module docstring.
- `08_Experiments/analyze_v2.py` : `E_ablations_M` (incl. `grid_change_T48_to_M`), matched-grid `isotropic` keys,
  matched-grid `T4_H2` shape ratios, `numerics.wall_pulse_error_by_tw` + QoI-window exceedance count, new CSV.
- `13_Manuscript/build_manuscript.py` : abstract — production-grid attribution wording, peak-shift subset, 249 words;
  §9.1 rewritten as a factual re-check record (1 ulp cross-build re-solve, deterministic re-analysis, 6-CSV state);
  placeholder-cell guard for generated tables; manifest label advanced to `submission_2026_10_03b` (supersedes, does not overwrite).
- `13_Manuscript/ms_results.py` : V0 note + Table 5 row from recorded values; §5.2 matched-grid shape sentences;
  §5.3 ablation table shows both grids with a same-grid/same-orientation-set rule; §6.5 grid labels; helpers
  `_v0_note`, `_v0_row`, `_shape_sentence`, `_iso_shape_sentence`.
- `13_Manuscript/ms_numerics.py` : Bromwich validity qualified per pulse width using measured errors (`_num_`).
- `13_Manuscript/build_calculations.py` : §11 provenance paragraph + placeholder guard + manifest label.
- Regenerated: `ANALYSIS_V2.json` (additive; only `numerics.n_runs` 150→175 among pre-existing values),
  `ANALYSIS_V2_TABLES.md`, `TEST_RESULTS.json` (28 cases), `TEST_REPORT.md`, `manuscript_IJHMT.md/.docx`,
  `FINAL_REVISED_MANUSCRIPT.tex/.pdf` (33 pp), `calculations_IJHMT.md/.pdf`, `FINAL_REVISED_CALCULATIONS.tex/.pdf`
  (14 pp), `SUPPLEMENTARY_TABLES.xlsx`, `MANUSCRIPT_STATS.json`, `highlights.txt`, `FINAL_REVISED_REFERENCES.bib`,
  `PAPER_PROJECT/README.md` (environment lines).
- Figures **not** regenerated (no figure input changed): the 8 PNGs are byte-identical to the archived set.

## Verification
`audit_tex.py` (manuscript 70 checks, companion) ALL PASSED · `check_tex_commands.py` ALL DEFINED ·
`check_crossrefs.py` all resolve · `test_md_to_tex.py` 26/26 · `renumber_crossrefs.py` 12 edits in place ·
`verify_pdf.py` both documents + both FINAL_* mirrors ALL PASSED · production run timings: 25 jobs 1696 CPU-s.
