# Deliverable 6 — Literature Acquisition and Citation Strategy

**Branch:** arena/40393d9f-le  
**Prepared:** 2026-10-21  
**Alignment:** Master Editorial Directive §3 (source-selection policy), §7 (deep literature development), §17 (scientific writing standards)

---

## 1. Literature Acquisition Strategy (Directive §7)

### 1.1 Search methods (in priority order)

| Method | Description | Status | Target output |
|--------|-------------|--------|---------------|
| Database searches | OpenAlex, Crossref, arXiv, Semantic Scholar queries | Phase 2: OpenAlex/Crossref done; arXiv/Semantic Scholar pending | 200–500 candidate papers |
| Citation chaining | Forward from foundational reviews (Chandrasekharaiah 1986/1998); backward from key papers | Phase 2: forward done; backward blocked (OpenAlex `referenced_works` empty) | 50–100 additional papers |
| Landmark paper tracing | Biot 1956, LS 1967, GL 1972, GN 1991, Tzou 1995, Eringen 1972, MDD papers | Phase 2: 11 foundational works identified | 11 landmark papers (done) |
| Mathematical terminology expansion | Search terms: "Lord-Shulman", "Green-Naghdi", "dual-phase-lag", "memory-dependent derivative", "nonlocal thermoelasticity", "piezothermoelastic interface" | Phase 2: partial | 100–200 papers |
| Model-specific searches | Each theory family: LS thermoelasticity interface, GN thermoelasticity wave propagation, etc. | Not started | 200–400 papers |
| Journal-focused searches | J. Thermal Stresses, Int. J. Solids Struct., Wave Motion, Meccanica, Continuum Mech. Thermodyn., Int. J. Eng. Sci., J. Appl. Mech. | Not started | 100–200 papers |
| Recent research searches | 2020–2026 publications in generalized thermoelasticity | Not started | 50–100 papers |
| Existing-review comparisons | Find and analyze existing reviews in the domain | Phase 2: 10 reviews identified in OpenAlex/Crossref, 0 on-target | 5–10 reviews |

### 1.2 Target record counts

| Category | Target | Phase 2 status |
|----------|--------|----------------|
| Discovered studies | 500–800 | 24 (seed corpus) |
| Screened studies | 300–500 | 24 |
| Eligible studies | 150–250 | 24 |
| Full texts obtained | 5–10 | 1 (RG-003) |
| Deeply analyzed studies | 20–30 | 1 (RG-003) |
| Studies cited in manuscript | 150–300 | ~50 (from corpus) |
| Studies used as mathematical foundations | 30–50 | 11 (foundational works) |

### 1.3 Search terms by theory family

| Theory family | Search terms |
|--------------|-------------|
| Classical elasticity | "elastic waves interface reflection transmission" |
| Lord–Shulman | "Lord-Shulman thermoelasticity wave propagation" |
| Green–Naghdi | "Green-Naghdi thermoelasticity" |
| Dual-phase-lag | "dual-phase-lag thermoelasticity wave" |
| Three-phase-lag | "three-phase-lag thermoelasticity" |
| Memory-dependent derivative | "memory-dependent derivative thermoelasticity" |
| Nonlocal elasticity | "nonlocal thermoelasticity wave propagation" |
| Piezoelectric | "piezoelastic wave propagation interface" |
| Piezothermoelastic | "piezothermoelastic interface reflection transmission" |
| Porous/double porosity | "double porosity thermoelasticity wave" |
| Micropolar | "micropolar thermoelasticity wave" |
| Semiconductor | "semiconductor photo-thermo-elastic wave" |
| Energy flux | "energy flux thermoelastic interface" |
| Energy ratio | "energy ratio reflection transmission interface" |

### 1.4 Access strategy

| Access level | Count | Strategy |
|-------------|-------|----------|
| Open access | Target 10–15 | arXiv, open access journals, author manuscripts |
| Institutional access | Target 20–30 | Through available institutional credentials |
| Abstract only | Accept for citation | Cite abstract/metadata; do not claim full-text verification |
| Paywalled, no access | Accept for citation | Cite from Crossref/OpenAlex metadata only |

---

## 2. Citation Strategy

### 2.1 Citation style

- **Inline numeric citations** ([1], [2], [3], ...) — follows reference model (Abdalla et al. 2022)
- **Bibliography sorted by citation order** (not alphabetical)
- Each citation includes: authors, title, journal, year, volume, pages, DOI

