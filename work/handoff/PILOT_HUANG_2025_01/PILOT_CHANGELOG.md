# Pilot change log

## Correction01 — after initialruns
- P03initialRUN_FAILED:deHoog0/0atidenticallyzero sigma boundarytransform. Preserveoriginalerror/stagelog/v01code. Analyticalendpoint handling added onlyforx0stress; nonzero interiortransforms/parameters unchanged.
- InitialCVmesh-refinementpointcriterionnotmet for1600->3200theta/stress. Addpost-resultCV6400diagnostic;keeporiginalcriterion/mask/results.
- No plan/sourceparameter/physicalequation/normalization change or agreement-driven calibration. Same1800CPU-second/noGPU/50MBcap.


## 30 September 2026 — practical completion + final close-out
- run_source_and_limiting_cases.py: source Figure-5 comparison + limiting cases executed (user pragmatic directive: "limiting case + jaisi curve").
- src/common.py: _ver() helper for package metadata (logging-only fix; scientific code untouched).
- Outlier diagnosis recorded (E18); curves NOT adjusted to match digitized points.
- PILOT_REPORT_FINAL.html/md, figures/SOURCE_CASE_COMPARISON.*, data/FINAL_COMPARISON_SUMMARY.json written.
- PILOT_ACCEPTANCE_STATUS.md rewritten to FINAL. Recovery package refreshed (excludes reference_local/, input PDFs).
- MAINTAINED: no parameter changes, no criteria changes, all prior failures preserved.
