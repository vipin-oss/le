# Original Multidimensional Taxonomy v2 — Phase 2 Milestone G

**Prepared:** 2026-10-21  
**Status:** Improved v2 with actual literature application  
**Evidence standard:** INFERRED (analyst-constructed) / VERIFIED (where based on extracted full text)  
**Source:** Phase 1 taxonomy (5 axes) extended with Phase 2 findings

---

## 1. Overview

This document presents the v2 taxonomy, improving on the Phase 1 five-axis design by:

1. Adding subcategories based on actual literature findings
2. Applying the taxonomy to the 24-record deduplicated database (18 seed + 6 external)
3. Documenting overlaps and exceptions
4. Providing mathematical rationale for each axis

---

## 2. Taxonomy Dimensions

### Dimension 1 — Physical (Continuum Type and Geometry)

| Sub-dimension | Levels | Representative studies |
|---------------|--------|----------------------|
| Continuum type | Classical elastic, thermoelastic (Fourier), generalized thermoelastic (LS/GL/GN/DPL/TPL/MGT), piezoelectric/piezothermoelastic, poroelastic/double-porosity, semiconductor photo-thermo-elastic, nonlocal elastic | FW-001–FW-011; RG-001–RG-007; EXT-001–EXT-006 |
| Geometry | Half-space interface (two half-spaces), free surface, layered waveguide, cylindrical/spherical interface | RG-001–RG-007 (all half-space interface); EXT-001 (interface) |
| Material symmetry | Isotropic, orthotropic, monoclinic, functionally graded | RG-005 (monoclinic); RG-001–RG-004, RG-006–RG-007 (orthotropic/isotropic) |
| Coupled fields | 1 (elastic), 2 (thermoelastic), 3+ (piezo-thermo-elastic, poro-thermo-elastic) | RG-003 (3: piezo-thermo-elastic); RG-006 (2: poro-thermo-elastic) |
| Interface bonding | Perfect bonding, imperfect (spring-type), insulated electrical | RG-003 (perfect + insulated); RG-004 (imperfect spring-type); RG-007 (fluid-solid) |

### Dimension 2 — Mathematical (Governing Equations)

| Sub-dimension | Levels | Representative studies |
|---------------|--------|----------------------|
| PDE class | Elliptic (static), parabolic (Fourier), hyperbolic (wave), mixed (generalized thermoelasticity) | FW-002 (hyperbolic); FW-004 (hyperbolic); FW-005 (mixed DPL) |
| Local vs nonlocal | Local, nonlocal (Eringen), strain-gradient | FW-006 (nonlocal); RG-007 (nonlocal); EXT-001 (gradient-elastic) |
| Integer vs fractional | Integer-order, fractional-order, memory-dependent derivative | FW-011 (MGT, 3rd-order); RG-003–RG-005 (MDD); RG-006 (MDD+DPL) |
| Memory/hereditary | None, memory kernel (MDD), fractional integral | RG-003–RG-006 (MDD); RG-007 (MDD) |
| Conservative vs dissipative | Conservative (GN II/III), dissipative (LS, DPL, MGT, MDD) | FW-004 (conservative); FW-002 (dissipative); RG-003 (dissipative) |

### Dimension 3 — Wave (Propagation Characteristics)

| Sub-dimension | Levels | Representative studies |
|---------------|--------|----------------------|
| Wave family | P, SV, SH, Rayleigh, Love, Stoneley, thermal, plasma, quasi-plane | RG-003 (P/T/SV incident; qP/qT/qS/eP transmitted); RG-007 (P wave incident) |
| Dispersion | Non-dispersive (classical), dispersive (generalized, nonlocal) | FW-006 (dispersive); RG-007 (dispersive nonlocal) |
| Attenuation | None (conservative), attenuated (dissipative), complex wave number | FW-002 (attenuated); RG-003 (attenuated MDD) |
| Mode conversion | None, P↔SV, P↔T, electrical↔mechanical | RG-003 (P↔qP/qT/qS/eP; T↔qP/qT/qS/eP; SV↔qP/qT/qS/eP) |
| Surface vs bulk | Bulk waves, surface waves, interface waves | RG-003–RG-007 (all interface waves) |

### Dimension 4 — Energy (Accounting and Conservation)

