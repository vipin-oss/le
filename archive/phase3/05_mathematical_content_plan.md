# Deliverable 5 — Subsection-Level Mathematical Content Plan

**Branch:** arena/40393d9f-le  
**Prepared:** 2026-10-21  
**Alignment:** Master Editorial Directive §8 (layered mathematical exposition), §9 (equation safety), §15 (manuscript architecture)

---

## 1. Overview

This document maps each subsection of the proposed outline (Deliverable 4) to:
- Mathematical content (equations, derivations, proofs)
- Source status (VERIFIED, VALID UNDER SPECIFIED ASSUMPTIONS, MODEL-SPECIFIC, UNCERTAIN)
- Phase 2 artifacts that support it
- New derivations required

---

## 2. Layer I — First Principles (Section 3)

### 3.1 Kinematics: displacement, strain, rotation

| Content | Equation | Source | Status | Phase 2 artifact |
|---------|----------|--------|--------|------------------|
| Displacement gradient | uᵢ,ⱼ | Standard continuum mechanics | VERIFIED | EQ-001 context |
| Infinitesimal strain | εᵢⱼ = ½(uᵢ,ⱼ + uⱼ,ᵢ) | Standard | VERIFIED | EQ-001 context |
| Rotation tensor | ωᵢⱼ = ½(uᵢ,ⱼ − uⱼ,ᵢ) | Standard | VERIFIED | EQ-001 context |
| Velocity | vᵢ = u̇ᵢ | Standard | VERIFIED | EQ-003 context |

### 3.2 Conservation laws

| Content | Equation | Source | Status | Phase 2 artifact |
|---------|----------|--------|--------|------------------|
| Linear momentum | ρv̇ᵢ = σⱼᵢ,ⱼ + ρfᵢ | Theorem 2.1 | DERIVED | `07_continuum_balance_derivations.md` |
| Angular momentum | σᵢⱼ = σⱼᵢ | Theorem 3.1 | DERIVED | `07_continuum_balance_derivations.md` |

### 3.3 Mechanical power and internal energy

| Content | Equation | Source | Status | Phase 2 artifact |
|---------|----------|--------|--------|------------------|
| Mechanical power | ρ d/dt(½vᵢvᵢ) = −σᵢⱼε̇ᵢⱼ + ρfᵢvᵢ + (σⱼᵢvᵢ)ⱼ | Theorem 4.1 | DERIVED | `07_continuum_balance_derivations.md` |
| Internal energy (1st law) | ρė = σᵢⱼε̇ᵢⱼ − qᵢ,ᵢ + ρr | Theorem 5.1 | DERIVED | `07_continuum_balance_derivations.md` |

### 3.4 Entropy and dissipation inequality

| Content | Equation | Source | Status | Phase 2 artifact |
|---------|----------|--------|--------|------------------|
| Clausius-Duhem | σᵢⱼε̇ᵢⱼ − ρ(ψ̇ + sṪ) − qᵢT,ᵢ/T ≥ 0 | Theorem 6.1 | DERIVED | `07_continuum_balance_derivations.md` |

### 3.5 Constitutive principles

| Content | Equation | Source | Status | Phase 2 artifact |
|---------|----------|--------|--------|------------------|
| Coleman-Noll restrictions | σᵢⱼ = ρ∂ψ/∂εᵢⱼ, s = −∂ψ/∂T | Theorem 7.1 | DERIVED | `07_continuum_balance_derivations.md` |

### 3.6 Classical elasticity: Navier equations

| Content | Equation | Source | Status | Phase 2 artifact |
|---------|----------|--------|--------|------------------|
| Navier equation | ρüᵢ = (λ+μ)uⱼ,ⱼᵢ + μuᵢ,ⱼⱼ | Standard | VERIFIED | BM-1 derivation |

### 3.7 Plane wave assumptions

| Content | Equation | Source | Status | Phase 2 artifact |
|---------|----------|--------|--------|------------------|
| Harmonic plane wave | uᵢ = Âᵢeⁱ(𝐤·𝐱−ωt) | Standard | VERIFIED | `10_harmonic_energy_transport.md` |
| Time-average identity | ⟨ab⟩ₜ = ½Re[âb̂*] | Derived | VERIFIED | `10_harmonic_energy_transport.md` |

