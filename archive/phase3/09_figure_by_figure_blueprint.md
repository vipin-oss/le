# Deliverable 9 — Figure-by-Figure Blueprint

**Branch:** arena/40393d9f-le  
**Prepared:** 2026-10-21  
**Alignment:** Master Editorial Directive §10 (major figure and illustration program)  
**Reference model:** Abdalla et al. (2022) — ~27 figures, 1 per 8 pages, each with specific scientific purpose  
**Builds on:** Phase 2 figure package (`phase2/16_scientific_figure_package.md`)

---

## 1. Figure Strategy

| Parameter | Target |
|-----------|--------|
| Total figures | 25–40 (depending on journal limits) |
| Format | Editable vector (TikZ/PGFPlots preferred, SVG alternative) |
| Density | ~1 figure per 8–10 pages of content |
| Caption style | Self-contained (understandable without reading main text) |
| Source file | Every figure has a source file in `figures/tikz/` or `figures/svg/` |
| Citation | Every figure cites its underlying data or equations |

---

## 2. Figure Groups

### Group A — Historical and Conceptual Figures (5 figures)

| Fig ID | Title | Purpose | Mathematical basis | Source | Priority |
|--------|-------|---------|-------------------|--------|----------|
| F-A01 | Evolution of continuum wave theories | Historical development timeline | Timeline of key publications (Biot 1956 → present) | Phase 2: FW-001 through FW-011 dates | HIGH |
| F-A02 | Historical development of thermoelasticity | Theory lineage | Theory family tree | Phase 2: `04_chapter_by_chapter_outline.md` §4.1 | HIGH |
| F-A03 | Emergence of generalized constitutive models | When each theory appeared | Publication dates by theory | Phase 2: `05_mathematical_content_plan.md` §4.1 | HIGH |
| F-A04 | Evolution of multiphysics coupling research | Coupling types over time | Piezoelectric, porous, semiconductor chronology | Phase 2: corpus classification | MEDIUM |
| F-A05 | Research evolution map | How the field developed | Citation network | Phase 2: `02_citation_chaining_network.csv` | MEDIUM |

### Group B — Physical Theory Figures (8 figures)

| Fig ID | Title | Purpose | Mathematical basis | Source | Priority |
|--------|-------|---------|-------------------|--------|----------|
| F-B01 | Continuum deformation and wave propagation | Kinematics basics | Displacement, strain, velocity | `07_continuum_balance_derivations.md` | HIGH |
| F-B02 | Mechanical–thermal field interactions | Thermoelastic coupling | σᵢⱼε̇ᵢⱼ − βT,ᵢ terms | §3.3, §4.2 | HIGH |
| F-B03 | Electromechanical coupling mechanisms | Piezoelectricity | eₖᵢⱼ, Dᵢ equations | §5.1, EQ-010–EQ-014 | HIGH |
| F-B04 | Semiconductor photothermal processes | Carrier diffusion | Drift-diffusion coupled to elasticity | §5.6 | MEDIUM |
| F-B05 | Void and double-porosity structures | Porous media | Porosity fields, pore-fluid coupling | §5.4 | MEDIUM |
| F-B06 | Nonlocal interactions | Integral constitutive relations | Eringen nonlocal kernel | §7.1 | HIGH |
| F-B07 | Strain-gradient effects | Higher-order gradients | Gradient terms in constitutive | §7.2 | MEDIUM |
| F-B08 | Relaxation and memory effects | MDD/fractional kernels | Convolution kernels | §6.1–6.4 | HIGH |

### Group C — Mathematical Figures (8 figures)

| Fig ID | Title | Purpose | Mathematical basis | Source | Priority |
|--------|-------|---------|-------------------|--------|----------|
| F-C01 | Governing-model relationships | Theory dependency graph | EQ-001 → EQ-007 chain | `07_continuum_balance_derivations.md` | HIGH |
| F-C02 | Wave propagation geometry | Plane wave setup | Wave vectors, polarization, angles | `11_scattering_matrix_derivations.md` | HIGH |
| F-C03 | Reflection and transmission at interfaces | Interface geometry | Incident/reflected/transmitted waves | §9.1–9.4 | HIGH |
| F-C04 | Modal conversion | P↔SV↔T conversion | Polarization vectors | RG-003 Eq. (27) modes | HIGH |
| F-C05 | Complex wave-number behavior | Propagating/evanescent/attenuating | Complex q = qᵣ + iqᵢ | §8.4 | HIGH |
| F-C06 | Dispersion curves by theory | Wave speed vs. frequency | Christoffel equation | §8.2 | HIGH |
| F-C07 | Energy transport pathways | Flux channels by theory | Jᵢ = σv + q (+ others) | §10.2–10.3 | HIGH |
| F-C08 | Dissipation mechanisms by theory | Where energy is lost | Thermal relaxation, viscous, electrical | §10.6 | HIGH |

### Group D — Review Synthesis Figures (6 figures)

