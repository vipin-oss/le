# Independent review — COMPLETE_WORK_HANDOFF_2026-09-30.zip (PROJECT_CRYSTAL_GEOMETRY_01)

Reviewer: Arena.ai agent, 1 Oct 2026. Everything below was run in a fresh sandbox
(Python 3.13.14 / numpy 2.3.5 / scipy 1.17.1 — same versions the authors recorded).
Original handoff files were NOT modified; working copy = `/home/user/work/rerun/proj/`.
Scripts + logs are in `/home/user/work/rerun/`.  Scope limits: 96x48 grid unless stated;
I did not re-run all 38 production cases; literature novelty only spot-checked.

## 0. Integrity / reproducibility  — OK
* `MANIFEST_SHA256.json`: 303/303 files match.
* Re-running 4 production cases (`A_chi1_phi015/045/105/135`) with the shipped code reproduces
  the stored peak stress to <= 9e-11 (relative). V3b (37 deg) and D(Lambda) baselines also reproduce.
* Inputs cross-checked with primary sources: all 13 Cij = Adachi et al., J. Appl. Phys. 124, 085102 (2018);
  K11=12.13, K33=14.09, K13=-0.992 W/mK = Klimm et al., Cryst. Res. Technol. 58, 2200204 (2023).

## 1. BUG: sign error in `rotate_Q_beta` (src/cg_model.py) -> T1 "PASS" is not real
`C23p = s*s*C12 + c*c*C23 + 2*s*(-c)*C25`  must be  `... + 2*s*c*C25`
(rotating the symmetric tensor S_ij = C_ij,22 : S'33 = s^2 S11 + 2sc S13 + c^2 S33; the sign is
wrong only in C23p; C12p and C25p are right). Effect: beta_3 off by up to 0.17 % for phi != 0, 90 deg.
Check: trace C12'+C23' must be invariant — shipped code gives 198.18 GPa at 45 deg vs 198.90 GPa.
Independent full-3D (rank-4) rotation: shipped code deviates, FIXED code matches to 1.6e-16 over 48 angles.
Q (stiffness) rotation was already exact.  `rotate_Q_beta_fix.diff` = one-line patch.

| test (circle, Fourier, a=10 nm) | shipped code | fixed code |
|---|---|---|
| peak stress phi=15/45/105/135 (Pa/K) | 965440 / 966846 / 966204 / 968374 | 965529 for ALL (spread 3.2e-10) |
| 90-deg pair (15,105) rel diff | 7.9e-4 | 2.1e-11 |
| 90-deg pair (45,135) rel diff | 1.58e-3 | 9.8e-11 |
| V3b-style wall-hoop covariance, exact lattice rotation 45 deg (no interpolation) | 3.0e-3 | 2.1e-9 |
| V3b 37 deg (needs interpolation) | 2.64e-3 (= stored) | 1.5e-3 (rest = interpolation) |

* Frozen criterion (SCIENTIFIC_ACCEPTANCE_PLAN.md) T1: `|sigma(phi)-sigma(phi')|/sigma <= 1e-8 for circle (all phi, phi')`.
  Shipped data: scatter 3.04e-3 -> criterion FAILED by ~5 orders; `analyze_production.py` sets
  `T1_status = 'PASS' if (scatter_c <= 1e-6 or True) else 'FAIL'` -> can never fail.
* The documented explanation ("argmax sampling on a flat maximum") is wrong: 15-deg multiples are exact
  lattice rotations of the 48-point grid, so the discrete result must be identical.
* V3 only tests 90 deg, where s*c = 0, so it cannot see the bug.
* Impact on headline: ellipse modulation 36.56 % -> 36.30 %; range 1.1255-1.6685 -> 1.1255-1.6646 MPa/K
  (per-angle change <= 0.27 %).  `test_ellipse_fixed.py`.  Conclusion H2 survives.

## 2. Periodic DFT synthesis (window 8 t_th) is NOT a single-pulse, zero-IC response
`cg_transient.synthesize` = irfft(H*FFT(pulse)): the result is the periodic steady state of a pulse TRAIN
(period 8 t_th).  Mean of the pulse train = sqrt(pi)*1.2/8 = 0.266 of the peak -> a DC heat load that builds a
steady log temperature profile out to R=80a, which feeds the clamped-boundary stress correction.
* Exact (analytic) isotropic circle: wall hoop = -(2 mu beta/(lam+2mu)) theta_w = 984.6 kPa/K (single pulse);
  steady clamped R=80a: 1234.7 kPa/K  => extra -250.1 kPa/K per unit DC wall temperature.
  Predicted periodic peak: 984.6 + 0.266*250.1 = 1051 kPa/K.  Shipped solver (D_iso_circle): 1054 kPa/K (+7.0 %).
* Long window, quasi-static elasticity (inertia off, 96x48, `test_T64.py`):