### 3.8 Energy flux in classical elasticity

| Content | Equation | Source | Status | Phase 2 artifact |
|---------|----------|--------|--------|------------------|
| Total energy flux | Jᵢ = σⱼᵢvᵢ + qᵢ | Section 8 | DERIVED | `07_continuum_balance_derivations.md` EQ-007 |

### 3.9 Interface conditions

| Content | Equation | Source | Status | Phase 2 artifact |
|---------|----------|--------|--------|------------------|
| Perfect bonding | uᵢ⁽¹⁾ = uᵢ⁽²⁾, σⱼᵢ⁽¹⁾nⱼ = σⱼᵢ⁽²⁾nⱼ | Standard | VERIFIED | `11_scattering_matrix_derivations.md` |
| Imperfect bonding (spring-type) | uᵢ⁽²⁾ − uᵢ⁽¹⁾ = Kᵢᵘtᵢ | Standard | MODEL-SPECIFIC | `11_scattering_matrix_derivations.md` |

---

## 3. Layer II — Classical and Generalized Thermoelastic Theories (Section 4)

### 4.1 Historical evolution

**Content:** Timeline narrative with citations. No equations required except reference to key papers.

| Theory | Year | Key reference | Status |
|--------|------|---------------|--------|
| Biot coupled thermoelasticity | 1956 | Biot 1956 | VERIFIED |
| Lord–Shulman | 1967 | LS 1967 | VERIFIED |
| Green–Lindsay | 1972 | GL 1972 | VERIFIED |
| Green–Naghdi II | 1991 | GN II 1991 | VERIFIED |
| Green–Naghdi III | 1991 | GN III 1991 | VERIFIED |
| Dual-phase-lag | 1995 | Tzou 1995 | VERIFIED |
| Three-phase-lag | 2007 | Roy Choudhuri 2007 | VERIFIED |
| MGT | 2019 | Quintanilla 2019 | VERIFIED |
| MDD | 2011/2021 | Wang & Li / Abouelregal | VERIFIED |

### 4.2 Classical coupled thermoelasticity

**Governing equations:**

| Content | Equation | Source | Status |
|---------|----------|--------|--------|
| Coupled motion | ρüᵢ = (λ+μ)uⱼ,ⱼᵢ + μuᵢ,ⱼⱼ − βT,ᵢ | Standard | VERIFIED |
| Heat equation | ρcᵥṪ = k∇²T − βT₀u̇ᵢ,ᵢ | Standard | VERIFIED |

**Wave speeds:** cₚ = √((λ+2μ)/ρ), cₛ = √(μ/ρ) — VERIFIED

### 4.3 Lord–Shulman (1967)

| Content | Equation | Source | Status | New derivation needed? |
|---------|----------|--------|--------|------------------------|
| Modified heat equation | qᵢ + τ₀q̇ᵢ = −kT,ᵢ | LS 1967 | VERIFIED | No |
| Combined equation | ρcᵥ(Ṫ + τ₀T̈) = k∇²T(1 + τ₀∂/∂t) − βT₀(u̇ᵢ,ᵢ + τ₀üᵢ,ᵢ) | LS 1967 | VERIFIED | No |
| Finite wave speed | c = √(k/(ρcᵥτ₀)) | LS 1967 | VERIFIED | No |
| Well-posedness | τ₀ > 0 | Standard | VERIFIED | No |
| Energy flux | Jᵢ = σⱼᵢvᵢ + qᵢ + τ₀(...) | **UNRESOLVED** | **UNCERTAIN** | YES — derive |

### 4.4 Green–Lindsay (1972)

| Content | Equation | Source | Status |
|---------|----------|--------|--------|
| Two temperatures | T (conductivity), T* (thermodynamic) | GL 1972 | VERIFIED |
| Heat equation with two temps | ρcᵥṪ* = k∇²T − βT₀u̇ᵢ,ᵢ | GL 1972 | VERIFIED |
| Dissipationless | No entropy production | GL 1972 | VERIFIED |

