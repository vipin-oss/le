# Deliverable 8 — Original Scientific Taxonomy Proposal

**Branch:** arena/40393d9f-le  
**Prepared:** 2026-10-21  
**Alignment:** Master Editorial Directive §13.2 (multidimensional classification), §14 (future research directions)  
**Builds on:** Phase 2 taxonomy v2 (`phase2/17_original_taxonomy_v2.md`)

---

## 1. Taxonomy Overview

The original multidimensional taxonomy classifies studies in generalized multiphysics continuum mechanics across five independent dimensions. Each dimension has multiple levels, and each study is assigned one level per dimension. This produces a classification vector that enables:

- Cross-study comparison under identical conditions
- Identification of empty cells (research gaps)
- Detection of contradictory approaches
- Evidence-based mapping of the literature landscape

---

## 2. The Five Dimensions

### Dimension 1 — Physical (Continuum Type, Geometry, Material, Coupling, Bonding)

| Sub-dimension | Levels | Example studies |
|---------------|--------|-----------------|
| Continuum type | Classical elastic, thermoelastic (Fourier), generalized thermoelastic (LS/GL/GN/DPL/TPL/MGT), piezoelectric/piezothermoelastic, poroelastic/double-porosity, semiconductor photo-thermo-elastic, nonlocal elastic | FW-001–FW-011; RG-001–RG-007 |
| Geometry | Half-space interface, free surface, layered waveguide, cylindrical/spherical interface | RG-001–RG-007 (all half-space interface) |
| Material symmetry | Isotropic, orthotropic, monoclinic, functionally graded | RG-005 (monoclinic); others isotropic/orthotropic |
| Coupled fields | 1 (elastic), 2 (thermoelastic), 3+ (piezo-thermo-elastic, poro-thermo-elastic) | RG-003 (3 fields); RG-006 (3 fields) |
| Interface bonding | Perfect bonding, imperfect (spring-type), insulated electrical | RG-003 (perfect + insulated); RG-004 (imperfect) |

### Dimension 2 — Mathematical (Governing Equations)

| Sub-dimension | Levels | Example studies |
|---------------|--------|-----------------|
| PDE class | Elliptic (static), parabolic (Fourier), hyperbolic (wave), mixed (generalized thermoelasticity) | FW-002 (hyperbolic); FW-005 (mixed DPL) |
| Local vs nonlocal | Local, nonlocal (Eringen), strain-gradient | FW-006 (nonlocal); RG-007 (nonlocal) |
| Integer vs fractional | Integer-order, fractional-order, memory-dependent derivative | FW-011 (MGT, 3rd-order); RG-003–RG-005 (MDD) |
| Memory/hereditary | None, memory kernel (MDD), fractional integral | RG-003–RG-006 (MDD); RG-007 (MDD) |
| Conservative vs dissipative | Conservative (GN II/III), dissipative (LS, DPL, MGT, MDD) | FW-004 (conservative); FW-002 (dissipative) |

### Dimension 3 — Wave (Propagation Characteristics)

| Sub-dimension | Levels | Example studies |
|---------------|--------|-----------------|
| Wave family | P, SV, SH, Rayleigh, Love, Stoneley, thermal, plasma, quasi-plane | RG-003 (P/T/SV incident; qP/qT/qS/eP transmitted) |
| Dispersion | Non-dispersive (classical), dispersive (generalized, nonlocal) | FW-006 (dispersive); RG-007 (dispersive nonlocal) |
| Attenuation | None (conservative), attenuated (dissipative), complex wave number | FW-002 (attenuated); RG-003 (attenuated MDD) |
| Mode conversion | None, P↔SV, P↔T, electrical↔mechanical | RG-003 (P↔qP/qT/qS/eP; T↔qP/qT/qS/eP; SV↔qP/qT/qS/eP) |
| Surface vs bulk | Bulk waves, surface waves, interface waves | RG-003–RG-007 (all interface waves) |

### Dimension 4 — Energy (Accounting and Conservation)

| Sub-dimension | Levels | Example studies |
|---------------|--------|-----------------|
| Energy-density definition | Classical kinetic+strain+thermal, generalized with relaxation terms | Not classified in corpus |
| Flux formulation | Local (q·n + σ·v), nonlocal (integral), hereditary (MDD), electrical | RG-003: local+electrical+thermal (HPS); local mechanical only (TS) |
| Dissipation mechanism | Thermal relaxation, viscous, electrical resistance, interface dissipation | Not classified in corpus |
| Interface power balance | Conservation assumed, not checked, explicitly verified | RG-003: assumed (claimed but asymmetric flux) |
| Normalization convention | Amplitude ratio, energy ratio, intensity ratio | All corpus papers: energy ratio |
| Conservation verification | Not performed, performed, failed | RG-003: claimed (Eq. 58) but not independently verified |

### Dimension 5 — Validation (Evidence Quality)

