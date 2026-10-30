# Deliverable 11 — Author-Publication Consistency Review Plan

**Branch:** arena/40393d9f-le  
**Prepared:** 2026-10-21  
**Alignment:** Master Editorial Directive §2 (authorship-aware scientific consistency), §17 (scientific writing standards)

---

## 1. Purpose

Ensure that the researcher's prior publications (Vipin Gupta, Gurugram University; ORCID 0000-0002-5238-1963) are treated fairly and accurately within the broader scientific literature, consistent with Directive §2:

- The review must **never become an article about alleged errors** in the researcher's publications
- All included statements must remain **scientifically accurate**
- Different formulations may be valid under different **assumptions, material symmetries, geometries, boundary conditions, thermal theories, wave regimes, frequency conventions, normalization approaches, and levels of approximation**
- Do **not treat model-specific differences as mathematical contradictions** without sufficient evidence
- Avoid **unnecessarily adversarial judgments** of existing research
- Do **not frame the paper as a retrospective audit** of the author's mathematical correctness

---

## 2. Researcher's Publication Record (Phase 2 Verified)

### 2.1 Researcher-corpus studies (RG-001 through RG-007)

| ID | DOI | Journal | Year | Topic | Co-authors | Crossref verified |
|----|-----|---------|------|-------|------------|-------------------|
| RG-001 | 10.1007/s12648-022-02568-w | Indian J. Phys. 97(8) | 2023 | Piezothermoelastic interface | Barak, Kumar, Kumar, Gupta | YES (22 cites) |
| RG-002 | 10.1108/hff-11-2022-0654 | Heat Mass Transfer? | 2023 | Nonlocal thermoelastic-piezothermoelastic + MDD + HTT + TPL | Gupta, Kumar, Kumar, Barak | YES (20 cites) |
| RG-003 | 10.1038/s41598-023-44339-5 | Scientific Reports 13 | 2023 | MDD+TPL piezothermoelastic-thermoelastic interface | Barak, Ahmad, Kumar, Kumar, Gupta, Awwad, Ismail | YES (18 cites); OPEN ACCESS |
| RG-004 | 10.1108/mmms-10-2022-0209 | Mechanics Based Design? | 2023 | Imperfect interface DPL+MDD graphite/cadmium selenide | Barak, Kumar, Kumar, Gupta | YES (18 cites) |
| RG-005 | 10.1080/01495739.2023.2253879 | J. Thermal Stresses 47(2) | 2024 | Monoclinic piezothermoelastic+thermoelastic MDD | Barak, Kumar, Kumar, Gupta | YES (8 cites) |
| RG-006 | 10.1088/1402-4896/acfced | Physica Scripta 98(11) | 2023 | Dual-porous+elastic+MDD+DPL+H2T | Kumar, Gupta, Pathania, Barak | YES (11 cites) |
| RG-007 | 10.1108/hff-04-2022-0259 | Heat Mass Transfer? | 2023 | Nonlocal piezothermoelastic+fluid+DPL+two-temperature+MDD | Gupta, Kumar, Kumar, Pathania, Barak | YES (28 cites) |

### 2.2 Identity verification

- **ORCID:** 0000-0002-5238-1963 (Vipin Gupta, Gurugram University, India)
- **OpenAlex author filter:** 49 publications found
- **Crossref verification:** All 7 RG DOIs verified with matching titles and citation counts

---

## 3. Consistency Review Principles (Directive §2)

### 3.1 Fair treatment principles

| Principle | Implementation |
|-----------|---------------|
| Contextual validity | Each RG study presented with its stated assumptions (material symmetry, geometry, boundary conditions, thermal theory) |
| No isolated error claims | No statement of the form "RG-XXX contains an error" without exceptional evidence |
| Comparative framing | Differences between RG studies and other work framed as "different assumptions" or "model-specific formulations" |
| Balanced citation | RG studies cited alongside competing work in the same sub-domain |
| Citation cap | RG studies ≤ 15–20% of citations in any single section |

### 3.2 Handling the RG-003 asymmetric flux finding (GAP-011)

This is the one area where a Phase 2 finding touches an RG publication directly. Handling per Directive §2:

