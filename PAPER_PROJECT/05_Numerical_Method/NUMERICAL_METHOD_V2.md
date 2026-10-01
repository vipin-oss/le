# NUMERICAL_METHOD_V2 — single-pulse (zero-initial-condition) time response by Bromwich inversion

Phase 7 · 2026-10-01 · status: IMPLEMENTED and VERIFIED (evidence: `07_Tests/TEST_REPORT.md`, tests U4–U8, V9, V11; `05_Numerical_Method/CONVERGENCE_REPORT.md`).
Change record: DECISION_LOG P7-D002, CHANGELOG 2026-10-01. **Unchanged:** governing equations, constitutive laws, BCs, ICs, geometry, material parameters, spatial discretisation (conservative mapped-grid finite differences), the frequency-domain solver `HarmonicSolver`. **Changed:** only the reconstruction of the time-domain response from the frequency-domain transfer values, plus removal of the hysteretic damping that existed solely to make that reconstruction well-behaved.

## 1. Problem as defined (initial condition)
Wall-temperature pulse p(t) = exp(−((t − t0)/tw)²), t0 = 2.5, tw = 1.2 (units of t_th = a²/κ̄), applied to a medium that is at rest at the reference temperature before the pulse (zero initial conditions; p is taken on the whole real line, so no truncation step appears at t = 0). Cavity wall: θ = p(t), traction-free. Outer boundary at R = 80a: θ = 0, u = 0.

## 2. What the handoff pipeline computed instead
`cg_transient.synthesize` evaluated `irfft(H(ω_k) · FFT(p)_k)` on a periodic window of T = 8 t_th (k ≤ 25). That is the **periodic steady state of a pulse train of period T**, not the response of a quiescent medium to one pulse:
- the train has mean θ̄ = √π·tw/T = 0.266 of the peak, a DC wall temperature that builds the steady logarithmic temperature profile out to R = 80a and a clamped-boundary stress correction;
- previous pulses and elastic echoes wrap around (the elastic round trip at R = 80a is 8.14 t_th for a = 10 nm, i.e. one window length);
- evidence (review, 2026-10-01): isotropic circle, exact single-pulse wall hoop 984.6 kPa/K vs shipped 1054 kPa/K (+7%); window 8 → 64 t_th lowered the anisotropic circle by 7.2% and the ellipse extremes by 9–12%.
The undamped finite-domain resonances made harmonic sampling erratic, which is why the handoff added hysteretic damping η_d = 0.05 (D014g). That damping was a numerical regulariser, not a material property.

## 3. Method
The frequency-domain operator is analytic in s = iw: A(s) = A_base − s² A_in + s A_d + g(s) A_lap with g = 1 (Fourier), 1/(1 + sτ) (Cattaneo–Vernotte / Lord–Shulman relaxation) or ½/(1 + ½sτ) + ½/(1 + 2sτ) (MCV3-type kernel). `HarmonicSolver.solve(w)` already accepts complex w, so passing w = −i s/t_th with Re s = γ > 0 evaluates the same operator on a vertical line of the Laplace plane, away from the imaginary-axis resonances of the undamped finite domain. With Y(s) = H(s) P(s) and the two-sided Laplace transform of the pulse

  P(s) = √π · tw · exp((s·tw/2)² − s·t0)       (entire; no truncation of the Gaussian)

the response is recovered by the trapezoidal Bromwich sum

  y(t) = (e^{γt}/T) · [ Y(γ) + 2 Re Σ_{k=1..K} Y(γ + iω_k) e^{iω_k t} ],   ω_k = 2πk/T.

The real-system symmetry Y(s̄) = conj Y(s) holds because K, Q, β, ρ, c_p are real once the hysteretic damping is removed (test V12, 9e-14). The same plan is used for wall θ (returns the Gaussian to 6e-9, a built-in accuracy check in every run), wall hoop stress, and radial probes.

## 4. Error control
| Source | Size | Control |
|---|---|---|
| alias of the periodised inverse | ≈ e^{−γT}·|y(t+T)|; images with n ≤ −1 are negligible (Gaussian pre-history < 1e-20 for t < t0 − 5.5·tw...) | defaults T = 20, γ = 0.9: e^{−18} = 1.5e-8; valid for 0 ≤ t ≤ T − 5.5 = 14.5 |
| spectral truncation | |P(s_K)|/|P(s_0)| < 1e-10 | K = ⌈ω_max T/2π⌉ with ω_max = √(γ² + 4 ln(1/ε)/tw²) → K = 26 (27 solves) |
| round-off growth | e^{γt}·1e-16: 5e4·1e-16 at t = 12 | window used ≤ 12 t_th |
| resonance sampling | resonance width ≈ γ = 0.9 vs spacing Δω = 0.314 | integrand smooth; no damping needed |
Verification: identity transfer H = 1 returns the Gaussian (6.3e-9, U4); a damped oscillator H = 1/(s² + 2ζω₀s + ω₀²) matches DOP853 time integration (5.0e-9, U5); results are unchanged between (T, γ) = (20, 0.9) and (32, 0.6) (4.7e-9, U6); Laplace-domain 1-D spectral solution + this inversion equals an independent time-domain Crank–Nicolson heat solve with closed-form quasi-static stress to 6.5e-7 (U8).

## 5. Consequences for the model
1. **No hysteretic damping.** The model is now the undamped linear coupled thermoelastic model in the finite domain R = 80a. Elastic echoes are therefore physical features of that finite domain: first return of the longitudinal wave to the wall at t_echo = 2(R/a − 1)·ε t_th with ε = κ̄/(c_ref a): 16.3, 8.14, 4.07, 1.63 t_th for a = 5, 10, 20, 50 nm. The pre-registered QoI window t ≤ 6 t_th is therefore echo-free only for a ≤ 10 nm (and the peak, at t = t0 = 2.5, for a ≤ 20 nm). Sensitivity to R is quantified in Phase 9 (C3); the inertia-off ablation isolates thermal memory from elastic inertia.
2. **QoI definitions** (pre-registered window unchanged): peak |hoop stress| over wall angle and 0 ≤ t ≤ 6 t_th. New in this version: the angular maximum is taken on a trigonometrically interpolated (16×) wall profile in addition to the nodal value, because nodal quantisation of the angular maximum is O(Δϑ²) and erratic on coarse grids; both are stored (`sig_nodal`, `sig_interp`).
3. **Dimensionless structure.** In the quasi-static, uncoupled limit the problem depends on (Λ = τκ̄/a²; geometry; crystal) only; inertia adds ε = κ̄/(c_ref a), the feedback adds δ = T0 β·β/(ρ c_p C̄) = 1.078e-3.

## 6. Cost (96×48 grid, 2 vCPU): 27 complex solves ≈ 14 s per run (handoff: 26 solves ≈ 13–17 s); 192×96 ≈ 100 s; 48×24 ≈ 3 s.
