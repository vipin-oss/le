# REPRODUCIBILITY_STATUS (2026-10-01)
- Source: `06_Source_Code/` (hashes in `CODE_FREEZE_v2_gate.json`, which is historical; the manifest
  describing the code as committed is `CODE_FREEZE_submission_2026_10_03.json`, 27/27 byte-identical — see
  DECISION_LOG P13-D002); environment identical to the handoff's (Python 3.13.14 / numpy 2.3.5 / scipy 1.17.1 / matplotlib 3.10.9, Linux x86_64).
- Tests: `python 07_Tests/run_tests.py` (≈ 20 min, one process at a time), supplement `run_tests_supplement.py`.
- Production: `python 08_Experiments/run_production_v2.py heavy|light` (two workers), analysis `analyze_v2.py`, figures `make_figures.py`, manuscript `13_Manuscript/build_manuscript.py`.
- Reproduction test: `07_Tests/REPRODUCTION_TEST_REPORT.md` (see its status).
- Not reproducible from this package: handoff pilot source-figure comparison (private digitisation absent); third-party PDFs not included.
