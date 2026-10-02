# NUMERICAL_METHOD_SELECTION + DISCRETIZATION + ALGORITHM + STABILITY (Phase 4)
Date: 30 September 2026.

## Candidates compared
1. Laplace-domain BEM/complex potentials (Lekhnitskii): elegant for steady/anisotropic, but memory models + transient + full coupling + circle↔ellipse morph → heavy analytic work; poor fit to bounded compute; rejected (kept: steady checks via analytic formulas instead).
2. Time-domain explicit FDM/FVM: wave+diffusion CFL on fine grids around nm cavities with t_th≫t_wave → prohibitive step counts; rejected (our pilot 1D FVM experience: 6400 cells × long windows = minutes; 2D × 50 runs too costly).
3. **Frequency-domain FD (FDFD) + FFT synthesis: SELECTED.** Linear system per ω on body-fitted grid; 48–64 freqs per run; transient recovered by DFT. Cost ~2400 sparse complex solves ≈ 30–60 CPU-min total. Matches verification anchors (steady ω=0 exact checks, dispersion checks).
4. Spectral/angular eigenmethods: strong for circle-only isotropic; ellipse+monoclinic+memory loses separability; rejected as primary, angular post-processing still used.

## Discretization (SELECTED)
- Grid: body-fitted TFI polar-type (r,ϑ) ∈ [1,25]×[0,2π): x=A(ρ)cosϑ, y=B(ρ)sinϑ, A=a_e+(R−a_e)ρ, B=b_e+(R−b_e)ρ, ρ=(r−1)/(R−1); circle: a_e=b_e=a. Metrics x_ξ,x_η,y_ξ,y_η by 2nd-order central differences of the analytic map; Jacobian J>0 checked.
- Operators: 2nd-order central FD in computational space with chain rule (strong form); stretched grid (tanh clustering near cavity: cluster factor 0.35).
- Unknowns: U=(θ,u1,u3) at interior nodes; boundary rows: θ-Dirichlet rows at wall/outer replaced; traction-free wall via ghost-free one-sided normal-traction rows (2nd-order); outer u=0 rows.
- Assembly: scipy.sparse COO → CSC; solve per ω with splu (complex128).
- Stress recovery: ε from central diffs of u (2nd order), σ from constitutive law; wall hoop via analytic normal.

## Algorithm
1. Build grid/metrics once per (shape χ, N,M).
2. For each model (g(ω)) and ω_n: assemble A(ω)U=F(ω) (F from wall θ̂ amplitude 1), factorize, solve → transfer functions of probes + wall stress modes + sparse field snapshots.
3. Multiply by pulse spectrum Θ̂(ω_n) (analytic Gaussian FT, exact on grid); Hermitian IFFT → time series.
4. Post: QoIs, modes, plots.

## Stability/accuracy
- Frequency-domain: no time-stepping stability limit; accuracy from (a) FD truncation O(h²) (V2), (b) DFT window/aliasing (pulse spectrum negligible beyond ω_max=Nπ/T — checked: Gaussian tw=t0/2 ⇒ |Θ̂(ω_max)|/|Θ̂(0)|<1e-6 recorded), (c) outer-boundary causality (recorded), (d) splu conditioning at small ω (residual check ‖AU−F‖/‖F‖ ≤ 1e-8 per solve — logged per run).
- Metric quality: min J, orthogonality skew logged; ellipse χ=2 with clustering keeps J>0.

## Compute estimate (§43)
51 harmonic runs × 48 freq × ~1.0 s ≈ 40 CPU-min + verification ≈ 15 CPU-min + figures ≈ 5 min → **~60 CPU-min ≤ 4 CPU-hour threshold** ✓ (NO user approval needed; estimate recorded BEFORE production). Storage ≈ 200 MB < 5 GB ✓. No GPU. 2-CPU sandbox; run serial with BLAS threads=1.
