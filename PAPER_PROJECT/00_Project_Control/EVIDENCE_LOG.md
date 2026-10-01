# EVIDENCE_LOG (MASTER_PROMPT §58) — 2026-10-01

| Claim | Source | Evidence | Verification level | Limitation |
|---|---|---|---|---|
| Circle peak is orientation-invariant to round-off | ANALYSIS_V2.json T1_H1; tests V3, V3d | spread 4.6e-15 (M), 6.7e-15 (R48) | verified (computed, exact lattice identity) | grid-aligned φ only; non-aligned 37°: 4e-6 (96×48) |
| Circle peak = 0.854 MPa/K | ANALYSIS_V2.json circle_peak | 0.8539 MPa/K extrapolated; M error −0.03% | verified (computed + 3-grid extrapolation) | scale ∝ β = Cα (factor 16 between expansion sets) |
| Ellipse orientation modulation ≈ 29% | ANALYSIS_V2.json T4_H2 | 28.7% extrapolated; 29.9% on M; u_num 1.31 pp | verified (computed; uncertainty quantified) | axis ratio 2, a = 10 nm, Fourier, plane strain |
| Modulation from competing expansion/stiffness anisotropy | ANALYSIS_V2.json E_ablations | ratios K 0.94, C 1.57, α 0.72 | computed (exploratory) | 96×48, six orientations; one tensor at a time |
| Thermal memory D ≤ 6.4% (≤ 1.6% for a ≥ 10 nm) | ANALYSIS_V2.json T2_H3 | max D dyn 6.4% | verified (computed; D accuracy tested vs 1-D) | circular cavity; τ hypothetical |
| Quasi-static collapse of D in Λ is exact | T2_H3 pair_QS; FORMULATION_ADDENDUM §3 | residual 0.0e+00 | analytically checked + computed | quasi-static uncoupled limit |
| Dynamic collapse fails at 52% (O(ε²) inertia) | T2_H3 pair_dynamic; H3_extended_map | 52% | computed; interpretation supported by slopes | inertia vs echo not separated for a ≥ 20 nm |
| Feedback below 5δ | ANALYSIS_V2.json T3_H4 | 6.2e-04 vs 5.4e-03 | computed | probe-based |
| Single-pulse Bromwich inversion verified | TEST_REPORT.md U4–U8, V9d, V11 | peak error 0.07% at 192×96; 6.5e-7 vs time-domain | verified (independent references) | undamped linear model |
| Handoff numbers were biased (periodic synthesis, rotation bug, coarse wall mesh) | CORRECTIONS_LOG.md; REVIEW_FINDINGS.md | circle −11.7%, ellipse range −17 to −26% | verified |  |
| α uncertain by >10× at 298 K | SEARCH_LOG #2 (Cheng 2018 abstract) | α_a ≈ 0.10e-6 vs 1.54e-6 | LITERATURE (abstract level) | full text not read |
| Phonon MFP up to ~0.7–1 µm; continuum validity not established | SEARCH_LOG; Yang 2023 [20] | max MFP ≈ 705 nm (snippet) | LITERATURE (abstract/snippet level) |  |
| IJHMT abstract ≤ 250 words; highlights required; AI declaration required | JOURNAL_FIT.md | official guide snippets | LITERATURE (official page snippet) | highlight length limit from third-party summaries |
| Reference metadata correct | REFERENCES_VERIFIED.md | 23 entries via Crossref | METADATA VERIFIED | no full-text check except Klimm/Adachi values |