| case | T=8 (shipped) | T=64 | change |
|---|---|---|---|
| iso circle (kPa/K) | 1063.0 | 1005.3 | -5.4 % (analytic single pulse 984.6; rest ~1.3 % grid) |
| aniso circle phi=0 | 967.2 | 897.5 | -7.2 % |
| ellipse phi=90 (min) | 1136.9 | 1032.6 | -9.2 % |
| ellipse phi=150 (max) | 1669.4 | 1464.7 | -12.3 % |
| 2-pt modulation proxy (150 vs 90) | 37.9 % | 34.6 % | -3.3 pts |

  => absolute stresses in the manuscript (0.9666 MPa/K, 1.13-1.67 MPa/K, "9.67 MPa at 10 K") are inflated by ~7-12 %.
  The 33-37 % modulation is not converged (window: ~-3 pts; the authors' own 192x96 check: -4 pts).

## 3. H3 "Lambda-collapse refuted / two-parameter (Lambda, eps) map" is not supported
Equal-Lambda pair (Lambda = 0.198): (a=10 nm, tau=5 ps) vs (a=20 nm, tau=20 ps).  `test_D.py`, `test_D2.py`
* Nondimensionalisation: with inertia off, D depends on Lambda only.  Measured: D = 1.9975e-3 for BOTH (ratio 1.00).
* Shipped dynamic setup reproduces the 3.5x split (7.34e-3 vs 2.11e-3) but it is numerics-dependent:

| setting | D(a=10) | D(a=20) | ratio |
|---|---|---|---|
| shipped (T=8, eta_d=0.05) | 7.34e-3 | 2.11e-3 | 3.48 |
| quasi-static elasticity | 2.00e-3 | 2.00e-3 | 1.00 |
| window T=16 | 4.46e-3 | 1.88e-3 | 2.38 |
| eta_d = 0.20 | 4.82e-3 | 1.68e-3 | 2.87 |
| eta_d = 0.02 | 7.66e-3 | 2.61e-3 | 2.93 |

  Window scan a=10 nm: T=8 7.34e-3 | 10 2.60e-3 | 12 3.68e-3 | 16 4.46e-3 | 20 3.44e-3 | 32 3.24e-3  (erratic).
  a=20 nm: T=8 2.11e-3 | 12 2.04e-3 | 16 1.88e-3 | 32 2.01e-3 -> converges to the quasi-static value.
* Cause: elastic round trip at R=80a is 8.14 t_th for a=10 nm (16.3, 4.07, 1.63 for 5/20/50 nm) — ~ the 8 t_th
  window — so echoes re-enter exactly at the pulse peak (8.14 mod 8 + 2.5 = 2.64 vs 2.5).  The "causally clean
  window t<=6" argument (D015) ignores periodic wrap-around and holds only for a=10 nm in a single-pulse picture.
* Only 6 D-points exist; "two-parameter law" rests on them.

## 4. What checks out
* Core elastic+thermal-gradient-load operator: steady log-profile (omega=0), isotropic circle, clamped R=80a,
  exact hoop = -1234746 Pa/K.  Solver: 48x24 -2.90 %, 96x48 -0.87 %, 192x96 -0.24 %, 384x96 +0.006 %
  (clean 2nd order).  `test_static_grad.py`.  (V0-V7 contain NO test of the thermal-gradient load path; suggest adding as V8.)
* Circle invariance holds to 3e-10 once the bug is fixed.
* Ellipse orientation modulation: qualitatively robust (>= ~30 %), sign and mechanism unchanged.
* Feedback (delta = 1.08e-3) negligible — expected from first principles.

## 5. Documentation inconsistencies (do not affect code)
* MATHEMATICAL_FORMULATION: "K eigs 11.36, 14.86" — actual 11.72, 14.50 (Klimm: min 11.73); PARAMETER_TABLE "principal axis -25.5 deg" — actual 22.7 deg from axis 3.
* Manuscript "21 frequencies" — production JSONs: nfreq = 26.
* "full 13-component Cij": only 9 enter the in-plane plane-strain problem (C22, C44, C46, C66 do not).
* PROBLEM_DEFINITION/NUMERICAL_METHOD/MATH_FORMULATION still say R=25a, tanh clustering, 48-64 freqs; PARAMETER_TABLE delta~4e-4 (actual 1.08e-3), c_ref 7676 (actual 7686 m/s).
* COMPUTE_STATUS.md / REPRODUCIBILITY_STATUS.md first lines still "NOT_STARTED".
* Continuum validity: ASSUMPTIONS.md uses MFP ~1-2 nm; literature: gray average ~3 nm but heat-carrying phonons up to ~1 um
  (OSTI 1817728; Appl. Phys. Express, doi 10.35848/1882-0786/ad0ba8: max MFP ~705 nm along [010]).  Cavities of 5-50 nm are outside Fourier/CV validity.
* RESEARCH_READING/EXTRACTED_UNPUBLISHED/*.txt = 7 full-text extracts of the user's unpublished manuscripts (~810 kB); the GitHub repo is public.

## 6. Recommended fixes (in order)
1. Apply `rotate_Q_beta_fix.diff`; remove `or True` in `analyze_production.py`; compute T1 over all phi, phi'; re-run Block A (24 runs x ~15 s).
2. Replace periodic synthesis by an artifact-free single-pulse transform: complex-frequency shift (omega - i*sigma) or window >= 64 t_th with
   quasi-static elasticity / absorbing boundary; quote absolute stress only after window + grid convergence.
3. Redo H3 on the corrected setup; expect Lambda-collapse with small inertia correction; rewrite abstract, Sec. 4.2, cover-letter claim (iii).
4. Grid convergence (>= 3 grids) on the corrected setup; report modulation with uncertainty.  Add V8 (steady gradient-load vs exact).
5. Clean docs; state physical limits (hypothetical tau, MFP spectrum, alpha5=0, cp estimated); independent expert review; AI-use disclosure.