| Aspect | Handling |
|--------|----------|
| Finding | HPS side energy flux (Eq. 45) includes thermal term; TS side (Eq. 46) does not |
| Framing | "RG-003 defines energy flux differently on the two sides of the same interface" — factual observation, not accusation |
| Implication | "The claimed energy conservation (Eq. 58) does not represent total energy conservation under these flux definitions" — logical consequence, not error allegation |
| Resolution path | "Deriving a symmetric flux definition for both media would test whether ΣR+ΣT+A=1 holds" — constructive forward direction |
| Language | Avoid: "RG-003 is wrong," "the authors made an error," "this invalidates their results" |
| Use instead: "The flux definition is model-specific," "the conservation claim applies to the defined flux subset," "a symmetric formulation remains an open question" |

---

## 4. Section-by-Section RG Treatment Plan

| Section | RG studies relevant | Treatment approach |
|---------|-------------------|-------------------|
| §3 Foundations | None (foundational only) | No RG citation needed |
| §4 Thermoelastic theories | RG-003 (MDD+TPL), RG-004 (DPL+MDD), RG-005 (MDD), RG-006 (MDD+DPL), RG-007 (MDD+DPL) | Cite as applications of generalized theories; present assumptions clearly |
| §5 Multiphysics continua | RG-001, RG-003, RG-005 (piezothermoelastic); RG-006 (porous); RG-007 (fluid+piezo) | Cite as interface problem examples; note model-specific conditions |
| §6 Transport and memory | RG-003–RG-007 (all use MDD) | Cite as MDD applications; note kernel choices |
| §7 Nonlocal models | RG-002, RG-007 (nonlocal) | Cite as nonlocal applications |
| §8 Mathematical methods | All RG (analytical methods) | Cite as analytical solution examples |
| §9 Interface phenomena | All RG (all are interface problems) | Cite as interface condition examples; note differences (perfect vs imperfect) |
| §10 Energy and dissipation | RG-003 (energy flux), RG-007 (claims conservation) | Cite with flux asymmetry finding; present as open question |
| §11 Advanced developments | RG-002–RG-007 | Cite as examples of advanced formulations |
| §12 Comparative synthesis | All RG | Compare across theories with assumption-aware framing |
| §13 Applications | All RG | Cite as application examples |
| §14 Taxonomy | All RG | Classify using five dimensions |
| §15 Challenges | RG-003 (flux asymmetry), RG-007 (conservation claim) | Frame as open questions, not errors |
| §16 Future opportunities | All RG | Suggest extensions based on identified gaps |

---

## 5. Citation Cap Enforcement

| Section | Total citations (target) | Max RG citations (15–20%) | RG studies to cite |
|---------|-------------------------|--------------------------|-------------------|
| §3 Foundations | 15–25 | 0 | None |
| §4 Thermoelastic | 30–50 | 4–6 | RG-003, RG-004, RG-005, RG-006 |
| §5 Multiphysics | 25–40 | 3–5 | RG-001, RG-003, RG-005, RG-006, RG-007 |
| §6 Transport | 20–30 | 3–4 | RG-003, RG-004, RG-005, RG-006 |
| §7 Nonlocal | 15–25 | 2–3 | RG-002, RG-007 |
| §8 Methods | 10–20 | 1–2 | RG-003 (analytical) |
| §9 Interfaces | 20–30 | 3–5 | All RG (as examples) |
| §10 Energy | 20–30 | 3–4 | RG-003, RG-007 |
| §11 Advanced | 10–20 | 1–2 | RG-002–RG-007 |
| §12 Synthesis | 30–50 | 4–6 | All RG (comparative) |
| §13 Applications | 15–25 | 2–3 | RG-003–RG-007 |
| §14 Taxonomy | 10–15 | 1–2 | RG-003 (example) |
| §15 Challenges | 10–20 | 1–2 | RG-003 (flux asymmetry) |
| §16 Future | 15–25 | 2–3 | RG-003–RG-007 (extensions) |

**Overall target:** RG studies ≤ 15% of total citations (~45 of 300)

---

## 6. Language Guidelines (Directive §2)

### 6.1 Prohibited language (never use)

| Prohibited | Reason |
|------------|--------|
| "The previous authors were mathematically wrong" | Adversarial; not supported by review objectives |
| "This publication contains erroneous results" | Accusatory; violates Directive §1 |
| "Earlier formulations are invalid" | Overgeneralization; different assumptions may apply |
| "Existing studies failed completely" | Exaggerated; not constructive |
| "RG-XXX made an error in Eq. Y" | Personalizes; violates Directive §2 |