### 4.5 Green–Naghdi Type II (1991)

| Content | Equation | Source | Status |
|---------|----------|--------|--------|
| Thermal displacement | ∂T/∂t = ∇²φ (thermal displacement φ) | GN II 1991 | VERIFIED |
| Energy conservation | No dissipation term | GN II 1991 | VERIFIED |
| Energy flux | Jᵢ = σⱼᵢvᵢ + qᵢ + ... | **UNRESOLVED** | **UNCERTAIN** | YES |

### 4.6 Green–Naghdi Type III (1991)

| Content | Equation | Source | Status |
|---------|----------|--------|--------|
| Mixed character | Dissipative but wave-like | GN III 1991 | VERIFIED |

### 4.7 Dual-phase-lag (Tzou, 1995)

| Content | Equation | Source | Status | New derivation needed? |
|---------|----------|--------|--------|------------------------|
| DPL heat equation | qᵢ(t+τ_q) = −kT,ᵢ(t+τ_T) | Tzou 1995 | VERIFIED | No |
| Taylor expansion | qᵢ + τ_qq̇ᵢ = −k(T,ᵢ + τ_TṪ,ᵢ) | Tzou 1995 | VERIFIED | No |
| Admissibility condition | τ_q ≥ τ_T | Standard | VERIFIED | No |
| Energy flux | Jᵢ = σⱼᵢvᵢ + qᵢ + ... | **UNRESOLVED** | **UNCERTAIN** | YES |

### 4.8 Three-phase-lag

| Content | Equation | Source | Status |
|---------|----------|--------|--------|
| TPL heat equation | qᵢ(t+τ_q) = −k[T,ᵢ(t+τ_T) + (τ_v/2)∂²T,ᵢ/∂t²] | Roy Choudhuri 2007 | VERIFIED |

### 4.9 Memory-dependent derivative models

| Content | Equation | Source | Status | Phase 2 artifact |
|---------|----------|--------|--------|------------------|
| MDD operator | D_τf(t) = (1/τ)∫ₜ₋τᵗκ(t−ζ)f'(ζ)dζ | RG-003 Eq. (1) | VERIFIED | `06_equation_provenance_register.csv` EQ-008 |
| MDD kernel | κ(t−ζ) = 1 − 2β/τ(t−ζ) + α²/τ²(t−ζ)² | RG-003 Eq. (2) | VERIFIED | EQ-009 |

### 4.10 Comparative table

| Theory | Relaxation params | Dissipation | Wave speed | Energy flux status |
|--------|------------------|-------------|------------|-------------------|
| Classical | 0 | Yes | Infinite | DERIVED |
| LS | 1 (τ₀) | Yes | Finite | UNRESOLVED |
| GL | 2 | No | Finite | UNRESOLVED |
| GN II | 0 | No | Finite | UNRESOLVED |
| GN III | τ | Yes | Finite | UNRESOLVED |
| DPL | 2 (τ_q, τ_T) | Yes | Finite | UNRESOLVED |
| TPL | 3 (τ_q, τ_T, τ_v) | Yes | Finite | UNRESOLVED |
| MGT | 1 (τ) | Yes | Finite | UNRESOLVED |
| MDD | 1 (τ) + kernel | Kernel-dependent | Finite | UNRESOLVED |
| Nonlocal | (e₀a)² | Yes | Finite (dispersive) | UNRESOLVED |

### 4.11 Limiting cases

| From | To | Conditions | Rigor |
|------|-----|------------|-------|
| MDD+TPL | Classical | All τ→0, kernel→1 | Parameter substitution only |
| MDD+TPL | LS | τ_T=τ_v=0, n=1 | Parameter substitution |
| MDD+TPL | GN II | K=0, specific limit | Parameter substitution |
| MDD+TPL | DPL | τ_v=0, specific limit | Parameter substitution |

**Note:** All limiting procedures in corpus are parameter substitutions, not rigorous limit theorems. No convergence proofs or error bounds.

---