### 2.2 Citation distribution targets

| Source type | Target count | Rationale |
|-------------|--------------|-----------|
| Foundational works (pre-2000) | 30–50 | Biot, LS, GL, GN, Tzou, Eringen, etc. |
| Researcher corpus (RG-001 through RG-007) | 7 | All Crossref-verified |
| External discoveries (EXT-001 through EXT-006) | 6 | All Crossref-verified |
| Additional peer-reviewed papers | 100–200 | From expanded search |
| Existing reviews | 5–10 | For saturation analysis and comparison |
| **Total** | **150–300** | Appropriate for 40–80 page review |

### 2.3 Citation quality rules (Directive §3)

1. **Prioritize primary studies** over secondary sources
2. **Prioritize peer-reviewed** journal articles
3. **Do not assume correctness from prestige** — verify equations independently
4. **Do not exclude sound work from less prominent venues**
5. **Never invent bibliographic records** — every citation must be verifiable
6. **Separate systematic screening from equation selection** — a paper can be in the evidence map without being an equation source

### 2.4 Self-citation policy

The researcher's own publications (RG-001 through RG-007) must be:
- **Cited fairly** alongside other work in the same sub-domain
- **Not overrepresented** — no more than ~15–20% of citations in any section
- **Presented with appropriate context** — assumptions, limitations, model-specific validity
- **Not framed as superior** to competing theories

### 2.5 Handling abstract-only papers

| Situation | Handling |
|-----------|----------|
| Paper cited for a well-known result (e.g., Biot 1956) | Cite normally; result is independently verifiable |
| Paper cited for a specific equation | Cite with qualifier "as reported in [X]" or "under the assumptions stated in [X]" |
| Paper cited for energy flux definition | Only if full text available or equation independently verified |
| Paper central to argument but only abstract available | Flag as limitation; seek full text before final manuscript |

---

## 3. Equation Selection and Citation (Directive §8–§9)

### 3.1 Equation inclusion criteria

An equation is included in the manuscript only when:

| Criterion | Description |
|-----------|-------------|
| Established standard | Classical result with reliable authoritative source |
| Derived and verified | Derived from clearly stated model; independently verified |
| Model-specific | Presented with accurately documented assumptions and validity domain |

### 3.2 Equation exclusion criteria

An equation is excluded when:

| Criterion | Description |
|-----------|-------------|
| Uncertain status | Cannot be independently verified; source unclear |
| Model-specific without documentation | Assumptions not stated; validity domain unknown |
| Contradicts better-established result | Without sufficient evidence to resolve |
| Redundant | Multiple equivalent forms; select one representative |

### 3.3 Equation verification register

All equations considered for the manuscript are recorded with:

| Field | Description |
|-------|-------------|
| Equation ID | Unique identifier |
| Equation | The mathematical expression |
| Source | Paper, book, or "derived" |
| Model family | Which theory it belongs to |
| Assumptions | Stated assumptions |
| Physical variables | Each symbol defined |
| Validity domain | Where it applies |
| Dimensional consistency | Checked |
| Independent verification status | VERIFIED / UNCERTAIN / REQUIRES REVIEW |
| Relationship to prior work | How it compares |
| Manuscript inclusion decision | INCLUDE / EXCLUDE / INCLUDE WITH CAVEAT |

### 3.4 Status categories (Directive §9)

| Status | Meaning | Manuscript treatment |
|--------|---------|---------------------|
| VERIFIED — SUITABLE FOR EXPOSITION | Independently verified, dimensionally consistent, source reliable | Include as canonical |
| VALID UNDER SPECIFIED ASSUMPTIONS | Valid but only under stated assumptions | Include with assumption caveat |
| MODEL-SPECIFIC — EXPLAIN CAREFULLY | Valid for one model family; not general | Include with model-specific framing |
| UNCERTAIN — DO NOT USE AS CANONICAL | Cannot be verified; source unclear | Do not present as universal identity |
| REQUIRES AUTHOR OR SPECIALIST REVIEW | Needs expert validation | Flag for review before inclusion |

### 3.5 Current register status (from Phase 2)