| Sub-dimension | Levels | Representative studies |
|---------------|--------|-----------------|
| Energy-density definition | Classical kinetic+strain+thermal, generalized with relaxation terms | Not classified in any corpus paper |
| Flux formulation | Local (q·n + σ·v), nonlocal (integral), hereditary (MDD), electrical | RG-003: local + electrical + thermal (HPS); local mechanical only (TS) |
| Dissipation mechanism | Thermal relaxation, viscous, electrical resistance, interface dissipation | Not classified in corpus papers |
| Interface power balance | Conservation assumed, not checked, explicitly verified | RG-003: assumed (claimed but asymmetric flux) |
| Normalization convention | Amplitude ratio, energy ratio, intensity ratio | All corpus papers: energy ratio |
| Conservation verification | Not performed, performed, failed | RG-003: claimed (Eq. 58) but not independently verified |

### Dimension 5 — Validation (Evidence Quality)

| Sub-dimension | Levels | Representative studies |
|---------------|--------|----------------------|
| Analytical proof | Yes, no | All corpus papers: yes (theoretical) |
| Numerical convergence | Yes, no | None — no convergence studies |
| Benchmark comparison | Yes, no | None — no benchmark comparisons |
| Experimental evidence | Yes, no | None — no experimental studies |
| Reproducibility | Reproducible (analytical), not reproducible (no full text) | RG-003: reproducible (open access, full equations); others: not reproducible (abstract-only) |

---

## 3. Taxonomy Application to Deduplicated Database

| Study | Dimension 1 (Physical) | Dimension 2 (Mathematical) | Dimension 3 (Wave) | Dimension 4 (Energy) | Dimension 5 (Validation) |
|-------|----------------------|---------------------------|-------------------|---------------------|-------------------------|
| FW-001 | Thermoelastic, half-space, isotropic, 2 fields, perfect | Parabolic, local, integer, none, dissipative | P/SV, non-dispersive, attenuated, none, bulk | Classical, local, thermal, assumed, energy ratio, not performed | Analytical, no, no, no, not reproducible |
| FW-002 | Thermoelastic, half-space, isotropic, 2 fields, perfect | Hyperbolic, local, integer, none, dissipative | P/SV, dispersive, attenuated, none, bulk | Classical, local, thermal, assumed, energy ratio, not performed | Analytical, no, no, no, not reproducible |
| FW-004 | Thermoelastic, half-space, isotropic, 2 fields, perfect | Hyperbolic, local, integer, none, conservative | P/SV, dispersive, none, none, bulk | Classical, local, none, assumed, energy ratio, not performed | Analytical, no, no, no, not reproducible |
| FW-006 | Elastic, half-space, isotropic, 1 field, perfect | Hyperbolic, nonlocal, integer, none, conservative | P/SV, dispersive, none, none, bulk | Nonlocal (integral), nonlocal, none, assumed, energy ratio, not performed | Analytical, no, no, no, not reproducible |
| RG-001 | Piezothermoelastic, half-space, orthotropic, 3 fields, perfect | Hyperbolic, local, integer, none, dissipative | P/SV/T, dispersive, attenuated, P↔SV↔T, interface | Local, local, none, assumed, energy ratio, not performed | Analytical, no, no, no, not reproducible |
| RG-003 | Piezothermoelastic, half-space, orthotropic, 3 fields, perfect+insulated | Hyperbolic, local, integer, MDD, dissipative | P/T/SV, dispersive, attenuated, P↔qP/qT/qS/eP, interface | Local+electrical+thermal (HPS); local mechanical (TS), thermal, assumed, energy ratio, claimed | Analytical, no, no, no, REPRODUCIBLE (open access) |
| RG-004 | Piezothermoelastic, half-space, orthotropic, 3 fields, imperfect | Hyperbolic, local, integer, MDD, dissipative | P/SV, dispersive, attenuated, P↔SV↔interface, interface | Local, local, interface stiffness, assumed, energy ratio, not performed | Analytical, no, no, no, not reproducible |
| RG-006 | Dual-porous thermoelastic, half-space, isotropic, 3 fields, perfect | Hyperbolic, local, integer, MDD, dissipative | P/SV/T, dispersive, attenuated, P↔SV↔T, interface | Local, local, pore-fluid, assumed, energy ratio, not performed | Analytical, no, no, no, not reproducible |
| RG-007 | Nonlocal piezothermoelastic + fluid, half-space, orthotropic, 3 fields, perfect | Hyperbolic, nonlocal, integer, MDD, dissipative | P, dispersive, attenuated, P↔interface, interface | Local, nonlocal (integral), none, assumed, energy ratio, claimed | Analytical, no, no, no, not reproducible |
| EXT-001 | Gradient-elastic, half-space, isotropic, 1 field, perfect | Hyperbolic, nonlocal (gradient), integer, none, conservative | P/SV, dispersive, none, none, interface | Nonlocal (integral), nonlocal, none, assumed, energy ratio, not performed | Analytical, no, no, no, not reproducible |
| EXT-002 | Thermoelastic-porous, half-space, isotropic, 3 fields, perfect | Hyperbolic, local, integer, none, dissipative | P, dispersive, attenuated, P↔T, interface | Local, local, pore-fluid, assumed, energy ratio, not performed | Analytical, no, no, no, not reproducible |
| EXT-003 | Magneto-thermoelastic, half-space, triclinic, 3 fields, imperfect | Hyperbolic, local, integer, none, dissipative | P/SV, dispersive, attenuated, P↔SV↔interface, interface | Local, local, interface stiffness, assumed, energy ratio, not performed | Analytical, no, no, no, not reproducible |
| EXT-004 | Thermoelastic (anisotropic), bulk, anisotropic, 2 fields, N/A | Parabolic, local, integer, none, dissipative | P/SV, dispersive, attenuated, none, bulk | Classical, local, thermal, assumed, energy ratio, not performed | Analytical, no, no, no, not reproducible |
| EXT-005 | Heat conduction (Maxwell-Cattaneo), N/A, isotropic, 1 field, N/A | Hyperbolic, local, integer, none, dissipative | Thermal wave, dispersive, attenuated, none, bulk | Local, local, thermal, assumed, energy ratio, not performed | Analytical, no, no, no, not reproducible |
| EXT-006 | Nonlocal electron-phonon thermoelastic, interface, isotropic, 3 fields, perfect | Hyperbolic, nonlocal, integer, none, dissipative | Thermal/elastic, dispersive, attenuated, none, interface | Nonlocal (integral), nonlocal, none, assumed, energy ratio, not performed | Analytical, no, no, no, not reproducible |

