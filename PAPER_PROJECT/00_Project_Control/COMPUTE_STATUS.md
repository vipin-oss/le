# COMPUTE_STATUS (2026-10-01)
- Hardware: sandbox 2 vCPU (Xeon 2.60 GHz), 1,984 MB RAM, no GPU; Python 3.13.14, numpy 2.3.5, scipy 1.17.1. User hardware: UNKNOWN.
- This session (all runs successful unless stated): review runs ≈ 22 min wall; verification suite runs 1–4 ≈ 7 + 5 + 20 min wall (run 2 killed by the out-of-memory killer, run 3 partial); convergence γ = 3.5 partial ≈ 22 min; mesh-direction study ≈ 8 min; production: 150/141 runs; per-run cost: 3 s (48×24) … 14 s (96×48) … 65 s (96×96) … 157 s (192×96).
- Memory constraint: 192×96 solves need ≈ 0.7–1.0 GB; at most one heavy job at a time (OOM at run 2).
- Cumulative project compute ≈ 2.7 CPU-h (estimate) < 4 CPU-h threshold; storage < 100 MB; failures: OOM (run 2).
