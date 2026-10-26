# Deliverable 10 — Table-by-Table Blueprint

**Branch:** arena/40393d9f-le  
**Prepared:** 2026-10-21  
**Alignment:** Master Editorial Directive §11 (comprehensive table design)  
**Builds on:** Phase 2 comparative synthesis and taxonomy

---

## 1. Table Strategy

| Parameter | Target |
|-----------|--------|
| Total tables | 14–16 |
| Format | LaTeX booktabs, publication-quality |
| Purpose | Each table serves a clear analytical purpose |
| Verification | Every entry verified from primary source |
| Notes | Explanatory notes when assumptions differ |
| No non-equivalent comparisons | Quantities compared only under identical conditions |

---

## 2. Table Specifications

### Table 1 — Notation Conventions (master symbol table)

| Purpose | Master reference for all symbols used in the manuscript |
| Section | Front matter (before §1) |
| Rows | ~40 symbols |
| Columns | Symbol | Meaning | Units | First appearance |
| Source | Derived from Phase 2 notation analysis |
| Status | REQUIRED (following reference model Table 1) |

**Sample entries:**

| Symbol | Meaning | Units | First appears |
|--------|---------|-------|---------------|
| uᵢ | Displacement vector component | m | §3.1 |
| vᵢ | Velocity vector component | m/s | §3.1 |
| εᵢⱼ | Infinitesimal strain tensor | dimensionless | §3.1 |
| σᵢⱼ | Cauchy stress tensor | Pa | §3.2 |
| qᵢ | Heat flux vector | W/m² | §3.3 |
| T | Absolute temperature | K | §3.3 |
| ψ | Helmholtz free energy density | J/kg | §3.5 |
| s | Specific entropy | J/(kg·K) | §3.5 |
| Jᵢ | Energy flux vector | W/m² | §3.8 |
| τ₀ | Lord–Shulman relaxation time | s | §4.3 |
| τ_q, τ_T | Dual-phase-lag times | s | §4.7 |
| eₖᵢⱼ | Piezoelectric stress coefficient | C/m² | §5.1 |
| Dᵢ | Electric displacement vector | C/m² | §5.1 |
| φ | Electric potential | V | §5.1 |
| κᵢⱼ | Dielectric permittivity tensor | F/m | §5.1 |

---

### Table 2 — Acronyms and Abbreviations

| Purpose | Master reference for all acronyms |
| Section | Front matter |
| Rows | ~30 acronyms |
| Columns | Acronym | Definition | First appears |
| Source | Phase 2 corpus |
| Status | REQUIRED (following reference model Table 2) |

**Sample entries:**

| Acronym | Definition | First appears |
|---------|-----------|---------------|
| LS | Lord–Shulman | §4.3 |
| GL | Green–Lindsay | §4.4 |
| GN | Green–Naghdi | §4.5–4.6 |
| DPL | Dual-phase-lag | §4.7 |
| TPL | Three-phase-lag | §4.8 |
| MGT | Modified generalized thermoelasticity | §4.x |
| MDD | Memory-dependent derivative | §4.9 |
| PDE | Partial differential equation | §3 |
| BC | Boundary condition | §9 |
| IC | Initial condition | §3 |

---

### Table 3 — Historical Development of Major Theories

| Purpose | Chronological development of continuum wave theories |
| Section | §4.1 |
| Rows | 10–12 theories |
| Columns | Theory | Year | Key reference | Main innovation | Mathematical class |
| Source | Phase 2: FW-001 through FW-011; Phase 3 §4.1 |
| Status | REQUIRED |

**Sample entries:**