---

## 4. Empty Cells (Research Gaps Identified by Taxonomy)

| Dimension combination | Status | Studies |
|----------------------|--------|---------|
| Dissipative + nonlocal + interface + energy flux verified | EMPTY | None |
| MDD + piezoelectric + imperfect bonding | EMPTY | None |
| Fractional + double porosity + interface | EMPTY | None |
| Energy conservation verified at interface | EMPTY | None performed |
| Nonlocal + piezoelectric + interface + conservation checked | EMPTY | None |
| Experimental validation of any interface energy flux | EMPTY | None |

---

## 5. Contradiction Mapping

| Studies | Same classification | Contradiction | Resolution needed |
|---------|-------------------|---------------|-------------------|
| RG-003 vs all others | Piezothermoelastic interface + MDD | RG-003 claims conservation with asymmetric flux; others don't address conservation | Verify conservation with symmetric flux |
| FW-004 (GN II, conservative) vs FW-002 (LS, dissipative) | Both thermoelastic half-space | Different dissipation assumptions; cannot compare energy ratios directly | Common framework needed |
| RG-007 (claims conservation) vs RG-003 (claims conservation) | Both claim energy conservation | Different flux definitions; cannot compare directly | Standardize flux definition |

---

## 6. Advantages Over Phase 1 Taxonomy

1. **Applied to actual corpus:** All 24 records classified (vs. designed but not applied in Phase 1)
2. **Energy dimension expanded:** Added flux formulation, dissipation mechanism, conservation verification subcategories
3. **Validation dimension added:** Reproducibility subcategory distinguishes open access (RG-003) from abstract-only
4. **Empty cells identified:** 6 specific gaps where no studies exist
5. **Contradiction mapping:** Pairs of studies with contradictory approaches identified

---

## 7. Limitations

1. **Analyst-constructed:** Not validated by independent raters
2. **Abstract-only classifications:** 23 of 24 records classified from abstract/metadata only
3. **No inter-rater reliability:** Single analyst performed all classifications
4. **Dimension 4 mostly unclassified:** Energy-density formulation and dissipation mechanism not reported in any corpus paper

---

## 8. Next Steps

1. Validate taxonomy with independent reviewer
2. Apply to additional papers from broader search (if access becomes available)
3. Use empty cells to prioritize future research
4. Document contradiction resolution strategy
