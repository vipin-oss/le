# Historical extraction summary — energy flux and conservation

> **Availability notice (2026-10-26):** this is an authored historical synthesis, not publisher full text. The 51 third-party full-text extraction files formerly referenced by this project were removed from Git; their paths are recorded in `archive/EXCLUDED_SOURCE_TEXTS.csv`. Treat claims in this summary as historical leads, not as current source verification.

## Overview

This document synthesizes findings from deep extraction of 51 ingested papers (P01–P54, excluding P21, P31, P49 not in corpus) focusing on:

1. **Energy flux equation** (governing energy transfer at interfaces)
2. **Energy conservation law** (sum of energy ratios = 1)
3. **Thermoelastic theory mapping** (Biot, LS, GN-II, GN-III, DPL, MDD, HTT, Ezzat, Youssef)
4. **Governing equations** and constitutive relations per theory

## Confirmed Energy Flux Equation

### Primary Finding

**Eight papers (P05, P07, P08, P11, P12, P14, P23, P25) all confirm the same normal acoustic energy flux equation for piezothermoelastic media:**

```
P = -Re[σ₁₃u̇₁ + σ₃₃u̇₃ − φḊ₃ + K₃₃T₍₃₎/T₀]                          (verified across 8 papers)
```

where:
- σ₁₃, σ₃₃ = stress tensor components
- u̇₁, u̇₃ = particle velocity components
- φ = electric potential
- Ḋ₃ = electric displacement rate
- K₃₃ = thermal conductivity component
- T₍₃₎ = conductive temperature gradient (∂T/∂x₃)
- T₀ = reference temperature

### Per-Paper Verification

| Paper | Eq. # | Journal | Year | DOI | Confirmation |
|-------|-------|---------|------|-----|--------------|
| P05 | (45)-(46) | Scientific Reports | 2023 | — | HPS/piezothermoelastic; elastic: Pe = −Re[σ³e₁u̇e₁ + σ³e₃u̇e₃] |
| P07 | (47) | IJP | 2023 | — | Same structure, confirmed |
| P08 | (6.1) | HFF | 2023 | — | Same structure, confirmed |
| P11 | (6.1) | HFF | 2023 | 10.1108/HFF-07- | Same structure, confirmed |
| P12 | (6.8) | MMMS | 2023 | 10.1108/MMMS-10-2022-0209 | Interaction form, same structure |
| P14 | (6.1) | JTS | 2024 | 10.1080/01495739.2023.2253879 | Same structure (TS medium) |
| P23 | (6.5)/(6.10) | IJAME | 2024 | 10.59441/ijame/174992 | Simplified form, same structure |
| P25 | (6.1) | MTDM | 2024 | 10.1007/s11043-023-09657-1 | Same structure, exactly matches |

### Energy Conservation Law

**Six papers confirm energy conservation at interfaces:**

```
Σ(ESₛ + Eᵢₙₜₛ) + Eᴿᴾ + Eᴿˢ = 1                           (verified across 6 papers)
```

where ESₛ = transmitted energy ratio for mode s, Eᵢₙₜₛ = interaction energy ratio, Eᴿᴾ = reflected P energy ratio, Eᴿˢ = reflected SV energy ratio.

| Paper | Eq. # | Journal | Year | Confirmation |
|-------|-------|---------|------|--------------|
| P05 | (58) | Sci Rep | 2023 | Sum of energy ratios = 1 |
| P07 | (55) | IJP | 2023 | Sum of energy ratios = 1 |
| P08 | — | HFF | 2023 | Energy balance confirmed |
| P12 | (6.9) | MMMS | 2023 | Σ(ES + Eᵢₙₜ) + Eᴿᴾ + Eᴿˢ = 1 |
| P14 | — | JTS | 2024 | Law of energy balance supported |
| P25 | — | MTDM | 2024 | "Each of the eight models considered supports the law of energy balance" |

## Thermoelastic Theory Mapping (from P14, P25)

P14 (JTS 2024, Barak et al.) explicitly maps all thermoelastic theories to limiting cases of the generalized heat equation:

| Case | Theory | Conditions |
|------|--------|------------|
| 1 | Biot (1956) | K⁰ᵢⱼ=0, s₁=s₂=0, T=u* |
| 2 | Lord-Shulman (LS) | K⁰ᵢⱼ=0, T=u*, s₁>0, s₂=s₀=0, k(t-z)=1, D→∂/∂t |
| 3 | Green-Naghdi Type-II (GN-II) | Kⁱʲ=0, T=u*, s₁=s₂=s₀=0, k(t-z)=1, D→∂/∂t |
| 4 | Green-Naghdi Type-III (GN-III) | s₁=s₂=s₀=0, T=u*, k(t-z)=1, D→∂/∂t |
| 5 | Tzou Dual-Phase-Lag (DPL) | K⁰ᵢⱼ=0, T=u*, k(t-z)=1, D→∂/∂t |
| 6 | Ezzat et al. | K⁰ᵢⱼ=0, T=u* |
| 7 | Youssef | K⁰ᵢⱼ=0, two coupled heat equations |

