# Deliverable 7 — High-Quality Source-Selection and Equation-Selection Criteria

**Branch:** arena/40393d9f-le  
**Prepared:** 2026-10-21  
**Alignment:** Master Editorial Directive §3 (source-selection policy), §8 (mathematical exposition), §9 (equation safety)

---

## 1. Source-Selection Criteria (Directive §3)

### 1.1 Priority ranking for including a primary study

| Priority | Criterion | Weight | Assessment method |
|----------|-----------|--------|-------------------|
| 1 | Direct scientific relevance to multiphysics continuum wave propagation | Critical | Must address wave propagation, interface phenomena, energy transport, or coupled-field mechanics in generalized continua |
| 2 | Mathematical clarity (clearly stated equations and assumptions) | Critical | Equations must be readable, well-defined, and internally consistent |
| 3 | Reliable source provenance (peer-reviewed journal, verifiable DOI) | Critical | Crossref/DOI verification required |
| 4 | Historical importance (foundational or seminal contribution) | High | Citation count, influence on subsequent work, theory introduction |
| 5 | Contribution to theory or applications | High | New model, new solution method, new application demonstration |
| 6 | Adequate evidence for claims | High | Claims supported by derivation, numerical result, or experimental data |
| 7 | Reproducibility where relevant | Medium | Full equations provided; analytical results reproducible |
| 8 | Reputable publication venue | Medium | Journal reputation considered but not determinative |

### 1.2 Venue priorities (Directive §3)

**Priority venues** (leading journals in the domain):
- Journal of the Mechanics and Physics of Solids
- International Journal of Solids and Structures
- Wave Motion
- Journal of Thermal Stresses
- International Journal of Engineering Science
- Continuum Mechanics and Thermodynamics
- Journal of Applied Mechanics
- Meccanica
- Mathematics and Mechanics of Solids
- International Journal of Solids and Structures
- Zeitschrift für Angewandte Mathematik und Mechanik (ZAMM)
- Journal of Engineering Mathematics

**Secondary venues** (sound work in less prominent venues):
- Regional mechanics journals
- Conference proceedings with peer review
- University technical reports (if mathematically sound)

