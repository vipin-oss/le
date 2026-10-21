# Multidimensional Taxonomy — Phase 1

**Prepared:** 2026-10-21  
**Status:** Partially completed (taxonomy designed; not yet applied to full corpus)  
**Evidence standard:** `INFERRED` (analyst-constructed framework) / `VERIFIED` (where based on verified sources)

---

## 1. Purpose

The taxonomy classifies studies in the multiphysics wave-interface literature according to
independent dimensions. It supports:

- Cross-study comparison of equivalent physical settings
- Identification of gaps where no studies exist
- Structured presentation of contradictory findings
- Reproducible categorization for future updates

---

## 2. Taxonomy Dimensions

### Dimension 1 — Physical

| Sub-dimension | Levels | Example studies |
|---------------|--------|-----------------|
| Continuum type | Elastic, thermoelastic, piezoelectric, piezothermoelastic, piezomagnetic, flexomagnetic, porous, double-porosity, semiconductor | FW-001 through RG-007 |
| Geometry | Half-space, interface (two half-spaces), free surface, layered waveguide, slab, cylindrical tunnel, spherical cavity | RG-001, RG-002, RG-006, RG-007 |
| Material symmetry | Isotropic, orthotropic, monoclinic, functionally graded | RG-005 (monoclinic) |
| Number of coupled fields | 1 (elastic), 2 (thermoelastic), 3+ (piezo-thermo-elastic, poro-thermo-elastic) | RG-003, RG-005 |
| Interface configuration | Perfect bonding, imperfect (spring-type), surface irregularity, parabolic discontinuity | Not yet classified in corpus |

### Dimension 2 — Mathematical

| Sub-dimension | Levels | Example studies |
|---------------|--------|-----------------|
| Governing PDE class | Elliptic (static), parabolic (Fourier diffusion), hyperbolic (wave), mixed (generalized thermoelasticity) | FW-002 (hyperbolic), FW-004 (hyperbolic) |
| Linear vs nonlinear | Linear, nonlinear | FW-007 (nonlinear voids) |
| Local vs nonlocal operators | Local, nonlocal (Eringen), strain-gradient, couple-stress | FW-006 (nonlocal) |
| Integer vs fractional derivatives | Integer-order, fractional-order, memory-dependent derivative | FW-011 (MGT); RG-003 (MDD) |
| Memory/hereditary terms | None, memory kernel (MDD), fractional integral | RG-003, RG-004, RG-005 |
| Conservative vs dissipative | Conservative (GN II/III), dissipative (LS, DPL, MGT, MDD) | FW-004 (conservative), FW-002 (dissipative) |

### Dimension 3 — Wave

| Sub-dimension | Levels | Example studies |
|---------------|--------|-----------------|
| Wave family | P, SV, SH, Rayleigh, Love, Stoneley, thermal, plasma, quasi-plane | RG-007 (P/SV at fluid-solid) |
| Dispersion | Non-dispersive (classical elastic), dispersive (generalized, nonlocal) | FW-006 (dispersive) |
| Attenuation | None (conservative), attenuated (dissipative), complex wave number | FW-002, FW-011 |
| Mode conversion | None, P↔SV, P↔thermal, electrical↔mechanical | RG-001, RG-002, RG-005 |
| Surface vs bulk | Bulk waves, surface waves (Rayleigh), interface waves | RG-007 (interface) |

### Dimension 4 — Energy

| Sub-dimension | Levels | Example studies |
|---------------|--------|-----------------|
| Energy-density definition | Classical kinetic+strain+thermal, generalized with relaxation terms | Not yet classified |
| Flux formulation | Local (q·n + σ·v), nonlocal (integral), hereditary (MDD), electrical | Not yet classified — central gap |
| Dissipation mechanism | Thermal relaxation, viscous, electrical resistance, interface dissipation | Not yet classified |
| Interface power balance | Conservation assumed, not checked, explicitly verified | Not checked in corpus |
| Normalization convention | Amplitude ratio, energy ratio, intensity ratio | Amplitude ratio in corpus |
| Conservation verification | Not performed, performed, failed | Not performed in corpus |

### Dimension 5 — Validation

| Sub-dimension | Levels | Example studies |
|---------------|--------|-----------------|
| Analytical proof | Yes, no | FW-001 through FW-011 (yes, theoretical) |
| Numerical convergence | Yes, no | Not yet classified |
| Benchmark comparison | Yes, no | Not yet classified |
| Experimental evidence | Yes, no | No experimental studies in corpus |
| Reproducibility | Reproducible (analytical), not reproducible (no full text) | RG-003 (open access); others abstract-only |

---

## 3. Classification Rules

1. **Primary classification:** Each study receives one level per sub-dimension where information is available.
2. **Multiple levels:** A study may span multiple levels (e.g., both thermoelastic and piezoelectric coupling).
3. **Uncertain classification:** Marked as `UNCERTAIN` when full text is inaccessible.
4. **Not applicable:** Marked as `N/A` when the sub-dimension does not apply (e.g., porosity for non-porous media).
5. **Not reported:** Marked as `NOT REPORTED` when the paper does not address the sub-dimension.

---

## 4. Utility

### 4.1 Gap identification

Empty cells in the taxonomy matrix indicate gaps where no studies exist. For example:

| Dimension combination | Status | Studies |
|----------------------|--------|---------|
| Dissipative + nonlocal + interface + energy flux verified | EMPTY | None |
| MDD + piezoelectric + imperfect bonding | EMPTY | None |
| Fractional + double porosity + interface | EMPTY | None |
| Energy conservation check at interface | EMPTY | None performed |

### 4.2 Contradiction mapping

Studies with the same dimension classification but contradictory results are flagged for detailed comparison.

### 4.3 Reproducibility

The taxonomy can be reapplied by independent reviewers using the classification rules. Inter-rater reliability should be assessed in Phase 1.

---

## 5. Limitations

- Taxonomy is analyst-constructed; not validated by independent raters
- Applied only to seed records (18 studies) so far
- Full corpus classification pending (Milestone F)
- Some sub-dimensions cannot be classified from abstract-only records

---

## 6. Next Steps

1. Apply taxonomy to all studies in `04_literature_master_database.csv`
2. Record classifications in a new column or separate file
3. Identify empty cells (gaps)
4. Map contradictory findings within cells
5. Validate taxonomy with independent reviewer