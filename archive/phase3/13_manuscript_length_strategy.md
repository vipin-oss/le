# Deliverable 13 — Manuscript Length and Supplementary-Material Strategy

**Branch:** arena/40393d9f-le  
**Prepared:** 2026-10-21  
**Alignment:** Master Editorial Directive §16 (journal strategy and article length)

---

## 1. Length Philosophy

Per Directive §16: **"Do not set a mandatory word count before investigating journal policy."** The manuscript length must be determined by:

1. Target journal's review article policies
2. Scientific content requirements (not arbitrary targets)
3. Reader usability (different paths for different reader types)
4. Reproducibility (supplementary material for derivations, data, code)

---

## 2. Version A — Comprehensive Journal Review

### 2.1 Target length: 60–90 pages (main text + references)

| Component | Pages | % of total |
|-----------|-------|------------|
| Front matter (title, abstract, notation, acronyms) | 4 | 5% |
| §1 Scope and purpose | 3 | 4% |
| §2 Literature strategy | 5 | 6% |
| §3 Foundations | 12 | 15% |
| §4 Thermoelastic theories | 18 | 23% |
| §5 Multiphysics continua | 15 | 19% |
| §6 Transport and memory | 10 | 13% |
| §7 Nonlocal models | 8 | 10% |
| §8 Mathematical methods | 8 | 10% |
| §9 Interface phenomena | 12 | 15% |
| §10 Energy and dissipation | 12 | 15% |
| §11 Advanced developments | 6 | 8% |
| §12 Comparative synthesis | 15 | 19% |
| §13 Applications | 6 | 8% |
| §14 Taxonomy | 8 | 10% |
| §15 Challenges | 6 | 8% |
| §16 Future opportunities | 8 | 10% |
| §17 Conclusions | 4 | 5% |
| References | 10 | 13% |
| **Main text total** | **~60-75** | |
| **With references** | **~70-85** | |

### 2.2 Figures: 10–15

Priority 1 and Priority 2 figures from Deliverable 9:

| Fig ID | Section | Purpose |
|--------|---------|---------|
| F-A01 | §1 | Historical timeline |
| F-B01 | §3 | Continuum kinematics |
| F-B02 | §4 | Thermoelastic coupling |
| F-B03 | §5 | Piezoelectricity |
| F-B06 | §7 | Nonlocal interactions |
| F-C01 | §3 | Balance-law dependency |
| F-C02 | §8 | Wave propagation geometry |
| F-C03 | §9 | Interface scattering |
| F-C05 | §8 | Complex wave numbers |
| F-C07 | §10 | Energy transport pathways |
| F-D01 | §14 | Taxonomy visualization |
| F-D05 | §15-16 | Open-problem map |
| F-E01 | §10 | RG-003 asymmetric flux (CRITICAL) |
| F-E02 | §9 | Scattering matrix |
| F-E03 | §10 | Conservation verification |

### 2.3 Tables: 8–10

| Table ID | Section | Purpose |
|----------|---------|---------|
| Table 1 | Front matter | Notation |
| Table 2 | Front matter | Acronyms |
| Table 3 | §4.1 | Historical development |
| Table 4 | §4-7 | Governing equations |
| Table 6 | §4-6 | Thermal transport models |
| Table 8 | §9.3 | Interface conditions |
| Table 11 | §10.2-10.3 | Energy transport formulations |
| Table 14 | §15 | Research limitations |
| Table 16 | Appendix A | Equation register (condensed) |

### 2.4 References: 150–200

Target distribution:
- Foundational works: 30–50
- Researcher corpus (RG): 7 (all)
- External discoveries (EXT): 6 (all)
- Additional peer-reviewed: 100–150
- Existing reviews: 5–10

### 2.5 Supplementary material (online only)

| Item | Content | Format |
|------|---------|--------|
| Equation register | Full 23-equation register with verification status | CSV/PDF |
| Benchmark specifications | BM-1 through BM-5 detailed specifications | PDF |
| Figure specifications | All 25-40 figure specs | PDF |
| Table specifications | All 14-16 table specs | PDF |
| Derivation details | Full mathematical derivations for classical balance laws | PDF |
| Validation scripts | Python validation scripts | .py files |

