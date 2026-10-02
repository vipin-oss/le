# PARAMETER_TABLE — Phase 1 (with source-verification levels)
All values at ≈300 K unless noted. Verification levels: EQUATIONS (full text equations/tables read) / FULL-TEXT / ABSTRACT / METADATA / ESTIMATED (derived here) / HYPOTHETICAL (no source; study parameter) / UNRESOLVED.

## A. Elastic tensor — monoclinic β-Ga2O3, C2/m, unique axis b (x2)
Source: Adachi, Ogi, Takeuchi, Nakamura, Watanabe, Ito, Ozaki, J. Appl. Phys. 124, 085102 (2018), DOI 10.1063/1.5047017. Method: RUS/LDI (>110 resonances). Level: **EQUATIONS** (matrix form + all values read from open VoR PDF: ir.library.osaka-u.ac.jp/repo/ouka/all/84235/JApplPhys_124_8.pdf).
Voigt basis (x1,x2,x3)=(a,b,c); nonzero pattern (their Eq. matrix): C11,C22,C33,C44,C55,C66,C12,C13,C23,C15,C25,C35,C46.

| Cij | Value (GPa) | ± |
|---|---|---|
| C11 | 242.8 | 2.9 |
| C22 | 343.8 | 3.8 |
| C33 | 347.4 | 2.5 |
| C44 | 47.8 | 0.2 |
| C55 | 88.6 | 0.5 |
| C66 | 104.0 | 0.5 |
| C12 | 128 | 0.1 |
| C13 | 160 | 1.5 |
| C23 | 70.9 | 2.1 |
| C15 | −1.62 | 0.05 |
| C25 | 0.36 | 0.01 |
| C35 | 0.97 | 0.03 |
| C46 | 5.59 | 0.69 |

Plane strain in a-c (x1-x3) plane (long body along b) uses: C11,C13,C33,C15,C35,C55 (+C12,C23,C25 for σ22 reaction). Note anomalous Poisson ratios ν21,ν31>0.5 reported by source (real, not error).

## B. Thermal conductivity — a-c plane
Source: Klimm et al., Cryst. Res. Technol. (2023), DOI 10.1002/crat.202200204 (full PDF read earlier, CC BY-NC). Basis e2||b, e3||c → our (x1,x3)=(a,c)-plane block: K11=12.13, K33=14.09, K13=−0.992 W/mK (300 K). K22(b)=24.26 out-of-plane. Level: **FULL-TEXT/EQUATIONS**. Principal axes rotated ≈−25.5° from (a,c): genuine in-plane misalignment.

## C. Thermal expansion (linear, crystal axes)
Source: "Thermal expansion coefficients of β-Ga2O3 single crystals" (2015), powder XRD 300–700 K. α_a=1.54e-6, α_b=3.37e-6, α_c=3.15e-6 1/K. Level: **ABSTRACT**. Cross-check: Cheng-Hanke synchrotron 2018 (α_a nonlinear 0.1–2.78e-6; α_b,α_c≈2α_a) — consistent order. Used: the 2015 RT-700K values.
α5 (a-c thermal shear): **UNRESOLVED** (no located measurement) → set 0; LIMITATION + sensitivity note (see THERMODYNAMIC_ADMISSIBILITY.md).

## D. Density and heat capacity
- ρ = 5880 kg/m³. Level: **METADATA** (two independent compilations agree 5.88 g/cm³; ACS Omega 2021 lists 5.9e3).
- c_p: **UNRESOLVED primary source**. Candidate "18.7 J/mol K" (Springer chapter 2020, ABSTRACT) is physically anomalous vs Dulong-Petit 3nR=124.7 J/mol K → NOT used. **ESTIMATED**: Debye ΘD=685 K (ACS Omega 2021, snippet; experimental 738 K cited there) → c_p(300K) ≈ 105 J/mol K ≈ 560 J/kg K. Sensitivity: all thermal times ∝ c_p; results reported vs Λ and ε so the map applies for any c_p; a worked dimensional example given for c_p∈{500,560,700}.

## E. Memory / relaxation parameters (generalized heat conduction)
τ_q (CV), (τ_a,τ_b,weights) (MCV3-type): **HYPOTHETICAL** — no measured thermal-relaxation data for β-Ga2O3 located. Study parameters: τ ∈ {0, 1, 5, 20} ps sweep (phonon-collision-order scale). All generalized-model results labeled "dimensionless-study with hypothetical relaxation times" per direction-note rule. Model operators: Huang-2025 family (DOI 10.1007/s10483-025-3280-7), verified against its Fig.5 in PILOT_HUANG_2025_01. Level: operators EQUATIONS; τ-values HYPOTHETICAL.

## F. Loading
T0 = 293 K (level FULL-TEXT, Huang-2025 Table 2 convention). θ_amp = 10 K (small-perturbation; linear theory). Pulse: wall-temperature Gaussian (t0, tw per PROBLEM_DEFINITION). Level: PROPOSED loading (study design).

## G. Derived quantities (computed in code, formulas here)
- c_ref = √(C33/ρ) = √(347.4e9/5880) ≈ 7676 m/s [DERIVED]
- κ̄ = √(det K_2D)/(ρ c_p) ≈ 13.04/(5880·560) ≈ 3.97e-6 m²/s [DERIVED]
- t_th = a²/κ̄; ε = κ̄/(c_ref a); Λ = τ κ̄/a²; δ = T0|β|²/(ρ c_p C̄) ≈ 4e-4 [DERIVED]
- β_i = C_ij α_j (2D plane-strain thermal-stress vector incl. α_b row) — formula in EQUATION_INVENTORY.

## H. Explicitly NOT supplied/used
No experimental transient dataset; no author code; no τ measurement; no α5; no high-T (>700K) extrapolation; no plasticity/fracture; no large-ΔT (ΔT/T0=0.034 ✓ linear).