| Theory | Year | Key reference | Main innovation | Mathematical class |
|--------|------|---------------|-----------------|-------------------|
| Classical coupled thermoelasticity | 1956 | Biot 1956 | Coupled mechanical–thermal equations | Parabolic-hyperbolic |
| Lord–Shulman | 1967 | LS 1967 | Single relaxation time; finite wave speed | Hyperbolic |
| Green–Lindsay | 1972 | GL 1972 | Two temperatures; dissipationless | Hyperbolic |
| Green–Naghdi II | 1991 | GN 1991 | Thermal displacement; energy conservation | Hyperbolic |
| Green–Naghdi III | 1991 | GN 1991 | Dissipative variant | Mixed |
| Dual-phase-lag | 1995 | Tzou 1995 | Two relaxation times | Hyperbolic |
| Three-phase-lag | 2007 | Roy Choudhuri 2007 | Three relaxation times | Hyperbolic |
| MGT | 2019 | Quintanilla 2019 | Third-order in time | Hyperbolic |
| MDD | 2011/2021 | Wang & Li; Abouelregal | Memory-dependent derivative | Hereditary |
| Nonlocal elasticity | 1972 | Eringen 1972 | Integral constitutive relations | Nonlocal |

---

### Table 4 — Governing Equations by Model Family

| Purpose | Compare governing equations across theories |
| Section | §4.2 through §4.9 |
| Rows | 9 theory families |
| Columns | Theory | Momentum equation | Heat equation | Constitutive relation | Key parameters |
| Source | Derived from Phase 2 equation register |
| Status | REQUIRED |

**Sample entries:**

| Theory | Momentum | Heat equation | Key parameters |
|--------|---------|---------------|----------------|
| Classical | ρüᵢ = σⱼᵢ,ⱼ | ρcᵥṪ = k∇²T − βT₀u̇ᵢ,ᵢ | None |
| LS | ρüᵢ = σⱼᵢ,ⱼ | ρcᵥ(Ṫ + τ₀T̈) = k∇²T(1 + τ₀∂/∂t) − ... | τ₀ |
| DPL | ρüᵢ = σⱼᵢ,ⱼ | qᵢ(t+τ_q) = −kT,ᵢ(t+τ_T) | τ_q, τ_T |
| TPL | ρüᵢ = σⱼᵢ,ⱼ | qᵢ(t+τ_q) = −k[T,ᵢ(t+τ_T) + (τ_v/2)T,ᵢₜₜ] | τ_q, τ_T, τ_v |
| MDD | ρüᵢ = σⱼᵢ,ⱼ | MDD-modified heat equation | τ + kernel κ |

---

### Table 5 — Constitutive Assumptions by Theory

| Purpose | Document what each theory assumes about materials |
| Section | §4–7 |
| Rows | 9 theory families |
| Columns | Theory | Stress-strain | Heat flux-temperature | Entropy-temperature | Free energy form |
| Source | Phase 2: EQ-006, EQ-010 |
| Status | REQUIRED |

---

### Table 6 — Thermal Transport Models

| Purpose | Compare heat conduction models |
| Section | §4–6 |
| Rows | 8 models |
| Columns | Model | Equation | Relaxation times | Wave speed | Dissipation |
| Source | Phase 2: `05_mathematical_content_plan.md` §4.2–4.9 |
| Status | REQUIRED |

---

### Table 7 — Coupling Mechanisms by Multiphysics Family

| Purpose | Document field couplings in each theory |
| Section | §5 |
| Rows | 7 coupling types |
| Columns | Coupling | Fields involved | Governing equations | Interface conditions | Example studies |
| Source | Phase 2: `05_mathematical_content_plan.md` §5 |
| Status | REQUIRED |

---

### Table 8 — Interface Conditions

| Purpose | Compare boundary conditions across theories |
| Section | §9.3 |
| Rows | 6 condition types |
| Columns | Condition | Classical | LS | GN | DPL | MDD | Nonlocal | Piezoelectric |
| Source | Phase 2: `11_scattering_matrix_derivations.md`, RG-003 Eq. (38) |
| Status | REQUIRED |

**Condition types:** Displacement continuity, traction continuity, temperature continuity, heat flux continuity, electric potential continuity, electric displacement continuity.

---

### Table 9 — Wave-Mode Characteristics

| Purpose | Compare wave propagation across theories |
| Section | §8.2–8.4 |
| Rows | 9 theory families × 3 wave types |
| Columns | Theory | Wave type | Speed | Dispersion | Attenuation | Polarization |
| Source | Phase 2: `10_harmonic_energy_transport.md`, RG-003 Eq. (27) |
| Status | REQUIRED |

---

### Table 10 — Mathematical Methods