### 6.2 Preferred language (always use)

| Preferred | Example |
|-----------|---------|
| "The model considers..." | "RG-003 considers a piezothermoelastic–thermoelastic interface with MDD+TPL heat conduction" |
| "Under the specified assumptions..." | "Under the assumptions of perfect bonding and insulated electrical contact..." |
| "An alternative formulation introduces..." | "An alternative formulation introduces spring-type interface conditions (RG-004)" |
| "A subsequent extension accounts for..." | "Subsequent work extends the model to include nonlocal effects (RG-007)" |
| "The available evidence is limited for..." | "The available evidence is limited for energy flux verification at nonlocal interfaces" |
| "This relationship warrants further investigation" | "Whether ΣR+ΣT+A=1 holds with symmetric flux definitions warrants further investigation" |

### 6.3 Handling apparent discrepancies

| Situation | Handling |
|-----------|----------|
| Two papers report different energy ratios for similar setup | "The differences may reflect different normalization conventions, material parameters, or interface conditions" |
| Paper claims conservation but flux definition is asymmetric | "The conservation claim applies to the defined flux subset; extension to total energy requires symmetric flux definitions" |
| Different theories give different wave speeds | "The differences reflect different relaxation mechanisms and constitutive assumptions" |

---

## 7. Consistency Review Checklist

Before manuscript submission, verify:

| Check | Description | Status |
|-------|-------------|--------|
| No adversarial language | Scan for "wrong," "error," "invalid," "failed" | ☐ |
| RG studies in context | Each RG citation includes assumptions and model specificity | ☐ |
| Citation cap respected | RG ≤ 15–20% per section | ☐ |
| GAP-011 framed constructively | Asymmetric flux presented as open question, not error | ☐ |
| Competing work cited fairly | Non-RG work in same sub-domain cited alongside RG | ☐ |
| No retrospective audit | Manuscript does not read as evaluation of author correctness | ☐ |
| All claims scientifically accurate | Every statement supported by evidence or derivation | ☐ |
| Source attribution clear | RG equations attributed to RG-003 with equation numbers | ☐ |

---

## 7.1 Special Handling: GAP-011 (RG-003 Asymmetric Flux)

This finding requires careful handling because it directly involves an RG publication.

**Manuscript treatment plan:**

1. **Present the observation factually:** "RG-003 defines energy flux on the HPS side (Eq. 45) as including mechanical, electrical, and thermal channels, while the TS side (Eq. 46) includes mechanical channels only."

2. **State the logical implication:** "Given this asymmetry, the claimed energy conservation (Eq. 58, Σ = 1) applies to the defined flux subset, not necessarily to total energy."

3. **Frame as open question:** "Whether ΣR + ΣT + A = 1 holds with symmetric flux definitions on both sides remains an open question."

4. **Provide constructive path forward:** "Deriving a complete, symmetric energy flux for both media would enable a definitive conservation test."

5. **Never say:** "RG-003 is wrong," "the authors made an error," "this invalidates their energy ratio results"

---

## 8. Escalation Protocol

If a reviewer or reader questions the treatment of RG publications:

| Situation | Response |
|-----------|----------|
| "You're being too soft on RG-003" | Point to the factual observation of flux asymmetry; explain it's presented as an open question, not an error |
| "You're being too hard on RG-003" | Point to the constructive framing; no error allegations made; all statements are factual observations |
| "RG-003 conservation claim should be accepted" | Explain that the claim is model-specific (defined flux subset); total energy conservation requires symmetric flux |
| "You should audit all RG papers for errors" | Decline; Directive §1 explicitly prohibits making error identification a principal objective |

---

## 9. Documentation

All consistency review decisions recorded in:

| File | Content |
|------|---------|
| `phase3/11_author_publication_consistency_plan.md` | This plan |
| `references/source_provenance.csv` | Source of each RG paper (Crossref-verified) |
| `phase2/06_equation_provenance_register.csv` | Equation attribution (RG-003 equations with source) |
| `phase2/14_validated_research_gaps.csv` | GAP-011 documentation with evidence level |

---

**Next:** Proceed to Deliverable 12 (Journal Suitability Comparison).