| Fig ID | Title | Purpose | Mathematical basis | Source | Priority |
|--------|-------|---------|-------------------|--------|----------|
| F-D01 | Original research taxonomy | Five-axis classification | Taxonomy vectors | `08_scientific_taxonomy_proposal.md` | HIGH |
| F-D02 | Cross-model relationship map | Limiting cases and specializations | Parameter substitutions | `05_mathematical_content_plan.md` §4.11 | HIGH |
| F-D03 | Theory selection framework | When to use which theory | Admissibility conditions | `09_thermodynamic_admissibility.md` | HIGH |
| F-D04 | Applications landscape | Where theories apply | Application × theory matrix | §13 | MEDIUM |
| F-D05 | Open-problem taxonomy | Research gaps organized | Empty cells + contradictions | `08_scientific_taxonomy_proposal.md` §4 | HIGH |
| F-D06 | Future research roadmap | Prioritized directions | Evidence-supported gaps | §16 | HIGH |

### Group E — Energy and Interface Figures (6 figures)

| Fig ID | Title | Purpose | Mathematical basis | Source | Priority |
|--------|-------|---------|-------------------|--------|----------|
| F-E01 | RG-003 asymmetric energy flux | HPS vs TS flux difference | Eqs. (45)-(46) | GAP-011 finding | CRITICAL |
| F-E02 | Interface scattering matrix | ΔX = Q system | RG-003 Eq. (44) | `11_scattering_matrix_derivations.md` | HIGH |
| F-E03 | Energy conservation verification | ΣR + ΣT + A = 1 check | BM-1 analytical | `15_mathematical_benchmark_results.md` | HIGH |
| F-E04 | Energy ratios by incidence angle | R_P, R_SV, T_P, T_SV | BM-1 results | BM-1 derivation | HIGH |
| F-E05 | Dissipation comparison across theories | τ₀, τ_q, kernel effects | Admissibility conditions | `09_thermodynamic_admissibility.md` | HIGH |
| F-E06 | Interface energy balance jump condition | [Jₙ] = 𝒫 − ∂ₜℰ_interface | Pillbox derivation | `12_interface_energy_balance.md` | HIGH |

---

## 3. Figure Priority Ranking

### Priority 1 — Must be created before manuscript drafting (7 figures)

These figures support the core scientific arguments and cannot be replaced by text alone.

| Fig ID | Why critical | Section | Evidence source |
|--------|--------------|---------|-----------------|
| F-E01 | Documents the critical asymmetric flux finding (GAP-011) | §10.3 | RG-003 Eqs. (45)-(46) |
| F-C01 | Shows the logical dependency of balance laws | §3 | EQ-001–EQ-007 |
| F-C03 | Illustrates interface geometry for scattering | §9 | Section 9.1–9.4 |
| F-D01 | Presents the original taxonomy visually | §14 | Taxonomy vectors |
| F-D05 | Maps open problems for future research | §15–16 | Empty cells + contradictions |
| F-E03 | Demonstrates conservation verification approach | §10.5 | BM-1 analytical |
| F-A01 | Provides historical context upfront | §1, §4.1 | Publication timeline |

### Priority 2 — Important for theoretical clarity (8 figures)

| Fig ID | Section | Evidence source |
|--------|---------|-----------------|
| F-B01 | §3.1 | Continuum kinematics |
| F-B02 | §4.2 | Thermoelastic coupling |
| F-B03 | §5.1 | Piezoelectricity |
| F-B06 | §7.1 | Nonlocal interactions |
| F-C02 | §8.2 | Wave propagation geometry |
| F-C05 | §8.4 | Complex wave numbers |
| F-C07 | §10.2 | Energy flux channels |
| F-E02 | §9.4 | Scattering matrix |

### Priority 3 — Supporting illustrations (10 figures)

| Fig ID | Section | Evidence source |
|--------|---------|-----------------|
| F-A02 | §4.1 | Theory lineage |
| F-A03 | §4.1 | Theory emergence |
| F-B04 | §5.6 | Semiconductor |
| F-B05 | §5.4 | Porous media |
| F-B07 | §7.2 | Strain-gradient |
| F-B08 | §6.4 | Memory kernels |
| F-C04 | §9.6 | Modal conversion |
| F-C06 | §8.2 | Dispersion curves |
| F-C08 | §10.6 | Dissipation mechanisms |
| F-D02 | §4.11 | Limiting cases |
| F-D03 | §10.7 | Theory selection |
| F-D04 | §13 | Applications |
| F-D06 | §16 | Future roadmap |
| F-E04 | §10.5 | Energy ratios |
| F-E05 | §10.6 | Dissipation comparison |
| F-E06 | §10.4 | Jump condition |

### Priority 4 — Optional (journal-dependent) (4 figures)

| Fig ID | Section | When to include |
|--------|---------|-----------------|
| F-A04 | §1 | If space permits |
| F-A05 | §2 | If citation network is substantial |
| F-B04 | §5.6 | If semiconductor section included |
| F-B05 | §5.4 | If porous media section included |