| Purpose | Catalog solution approaches |
| Section | §8 |
| Rows | 8 methods |
| Columns | Method | Applicable theories | Advantages | Limitations | Example studies |
| Source | Phase 2: `15_mathematical_benchmark_results.md` |
| Status | REQUIRED |

---

### Table 11 — Energy Transport Formulations

| Purpose | Compare energy flux definitions across theories |
| Section | §10.2–10.3 |
| Rows | 9 theory families |
| Columns | Theory | Energy flux form | Thermal term | Electrical term | Memory term | Verification status |
| Source | Phase 2: `06_equation_provenance_register.csv`, GAP-011 |
| Status | REQUIRED |

**Key finding to document:** RG-003 asymmetric flux (HPS has thermal term; TS does not)

---

### Table 12 — Material Systems Studied

| Purpose | Document materials used in the literature |
| Section | §13 |
| Rows | 10–12 material systems |
| Columns | Material | Theory applied | Wave types | Key findings | Reference |
| Source | Phase 2: RG-003 Table 1 (magnesium, cadmium selenide); corpus |
| Status | REQUIRED |

---

### Table 13 — Existing Review Coverage

| Purpose | Document what existing reviews cover |
| Section | §2.7, §12.1 |
| Rows | 5–10 reviews |
| Columns | Review | Year | Scope | Theories covered | Interface phenomena | Energy transport | Gap |
| Source | Phase 2: Family F search results |
| Status | REQUIRED |

---

### Table 14 — Model-Specific Research Limitations

| Purpose | Document known limitations of each theory |
| Section | §15 |
| Rows | 9 theory families |
| Columns | Theory | Mathematical limitation | Physical limitation | Interface limitation | Energy flux status | Open questions |
| Source | Phase 2: `14_validated_research_gaps.csv` |
| Status | REQUIRED |

---

### Table 15 — Emerging Research Directions

| Purpose | Map future opportunities to evidence |
| Section | §16 |
| Rows | 8–10 directions |
| Columns | Direction | Foundation | Why important | What achieved | What remains open | Approaches | Obstacles |
| Source | Phase 2: `14_validated_research_gaps.csv`; Phase 3 §16 |
| Status | REQUIRED |

---

### Table 16 — Equation Verification Register (supplementary)

| Purpose | Track every equation's verification status |
| Section | Appendix A |
| Rows | 23+ equations |
| Columns | Eq. ID | Equation | Source | Status | Assumptions | Validity domain | Decision |
| Source | Phase 2: `06_equation_provenance_register.csv` |
| Status | REQUIRED (Appendix) |

---

## 3. Table Priority Ranking

### Priority 1 — Must be created before manuscript drafting (6 tables)

| Table ID | Why critical | Section |
|----------|--------------|---------|
| Table 1 | Notation — readers need symbol reference | Front matter |
| Table 2 | Acronyms — readers need abbreviation reference | Front matter |
| Table 3 | Historical development — establishes context | §4.1 |
| Table 4 | Governing equations — core mathematical content | §4–7 |
| Table 11 | Energy transport — central Phase 2 finding | §10.2–10.3 |
| Table 16 | Equation register — quality control | Appendix A |

### Priority 2 — Important for comparative clarity (5 tables)

| Table ID | Section |
|----------|---------|
| Table 5 | Constitutive assumptions | §4–7 |
| Table 6 | Thermal transport models | §4–6 |
| Table 8 | Interface conditions | §9.3 |
| Table 9 | Wave-mode characteristics | §8.2–8.4 |
| Table 14 | Research limitations | §15 |

### Priority 3 — Supporting tables (5 tables)

| Table ID | Section |
|----------|---------|
| Table 7 | Coupling mechanisms | §5 |
| Table 10 | Mathematical methods | §8 |
| Table 12 | Material systems | §13 |
| Table 13 | Existing review coverage | §2.7 |
| Table 15 | Future directions | §16 |

---

## 4. Table Design Standards (Directive §11)

| Standard | Requirement |
|----------|-------------|
| Clear analytical purpose | Every table answers a specific comparative question |
| Verified entries | Every entry traceable to primary source |
| No non-equivalent comparisons | Compare only under identical conditions |
| Explanatory notes | When assumptions differ between entries |
| Consistent formatting | LaTeX booktabs, consistent column widths |
| Self-contained caption | Understandable without main text |
| Source attribution | Each table cites its data sources |

