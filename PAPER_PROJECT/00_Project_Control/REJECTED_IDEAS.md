# REJECTED_IDEAS — this session (2026-10-01); handoff history in `/home/user/work/handoff/REJECTED_IDEAS.md` (MASTER_PROMPT §61)

| Idea | Rejection reason | Evidence | Revisitable? |
|---|---|---|---|
| Keep the handoff's periodic-DFT synthesis (window 8 t_th) and only fix the rotation sign | returns the periodic steady state of a pulse train (mean 0.27 of the peak) → absolute stresses +7–12%; H3 depended on window and damping | review tests T64/D/D2 (`/home/user/work/rerun/`), tests U4–U8, V11 | no |
| Long-window (T ≥ 64 t_th) quasi-static elasticity as the production route | a model change (drops inertia) and still biased: the 2-D diffusion tail decays only like 1/t, so the pulse-train bias converges slowly (−7.2% at 64 t_th, not converged) | `/home/user/work/rerun/T64_*.log` | only as the quasi-static *ablation* (done) |
| Hysteretic damping η_d = 0.05 as a regulariser | not causal, changes with window, was only needed because of the periodic synthesis; the complex-frequency contour removes the need | P7-D002; handoff D014g; review D-tests | no |
| Explain the circle's 0.30% peak scatter as "argmax sampling on a flat peak" | wrong: 15° multiples are exact lattice rotations; the cause is the sign error in `rotate_Q_beta` | V3, V3p, V3d; review `test_rot_fix.py` | no |
| Take T1 from the single (0°, 90°) pair | blind to the sign error (s·c = 0 there) | V3p: 6e-14 at 90° vs 3.0e-3 at 45° | no |
| Radial clustering γ = 3.5 (handoff) | near-wall resolution controls the ellipse-tip stress (−12% change at γ = 5; orders 0.8–1.35 at γ = 3.5) | C4, `convergence_gamma3p5/` | no |
| 192×192 grid for the ellipse | exceeds the 2 GB memory of the environment (192×96 needs 0.7–1.0 GB; OOM at the concurrent run) | run-2 OOM kill | yes, on a larger machine |
| Normalising displacement covariance by max(|u|, |θ|) | unit mix → blind to displacement/stress errors (handoff V3 and my run-1 V3) | V3 run 1 vs run 4 | no |
| Unweighted worst-case high-frequency transfer-function test (V9 run 1) | dominated by content with weight ≈ 1e-10 in the pulse spectrum | run-1 log; V9a/V9d | no |
| Citing "Tzou (1995)" as the 1997 book and the "ACS Omega 2021" Debye-temperature source | metadata mismatch / source not identifiable | Crossref verification | no |
| Quoting a single expansion set as established | α is secondary-quoted and ≈10× different at 298 K in synchrotron data | search #2; block E1 | — (kept as sensitivity) |
| "Locality (thin-layer) explains the orientation modulation of the ellipse" | block F: modulation falls only from 32.0% to 24.8% when t_w drops by a factor 8; thin-layer limit unreachable (layer ≳ tip radius); isotropic ellipse already 1.5× the isotropic circle | `ANALYSIS_V2_TABLES.md` §F | yes — needs t_w ≪ 0.1 t_th (several hundred solves per run) |
| Treat the echo as the main cause of the dynamic D excess | for a = 10 nm the echo is outside the window yet the dynamic D is 2.6× the quasi-static one; excess scales ≈ ε² (inertia) | extended map, slopes | no |
| Quote one modulation number from the 12-orientation sweep on a single grid | amplitude depends on grid by up to 3 points (R48 33.0%, M 29.9%, R192 29.0% on 6 φ) | convergence report | no |
