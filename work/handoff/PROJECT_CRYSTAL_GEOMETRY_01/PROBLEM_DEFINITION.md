# PROBLEM_DEFINITION — Phase 1
Project: PROJECT_CRYSTAL_GEOMETRY_01 | Date: 30 September 2026 | Master: MASTER_PROMPT v2.1
Label: research phases (production within pre-approved compute; see COMPUTE_STATUS.md)

## Working title
Size-dependent crystal–geometry symmetry mismatch in monoclinic β-Ga2O3: coupled thermoelasticity with generalized heat conduction around circular and elliptical cavities

## Research type (§15)
**Computational scientific study** with analytical verification anchors.
Evidence route: verified implementation + credible model + controlled comparisons + baselines + robust findings (primary). Physical validation: NOT available (no experiments supplied; literature datasets are transport/elastic only) — recorded scientifically, not for convenience.

## Research question (falsifiable)
How do crystal orientation (monoclinic β-Ga2O3 tensors) and cavity geometry (circle vs equal-area ellipse) interact to shape the transient thermoelastic response around a heated cavity — and at what cavity sizes / memory times do generalized (CV, MCV3-type) heat-conduction laws produce resolvable changes relative to Fourier thermoelasticity?

## Objective
1. Formulate coupled anisotropic generalized thermoelasticity (plane strain, a-c crystal plane) around circular/elliptical cavities with prescribed wall-temperature pulse, traction-free wall.
2. Verify solver against exact/limiting checks (V1–V7, VERIFICATION_PLAN.md).
3. Quantify: peak hoop stress and its angle/time, angular mode content, temperature-layer growth, phase lags — as functions of crystal angle φ, aspect ratio χ, memory Λ=τκ/a², inertia ε=κ/(c_ref·a), coupling on/off, thermal model (Fourier/CV/MCV3).
4. Deliver honest conclusions incl. null results (e.g., weak thermoelastic feedback δ~4e-4 expected → coupling feedback may be negligible; bound it).

## Hypotheses (pre-hoc)
- H1 (confirmatory): for a circular cavity in a monoclinic anisotropic crystal with rotation-covariant load, the FIELD is non-axisymmetric but rotation-covariant; σ_max is rotation-invariant (exact numerical identity expected <1e-10 rel.).
- H2 (confirmatory): peak hoop stress and its angular position change measurably with crystal angle φ for the ellipse (symmetry mismatch); for the circle, φ rotates the pattern without changing σ_max.
- H3 (confirmatory): generalized models deviate from Fourier in a size-dependent way governed mainly by Λ=τκ/a²; deviation collapses when plotted vs Λ (tests memory-similarity).
- H4 (confirmatory-null): thermoelastic feedback on the temperature field is bounded by ~δ (dimensionless coupling ~1e-3 for β-Ga2O3); report bound, do not oversell.
- H5 (exploratory): angular mode content m≥2 grows with anisotropy×χ interaction.

## Geometry / loading (per THERMOELASTIC_DIRECTION_NOTE.md, refined)
- 2D plane strain, long solid along crystal b-axis; cross-section = a-c crystal plane.
- Central cavity: circle (radius a) or equal-area ellipse (a√χ × a/√χ, χ=2); outer computational boundary: circle radius 25a (no reflections within analysis window; verified causally).
- Loading: prescribed wall-temperature pulse θ_w(t)=exp(-((t-t0)/tw)²), t0=2.5 t_th, tw=1.2 t_th (t_th=a²/κ̄); traction-free cavity wall; u=0, θ=0 at outer boundary; zero ICs. WALL-TEMPERATURE BC chosen over flux BC: well-posed for memory models (no flux-BC evolution condition needed); consistent with closest prior cavity literature (decaying thermal field on hole boundary). RECORDED DECISION.
- Crystal orientation φ ∈ {0,15,...,165}°: rotation of ALL material tensors (K, C, β) together — never K alone.

## Materials
Primary: monoclinic β-Ga2O3 (space group C2/m, unique axis b), REAL data where verified (PARAMETER_TABLE.md): full 13-Cij (Adachi 2018, full-text), K a-c plane incl. K13 (Klimm 2023, full-text read earlier), α_a,b,c (2015, abstract), ρ (metadata). α5 (thermal shear): unmeasured → 0, LIMITATION. c_p: ESTIMATED (Debye). Memory τ_q etc.: HYPOTHETICAL parameters (no measured thermal-relaxation data for β-Ga2O3 located) → dimensionless-study label per direction note.
Comparator: isotropic control with matched mean moduli (ablation B1). No second real material (scope control).

## Variables / outputs
Primary QoIs: (Q1) max hoop stress σ̂ on cavity wall + angle θ* + time t*; (Q2) angular Fourier modes of σ_θθ (m=1..8); (Q3) wall-temperature-layer thickness & peak θ gradient at t=t0+tw; (Q4) phase/timing offsets between θ and σ peaks.

## Novelty boundary (claims allowed/forbidden)
Allowed (if evidence holds): first systematic φ×χ×Λ study for monoclinic-crystal + circular/elliptical cavity transient generalized thermoelasticity; size-dependent validity map of Fourier; symmetry-covariance audit; upper bound on coupling feedback.
Forbidden: "new theory of heat conduction"; physical validation claims; β-Ga2O3 device design claims; Q1/journal guarantees; claims beyond linear small-strain, small-ΔT, continuum range (a ≥ 5 nm flagged; below that continuum assumptions fail).

## Expected outputs
Verified solver + convergence data + production matrix (~50 harmonic runs, 48–64 freq each, 96×48 grid + refinements), 8–12 figures, tables, manuscript draft (Phase 13).
