# CORRECTIONS_LOG — handoff (2026-09-30) vs this work (2026-10-01)

Every corrected number is computed by `08_Experiments/analyze_v2.py` from stored raw outputs. "Handoff" values are those of `PROJECT_CRYSTAL_GEOMETRY_01/data/ANALYSIS.json` and the manuscript v1.0.

| # | Handoff claim | Finding of this work | Cause | Evidence |
|---|---|---|---|---|
| 1 | T1/H1 PASS (machine class); circle peak scatter 0.30% 'argmax sampling' | circle peak spread 4.6e-15 (6 lattice φ, grid M), 6.7e-15 (12 φ, R48); T1 PASS | sign error in the C23′ cross-term of `rotate_Q_beta` (β error up to 0.17%); `or True` in the analysis script; V3 normalisation mixed units and tested φ = 90° only | tests U1, V3, V3p, V3d; `/home/user/work/rerun/REVIEW_FINDINGS.md` |
| 2 | circle peak 0.9666 MPa/K | 0.8539 MPa/K (extrapolated), 0.8536 on grid M; ratio to handoff 0.883 | periodic-pulse-train synthesis (+7–12%), under-resolved near-wall mesh (γ = 3.5, 96×48: further +5–12%) | V11, C4, convergence report |
| 3 | ellipse 1.1255–1.6685 MPa/K, modulation 36.6% (33–37%) | extrapolated six-orientation range 0.9640–1.3010 MPa/K, modulation 28.7% (grid M, 12 φ: 29.9%; u_num 1.31%); T4 RESOLVABLE | same as #2; the handoff amplitude was not converged | `CONVERGENCE_REPORT.md` |
| 4 | H3 NOT SUPPORTED; equal-Λ pair D = 7.36e-3 vs 2.10e-3 (3.5×); '(Λ, ε) two-parameter map' | quasi-static pair 2.0e-03 vs 2.0e-03 (residual 0.000%, SUPPORTED); dynamic pair 5.3e-03 vs 2.6e-03 (residual 51.6%, NOT-SUPPORTED); D ≲ 1e-2 throughout | echoes wrapped by the 8 t_th window, D evaluated over the whole window, damping dependence; the collapse in Λ is an exact scaling identity of the quasi-static uncoupled limit | tests U8, V9e; `FORMULATION_ADDENDUM.md` §3 |
| 5 | T3 feedback WITHIN-BOUND 0.2δ (partly hard-coded) | max probe deviation 6.2e-04 vs 5δ = 5.4e-03: WITHIN-BOUND | recomputed in the script; no hard-coded values | `analyze_v2.py` |
| 6 | V2 grid convergence PARTIAL (2.35% circle, 6.8% ellipse, 96×48 vs 192×96) | at the handoff grid the ellipse-tip stress was ≈12% too large; orders 0.8–1.35 | near-wall radial resolution (clustering γ = 3.5) | C4 |
| 7 | hysteretic damping η_d = 0.05 regularises resonances | removed; contour evaluation at Re s = 0.9/t_th makes it unnecessary; undamped model | the periodic synthesis needed it | NUMERICAL_METHOD_V2.md |
| 8 | 21 frequencies (manuscript) / 26 (production) | 27 complex solves per run (T = 20, γ_B = 0.9, K = 26) | documentation inconsistency | run JSONs |
| 9 | K eigenvalues 11.36/14.86 W/(m K), axis 25.5° | 11.72/14.50 W/(m K), axis 22.7° | documentation error | test U3 |
| 10 | "full 13-component Cij" | only C11, C13, C15, C33, C35, C55 (Q) and C12, C23, C25 (β via α_b) enter | plane-strain reduction | test U0 |
| 11 | reference [4] "Mech. Adv. Mater. Struct."; [9] Tzou 1995 = book; [10]/[11] placeholders | [4] Mechanics Based Design of Structures and Machines 43, 501–513 (2015); Tzou 1995 = J. Heat Transfer 117, 8–16; [10] = Orlandi et al. 2015; "ACS Omega 2021" source unidentifiable, dropped | metadata errors | `01_Literature/` |
| 12 | α = (1.54, 3.37, 3.15)×10⁻⁶ 1/K "consistent" with synchrotron data | at 298 K the synchrotron data give α_a ≈ 0.10×10⁻⁶ and α_b, α_c ≈ 2α_a: ≈10× smaller; absolute stresses scale with α | parameter uncertainty | search #2; block E1 |
| 13 | MFP 1–2 nm, continuum flag a ≥ 5 nm | gray MFP ≈ 3 nm but spectrum to ≈ 0.7–1 µm; continuum validity at 5–50 nm not established | assumption too optimistic | `PROJECT_CONSTRAINTS.md` §4 |
| 14 | abstract limit possibly 200 words | IJHMT guide: ≤ 250 words | unverified assumption | JOURNAL_FIT.md |
