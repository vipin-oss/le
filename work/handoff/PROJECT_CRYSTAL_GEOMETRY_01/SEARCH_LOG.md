# SEARCH_LOG — live literature search (Phase 1, novelty/gap + material data)
Date: 30 September 2026 (Asia/Calcutta). Tool: Arena web_search (live). All queries and results recorded per MASTER_PROMPT §9–10. Snippet-level results cannot support equation claims; verification levels noted.

## Q1 [depth=2] "generalized thermoelasticity anisotropic elliptical cavity thermal stress dual-phase-lag"
- R1.1: DPL + fiber-reinforced anisotropic medium + circular hole (Mech Based Design Struct Mach 43(4), 2015, DOI 10.1080/15397734.2015.1029589). FEM; decaying thermal field on hole boundary; isotropic exact solution discussed. Level: ABSTRACT.
- R1.2: DPL thick beams, harmonic loads (2018). Level: ABSTRACT/snippet.
- R1.3: Karmakar-Sur-Kanoria 2016, DPL spherical cavity isotropic (DOI 10.1134/S002189441604009X). Level: ABSTRACT.
- R1.4: JCDE 2021 DPL review (Open Access). Level: snippet.
- R1.5: fractional DPL with voids (2025). Level: ABSTRACT.
→ Takeaway: generalized (DPL/LS) + cavity exists for ISOTROPIC or fiber-reinforced cases, mostly spherical/circular; no crystal-orientation × cavity-shape mismatch study found.

## Q2 [depth=2] "monoclinic anisotropic thermoelasticity circular hole stress concentration thermal"
- R2.3: "Thermal stress analysis of infinite anisotropic plate with elliptical hole under uniform heat flux" (2016) — Lekhnitskii complex potentials, STEADY state, anisotropic, elliptical hole. Level: snippet. CLOSEST geometric-analog; steady Fourier only.
- R2.3 also cites Chao & Gao 2001 (anisotropic thermoelastic body, elliptic hole, mixed BVP) — Level: snippet.
→ Takeaway: steady anisotropic elliptical-hole thermoelasticity EXISTS (classical). Gap remains for transient generalized (memory) + orientation-mismatch + coupled dynamics.

## Q3 [depth=2] "Goodier thermoelastic stress circular hole uniform heat flow hoop stress solution"
- R3.1: Florence & Goodier, "Thermal stress at spherical cavities and circular holes in uniform heat flow", J. Appl. Mech. 26 (1959) 293–294. Level: snippet (bibliographic).
- R3.1/3.5: Florence-Goodier 1960 "Thermal stresses at an insulated ovaloid hole" (elliptic hole closed form) — Level: snippet (bibliographic).
- R3.2: Goodier-Florence 1966 chapter. Level: snippet.
→ Takeaway: classical steady benchmarks EXIST for isotropic circular/ovaloid holes under uniform heat flow — used as SECONDARY verification anchors (steady limit). Primary verification uses our own exact annulus/log + conformal checks.

## Q4 [depth=1] "beta-Ga2O3 thermoelastic stress cavity wave propagation 2025 2026"
- No β-Ga2O3-specific thermoelastic cavity work found (returned unrelated magneto-micropolar media papers 2026). Level: ABSTRACT.
→ Takeaway: no scooping evidence for the material×geometry application; absence-of-evidence only (search bounded).

## Q5 [depth=2] "beta-Ga2O3 single crystal elastic constants c11 c22 c33 monoclinic stiffness tensor experimental"
- R5: Adachi, Ogi, Takeuchi, Nakamura, Watanabe, Ito, Ozaki, "Unusual elasticity of monoclinic β-Ga2O3", J. Appl. Phys. 124, 085102 (2018), DOI 10.1063/1.5047017. Complete 13 Cij via RUS/LDI. Open PDF at Osaka repository FETCHED (full text of matrix + values verified).
- Other sets in snippets (DFT sets; one "C11=222..." set is from a DIFFERENT paper — NOT used).
→ Takeaway: FULL elastic tensor verified (level: EQUATIONS). Source: https://ir.library.osaka-u.ac.jp/repo/ouka/all/84235/JApplPhys_124_8.pdf

