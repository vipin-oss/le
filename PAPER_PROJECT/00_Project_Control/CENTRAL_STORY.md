# CENTRAL_STORY (MASTER_PROMPT §47) — 2026-10-01



1. **Problem.** How do crystal orientation, cavity shape and heat-conduction law (Fourier vs relaxation-time) interact in the transient thermoelastic stress around a cavity in a low-symmetry crystal (monoclinic β-Ga₂O₃, plane strain in the a–c plane)?

2. **Existing limitation.** Cavity studies with finite heat-wave speed treat isotropic or highly symmetric media and circular/spherical geometry; studies of general anisotropy and non-circular holes are steady/quasi-static (bounded search, PROVISIONAL). In addition, the preliminary internal analysis from which this work started contained a rotation-tensor sign error, a periodic-pulse-train synthesis and an under-resolved wall mesh, so none of its numbers could be used.

3. **Proposed solution.** A verified computational study: frequency-domain mapped-grid solver evaluated at complex frequency; single-pulse response by Bromwich inversion (verified against exact/independent solutions); mesh-direction study and Richardson uncertainty; ablations (isotropic K, C, α; expansion set; quasi-static; feedback off; pulse width).

4. **Scientific mechanism.** The peak wall stress is, to ≈ 10⁻³ in the far-field term, a local–instantaneous constraint response (isotropic Lamé closed form). The circle peak is orientation-invariant (4.6e-15); the ellipse breaks locality (iso ellipse ≈ 1.5× iso circle) and its orientation modulation depends only weakly on the heated-layer thickness (pulse-width test) — a non-local interaction of the heated region with the cavity shape; the thin-layer limit is not reached. Thermal memory enters the wall stress only through the weak far-field term; in the quasi-static uncoupled limit D depends on Λ alone (exact scaling).

5. **Main evidence.** Circle peak 0.854 MPa/K (extrapolated); ellipse modulation 28.7% (six-orientation, extrapolated; grid M 12 φ: 29.9%; u_num 1.31%; T4 RESOLVABLE); D ≤ 6.38%; quasi-static equal-Λ residual 0.0000% (SUPPORTED), dynamic residual 51.6% (NOT-SUPPORTED); feedback WITHIN-BOUND; ablation ratios (amplitude / baseline): E3_K_iso=0.94, E4_C_iso=1.57, E2_alpha_iso=0.72, E1_alpha_cheng298=1.03; pulse-width test A₂ = ['24.8%', '27.7%', '30.0%', '32.0%'] for t_w = [0.3, 0.6, 1.2, 2.4].

6. **Main finding.** Crystal orientation matters for the stress around a non-circular cavity (≈ 29% modulation of the peak wall stress for an axis ratio of 2) but not for a circular one; the heat-conduction law has a bounded, small effect (≤ 6.4%) on this observable. Absolute stress scale is parameter-uncertain (α) by more than an order of magnitude (factor ≈ 16 between two literature-based expansion sets). Thermal-memory runs were made for the circular cavity only.

7. **Why it matters.** (i) A verification-grade route to single-pulse responses from frequency-domain solvers and a cautionary example of how a periodic synthesis and an unseen rotation-sign error inflate/blur results; (ii) shows that wall stress under a prescribed wall temperature is a poor discriminator of non-Fourier conduction → guides which observables to study; (iii) quantifies when crystal orientation must be considered for cavity-containing β-Ga₂O₃ components (relative, not absolute, statements).

8. **Exact novelty (bounded).** The combination: monoclinic crystal × circular/elliptical cavity × orientation sweep × thermal-memory parameter × transient coupled thermoelasticity × verification chain with uncertainty (not a claim of priority).

9. **Evidence supporting novelty.** `01_Literature/SEARCH_LOG.md` (11 logged searches + handoff searches), `REFERENCES_VERIFIED.md`; closest works: Chao & Gao 2001 (steady, elliptic, anisotropic), Shiah & Liu 2026 (BEM, anisotropic holes), Abbas et al. 2015/2022 (generalized, circular/cylindrical).

10. **What the work does NOT claim.** No physical validation; no validity of Fourier/CV conduction at 5–50 nm; no measured relaxation times; no absolute stress predictions for real devices (α uncertain by more than 10×, c_p assumed); no 3-D, nonlinear, or temperature-dependent effects; no interior-stress or heat-flux conclusions; no priority claim; no expert review yet.