| Sub-dimension | Levels | Example studies |
|---------------|--------|-----------------|
| Analytical proof | Yes, no | All corpus papers: yes (theoretical) |
| Numerical convergence | Yes, no | None — no convergence studies |
| Benchmark comparison | Yes, no | None — no benchmark comparisons |
| Experimental evidence | Yes, no | None — no experimental studies |
| Reproducibility | Reproducible (analytical), not reproducible (no full text) | RG-003: reproducible (open access); others: not reproducible |

---

## 3. Taxonomy Application Table

| Study | D1: Physical | D2: Mathematical | D3: Wave | D4: Energy | D5: Validation |
|-------|-------------|-----------------|---------|-----------|----------------|
| FW-001 | Thermoelastic, half-space, isotropic, 2 fields, perfect | Parabolic, local, integer, none, dissipative | P/SV, non-dispersive, attenuated, none, bulk | Classical, local, thermal, assumed, energy ratio, not performed | Analytical, no, no, no, not reproducible |
| FW-002 | Thermoelastic, half-space, isotropic, 2 fields, perfect | Hyperbolic, local, integer, none, dissipative | P/SV, dispersive, attenuated, none, bulk | Classical, local, thermal, assumed, energy ratio, not performed | Analytical, no, no, no, not reproducible |
| FW-004 | Thermoelastic, half-space, isotropic, 2 fields, perfect | Hyperbolic, local, integer, none, conservative | P/SV, dispersive, none, none, bulk | Classical, local, none, assumed, energy ratio, not performed | Analytical, no, no, no, not reproducible |
| FW-006 | Elastic, half-space, isotropic, 1 field, perfect | Hyperbolic, nonlocal, integer, none, conservative | P/SV, dispersive, none, none, bulk | Nonlocal (integral), nonlocal, none, assumed, energy ratio, not performed | Analytical, no, no, no, not reproducible |
| RG-001 | Piezothermoelastic, half-space, orthotropic, 3 fields, perfect | Hyperbolic, local, integer, none, dissipative | P/SV/T, dispersive, attenuated, P↔SV↔T, interface | Local, local, none, assumed, energy ratio, not performed | Analytical, no, no, no, not reproducible |
| RG-003 | Piezothermoelastic, half-space, orthotropic, 3 fields, perfect+insulated | Hyperbolic, local, integer, MDD, dissipative | P/T/SV, dispersive, attenuated, P↔qP/qT/qS/eP, interface | Local+electrical+thermal (HPS); local mechanical (TS), thermal, assumed, energy ratio, claimed | Analytical, no, no, no, REPRODUCIBLE |
| RG-004 | Piezothermoelastic, half-space, orthotropic, 3 fields, imperfect | Hyperbolic, local, integer, MDD, dissipative | P/SV, dispersive, attenuated, P↔SV↔interface, interface | Local, local, interface stiffness, assumed, energy ratio, not performed | Analytical, no, no, no, not reproducible |
| RG-006 | Dual-porous thermoelastic, half-space, isotropic, 3 fields, perfect | Hyperbolic, local, integer, MDD, dissipative | P/SV/T, dispersive, attenuated, P↔SV↔T, interface | Local, local, pore-fluid, assumed, energy ratio, not performed | Analytical, no, no, no, not reproducible |
| RG-007 | Nonlocal piezothermoelastic + fluid, half-space, orthotropic, 3 fields, perfect | Hyperbolic, nonlocal, integer, MDD, dissipative | P, dispersive, attenuated, P↔interface, interface | Local, nonlocal (integral), none, assumed, energy ratio, claimed | Analytical, no, no, no, not reproducible |
| EXT-001 | Gradient-elastic, half-space, isotropic, 1 field, perfect | Hyperbolic, nonlocal (gradient), integer, none, conservative | P/SV, dispersive, none, none, interface | Nonlocal (integral), nonlocal, none, assumed, energy ratio, not performed | Analytical, no, no, no, not reproducible |

---

## 4. Empty Cells (Research Gaps Identified by Taxonomy)

| Dimension combination | Cell | Studies | Gap type |
|----------------------|------|---------|----------|
| Dissipative + nonlocal + interface + energy flux verified | D2=nonlocal, D4=flux verified, D3=interface | None | **No study verifies energy flux at nonlocal interfaces** |
| MDD + piezoelectric + imperfect bonding | D1=piezoelectric+imperfect, D2=MDD | None | **No study combines MDD with piezoelectricity and imperfect bonding** |
| Fractional + double porosity + interface | D2=fractional, D1=double porosity+interface | None | **No fractional double-porosity interface study** |
| Energy conservation verified at interface | D4=conservation verified | None performed | **No study independently verifies ΣR+ΣT+A=1 at interface** |
| Nonlocal + piezoelectric + interface + conservation checked | D2=nonlocal, D1=piezoelectric+interface, D4=conservation checked | None | **No study checks conservation at nonlocal piezoelectric interface** |
| Experimental validation of any interface energy flux | D5=experimental | None | **No experimental validation of interface energy flux** |