**Excluded venues**:
- Predatory journals (Beale's list or equivalent)
- Non-peer-reviewed preprints (unless no other source exists and clearly labeled)
- Unverifiable sources

### 1.3 Inclusion decision tree

```
Is the paper peer-reviewed?
├── NO → Exclude (unless preprint with no alternative; label clearly)
├── YES → Is it directly relevant to multiphysics continuum waves?
    ├── NO → Exclude
    ├── YES → Are equations clearly stated with assumptions?
        ├── NO → Include in evidence map only; not for equation exposition
        ├── YES → Is DOI/Crossref verifiable?
            ├── NO → Include with caution; attempt verification
            ├── YES → Include for detailed exposition
```

### 1.4 Evidence map vs. exposition selection

| Category | Definition | Example treatment |
|----------|------------|-------------------|
| Evidence map | All screened, eligible studies — part of the literature landscape | Listed in database; cited for context; not necessarily equation source |
| Exposition selection | Studies selected for detailed mathematical exposition | Equations cited; derivations discussed; results compared |
| Mathematical foundation | Studies providing canonical equations | Primary source for equation verification register |

A paper with an unclear equation may remain in the **evidence map** without being selected as a **canonical equation source**.

---

## 2. Equation-Selection Criteria (Directive §8–§9)

### 2.1 Inclusion criteria (all must be satisfied)

An equation is included in the manuscript only when:

| # | Criterion | Verification method |
|---|-----------|---------------------|
| 1 | Established standard result with reliable authoritative source | Textbook or seminal paper citation |
| 2 | OR derived from clearly stated model and independently verified | Derivation traceable; dimensional consistency checked |
| 3 | OR presented as model-specific formulation with accurately documented assumptions | Assumptions stated; validity domain defined |
| 4 | Equation is strategically valuable (not redundant) | Smaller collection of precise equations preferred |
| 5 | Competing formulations are summarized fairly (if applicable) | Assumptions and use cases documented for each |

### 2.2 Exclusion criteria (any triggers exclusion)

| # | Criterion | Handling |
|---|-----------|----------|
| 1 | Uncertain verification status | Do not present as canonical; flag for review |
| 2 | Model-specific without documented assumptions | Do not include without assumption caveat |
| 3 | Contradicts better-established result without resolution | Do not include; document as open question |
| 4 | Purely redundant (equivalent to another included equation) | Select one representative form |
| 5 | Cannot be dimensionally verified | Do not include |

### 2.3 Status categories (Directive §9)

| Status | Definition | Manuscript treatment |
|--------|------------|---------------------|
| **VERIFIED — SUITABLE FOR EXPOSITION** | Independently verified; dimensionally consistent; reliable source | Include as canonical equation |
| **VALID UNDER SPECIFIED ASSUMPTIONS** | Valid but only under stated assumptions | Include with explicit assumption statement |
| **MODEL-SPECIFIC — EXPLAIN CAREFULLY** | Valid for one model family; not generalizable | Include with model-specific framing and caveat |
| **UNCERTAIN — DO NOT USE AS CANONICAL** | Cannot be independently verified; source unclear | Do not present as universal identity; discuss as open question |
| **REQUIRES AUTHOR OR SPECIALIST REVIEW** | Needs expert validation before inclusion | Flag; do not include until reviewed |

### 2.4 Current equation register (Phase 2)

| Eq. ID | Equation | Source | Status | Section | Decision |
|--------|----------|--------|--------|---------|----------|
| EQ-001 | ρv̇ᵢ = σⱼᵢ,ⱼ + ρfᵢ | Derived (Thm 2.1) | VERIFIED | §3.2 | Include |
| EQ-002 | σᵢⱼ = σⱼᵢ | Derived (Thm 3.1) | VERIFIED | §3.2 | Include |
| EQ-003 | Mechanical power balance | Derived (Thm 4.1) | VERIFIED | §3.3 | Include |
| EQ-004 | Internal energy balance | Derived (Thm 5.1) | VERIFIED | §3.3 | Include |
| EQ-005 | Dissipation inequality | Derived (Thm 6.1) | VERIFIED | §3.4 | Include |
| EQ-006 | Coleman-Noll restrictions | Derived (Thm 7.1) | VERIFIED | §3.5 | Include |
| EQ-007 | Classical energy flux Jᵢ = σⱼᵢvᵢ + qᵢ | Derived (Sec 8) | VERIFIED | §3.8, §10.2 | Include |
| EQ-008 | MDD operator | RG-003 Eq. (1) | VERIFIED | §4.9 | Include |
| EQ-009 | MDD kernel | RG-003 Eq. (2) | VERIFIED | §4.9 | Include |
| EQ-010 | Piezothermoelastic constitutive | RG-003 Eq. (3) | VERIFIED | §5.2 | Include |
| EQ-011 | Momentum equation | RG-003 Eq. (4) | VERIFIED | §5.2 | Include |
| EQ-012 | Electric field from potential | RG-003 Eq. (5) | VERIFIED | §5.1 | Include |
| EQ-013 | Electric displacement | RG-003 Eq. (6) | VERIFIED | §5.1 | Include |
| EQ-014 | Charge conservation | RG-003 Eq. (7) | VERIFIED | §5.1 | Include |
| EQ-015 | Heat equation with TPL+MDD | RG-003 Eq. (8) | VERIFIED | §4.9 | Include |
| EQ-016 | HPS energy flux | RG-003 Eq. (45) | VERIFIED | §10.3 | Include (model-specific) |
| EQ-017 | TS energy flux | RG-003 Eq. (46) | VERIFIED | §10.3 | Include (model-specific; asymmetry noted) |
| EQ-018 | Incident P-wave energy flux | RG-003 Eq. (47) | VERIFIED | §9.8 | Include |
| EQ-019 | Conservation claim Σ = 1 | RG-003 Eq. (58) | CLAIMED (uncertain) | §10.5 | Include with caveat |
| EQ-020 | Secular equation (8th order) | RG-003 Eq. (27) | VERIFIED | §9.5 | Include |
| EQ-021 | Interface conditions | RG-003 Eq. (38) | VERIFIED | §9.3 | Include |
| EQ-022 | Heat flux continuity (MDD+TPL) | RG-003 Eq. (38) | VERIFIED | §9.3 | Include |
| EQ-023 | D₃ = 0 electrical BC | RG-003 Eq. (38) | VERIFIED | §5.3 | Include |

### 2.5 Equations requiring new derivation (NOT yet in register)

| Equation | Target section | Status | Required before inclusion |
|----------|---------------|--------|--------------------------|
| LS energy flux | §10.3 | UNCERTAIN | Derive from relaxation equation; verify dimensional consistency |
| GL/GN energy flux | §10.3 | UNCERTAIN | Derive from thermal displacement formulation |
| DPL energy flux | §10.3 | UNCERTAIN | Derive from two-lag heat equation |
| TPL energy flux | §10.3 | UNCERTAIN | Derive from three-lag heat equation |
| MGT energy flux | §10.3 | UNCERTAIN | Derive from third-order heat equation |
| MDD hereditary energy flux | §10.3 | UNCERTAIN | Derive convolution-form flux |
| Nonlocal integral-form energy flux | §10.3 | UNCERTAIN | Derive integral-form flux (divergence theorem modification) |
| Electrical energy flux | §5.3 | UNCERTAIN | Derive Jᵢᵉˡᵉᶜ = −φḊᵢ or equivalent |

---

## 3. Dimensional Consistency Check

Every equation included in the manuscript must pass:

| Check | Method | Pass criterion |
|-------|--------|----------------|
| SI unit consistency | All terms in an equation have same dimensions | ✓ or ✗ |
| Symbol definition | Every symbol defined at first use | ✓ or ✗ |
| Domain validity | Range of applicability stated | ✓ or ✗ |
| Limiting behavior | Reduces to known result in appropriate limit | ✓ or ✗ |

---

## 4. Handling Uncertainty (Directive §9)

### 4.1 Uncertain ≠ Error

An uncertain equation should NOT be:
- Presented as a universally valid mathematical identity
- Used to support a strong claim without qualification
- Cited as evidence of another paper's error

An uncertain equation MAY be:
- Discussed as an open research question
- Presented with explicit assumption caveats
- Listed in the equation verification register with status UNCERTAIN

### 4.2 Language for uncertain equations

| Avoid | Use instead |
|-------|-------------|
| "This equation is wrong" | "This equation's validity domain is unclear" |
| "The authors made an error" | "The assumptions underlying this formulation require clarification" |
| "This is invalid" | "This formulation applies under specified conditions; extension to other cases requires verification" |
| "Previous work failed" | "This relationship warrants further investigation" |

---

## 5. Source Selection Workflow

### Step 1: Discovery
- Search databases using theory-specific terms
- Record source of discovery (search method, query, date)

### Step 2: Screening
- Apply inclusion decision tree
- Record include/exclude/undecided decision with reason
- Update deduplicated literature database

### Step 3: Verification
- Verify DOI via Crossref
- Record citation counts (OpenAlex, Crossref)
- Record full-text access status

### Step 4: Classification
- Classify by theory family, physical domain, mathematical class
- Apply taxonomy (Deliverable 8)

### Step 5: Equation selection
- For each included paper, identify candidate equations
- Apply equation selection criteria
- Record in equation verification register

### Step 6: Deep analysis (full-text papers only)
- Extract all equations, boundary conditions, material parameters
- Verify dimensional consistency
- Note limiting cases and assumptions

---

## 6. Quality Control Checklist

Before any source or equation is included in the manuscript:

| Check | Status |
|-------|--------|
| DOI verified via Crossref | ☐ |
| Peer-reviewed venue confirmed | ☐ |
| Relevance to domain documented | ☐ |
| Equations clearly stated | ☐ |
| Assumptions explicitly defined | ☐ |
| Dimensional consistency checked | ☐ |
| Independent verification performed | ☐ |
| Status category assigned | ☐ |
| Manuscript inclusion decision recorded | ☐ |
| No adversarial language about authors | ☐ |

---

## 7. Records to Maintain

| File | Content | Update frequency |
|------|---------|-----------------|
| `references/library.bib` | Master BibTeX library | After each search batch |
| `references/doi_verification.csv` | DOI verification for all papers | After each search batch |
| `references/source_provenance.csv` | Source of discovery for each paper | After each search batch |
| `phase2/03_deduplicated_literature_database.csv` | Screening decisions | After screening |
| `phase2/04_fulltext_access_register.csv` | Access status | After access attempts |
| `phase2/06_equation_provenance_register.csv` | Equation verification register | After each equation review |

---

**Next:** Proceed to Deliverable 8 (Original Scientific Taxonomy Proposal).