| Equation IDs | Status | Section | Decision |
|-------------|--------|---------|----------|
| EQ-001 through EQ-007 | VERIFIED | §3 | Include as canonical |
| EQ-008 through EQ-023 | VERIFIED (RG-003 source) | §4.9, §5.2, §9 | Include with source attribution |
| LS energy flux | UNCERTAIN | §10.3 | Exclude as canonical; discuss as open question |
| DPL/TPL/MGT energy flux | UNCERTAIN | §10.3 | Exclude as canonical; discuss as open question |
| MDD energy flux | UNCERTAIN | §10.3 | Exclude as canonical; discuss as open question |
| Nonlocal energy flux | UNCERTAIN | §10.3 | Exclude as canonical; discuss as open question |

---

## 4. Literature Database Management

### 4.1 File structure

```
references/
├── library.bib              # Master BibTeX library (all discovered papers)
├── doi_verification.csv     # DOI verification status (all papers)
├── source_provenance.csv    # Source of each paper (search method, query)
├── screening_decisions.csv  # Include/exclude/undecided for each paper
├── fulltext_access.csv      # Open access / abstract-only / paywalled
├── deep_analysis.csv        # Papers with full-text extraction
└── equation_register.csv    # Equation verification register
```

### 4.2 Deduplication rules

| Rule | Description |
|------|-------------|
| DOI match | Same DOI = same paper (keep one record) |
| Title + author match | Same title and first author = likely duplicate (manual review) |
| arXiv + journal version | Keep journal version; note arXiv preprint |
| Conference + journal version | Keep journal version; note conference predecessor |

### 4.3 Current database state (Phase 2)

| File | Records | Status |
|------|---------|--------|
| `03_deduplicated_literature_database.csv` | 24 | Complete (seed corpus) |
| `04_fulltext_access_register.csv` | 24 | Complete |
| `06_equation_provenance_register.csv` | 23 equations | Complete |
| `references/doi_verification.csv` | 24 DOIs | Complete (all Crossref-verified) |

---

## 5. Citation Coverage by Section

| Section | Target citations | Primary sources |
|---------|-----------------|-----------------|
| 1. Scope and purpose | 5–10 | Directive, reference model |
| 2. Literature strategy | 5–10 | Search methodology references |
| 3. Foundations | 15–25 | Continuum mechanics textbooks, foundational papers |
| 4. Thermoelastic theories | 30–50 | Biot 1956, LS 1967, GL 1972, GN 1991, Tzou 1995, etc. |
| 5. Multiphysics continua | 25–40 | Piezoelectric, porous, semiconductor papers |
| 6. Transport and memory | 20–30 | MDD, fractional, hereditary papers |
| 7. Nonlocal models | 15–25 | Eringen 1972, strain-gradient papers |
| 8. Mathematical methods | 10–20 | Wave propagation texts, transform methods |
| 9. Interface phenomena | 20–30 | Interface condition papers, scattering theory |
| 10. Energy and dissipation | 20–30 | Energy flux papers, thermodynamics texts |
| 11. Advanced developments | 10–20 | Emerging theory papers |
| 12. Comparative synthesis | 30–50 | All theory families |
| 13. Applications | 15–25 | Application-specific papers |
| 14. Taxonomy | 10–15 | Classification literature |
| 15. Challenges | 10–20 | Open problem papers |
| 16. Future opportunities | 15–25 | Future direction papers |
| 17. Conclusions | 5–10 | Synthesis references |
| **Total** | **250–420** | **Target: 150–300 unique** |

---

## 6. Risk Mitigation

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Key paper paywalled, no access | HIGH | MEDIUM | Cite from metadata; flag as limitation; seek preprint |
| Citation count discrepancy between databases | MEDIUM | LOW | Report both OpenAlex and Crossref counts |
| Important theory family under-represented | MEDIUM | MEDIUM | Targeted journal-focused searches |
| Researcher's own work over-cited | LOW | HIGH | Enforce 15–20% cap per section |
| Equation presented as universal when model-specific | MEDIUM | HIGH | Equation verification register; status categories |
| Bibliographic record invented | LOW | CRITICAL | Every citation must have DOI or verifiable source |

---

## 7. Next Steps

1. Expand search to Semantic Scholar and arXiv (theory-specific terms)
2. Execute citation chaining backward from foundational reviews (alternative to OpenAlex `referenced_works`)
3. Attempt full-text access for RG-001, RG-002, RG-004 through RG-007
4. Build master BibTeX library from Crossref/OpenAlex metadata
5. Populate equation verification register for all candidate equations
6. Conduct existing-review saturation analysis (5–10 reviews)

---

**Next:** Proceed to Deliverable 7 (High-Quality Source-Selection and Equation-Selection Criteria).
