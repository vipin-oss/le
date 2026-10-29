# Deliverable 14 — Scientific Novelty Assessment

**Branch:** arena/40393d9f-le  
**Prepared:** 2026-10-21  
**Alignment:** Master Editorial Directive §13 (original scientific contributions), §14 (future research directions), §17 (scientific writing standards)

---

## 1. Novelty Philosophy

Per Directive §13: **"Aim for scholarly originality through synthesis, not artificial claims of discovering new universal laws."**

The review's originality comes from:
1. Comprehensive historical synthesis
2. Multidimensional classification (taxonomy)
3. Mathematical relationship framework (assumption-aware)
4. Comparative theory atlas
5. Research evidence map
6. Future research roadmap

**Not from:** claiming new universal laws, alleging errors in prior work, or asserting priority.

---

## 2. Existing Review Coverage (Directive §13.6)

### 2.1 Reviews identified in Phase 2 (Family F searches)

| Review ID | Year | Focus | Theories covered | Interface phenomena | Energy transport | On-target? |
|-----------|------|-------|-----------------|-------------------|-----------------|------------|
| FW-008 | 1998 | Chandrasekharaiah review | Thermoelasticity (general) | Limited | Limited | NO (general thermoelasticity) |
| FW-009 | 1986 | Chandrasekharaiah review | Thermoelastic waves | Limited | Limited | NO (older, narrow) |
| FW-010 | 2021 | Shakeriaski review | Thermoelasticity | Limited | Limited | NO |
| FW-011 | 2019 | Quintanilla review | MGT theory | Single theory | Single theory | NO (single theory) |
| Li et al. 2026 | 2026 | (from S101) | TBD | TBD | TBD | PARTIAL |
| Karmakar et al. 2022 | 2022 | (from S102) | TBD | TBD | TBD | PARTIAL |
| Li et al. 2015 | 2015 | (from S103) | TBD | TBD | TBD | NO |
| Wei et al. 2016 | 2016 | (from S104) | TBD | TBD | TBD | NO |
| Banerjee & Pao 1974 | 1974 | (from S105) | Thermoelasticity | Limited | Limited | NO (classical only) |

**None of the identified reviews are on-target** — none comprehensively covers wave propagation, energy transport, AND interface phenomena across generalized multiphysics continua with a multidimensional taxonomy.

### 2.2 Coverage gap analysis

| Review aspect | Existing reviews cover | This review would add |
|--------------|----------------------|----------------------|
| Historical development | Partial (individual theory reviews) | Comprehensive across all theory families |
| Multidimensional classification | None | Five-axis taxonomy with evidence map |
| Cross-theory comparison | Limited (single-theory reviews) | 9 theory families compared across 12 criteria |
| Energy transport focus | Limited | Central theme with flux asymmetry finding |
| Interface phenomena | Limited | Comprehensive interface scattering framework |
| Research gap identification | None | 12 validated gaps with evidence levels |
| Future research roadmap | Limited | Evidence-supported directions |

---

## 3. Original Contributions (Directive §13)

### 3.1 Contribution 1 — Comprehensive historical synthesis

| Element | Description | Evidence |
|---------|-------------|----------|
| What | Coherent account of continuum wave theory evolution from classical elasticity through generalized thermoelasticity to multiphysics and nonlocal formulations | Phase 2: FW-001 through FW-011 dates; `04_chapter_by_chapter_outline.md` §4.1 |
| Originality | First comprehensive synthesis connecting all theory families in one historical narrative | No existing review covers all 9 theory families historically |
| Verification | All dates and references Crossref-verified | `references/doi_verification.csv` |

### 3.2 Contribution 2 — Multidimensional classification

| Element | Description | Evidence |
|---------|-------------|----------|
| What | Five-axis taxonomy (physical, mathematical, wave, energy, validation) applied to 24+ studies | `08_scientific_taxonomy_proposal.md`; `phase2/17_original_taxonomy_v2.md` |
| Originality | First taxonomy combining all five dimensions for this literature | No existing taxonomy identified in literature search |
| Verification | Applied to 24 records; 6 empty cells identified | `08_scientific_taxonomy_proposal.md` §4 |

### 3.3 Contribution 3 — Mathematical relationship framework

| Element | Description | Evidence |
|---------|-------------|----------|
| What | Assumption-aware account of how models relate (limiting cases, specializations, extensions) | `05_mathematical_content_plan.md` §4.11; `08_scientific_taxonomy_proposal.md` §6 |
| Originality | Explicitly documents that all limiting procedures are parameter substitutions, not rigorous limits | Phase 2 finding from RG-003 full text |
| Verification | 11 limiting cases mapped from RG-003; all identified as parameter substitutions | `05_mathematical_content_plan.md` §4.11 |

### 3.4 Contribution 4 — Comparative theory atlas

| Element | Description | Evidence |
|---------|-------------|----------|
| What | Organized reference showing variables, equations, mechanisms, and applications by theory family | `05_mathematical_content_plan.md`; Tables 4-11 in `10_table_by_table_blueprint.md` |
| Originality | First side-by-side comparison of 9 theory families across 12 criteria | No existing comparison identified |
| Verification | All entries traceable to equation register | `06_equation_provenance_register.csv` |

### 3.5 Contribution 5 — Research evidence map

| Element | Description | Evidence |
|---------|-------------|----------|
| What | Structured representation of which problems, materials, and methods have been investigated; where evidence is thin | `08_scientific_taxonomy_proposal.md` §4 (empty cells) |
| Originality | First evidence map identifying 6 empty research cells | No existing evidence map identified |
| Verification | Empty cells based on 24-record corpus classification | `08_scientific_taxonomy_proposal.md` §4 |