---

## 3. Version B — Extended Authoritative Review

### 3.1 Target length: 100–150 pages (main text + references)

| Component | Pages | % of total |
|-----------|-------|------------|
| Front matter | 6 | 5% |
| §1-2 (Scope, strategy) | 10 | 8% |
| §3-7 (Foundations + theories) | 55 | 45% |
| §8-10 (Methods, interfaces, energy) | 40 | 33% |
| §11-13 (Advanced, synthesis, applications) | 35 | 30% |
| §14-17 (Taxonomy, challenges, future, conclusions) | 25 | 20% |
| References | 15 | 13% |
| **Main text total** | **~120-140** | |
| **With references** | **~135-155** | |

### 3.2 Figures: 25–40 (all from Deliverable 9)

All Priority 1, 2, 3, and 4 figures included.

### 3.3 Tables: 14–16 (all from Deliverable 10)

All tables included with full verification.

### 3.4 References: 300–400

Expanded from Version A with additional literature from systematic search.

### 3.5 Appendices (included in main document or supplementary)

| Appendix | Content | Pages |
|----------|---------|-------|
| Appendix A | Equation verification register (full) | 10 |
| Appendix B | Classical balance law derivations | 15 |
| Appendix C | Benchmark specifications (BM-1 through BM-5) | 15 |
| Appendix D | Figure-by-figure blueprint | 10 |
| Appendix E | Table-by-table blueprint | 10 |
| Appendix F | Reproducibility statement | 5 |
| **Total appendices** | | **~65** |

---

## 4. Section-by-Section Length Allocation

| Section | Version A | Version B | Rationale for difference |
|---------|-----------|-----------|-------------------------|
| §1 Scope and purpose | 3 | 4 | Version B adds more motivation detail |
| §2 Literature strategy | 5 | 8 | Version B includes expanded search methodology |
| §3 Foundations | 12 | 20 | Version B includes more worked derivations |
| §4 Thermoelastic theories | 18 | 35 | Version B includes all 9 theories with equations |
| §5 Multiphysics continua | 15 | 25 | Version B includes all coupling types |
| §6 Transport and memory | 10 | 15 | Version B includes fractional operators |
| §7 Nonlocal models | 8 | 12 | Version B includes strain-gradient details |
| §8 Mathematical methods | 8 | 12 | Version B includes more numerical methods |
| §9 Interface phenomena | 12 | 20 | Version B includes imperfect bonding details |
| §10 Energy and dissipation | 12 | 20 | Version B includes all theory flux forms (if derived) |
| §11 Advanced developments | 6 | 10 | Version B includes more emerging theories |
| §12 Comparative synthesis | 15 | 30 | Version B includes full comparison tables |
| §13 Applications | 6 | 10 | Version B includes more application domains |
| §14 Taxonomy | 8 | 15 | Version B includes full classification of 150+ studies |
| §15 Challenges | 6 | 10 | Version B includes more challenge detail |
| §16 Future opportunities | 8 | 15 | Version B includes more direction detail |
| §17 Conclusions | 4 | 6 | Version B includes more synthesis |

---

## 5. Reader Path Optimization

### 5.1 Beginning researcher path (~20 pages)

| Component | Pages |
|-----------|-------|
| Front matter (notation table) | 4 |
| §1 Scope and purpose | 3 |
| §3 Foundations | 12 |
| §17 Conclusions | 4 |
| Table 1 (notation) | Referenced |
| **Total** | **~20** |

### 5.2 Doctoral student path (~50 pages)

| Component | Pages |
|-----------|-------|
| Front matter | 4 |
| §1-3 (Scope, strategy, foundations) | 20 |
| §4-7 (Theories) | 25 |
| Appendix A (equation register) | Referenced |
| **Total** | **~50** |

### 5.3 Experienced scientist path (~30 pages)

| Component | Pages |
|-----------|-------|
| §1 Scope and purpose | 3 |
| §12 Comparative synthesis | 15 |
| §14 Taxonomy | 8 |
| §16 Future opportunities | 8 |
| Table 14 (limitations) | Referenced |
| **Total** | **~30** |

