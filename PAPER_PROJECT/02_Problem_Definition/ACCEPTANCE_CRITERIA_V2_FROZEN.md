# ACCEPTANCE_CRITERIA_V2_FROZEN — confirmatory criteria for the v2 production (Phase 10 gate)

Frozen: 2026-10-01, **before any v2 production run** (code hashes: `06_Source_Code/CODE_FREEZE_v2_gate.json`). MASTER_PROMPT §24–27.
Basis: `PROJECT_CRYSTAL_GEOMETRY_01/SCIENTIFIC_ACCEPTANCE_PLAN.md` (T1–T4, H1–H5). **Thresholds are inherited unchanged** (1e-8; 25%; 5δ; max(5·noise, 2%)).

## 0. Honest status of "pre-registration"
The handoff criteria were frozen before the handoff's production, but the handoff's analysis did not honour them (T1 forced to PASS; H3 evaluated on an artefact). I inspected the handoff results and ran diagnostic tests before writing this file (REVIEW_FINDINGS.md, Phase 9 C4). Therefore:
- the *thresholds* below are the original ones; the *definitions/wordings* are clarified (logged as P10-D001…D004);
- the new production (v2) is **confirmatory with respect to this document** (nothing here is changed after v2 results are seen); the handoff's numbers are not;
- the ablation block E, the extended (Λ, ε) map B2/B2QS and the expansion-set sensitivity are **EXPLORATORY** (specified before running, not pre-registered hypotheses).
Any later change to this file must be logged and every analysis that depends on it labelled post-result (§25).

## 1. Primary quantities and metrics
| Quantity | Definition |
|---|---|
| σ̂ (peak wall hoop stress) | max over wall angle and 0 ≤ t ≤ 6 t_th of |σ_θθ| per kelvin of wall amplitude; two versions: nodal (handoff definition) and angularly interpolated (16× trigonometric interpolation of the 48–96 wall values). T1 uses nodal; T4/T5 use interpolated. |
| D | max over wall nodes and 0 ≤ t ≤ 6 t_th of |σ_CV − σ_F| / max|σ_F| (circle, φ = 0; same grid, same plan) |
| A_φ | (max_φ σ̂ − min_φ σ̂)/mean_φ σ̂ over the orientation list |
| feedback | relative change of θ at radial probes r/a ≈ 1.5, 2, 3 (wall angle index 0), energy coupling on vs off |

## 2. Frozen criteria
**T1 (H1: circle peak is orientation-invariant).** For all orientations in the lists {0,…,165° step 15°} on grid R48 (12 φ) and {0, 15, 45, 75, 105, 135°} on grid M, (max − min)/mean of nodal σ̂ ≤ 1e-8. These φ are exact lattice rotations of the polar grid (15° = 4 cells at Nt = 96, i.e. grids M and R48; 2 cells at Nt = 48), so the discrete identity must hold to round-off; the criterion applies to every pair, not only to (0°, 90°). PASS/FAIL, no override. (Handoff wording "(all φ, φ′) on the 90° discrete-rotation identity" is ambiguous; this is the strict reading.)
**T2 (H3: thermal-memory deviation collapses in Λ alone).** Equal-Λ pair (a = 10 nm, τ = 5 ps) vs (a = 20 nm, τ = 20 ps), Λ = 0.198: residual |D₁ − D₂|/max(D₁, D₂) ≤ 25% AND D monotone in Λ within each family (tolerance band 25%). Evaluated twice, both reported: (i) quasi-static ablation (inertia off), (ii) full elastodynamics (undamped, R = 80a). D uses the QoI window t ≤ 6 (the handoff used the full window).
**T3 (H4: feedback bound).** max probe deviation ≤ 5δ with δ = T0 β·β/(ρ c_p C̄) computed in the code (1.078e-3). Also report the change of σ̂.
**T4 (H2: orientation modulation of the ellipse is resolvable).** A₁₂(M) ≥ max(5 u_num, 2%), where A₁₂(M) = amplitude of interpolated σ̂ over the 12 orientations on grid M, and u_num = max(|A₆(R192) − A₆(M)|, |A₆(T144) − A₆(M)|, |A₆(extrapolated) − A₆(M)|) over the 6 orientations {0, 30, 60, 90, 120, 150°} that carry all grids. If A < threshold report NULL with the resolution limit. (The handoff used the circle scatter — which was the rotation bug — as "noise".)
**T5 (numerical uncertainty; new).** Absolute stresses are quoted as: value on grid M, Richardson-extrapolated value, and the radial/angular corrections. If the observed order lies outside [1, 3] the extrapolation is capped at the bounding order and the case is labelled "grid-uncertain". Verification criteria V0–V12 (07_Tests): all must PASS before production; failures block the corresponding claims (§78).
**H5 (angular-mode content), ablations E, extended map B2:** exploratory — reported without a pass/fail status.

## 3. Interpretation rules (stated before the results)
- A positive finding is reported with its uncertainty; "RESOLVABLE" does not mean "physically validated".
- A null/negligible finding (e.g. D, feedback) is reported with the resolution limit (grid/contour uncertainty) and an upper bound.
- Absolute-stress statements carry the parameter uncertainty of α (secondary-quoted Orlandi values vs. 298 K-like set, up to ≈10×); only relative effects are claimed as results.
- No claim about validity of Fourier/CV conduction at 5–50 nm is made.

## 4. Numerical design frozen with this file
Pulse p(t) = exp(−((t − 2.5)/1.2)²) on the whole line; Bromwich plan T = 20, γ = 0.9 (K = 26, 27 solves, alias 1.5e-8); undamped model; R = 80a; refinement of the solver `refine = 2`; radial clustering γ_grid = 5 (P9-D001); grids R48 = 48×96, T48 = 96×48, M = 96×96, R192 = 192×96, T144 = 96×144; production matrix `08_Experiments/production_matrix.py` (141 runs, ≈87 CPU-min estimated). Compute budget (§43): cumulative project compute including verification, convergence and review runs ≈ 2.7 CPU-h (estimate), below the 4 CPU-h approval threshold; no GPU; stored data < 100 MB.