---

## 5. Contradiction Mapping

| Studies | Same D-classification | Contradiction | Resolution needed |
|---------|---------------------|---------------|-------------------|
| RG-003 vs all others | Piezothermoelastic interface + MDD | RG-003 claims conservation with asymmetric flux; others don't address conservation | Verify conservation with symmetric flux |
| FW-004 (GN II, conservative) vs FW-002 (LS, dissipative) | Both thermoelastic half-space | Different dissipation assumptions; cannot compare energy ratios directly | Common framework needed |
| RG-007 (claims conservation) vs RG-003 (claims conservation) | Both claim energy conservation | Different flux definitions; cannot compare directly | Standardize flux definition |

---

## 6. Taxonomy Visualization

### F-006: Theory hierarchy diagram

```
Generalized Multiphysics Continua
├── Classical (local, integer, dissipative)
│   ├── Elastic (1 field)
│   └── Thermoelastic (2 fields, Fourier)
├── Generalized Thermoelastic (local, integer)
│   ├── LS (1 relaxation, dissipative)
│   ├── GL (2 temperatures, conservative)
│   ├── GN II (thermal displacement, conservative)
│   ├── GN III (mixed, dissipative)
│   ├── DPL (2 lags, dissipative)
│   └── TPL (3 lags, dissipative)
├── Memory-Dependent (integral, hereditary)
│   └── MDD (kernel-defined, dissipative)
├── Nonlocal (integral, scale-dependent)
│   └── Eringen-type nonlocal
├── Coupled-Field (multi-physics)
│   ├── Piezoelectric (mechanical+electrical)
│   ├── Piezothermoelastic (mechanical+thermal+electrical)
│   ├── Poroelastic (mechanical+fluid)
│   └── Semiconductor (mechanical+thermal+carrier)
└── Advanced (fractional, strain-gradient, micropolar)
```

### F-007: Thermodynamic admissibility hierarchy

```
Thermodynamic Admissibility
├── Fully admissible (dissipation ≥ 0, well-posed, causal)
│   ├── Classical (Fourier, τ₀>0)
│   ├── LS (τ₀>0)
│   ├── DPL (τ_q ≥ τ_T)
│   └── GN III (parameter conditions)
├── Conditionally admissible
│   ├── MGT (parameter-dependent)
│   └── MDD (kernel-dependent)
└── Not classically dissipative
    ├── GN II (dissipationless by construction)
    └── Nonlocal (depends on formulation)
```

### F-008: Cross-model relationship map

```
Limiting cases (parameter substitutions):
MDD+TPL → Classical (all τ→0)
MDD+TPL → LS (τ_T=τ_v=0, n=1)
MDD+TPL → GN II (K=0)
MDD+TPL → DPL (τ_v=0)
DPL → Classical (τ_q, τ_T→0)
TPL → DPL (τ_v→0)
```

**Note:** All limiting procedures in corpus are parameter substitutions, not rigorous mathematical limit theorems.

---

## 7. Taxonomy Advantages Over Single-Axis Classification

| Feature | Single-axis | Five-dimensional taxonomy |
|---------|------------|--------------------------|
| Captures coupling complexity | No (one property at a time) | Yes (physical + mathematical + wave + energy + validation) |
| Identifies empty research cells | Partially | Systematically (6 empty cells identified) |
| Detects contradictions | No | Yes (3 contradiction pairs mapped) |
| Enables cross-study comparison | Limited | Under identical dimension-level conditions |
| Supports future research prioritization | Partially | Evidence-based gap identification |

---

## 8. Limitations

1. **Analyst-constructed**: Not validated by independent raters
2. **Abstract-only classifications**: 23 of 24 records classified from abstract/metadata only
3. **Dimension 4 mostly unclassified**: Energy-density formulation and dissipation mechanism not reported in corpus papers
4. **No inter-rater reliability**: Single analyst performed all classifications

---

## 9. Validation Plan

| Step | Action | Target |
|------|--------|--------|
| 1 | Independent reviewer applies taxonomy to 10 papers | Inter-rater reliability > 0.8 |
| 2 | Apply to additional papers from expanded search | 50–100 papers classified |
| 3 | Use empty cells to prioritize future research | Top 3 gaps identified |
| 4 | Document contradiction resolution strategy | 3 contradiction pairs addressed |

---

## 10. Integration with Manuscript

| Section | Taxonomy use |
|---------|-------------|
| §14 (Original Multidimensional Research Taxonomy) | Full presentation with all five dimensions |
| §12 (Comparative Synthesis) | Cross-theory comparison using taxonomy levels |
| §15 (Major Scientific Challenges) | Empty cells as challenge statements |
| §16 (Future Research Opportunities) | Gap-based research directions |
| Figures F-006 through F-009 | Visualizations of taxonomy |

---

**Next:** Proceed to Deliverable 9 (Figure-by-Figure Blueprint).