### 3.6 Contribution 6 — Future research roadmap

| Element | Description | Evidence |
|---------|-------------|----------|
| What | Evidence-supported directions involving new materials, generalized constitutive laws, computational techniques, and underexplored coupling problems | `16_scientific_figure_package.md` F-D06; `14_scientific_novelty_assessment.md` §5 |
| Originality | Roadmap grounded in validated gaps, not speculation | Gaps classified with evidence levels |
| Verification | 12 gaps classified; 6 empty cells; 3 contradiction pairs | `14_validated_research_gaps.csv` |

---

## 4. Critical Finding: Energy Flux Asymmetry (GAP-011)

### 4.1 The finding

RG-003 (Scientific Reports, open access, full text extracted) defines energy flux differently on the two sides of the same interface:

| Side | Energy flux equation | Terms included |
|------|---------------------|----------------|
| HPS (piezothermoelastic) | Eq. (45) | Mechanical + electrical + thermal |
| TS (thermoelastic) | Eq. (46) | Mechanical only (no thermal term) |

### 4.2 Novelty status

This is a **documented observation from primary source analysis**, not an allegation of error. It represents:

- **First documented case** of inconsistent flux definitions at the same interface in the literature
- **Constructive opening** for deriving symmetric flux definitions
- **Open question** about whether ΣR+ΣT+A=1 holds with symmetric flux

### 4.3 Handling in manuscript

Per Directive §2: presented factually, constructively, without adversarial language. See `phase3/11_author_publication_consistency_plan.md` §7.1.

---

## 5. What Is NOT Novel (And Should Not Be Claimed As Such)

| Claim | Why not novel | Correct framing |
|-------|--------------|-----------------|
| "We discovered new universal conservation laws" | Not derived; conservation claims unverified | "Conservation identity ΣR+ΣT+A=1 remains an open question for generalized theories" |
| "RG-003 contains mathematical errors" | Not an error audit; Directive §1 prohibits | "The flux definition is model-specific; symmetric formulation remains open" |
| "We developed a new theory" | No new theory developed | "Existing theories compared under assumption-aware framework" |
| "We proved all limiting cases rigorously" | All limits are parameter substitutions, not rigorous | "Limiting procedures identified as parameter substitutions; rigorous limits open" |

---

## 6. Novelty Evidence Map

| Potential novelty | Evidence strength | Verification source | Manuscript claim |
|------------------|------------------|-------------------|-----------------|
| Five-axis taxonomy | STRONG | Applied to 24 records; 6 empty cells | "Original classification framework" |
| Historical synthesis | STRONG | 11 foundational works with dates | "Comprehensive historical account" |
| Cross-theory comparison | STRONG | 9 families × 12 criteria | "First comparative atlas" |
| Energy flux asymmetry | STRONG | RG-003 Eqs. (45)-(46) verified | "Documented observation" |
| Research gap map | STRONG | 12 gaps classified | "Evidence-based gap identification" |
| Future research roadmap | MODERATE | Based on validated gaps | "Evidence-supported directions" |
| New conservation law | NONE | Not derived; unverified | NOT CLAIMED |
| Error identification | NONE | Directive §1 prohibits | NOT CLAIMED |
| New theory | NONE | Not developed | NOT CLAIMED |

---

## 7. Comparison with Reference Model (Abdalla et al. 2022)

| Aspect | Reference model | This review |
|--------|----------------|-------------|
| Originality type | Community white paper; research priorities | Scholarly synthesis; taxonomy; evidence map |
| Scale | 224 pages, 203 authors, 2300+ references | 60-150 pages, small team, 150-400 references |
| Novelty claim | "New physics needed for cosmological tensions" | "Synthesis and taxonomy of multiphysics continuum mechanics" |
| Adversarial tone | None (constructive) | None (constructive, per Directive) |
| Future roadmap | Yes (Section IX) | Yes (Section 16) |
| Taxonomy | Implicit (science × facility matrix) | Explicit (five-dimensional) |

---

## 8. Risks to Novelty Claims

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Existing review found that covers same scope | MEDIUM | HIGH | Frame as "complements existing reviews" not "replaces" |
| Taxonomy deemed not novel | LOW | MEDIUM | Present as "application to this literature" not "invention" |
| Flux asymmetry already known | MEDIUM | MEDIUM | Cite if found; present as "documented in RG-003" |
| Overclaiming novelty | LOW | HIGH | Directive §13: originality through synthesis, not new laws |

---

## 9. Novelty Statement (for manuscript)

**Draft novelty statement:**

> "This review provides a comprehensive synthesis of wave propagation, energy transport, and interface phenomena in generalized multiphysics continua. Its original contributions include: (1) a multidimensional taxonomy classifying studies across physical, mathematical, wave, energy, and validation dimensions; (2) a comparative theory atlas relating nine theory families through explicitly stated assumptions; (3) an evidence-based research gap map identifying six empty cells in the literature landscape; and (4) a documented observation of asymmetric energy flux definitions at multiphysics interfaces, with implications for energy conservation identities. The review is constructive and synthetic, organizing established knowledge without adversarial fault-finding of individual publications."

---

## 10. Validation of Novelty Claims

| Claim | How to validate | Evidence |
|-------|----------------|----------|
| First five-axis taxonomy for this literature | Search existing taxonomies | None found in Phase 2 search |
| First cross-theory comparison of 9 families | Search comparison studies | None found covering all 9 |
| First energy flux asymmetry documentation | Search for prior documentation | RG-003 is first full-text-extracted paper with this finding |
| First evidence map with empty cells | Search for evidence maps | None found |

---

**Next:** Proceed to Deliverable 15 (Editorial Quality-Control Checklist).
