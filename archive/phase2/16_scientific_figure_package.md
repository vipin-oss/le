# Scientific Figure Package — Phase 2 Milestone G

**Prepared:** 2026-10-21  
**Status:** Specifications only — no figures generated  
**Evidence standard:** SPECIFIED  
**Source:** Independent specification based on Phase 2 findings

---

## 1. Figure Package Overview

Approximately 15–20 original vector figures, organized by research theme. Each figure has a specification with scientific objective, mathematical basis, verified labels, source attribution, and caption.

**Format:** TikZ/PGFPlots (preferred) or SVG with reproducible source code  
**Directory:** `figures/tikz/` and `figures/svg/` (to be created)

---

## 2. Priority 1 — Core Mathematical Figures (Must be created before manuscript drafting)

| Fig ID | Title | Mathematical basis | Source | Status |
|--------|-------|-------------------|--------|--------|
| F-001 | Continuum balance-law dependency graph | Theorems 2.1–7.1 from `07_continuum_balance_derivations.md` | Independent derivation | NOT STARTED |
| F-002 | Theory-specific energy flux comparison | Section 14 of `08_theory_specific_energy_flux.md` | Independent derivation | NOT STARTED |
| F-003 | RG-003 asymmetric energy flux | Eqs. (45)-(46) from RG-003 full text | Verified from full text | NOT STARTED |
| F-004 | Interface scattering geometry | Section 1 of `11_scattering_matrix_derivations.md` | Independent derivation | NOT STARTED |
| F-005 | Energy conservation identity verification | Section 5 of `12_interface_energy_balance.md` | Independent derivation | NOT STARTED |

---

## 3. Priority 2 — Theory Classification Figures

| Fig ID | Title | Mathematical basis | Source | Status |
|--------|-------|-------------------|--------|--------|
| F-006 | Generalized thermoelasticity theory hierarchy | Section 6 of `08_theory_specific_energy_flux.md` | Independent derivation | NOT STARTED |
| F-007 | Thermodynamic admissibility hierarchy | Section 4 of `09_thermodynamic_admissibility.md` | Independent derivation | NOT STARTED |
| F-008 | Five-axis taxonomy application | `11_multidimensional_taxonomy.md` (Phase 1) | Analyst-constructed | NOT STARTED |
| F-009 | Research gap network | `14_validated_research_gaps.csv` | Evidence-based | NOT STARTED |

---

## 4. Priority 3 — Benchmark and Validation Figures

| Fig ID | Title | Mathematical basis | Source | Status |
|--------|-------|-------------------|--------|--------|
| F-010 | BM-1 classical elastic interface geometry | Section 2 of `15_mathematical_benchmark_results.md` | Independent derivation | NOT STARTED |
| F-011 | BM-1 conservation check (R+T=1) | Section 2.9 of `15_mathematical_benchmark_results.md` | Independent derivation | NOT STARTED |
| F-012 | Dissipation comparison across theories | Section 3 of `09_thermodynamic_admissibility.md` | Independent derivation | NOT STARTED |

---

## 5. Priority 4 — Synthesis Figures

| Fig ID | Title | Mathematical basis | Source | Status |
|--------|-------|-------------------|--------|--------|
| F-013 | Literature coverage map | `01_extended_search_results.csv`, `03_deduplicated_literature_database.csv` | Search results | NOT STARTED |
| F-014 | Citation chaining network | `02_citation_chaining_network.csv` | Citation chasing | NOT STARTED |
| F-015 | Multiphysics coupling network | Section 1 of `13_multiphysics_comparative_synthesis.md` | Independent synthesis | NOT STARTED |

---

## 6. Figure Quality Standards

1. **Mathematical correctness:** Every equation, arrow, and label must reflect actual mathematical relationships derived in this project
2. **Source traceability:** Each figure cites its underlying equations or data sources
3. **Editable format:** TikZ/PGFPlots source code required; SVG as alternative
4. **No decorative figures:** Every figure answers a specific scientific question
5. **No unjustified relationships:** No arrows or connections without mathematical basis
6. **Standalone caption:** Each figure must be understandable without reading the main text

---

## 7. Next Steps

1. Create `figures/tikz/` and `figures/svg/` directories
2. Draft TikZ code for F-001 (balance-law dependency graph)
3. Draft TikZ code for F-003 (RG-003 asymmetric flux — critical finding)
4. Draft TikZ code for F-005 (conservation identity)
5. Create figure captions with source references