## Q6 [depth=1] "beta-Ga2O3 thermal expansion coefficients anisotropic lattice parameters temperature"
- R6.1: "Thermal expansion coefficients of β-Ga2O3 single crystals" (2015): α_a=1.54e-6, α_b=3.37e-6, α_c=3.15e-6 1/K (300–700 K linear). Level: ABSTRACT.
- R6.2: Cheng-Hanke, synchrotron XRD 298–1200 K (2018): α_a nonlinear 0.10–2.78e-6; α_b, α_c ≈ 2×α_a. Level: ABSTRACT.
→ Takeaway: anisotropic expansion verified at ABSTRACT level (300–700 K values used). Shear expansion α5 in a-c plane: NOT measured in located sources → set 0, LIMITATION recorded.

## Q7 [depth=1] "beta-Ga2O3 density 5880 kg/m3 specific heat capacity J/gK room temperature"
- R7.1: Springer "Thermal Properties" chapter (2020): c_p(RT)=18.7 J/mol K [ABSTRACT] — physically anomalous vs Dulong-Petit (3nR=124.7 J/mol K); flagged, NOT used uncritically.
- R7.2: ρ = 5880 kg/m³ (compiled crystallographic density) [metadata-level]. Consistent with ACS Omega paper's 5.9e3 kg/m³.
→ Takeaway: ρ verified (metadata, 2 independent compilations). c_p UNRESOLVED → ESTIMATED via Debye ΘD=685 K (ACS Omega 2021, snippet) → c_p(300K)≈105 J/mol K≈560 J/kg·K, labeled ESTIMATED; sensitivity documented.

## Q8 [depth=2] "Ga2O3 heat capacity J mol 300 K calorimetry heat capacity of beta-Ga2O3 first principles"
- No primary c_p measurement obtained (only In2O3). c_p remains ESTIMATED as above.

## Gap statement (pre-hoc, to be tested against closest-five during Phase 2)
Located work covers separately: (a) steady anisotropic thermoelasticity of elliptical holes (Lekhnitskii; Florence-Goodier isotropic ovaloid); (b) generalized/DPL thermoelasticity of circular/spherical cavities, isotropic or fiber-reinforced. NOT located (as of 30 Sep 2026, bounded search): transient COUPLED generalized-heat-conduction thermoelasticity around circular vs elliptical cavities in a real MONOCLINIC crystal with systematic crystal-orientation vs cavity-orientation symmetry-mismatch analysis, incl. size-dependent memory relevance. Novelty claim remains PROVISIONAL (level: bounded search, mostly abstract) — full-text comparison with R2.3/R1.1 required before manuscript novelty claims (Phase 12-13 gate).

## §live-2026-09-30 — Fresh gap + prior-work verification searches (Phase 11)
Date: 30 September 2026. Tool: web_search (depth 1–2).
Q1 "thermoelastic elliptical cavity anisotropic crystal orientation transient 2024 2025 2026" (depth 2) → 5 results, all unrelated (FEL crystal optics, crystal plasticity FE, thermosalient molecular crystals, NLC). No cavity+anisotropy+memory combo. GAP HOLDS.
Q2 "generalized thermoelasticity thermal relaxation cavity gallium oxide Ga2O3" (depth 2) → 5 results, all Ga2O3 thermal-conductivity measurement/computation (TDTR/DFT). NO thermoelastic cavity work for Ga2O3. GAP HOLDS.
Q3 "elliptical hole OR elliptic hole thermoelastic anisotropic plate thermal stress concentration" (depth 2) → Chao-Gao-2001 IJSS (steady anisotropic ellipse, ABSTRACT captured), thermoelectroelastic elliptic hole 1999 (ABSTRACT), multiple-inclusion thermo-elastic 2013 (ABSTRACT), TSA-SCF works. Transient+memory ellipse absent.
Q4 "Green-Lindsay OR dual phase lag thermoelastic cavity hole thermal shock fiber reinforced" (depth 2) → MDSN-2015 DPL fiber circular hole (ABSTRACT captured — closest prior work #1), orthotropic cylindrical-cavity generalized thermoelasticity family (ABSTRACT level), hollow-cylinder/sphere FEM works. No ellipse+orientation+memory map.
Q5 "Chao Gao 2001 elliptic hole anisotropic thermoelasticity boundary value problem" (depth 1) → metadata + abstract verified: IJSS 38 (2001) 5975–5994, DOI 10.1016/S0020-7683(00)00403-0 (ABSTRACT level).
Q6–Q8 journal metrics queries (see JOURNAL_SCREENING.md).
Verification levels recorded in PRIOR_WORK_COMPARISON_R2.md + JOURNAL_SCREENING.md. Full texts paywalled (MDSN-2015, Chao-Gao-2001) — abstract level only; equation-level comparison NOT claimed.
