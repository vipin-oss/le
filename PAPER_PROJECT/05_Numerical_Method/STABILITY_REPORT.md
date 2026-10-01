# STABILITY_REPORT — Phase 9 (2026-10-01)

- Solver backward error (relative, after 2 refinement steps): max over all production runs = 7.226266702964897e-17; wall-pulse reconstruction error: max = 1.0054844078071441e-10 (≤ 6.3e-9, inversion check in every run).
- Inversion plan: alias e^{−γ_B T} = 1.5e-8; round-off growth e^{γ_B t} ≤ 5e4 up to t = 12 (negligible vs 1e-16 × condition); plan independence C2 above.
- Resonance handling: the undamped finite domain has real-axis resonances; the contour Re s = γ_B = 0.9/t_th keeps the integrand smooth (frequency spacing 0.31 < 0.9). No damping device is used.
- Conjugate symmetry H(s̄) = conj H(s): 1.7e-15 (V12). τ → 0 limit: 4e-7 (V5). Rotation covariance 6e-14 (V3).
- Memory: 192×96 solves need ≈ 0.7–1.0 GB (one such job at a time in the 2 GB environment); the single out-of-memory event (verification run 2) was a scheduling error, not a numerical instability.
- Condition number: not computed explicitly (the refinement experiment shows the forward-error floor 1e-8 → 1e-14, which bounds the effective conditioning).