## 4. Layer III — Coupled Multiphysics Continua (Section 5)

### 5.1 Piezoelectricity

| Content | Equation | Source | Status |
|---------|----------|--------|--------|
| Constitutive | σᵢⱼ = cᵢⱼₖₗεₖₗ − eₖᵢⱼEₖ | Standard | VERIFIED |
| Electric displacement | Dᵢ = eᵢₖₗεₖₗ + κᵢⱼEⱼ | Standard | VERIFIED |
| Electric field | Eᵢ = −φ,ᵢ | Standard | VERIFIED |
| Charge conservation | Dᵢ,ᵢ = 0 | Standard | VERIFIED |

### 5.2 Piezothermoelasticity

| Content | Equation | Source | Status | Phase 2 artifact |
|---------|----------|--------|--------|------------------|
| Constitutive (RG-003 Eq. 3) | σᵢⱼ = cᵢⱼᵣₒeᵣₒ − ηᵢⱼᵣEᵣ − βᵢⱼT | RG-003 Eq. (3) | VERIFIED | EQ-010 |
| Momentum | σᵢⱼ,ⱼ = ρüᵢ | RG-003 Eq. (4) | VERIFIED | EQ-011 |
| Electric field | Eᵢ = −φ,ᵢ | RG-003 Eq. (5) | VERIFIED | EQ-012 |
| Electric displacement | Dᵢ = εᵢⱼEⱼ + ηᵢⱼᵣeⱼᵣ + pᵢT | RG-003 Eq. (6) | VERIFIED | EQ-013 |
| Charge conservation | Dᵢ,ᵢ = 0 | RG-003 Eq. (7) | VERIFIED | EQ-014 |

### 5.3 Electrical boundary conditions

| Content | Equation | Source | Status |
|---------|----------|--------|--------|
| Perfect electrical contact | φ⁽¹⁾ = φ⁽²⁾ | Standard | VERIFIED |
| Insulated interface | D₃ = 0 | RG-003 Eq. (38) | VERIFIED | EQ-023 |
| Charge continuity | D₃⁽¹⁾ = D₃⁽²⁾ | Standard | VERIFIED |

### 5.4–5.7 Porous, micropolar, semiconductor, magneto

| Content | Equation | Source | Status |
|---------|----------|--------|--------|
| Porous: void distribution | φ (volume fraction) | Standard | VERIFIED |
| Double porosity | Two porosity fields | Standard | VERIFIED |
| Micropolar: micro-rotation | ϕᵢ | Standard | VERIFIED |
| Couple stresses | μᵢⱼ | Standard | VERIFIED |
| Semiconductor: carrier diffusion | ∂n/∂t = D∇²n + ... | Standard | VERIFIED |
| Magneto: magnetic field | Bᵢ, Hᵢ | Standard | VERIFIED |

---

## 5. Layer IV — Generalized Transport and Memory Effects (Section 6)

### 6.1–6.4 Memory and relaxation

| Content | Equation | Source | Status | Phase 2 artifact |
|---------|----------|--------|--------|------------------|
| MDD operator | D_τf(t) = (1/τ)∫ₜ₋τᵗκ(t−ζ)f'(ζ)dζ | RG-003 Eq. (1) | VERIFIED | EQ-008 |
| MDD kernel | κ = 1 − 2β/τ(t−ζ) + α²/τ²(t−ζ)² | RG-003 Eq. (2) | VERIFIED | EQ-009 |

### 6.5 Energy flux in memory-dependent media

| Content | Status | Source | New derivation needed? |
|---------|--------|--------|------------------------|
| Hereditary energy flux | UNRESOLVED | — | YES — derive convolution-form flux |
| Instantaneous flux ambiguity | UNRESOLVED | — | YES — discuss physical interpretation |

### 6.6 Well-posedness and causality

| Content | Status | Notes |
|---------|--------|-------|
| Well-posedness conditions | MODEL-SPECIFIC | Each theory has own conditions |
| Causality (finite wave speed) | VERIFIED | LS, DPL, TPL, MGT, MDD all finite |
| Kernel positivity | MODEL-SPECIFIC | MDD kernel must be positive definite |