---

## 5. Sample Table Specification (Table 11 — Critical)

| Field | Specification |
|-------|---------------|
| Table ID | Table 11 |
| Title | Energy transport formulations across generalized continuum theories |
| Purpose | Compare energy flux definitions; document RG-003 asymmetry (GAP-011) |
| Section | §10.2–10.3 |
| Rows | 9 theory families |
| Columns | Theory | Mechanical flux | Thermal flux | Electrical flux | Memory/hereditary | Verification status |
| Key finding | RG-003: HPS side has all three flux channels; TS side has mechanical only |
| Source | Phase 2: `06_equation_provenance_register.csv` EQ-016, EQ-017; GAP-011 |
| Verification | All entries checked against source papers |
| Notes | "UNCERTAIN" entries are open questions, not canonical equations |

**Draft row entries:**

| Theory | Mechanical (σv) | Thermal (q) | Electrical | Memory | Status |
|--------|----------------|-------------|------------|--------|--------|
| Classical | ✓ | ✓ | ✗ | ✗ | VERIFIED |
| LS | ✓ | ✓ | ✗ | ✗ (relaxation) | VERIFIED (flux form UNCERTAIN) |
| GN II | ✓ | ✓ | ✗ | ✗ | VERIFIED (flux form UNCERTAIN) |
| DPL | ✓ | ✓ | ✗ | ✗ (lag) | VERIFIED (flux form UNCERTAIN) |
| MDD | ✓ | ✓ | ✗ | ✓ (kernel) | VERIFIED (flux form UNCERTAIN) |
| Nonlocal | ✓ (integral) | ✓ (integral) | ✗ | ✗ | VERIFIED (flux form UNCERTAIN) |
| Piezoelectric | ✓ | ✓ | ✓ | ✗ | VERIFIED (flux form UNCERTAIN) |
| Piezothermoelastic (RG-003 HPS) | ✓ | ✓ | ✓ | ✓ (MDD) | VERIFIED (Eq. 45) |
| Piezothermoelastic (RG-003 TS) | ✓ | ✗ | ✗ | ✗ | VERIFIED (Eq. 46; ASYMMETRIC) |

---

## 6. Table Creation Workflow

```
1. Draft specification (this document)
2. Collect data from Phase 2 artifacts and primary sources
3. Verify every entry against source
4. Create LaTeX booktabs table
5. Add explanatory notes for assumption differences
6. Write self-contained caption
7. Save source file in tables/
8. Record in table register
```

---

## 7. Directory Structure

```
tables/
├── Table1_notation.tex
├── Table2_acronyms.tex
├── Table3_historical_development.tex
├── ...
└── table_register.csv  # Status tracking
```

---

## 8. Estimated Effort

| Priority group | Table count | Est. hours per table | Total hours |
|---------------|-------------|---------------------|-------------|
| Priority 1 | 6 | 4 | 24 |
| Priority 2 | 5 | 3 | 15 |
| Priority 3 | 5 | 2 | 10 |
| **Total** | **16** | — | **49 hours** |

---

## 9. Integration with Manuscript

| Section | Tables referenced |
|---------|------------------|
| Front matter | Table 1, Table 2 |
| §3 (Foundations) | — |
| §4 (Thermoelastic) | Table 3, Table 4, Table 5, Table 6 |
| §5 (Multiphysics) | Table 4, Table 5, Table 7 |
| §6 (Transport) | Table 4, Table 6 |
| §7 (Nonlocal) | Table 4, Table 5 |
| §8 (Methods) | Table 10 |
| §9 (Interfaces) | Table 8, Table 9 |
| §10 (Energy) | Table 4, Table 11, Table 16 |
| §12 (Synthesis) | Table 4, Table 5, Table 9, Table 11, Table 14 |
| §13 (Applications) | Table 12 |
| §14 (Taxonomy) | — |
| §15 (Challenges) | Table 14 |
| §16 (Future) | Table 15 |
| Appendix A | Table 16 |

---

**Next:** Proceed to Deliverable 11 (Author-Publication Consistency Review Plan).