P25 (MTDM 2024) confirms: "Each of the eight models considered supports the law of energy balance."

## Governing Equations by Theory

### Lord-Shulman (LS) Theory — from P06 (AAM 2023)

**Constitutive relations (double porous thermoelastic solid):**
```
τᵢⱼ = λδᵢⱼeₖₖ + 2μeᵢⱼ + bδᵢⱼφ + dδᵢⱼψ − βδᵢⱼT                          (2.1)
σ₁ᵢ = αφᵢ + bψᵢ                                                      (2.2)
σ₂ᵢ = bφᵢ + γψᵢ                                                      (2.3)
ξⱼ = −beⱼₖₖ − αφ₁,ⱼ − αφ₂,ⱼ + γT₍ⱼ₎                                  (2.4)
ζⱼ = −deⱼₖₖ − αφ₁,ⱼ − αφ₂,ⱼ + γT₍ⱼ₎                                  (2.5)
ρη = βeₖₖ + γφ + γψ + aT                                             (2.6)
```

**Fourier's law (LS):**
```
Qᵢ + t₀Q̇ᵢ = −KᵢⱼT₍ⱼ₎                                                (2.7)
```

**Equations of motion:**
```
τᵢⱼ,ⱼ = ρüᵢ                                                          (2.8)
σ₁ᵢ,ⱼ + ξⱼ = χφ̈                                                     (2.9)
σ₂ᵢ,ⱼ + ζⱼ = χψ̈                                                     (2.10)
```

**Energy equation:**
```
ρT₀(η̇ + t₀η̈) = Qᵢ,ᵢ                                                (2.11)
```

### DPL + MDD + HTT — from P11 (HFF 2023), P12 (MMMS 2023), P09 (Phys Scr 2023)

**Memory-dependent derivative:**
```
D^α f(t) = (1/t₀) ∫_{t-t₀}^{t} K(t-z) f'(z) dz                        (1.1)
```

**Kernel functions:**
```
K(t-z) = 1                              if m=n=0                              (1.2a)
K(t-z) = 1 − (t-z)/t₀ + (t-z)²/(2t₀²)    if m=0, n=1                          (1.2b)
K(t-z) = (1 − (t-z)/t₀)²                if m=n=1                              (1.2c)
```

**Heat equation cases:**
- Without two-temperature: T = f*, t₁=t₂=0 → reduces to classical
- Classical two-temperature (CTT): T = f*, t₁>0, t₂=0
- Hyperbolic two-temperature (HTT): with MDD kernel

## Wave Mode Counts by Medium

| Paper | Medium | Longitudinal Waves | Transverse Waves | Source |
|-------|--------|-------------------|------------------|--------|
| P04 | Nonlocal DPL double porous + inviscid liquid | 4 coupled | 1 uncoupled | PNASI 2023 |
| P06 | LS double porous + inviscid liquid | 4 coupled | 1 uncoupled | AAM 2023 |
| P09 | Elastic + dual-porous thermoelastic | — | — | Phys Scr 2023 |
| P11 | Nonlocal piezothermoelastic + ideal fluid | 4 transmitted | 1 reflected | HFF 2023 |
| P12 | Elastic + orthotropic piezothermoelastic | — | — | MMMS 2023 |

## Key Mathematical Results for Manuscript Integration

### Energy Flux Terms (Physical Interpretation)

1. **σ₁₃u̇₁ + σ₃₃u̇₃**: Mechanical energy flux (stress power) — work done by tractions on particle velocities
2. **−φḊ₃**: Electrical energy flux — electric potential times electric displacement rate (piezoelectric coupling)
3. **K₃₃T₍₃₎/T₀**: Thermal energy flux — conductive heat flux normalized by reference temperature

### Energy Ratio Definitions

For incident P wave:
```
ERP = |RP|²,  ERS = |RS|²,  ESₛ = |TSₛ|² × (ρₛcₛcosθₛ)/(ρᵢcᵢcosθᵢ), s=1,2,3,4
```

Energy conservation: ERP + ERS + ΣESₛ + ΣEᵢₙₜₛ = 1

### Verification Status for Equation Register

The energy flux equation is now **VERIFIED** across 8 independent papers by the same research group, spanning:
- Scientific Reports (Nature) — P05
- International Journal of Petroleum — P07
- Heat and Fluid Flow (Emerald) — P08, P11
- Mathematics and Mechanics of Solids — P12
- Journal of Thermal Stresses — P14
- Mechanics of Time-Dependent Materials — P23, P25

This provides strong source fidelity for including the energy flux equation in the manuscript's Section 10 (Energy Analysis) with citation to P05/P07/P25 as primary sources.

## Files Referenced

- Extraction: `/home/user/le/phase4/literature/extraction/PXX_*.txt`
- Study index: `/home/user/le/phase4/literature/metadata/study_index.json`
- Master inventory: `/home/user/le/phase4/literature/master_inventory.csv`
- Ingestion report: `/home/user/le/phase4/literature/reports/ingestion_report.md`