---

## 5. Layer V — Interface Phenomena (Section 9)

### 9.1–9.4 Scattering matrix

| Content | Equation | Source | Status | Phase 2 artifact |
|---------|----------|--------|--------|------------------|
| Interface system | ΔX = Q | RG-003 Eq. (44) | VERIFIED | `11_scattering_matrix_derivations.md` |
| Δ matrix (7×7) | Δᵢⱼ entries | RG-003 Eq. (44) | VERIFIED | EQ-016 through EQ-018 context |
| Boundary conditions (7) | Eq. (38) | RG-003 Eq. (38) | VERIFIED | EQ-021 through EQ-023 |

### 9.5 Secular equation

| Content | Equation | Source | Status |
|---------|----------|--------|--------|
| Characteristic polynomial | G₁₁q⁸ + ... + G₁₅ = 0 | RG-003 Eq. (27) | VERIFIED | EQ-020 |

### 9.6–9.8 Energy ratios

| Content | Equation | Source | Status |
|---------|----------|--------|--------|
| Energy ratio definition | R = |J_ref|/|J_inc| | Standard | VERIFIED |
| Conservation claim | Σ(ES + E_int + E_RP + E_RT + E_RS) = 1 | RG-003 Eq. (58) | CLAIMED (uncertain) | EQ-019 |
| Asymmetric flux finding | HPS has thermal term; TS does not | RG-003 Eqs. (45)-(46) | VERIFIED | GAP-011 |

---

## 5. Layer VI — Energy Transport and Dissipation (Section 10)

### 10.1 General energy balance

| Content | Equation | Source | Status |
|---------|----------|--------|--------|
| General balance | ∂ₜℰ + ∇·J = 𝒫 − 𝒟 | Derived | DERIVED |

### 10.2 Classical energy flux

| Content | Equation | Source | Status | Phase 2 artifact |
|---------|----------|--------|--------|------------------|
| Classical flux | Jᵢ = σⱼᵢvᵢ + qᵢ | Section 8 | DERIVED | EQ-007 |

### 10.3 Energy flux in generalized theories

| Theory | Flux form | Status | Derivation needed |
|--------|----------|--------|-------------------|
| LS | σv + q + relaxation term | UNRESOLVED | YES |
| GL/GN II | σv + q + thermal displacement term | UNRESOLVED | YES |
| DPL | σv + q + lag terms | UNRESOLVED | YES |
| TPL | σv + q + higher-order lag terms | UNRESOLVED | YES |
| MGT | σv + q + third-order term | UNRESOLVED | YES |
| MDD | Hereditary (convolution) flux | UNRESOLVED | YES |
| Nonlocal | Integral-form flux | UNRESOLVED | YES |

### 10.4 Interface energy balance

| Content | Equation | Source | Status |
|---------|----------|--------|--------|
| Jump condition | [Jₙ] = 𝒫 − ∂ₜℰ_interface | Derived | DERIVED |
| Passive interface | [Jₙ] = 0 | Derived | DERIVED |

### 10.5 Conservation identity

| Content | Equation | Source | Status |
|---------|----------|--------|--------|
| Conservation | ΣR + ΣT + A = 1 | Standard | VERIFIED (for classical) |
| RG-003 claim | Σ = 1 | RG-003 Eq. (58) | CLAIMED (asymmetric flux) |

### 10.6–10.7 Dissipation and admissibility

| Content | Source | Status | Phase 2 artifact |
|---------|--------|--------|------------------|
| Dissipation mechanisms | `09_thermodynamic_admissibility.md` | VERIFIED | Theory-by-theory |
| Well-posedness assessments | `09_thermodynamic_admissibility.md` | VERIFIED | Theory-by-theory |

---

## 6. Equation Verification Register Summary

