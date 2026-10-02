# VALIDATION STATUS — FINAL (source-case pilot)
Date:30September2026 | Label: PILOT — NOT FINAL VALIDATION (mathematical source case)

## FINAL verdict — P0A-2 Huang2025 source case
**SOURCE CASE REPRODUCED (within documented uncertainty).**
- Full profile comparison: FVM curves vs de Hoog closed-form — agreement at stored probes <=8e-6 scaled.
- Source Figure5 quantitative match: **175/177 digitized points within combined figure+numerical envelope (98.9%)**; MCV3 102/102 (theta36/36,sigma33/33,u33/33); CV theta38/39,sigma29/30,u6/6. 2 outliers = digitization artifacts (documented; curves NOT adjusted). 11 pre-excluded near-front points.
- Limiting cases PASS: wavefront speed 5.0018 vs source 5 (0.035%); fronts 0.3001/0.05998 vs source 0.3/0.06; alpha=0 uncoupled exact 7e-18; tails ~1e-88.
- 40 equation/BC/matrix checks PASS; de Hoog 48/64 PASS; FVM refinement PASS (post-result CV6400 logged).

## Retained failures/limits (honest)
- Cohen-80 inversion cross-check FAILED (huge inconsistent values, root cause unconfirmed) — excluded from verdict; two independent methods + source figure agree; failure record preserved (logs/).
- INITIAL CV 1600->3200 off-front 3e-3 criterion FAILED; extension CV3200->6400 passed; both kept.
- P03 initial run de Hoog 0/0 endpoint failure: fixed analytically at zero transform only; v01 preserved.
- Physical validation: NOT_RUN (no experiment/converged literature benchmark reproduction beyond this source case).
- NOT produced: beta-Ga2O3, elliptical cavity, new tensor model, manuscript, journal selection, novelty claims, Q1 guarantee.

## Next
User decision among: (1) beta-Ga2O3+circle/ellipse coupled problem plan; (2) Bagri/Gordeliy reference case; (3) manuscript direction. Explicit choice required.


## Update 2026-09-30 (post operator correction chain, D014)
V0–V7 RE-EARNED on corrected conservative operator (log: PROJECT_CRYSTAL_GEOMETRY_01/logs/verify_rerun_v3.log):
V0 PASS | V1 PASS | V2 PARTIAL (2.35% circle, 6.80% ellipse med-vs-fine; handled per pre-defined plan: per-quantity grid uncertainty + 192×96 confirmatory spot checks for T4 amplitudes) | V3 PASS 6.26e-14 | V3b PASS | V4 PASS | V5 PASS 1.09e-7 | V6 PASS 9.5e-6 | V7 PASS 0.68%.
Physics-validation remains NOT_AVAILABLE (no experimental dataset). Damping η_d=0.05 (dynamic) is a documented model regularization with sensitivity study; statics undamped. Physical-validation claims still forbidden.