---

## 4. Figure Specifications Template

Each figure specification includes:

| Field | Description |
|-------|-------------|
| Figure ID | Unique identifier (F-A01 through F-E06) |
| Title | Descriptive title |
| Scientific purpose | What question the figure answers |
| Mathematical basis | Equations or concepts illustrated |
| Source | Phase 2 artifact or new derivation |
| Priority | 1–4 (as ranked above) |
| Format | TikZ/PGFPlots or SVG |
| Estimated effort | Time to create |
| Dependencies | Other figures or derivations needed first |
| Caption draft | 2–3 sentence caption |

---

## 5. Sample Figure Specification (F-E01 — Critical)

| Field | Specification |
|-------|---------------|
| Figure ID | F-E01 |
| Title | Asymmetric energy flux definition at piezothermoelastic–thermoelastic interface |
| Scientific purpose | Documents GAP-011: HPS side includes thermal flux term; TS side omits it, invalidating claimed total energy conservation |
| Mathematical basis | RG-003 Eq. (45): P = −Re(σ₁₃u̇₁ + σ₃₃u̇₃ − φḊ₃ + K₃T̄₃T/T₀); Eq. (46): Pᵉ = −Re(σ₃₁ᵉu̇₁ᵉ + σ₃₃ᵉu̇₃ᵉ) |
| Source | RG-003 full text; GAP-011 in `14_validated_research_gaps.csv` |
| Priority | 1 (CRITICAL) |
| Format | TikZ |
| Estimated effort | 4–6 hours |
| Dependencies | None |
| Caption draft | "Energy flux definitions at the piezothermoelastic–thermoelastic interface from RG-003. The HPS side (Eq. 45) includes mechanical, electrical, and thermal flux channels. The TS side (Eq. 46) includes only mechanical flux channels, omitting thermal conduction. This asymmetry means the claimed energy conservation (Eq. 58) does not represent total energy conservation." |

---

## 6. Figure Creation Workflow

```
1. Draft specification (this document)
2. Verify mathematical content against source
3. Create TikZ/PGFPlots source code
4. Compile and verify output
5. Check caption for self-containedness
6. Verify citations are accurate
7. Save source file in figures/tikz/ or figures/svg/
8. Record in figure register
```

---

## 7. Figure Register (to be maintained)

| Fig ID | Status | Source file | Compiled output | Verified |
|--------|--------|-------------|-----------------|----------|
| F-A01 | NOT STARTED | — | — | ☐ |
| F-E01 | NOT STARTED | — | — | ☐ |
| ... | ... | ... | ... | ... |

---

## 8. Quality Standards (Directive §10)

| Standard | Requirement |
|----------|-------------|
| Clear scientific purpose | Every figure answers a specific question |
| Validated scientific content | No decorative or misleading elements |
| Relevant citations | Source equations/papers cited |
| Accurate symbols | Consistent with manuscript notation |
| Consistent notation | Same symbols as main text |
| Publication-quality caption | Self-contained, 2–3 sentences |
| Source file | TikZ or SVG; editable |
| Never copy reference review | Original illustrations only |

---

## 9. Directory Structure

```
figures/
├── tikz/
│   ├── F-A01_evolution_timeline.tikz
│   ├── F-E01_asymmetric_flux.tikz
│   └── ...
├── svg/
│   ├── F-A01_evolution_timeline.svg
│   └── ...
├── compiled/          # PDF/PNG outputs (for review)
│   └── ...
└── figure_register.csv  # Status tracking
```

---

## 10. Estimated Effort

| Priority group | Figure count | Est. hours per figure | Total hours |
|---------------|--------------|----------------------|-------------|
| Priority 1 | 7 | 6 | 42 |
| Priority 2 | 8 | 5 | 40 |
| Priority 3 | 10 | 4 | 40 |
| Priority 4 | 4 | 4 | 16 |
| **Total** | **29** | — | **138 hours** |

---

## 11. Integration with Manuscript

| Section | Figures referenced |
|---------|-------------------|
| §1 (Scope) | F-A01 |
| §3 (Foundations) | F-B01, F-C01 |
| §4 (Thermoelastic) | F-A02, F-A03, F-B02 |
| §5 (Multiphysics) | F-B03, F-B04, F-B05 |
| §6 (Transport) | F-B06, F-B07, F-B08 |
| §7 (Nonlocal) | F-B06 |
| §8 (Methods) | F-C02, F-C05, F-C06 |
| §9 (Interfaces) | F-C03, F-C04, F-E02 |
| §10 (Energy) | F-C07, F-C08, F-E01, F-E03, F-E04, F-E05, F-E06 |
| §12 (Synthesis) | F-D01, F-D02, F-D03 |
| §14 (Taxonomy) | F-D01, F-D05 |
| §15 (Challenges) | F-D05 |
| §16 (Future) | F-D06 |

---

**Next:** Proceed to Deliverable 10 (Table-by-Table Blueprint).