| Equation ID | Equation | Source | Status | Manuscript section | Inclusion decision |
|-------------|----------|--------|--------|-------------------|-------------------|
| EQ-001 | ρv̇ᵢ = σⱼᵢ,ⱼ + ρfᵢ | Derived (Thm 2.1) | VERIFIED | §3.2 | Include |
| EQ-002 | σᵢⱼ = σⱼᵢ | Derived (Thm 3.1) | VERIFIED | §3.2 | Include |
| EQ-003 | Mechanical power balance | Derived (Thm 4.1) | VERIFIED | §3.3 | Include |
| EQ-004 | Internal energy balance | Derived (Thm 5.1) | VERIFIED | §3.3 | Include |
| EQ-005 | Dissipation inequality | Derived (Thm 6.1) | VERIFIED | §3.4 | Include |
| EQ-006 | Coleman-Noll restrictions | Derived (Thm 7.1) | VERIFIED | §3.5 | Include |
| EQ-007 | Classical energy flux Jᵢ = σⱼᵢvᵢ + qᵢ | Derived (Sec 8) | VERIFIED | §3.8, §10.2 | Include |
| EQ-008 through EQ-023 | RG-003 equations | RG-003 full text | VERIFIED | §4.9, §5.2, §9 | Include with source attribution |
| LS energy flux | σv + q + ? | Unresolved | UNCERTAIN | §10.3 | Do NOT include as canonical |
| DPL energy flux | σv + q + ? | Unresolved | UNCERTAIN | §10.3 | Do NOT include as canonical |
| MDD energy flux | Hereditary | Unresolved | UNCERTAIN | §10.3 | Do NOT include as canonical |
| Nonlocal energy flux | Integral form | Unresolved | UNCERTAIN | §10.3 | Do NOT include as canonical |

---

## 7. Derivations Required Before Manuscript Writing

| Priority | Derivation | Target section | Estimated effort |
|----------|------------|----------------|------------------|
| CRITICAL | LS energy flux from relaxation equation | §10.3 | 1–2 weeks |
| CRITICAL | DPL energy flux | §10.3 | 1–2 weeks |
| CRITICAL | TPL energy flux | §10.3 | 1–2 weeks |
| CRITICAL | MGT energy flux | §10.3 | 1–2 weeks |
| CRITICAL | MDD hereditary energy flux | §10.3 | 2–3 weeks |
| CRITICAL | Nonlocal integral-form energy flux | §10.3 | 2–3 weeks |
| HIGH | GN II/III energy flux | §10.3 | 1–2 weeks |
| HIGH | Electrical energy flux (piezoelectric) | §5.3 | 1 week |

---

## 8. Symbols Requiring Definition (Master Notation Table)

| Symbol | Meaning | Units | First appearance |
|--------|---------|-------|-----------------|
| uᵢ | Displacement | m | §3.1 |
| vᵢ | Velocity | m/s | §3.1 |
| εᵢⱼ | Strain | dimensionless | §3.1 |
| σᵢⱼ | Stress | Pa | §3.2 |
| qᵢ | Heat flux | W/m² | §3.3 |
| T | Temperature | K | §3.3 |
| ψ | Free energy | J/kg | §3.5 |
| s | Entropy | J/(kg·K) | §3.5 |
| Jᵢ | Energy flux | W/m² | §3.8 |
| τ₀, τ_q, τ_T, τ_v | Relaxation times | s | §4.3–4.8 |
| eᵢⱼₖ | Piezoelectric coefficient | C/m² | §5.1 |
| Dᵢ | Electric displacement | C/m² | §5.1 |
| φ | Electric potential | V | §5.1 |
| κᵢⱼ | Dielectric permittivity | F/m | §5.1 |

---

## 9. Figure-Ready Mathematical Content

| Figure | Mathematical content | Section | Data source |
|--------|---------------------|---------|-------------|
| F-001 | Balance-law dependency graph | §3 | EQ-001 through EQ-007 |
| F-002 | Theory comparison tree | §4 | Comparative table 4.10 |
| F-003 | Energy flux asymmetry (RG-003) | §10.3 | Eqs. (45)-(46) |
| F-004 | Interface scattering geometry | §9 | Section 9.1 |
| F-005 | Energy conservation verification | §10.5 | BM-1 analytical |

---

**Next:** Proceed to Deliverable 6 (Literature Acquisition and Citation Strategy).