### 5.4 Journal reviewer path (~15 pages)

| Component | Pages |
|-----------|-------|
| §1 Scope and purpose | 3 |
| §2 Literature strategy | 5 |
| §12 Comparative synthesis | 5 |
| §16-17 (Future, conclusions) | 4 |
| **Total** | **~15** |

---

## 6. Supplementary Material Decision Matrix

| Item | Version A | Version B | Rationale |
|------|-----------|-----------|-----------|
| Notation table | In main text | In main text | Needed for readability |
| Acronym table | In main text | In main text | Needed for readability |
| Equation register | Supplementary | Appendix A | Quality control; too long for main text |
| Balance law derivations | Supplementary | Appendix B | Supporting detail |
| Benchmark specifications | Supplementary | Appendix C | Reproducibility |
| Figure specifications | Supplementary | Appendix D | Reference |
| Table specifications | Supplementary | Appendix E | Reference |
| Validation scripts | Online repository | Online repository | Code availability |
| Full literature database | Supplementary | Supplementary | Reference |
| Deep extraction records | Supplementary | Supplementary | Reference |

---

## 7. Word Count Equivalents

| Format | Approximate words |
|--------|-------------------|
| Version A (70-85 pages) | ~35,000-42,500 words |
| Version B (135-155 pages) | ~67,500-77,500 words |

**Typical page assumption:** 500 words per page (including equations, tables, figures)

---

## 8. Compression Strategies (if journal requires shorter)

| Strategy | Pages saved | Impact |
|----------|-------------|--------|
| Condense §4-7 theory descriptions | 8-12 | Some theory detail moved to tables |
| Combine §11 into §12 | 3-5 | Less repetition |
| Reduce §13 applications | 2-4 | Fewer application examples |
| Move Table 16 to supplementary | 3-5 | Equation register online only |
| Reduce figures from 15 to 10 | 3-5 | Only Priority 1 figures |
| **Total potential savings** | **18-31 pages** | |

---

## 9. Expansion Strategies (if journal encourages longer)

| Strategy | Pages added | Impact |
|----------|-------------|--------|
| Add more worked derivations | 10-15 | §3, §4 derivations expanded |
| Add more comparison tables | 5-8 | Additional cross-theory comparisons |
| Add more application examples | 5-10 | §13 expanded |
| Add more future direction detail | 5-8 | §16 expanded |
| Add full appendices | 40-60 | Version B appendices |
| **Total potential addition** | **65-102 pages** | |

---

## 10. Journal-Specific Length Recommendations

| Journal | Recommended version | Target pages | Rationale |
|---------|-------------------|--------------|-----------|
| JMPS | Version A | 60-80 | Premier mechanics journal; concise reviews preferred |
| IJSS | Version A | 60-80 | Similar to JMPS |
| Wave Motion | Version A | 50-70 | Specialized journal; focused scope |
| Royal Society A | Version B | 100-150 | Prestigious; comprehensive treatment welcomed |
| CMT | Version A | 60-80 | Targeted audience; concise preferred |
| JTS | Version A | 50-70 | Narrower scope; focused on thermal aspects |

---

## 11. Timeline for Length Decisions

| Milestone | Timing | Decision |
|-----------|--------|----------|
| Presubmission inquiries | Month 4.5 | Learn journal length preferences |
| Version A outline finalized | Month 5 | Lock section page allocations |
| First draft | Month 6-8 | Write to Version A length |
| Journal feedback | Month 9-10 | Adjust length if needed |
| Version B preparation (fallback) | Month 9+ | Only if needed |

---

## 12. Alignment with Directive §16

| Directive provision | Our approach |
|---------------------|-------------|
| Do not set mandatory word count before journal policy | Ranges provided; presubmission inquiry planned |
| Prepare Version A (journal-focused) | 60-90 pages specified |
| Prepare Version B (extended authoritative) | 100-150 pages + appendices specified |
| Preserve scientific depth while respecting constraints | Compression/expansion strategies defined |
| 100-page-plus may be appropriate for some formats | Version B accommodates this |
| Unsuitable for others | Version A for concise journals |

---

**Next:** Proceed to Deliverable 14 (Scientific Novelty Assessment).
