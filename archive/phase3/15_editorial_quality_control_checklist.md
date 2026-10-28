# Deliverable 15 — Editorial Quality-Control Checklist

**Branch:** arena/40393d9f-le  
**Prepared:** 2026-10-21  
**Alignment:** Master Editorial Directive §18 (seven-perspective quality control), §17 (scientific writing standards)

---

## 1. Seven-Perspective Audit Framework

The manuscript must be audited from seven perspectives before submission:

| # | Perspective | Focus | Key questions |
|---|-------------|-------|---------------|
| 1 | Applied mathematics | Equation correctness, notation consistency | Are all equations dimensionally consistent? Is notation consistent throughout? |
| 2 | Continuum mechanics | Physical validity, model assumptions | Are constitutive assumptions clearly stated? Are models physically meaningful? |
| 3 | Thermodynamics | Dissipation, admissibility, energy | Is the dissipation inequality correctly applied? Is energy flux well-defined? |
| 4 | Wave propagation | Wave speeds, dispersion, modes | Are wave speeds correctly derived? Are complex modes handled consistently? |
| 5 | Scientific literature methodology | Citation quality, source selection | Are citations verifiable? Is source selection fair and comprehensive? |
| 6 | Mathematical visualization | Figure quality, clarity | Are figures scientifically accurate? Are captions self-contained? |
| 7 | Journal editorial standards | Format, scope, length | Does the manuscript fit the target journal? Are length and format appropriate? |

---

## 2. Perspective 1 — Applied Mathematics

### 2.1 Equation correctness

| Check | Description | Pass criterion | Status |
|-------|-------------|----------------|--------|
| Dimensional consistency | All terms in every equation have same dimensions | ✓ for all equations | ☐ |
| Symbol definition | Every symbol defined at first use | ✓ for all symbols | ☐ |
| Sequential numbering | Equations numbered 1, 2, 3... through manuscript | ✓ | ☐ |
| Equation citation | Every equation cited in text | ✓ | ☐ |
| Verification status | Each equation has register status | VERIFIED or VALID UNDER ASSUMPTIONS | ☐ |

### 2.2 Notation consistency

| Check | Description | Pass criterion | Status |
|-------|-------------|----------------|--------|
| Master notation table | All symbols in Table 1 | Complete | ☐ |
| No symbol reuse | Same symbol not used for different quantities | ✓ | ☐ |
| Index notation | Einstein summation used consistently | ✓ | ☐ |
| Vector/tensor notation | Consistent throughout | ✓ | ☐ |

### 2.3 Mathematical exposition

| Check | Description | Pass criterion | Status |
|-------|-------------|----------------|--------|
| Layered structure | Layers I-VII followed | ✓ | ☐ |
| Assumptions stated | Each derivation states assumptions | ✓ | ☐ |
| Physical interpretation | Each equation followed by interpretation | ✓ | ☐ |
| Citation of sources | Each equation cites its source | ✓ | ☐ |

---

## 3. Perspective 2 — Continuum Mechanics

### 3.1 Physical validity

| Check | Description | Pass criterion | Status |
|-------|-------------|----------------|--------|
| Conservation laws | Linear momentum, angular momentum satisfied | ✓ | ☐ |
| Constitutive assumptions | Clearly stated for each theory | ✓ | ☐ |
| Material symmetry | Correctly specified (isotropic, orthotropic, etc.) | ✓ | ☐ |
| Geometry | Correctly specified (half-space, interface, etc.) | ✓ | ☐ |

### 3.2 Model assumptions

| Check | Description | Pass criterion | Status |
|-------|-------------|----------------|--------|
| Boundary conditions | Correctly specified for each problem | ✓ | ☐ |
| Interface conditions | Correctly specified (perfect vs imperfect) | ✓ | ☐ |
| Thermal theory | Correctly specified (Fourier, LS, DPL, etc.) | ✓ | ☐ |
| Coupling fields | Correctly specified (mechanical, thermal, electrical, etc.) | ✓ | ☐ |

---

## 4. Perspective 3 — Thermodynamics

### 4.1 Dissipation and admissibility

| Check | Description | Pass criterion | Status |
|-------|-------------|----------------|--------|
| Clausius-Duhem inequality | Correctly stated | ✓ | ☐ |
| Coleman-Noll restrictions | Correctly derived | ✓ | ☐ |
| Dissipation sign | Dissipation ≥ 0 for dissipative theories | ✓ | ☐ |
| Well-posedness | Conditions stated for each theory | ✓ | ☐ |

### 4.2 Energy

| Check | Description | Pass criterion | Status |
|-------|-------------|----------------|--------|
| Energy flux | Correctly defined for classical theories | ✓ | ☐ |
| Flux asymmetry | RG-003 finding documented factually | ✓ | ☐ |
| Conservation identity | Conditions for ΣR+ΣT+A=1 stated | ✓ | ☐ |
| No overclaiming | No claim of total conservation without symmetric flux | ✓ | ☐ |

---

## 5. Perspective 4 — Wave Propagation

### 5.1 Wave characteristics

| Check | Description | Pass criterion | Status |
|-------|-------------|----------------|--------|
| Wave speeds | Correctly derived for each theory | ✓ | ☐ |
| Dispersion | Correctly characterized | ✓ | ☐ |
| Attenuation | Correctly characterized | ✓ | ☐ |
| Polarization | Correctly described | ✓ | ☐ |

### 5.2 Complex modes

| Check | Description | Pass criterion | Status |
|-------|-------------|----------------|--------|
| Evanescent modes | Correctly handled (no net energy flux) | ✓ | ☐ |
| Attenuating modes | Correctly handled (complex Poynting vector) | ✓ | ☐ |
| Normalization | Consistent normalization for energy computation | ✓ | ☐ |

### 5.3 Interface phenomena

| Check | Description | Pass criterion | Status |
|-------|-------------|----------------|--------|
| Scattering matrix | Correctly formulated (ΔX = Q) | ✓ | ☐ |
| Mode conversion | Correctly described (P↔SV↔T, etc.) | ✓ | ☐ |
| Reciprocity | Correctly stated (where applicable) | ✓ | ☐ |

---

## 6. Perspective 5 — Scientific Literature Methodology

### 6.1 Citation quality

| Check | Description | Pass criterion | Status |
|-------|-------------|----------------|--------|
| DOI verification | All DOIs Crossref-verified | ✓ | ☐ |
| Peer review | All cited works peer-reviewed | ✓ | ☐ |
| No invented records | Every citation has verifiable source | ✓ | ☐ |
| Fair representation | Competing work cited fairly | ✓ | ☐ |

### 6.2 Source selection

| Check | Description | Pass criterion | Status |
|-------|-------------|----------------|--------|
| Inclusion criteria followed | Directive §3 criteria applied | ✓ | ☐ |
| Exclusion documented | Excluded studies have documented reasons | ✓ | ☐ |
| Full-text access noted | Open access vs abstract-only recorded | ✓ | ☐ |
| Abstract-only limitations | Limitations acknowledged | ✓ | ☐ |

### 6.3 RG treatment (Directive §2)

| Check | Description | Pass criterion | Status |
|-------|-------------|----------------|--------|
| No adversarial language | No "wrong," "error," "invalid," "failed" | ✓ | ☐ |
| RG in context | Each RG citation includes assumptions | ✓ | ☐ |
| Citation cap | RG ≤ 15-20% per section | ✓ | ☐ |
| GAP-011 constructive | Asymmetric flux as open question | ✓ | ☐ |

---

## 7. Perspective 6 — Mathematical Visualization

### 7.1 Figure quality

| Check | Description | Pass criterion | Status |
|-------|-------------|----------------|--------|
| Scientific purpose | Every figure answers a specific question | ✓ | ☐ |
| No decorative figures | Every figure has scientific content | ✓ | ☐ |
| Validated content | No misleading or incorrect elements | ✓ | ☐ |
| Editable source | TikZ or SVG source file exists | ✓ | ☐ |

### 7.2 Figure presentation

| Check | Description | Pass criterion | Status |
|-------|-------------|----------------|--------|
| Self-contained caption | Understandable without main text | ✓ | ☐ |
| Accurate symbols | Consistent with manuscript notation | ✓ | ☐ |
| Relevant citations | Source equations/papers cited | ✓ | ☐ |
| Consistent notation | Same symbols as main text | ✓ | ☐ |

### 7.3 Table quality

| Check | Description | Pass criterion | Status |
|-------|-------------|----------------|--------|
| Analytical purpose | Every table answers a comparative question | ✓ | ☐ |
| Verified entries | Every entry traceable to primary source | ✓ | ☐ |
| No non-equivalent comparison | Compare only under identical conditions | ✓ | ☐ |
| Explanatory notes | Assumption differences documented | ✓ | ☐ |

---

## 8. Perspective 7 — Journal Editorial Standards

### 8.1 Format and scope

| Check | Description | Pass criterion | Status |
|-------|-------------|----------------|--------|
| Journal scope | Manuscript fits target journal scope | ✓ | ☐ |
| Review policy | Journal accepts unsolicited reviews | ✓ | ☐ |
| Length | Within journal's preferred range | ✓ | ☐ |
| Format | Follows journal's author guidelines | ✓ | ☐ |

### 8.2 Writing quality

| Check | Description | Pass criterion | Status |
|-------|-------------|----------------|--------|
| Academic English | Formal, polished academic writing | ✓ | ☐ |
| No exaggeration | No promotional or inflated language | ✓ | ☐ |
| Coherent argument | Each section has coherent structure | ✓ | ☐ |
| Section summaries | Concise summaries at end of major sections | ✓ | ☐ |

### 8.3 Integrity

| Check | Description | Pass criterion | Status |
|-------|-------------|----------------|--------|
| No error allegations | No claims of mathematical errors in prior work | ✓ | ☐ |
| No concealment | No material scientific findings concealed | ✓ | ☐ |
| No citation manipulation | Citations not selected solely on journal prestige | ✓ | ☐ |
| RG fair treatment | Researcher's prior work treated fairly | ✓ | ☐ |

---

## 9. Pre-Submission Checklist (All Seven Perspectives)

| # | Item | Perspective | Pass criterion | Status |
|---|------|-------------|----------------|--------|
| 1 | All equations dimensionally consistent | 1 | ✓ for all | ☐ |
| 2 | All symbols defined at first use | 1 | ✓ for all | ☐ |
| 3 | Master notation table complete | 1 | All symbols included | ☐ |
| 4 | Conservation laws correctly stated | 2 | ✓ | ☐ |
| 5 | Constitutive assumptions clearly stated | 2 | ✓ for all theories | ☐ |
| 6 | Dissipation inequality correctly applied | 3 | ✓ | ☐ |
| 7 | Energy flux correctly defined (classical) | 3 | ✓ | ☐ |
| 8 | RG-003 flux asymmetry documented factually | 3 | ✓ | ☐ |
| 9 | No claim of total conservation without symmetric flux | 3 | ✓ | ☐ |
| 10 | Wave speeds correctly derived | 4 | ✓ for all theories | ☐ |
| 11 | Complex modes handled consistently | 4 | ✓ | ☐ |
| 12 | Scattering matrix correctly formulated | 4 | ✓ | ☐ |
| 13 | All DOIs Crossref-verified | 5 | ✓ for all | ☐ |
| 14 | All cited works peer-reviewed | 5 | ✓ | ☐ |
| 15 | No invented bibliographic records | 5 | ✓ | ☐ |
| 16 | No adversarial language about any author | 5, 7 | ✓ | ☐ |
| 17 | RG studies ≤ 15-20% per section | 5 | ✓ | ☐ |
| 18 | GAP-011 framed as open question | 5, 7 | ✓ | ☐ |
| 19 | Every figure has scientific purpose | 6 | ✓ | ☐ |
| 20 | Every figure has editable source file | 6 | TikZ or SVG | ☐ |
| 21 | Every figure caption self-contained | 6 | ✓ | ☐ |
| 22 | Every table has analytical purpose | 6 | ✓ | ☐ |
| 23 | Every table entry verified | 6 | ✓ | ☐ |
| 24 | Manuscript fits target journal scope | 7 | ✓ | ☐ |
| 25 | Length within journal range | 7 | ✓ | ☐ |
| 26 | Formal academic English | 7 | ✓ | ☐ |
| 27 | No exaggeration or promotional language | 7 | ✓ | ☐ |
| 28 | Section summaries present | 7 | ✓ for major sections | ☐ |
| 29 | No error allegations in prior work | 7 | ✓ | ☐ |
| 30 | No material findings concealed | 7 | ✓ | ☐ |

---

## 10. Quality Gates

### Gate 1: After first draft (all sections written)

| Check | Required before proceeding |
|-------|---------------------------|
| All equations have verification status | YES |
| All figures have specifications | YES |
| All tables have specifications | YES |
| RG treatment reviewed for adversarial language | YES |

### Gate 2: After revision (before submission)

| Check | Required before submission |
|-------|---------------------------|
| All seven perspectives audited | YES |
| All 30 pre-submission checks passed | YES |
| Presubmission inquiry sent to target journal | YES |
| Journal length preferences confirmed | YES |

### Gate 3: After reviewer feedback

| Check | Required before resubmission |
|-------|-----------------------------|
| All reviewer concerns addressed | YES |
| No new adversarial language introduced | YES |
| All equation verifications re-checked | YES |

---

## 11. Common Issues and Remedies

| Issue | Perspective | Remedy |
|-------|-------------|--------|
| Equation not dimensionally consistent | 1 | Derive again; check units; flag as UNCERTAIN |
| Symbol reused for different quantities | 1 | Rename; update notation table |
| Constitutive assumption not stated | 2 | Add assumption statement before equation |
| Dissipation sign incorrect | 3 | Re-derive; check sign convention |
| Claim of total conservation without symmetric flux | 3 | Qualify: "applies to defined flux subset" |
| Wave speed incorrectly derived | 4 | Re-derive from Christoffel equation |
| Complex mode mishandled | 4 | Use complex Poynting vector; state normalization |
| DOI not verified | 5 | Check Crossref; remove if unverifiable |
| Adversarial language about author | 5, 7 | Rewrite constructively (Directive §2) |
| RG > 20% of citations in section | 5 | Add non-RG citations; reduce RG citations |
| Figure without scientific purpose | 6 | Remove or repurpose |
| Figure without editable source | 6 | Create TikZ/SVG source |
| Table comparing non-equivalent quantities | 6 | Separate tables; add explanatory notes |
| Manuscript too long for journal | 7 | Apply compression strategies (Deliverable 13) |
| Manuscript too short for journal | 7 | Apply expansion strategies (Deliverable 13) |

---

## 12. Sign-Off Record

| Role | Name | Date | Status |
|------|------|------|--------|
| Mathematical auditor (Perspective 1) | | | ☐ |
| Continuum mechanics auditor (Perspective 2) | | | ☐ |
| Thermodynamics auditor (Perspective 3) | | | ☐ |
| Wave propagation auditor (Perspective 4) | | | ☐ |
| Literature methodology auditor (Perspective 5) | | | ☐ |
| Visualization auditor (Perspective 6) | | | ☐ |
| Editorial standards auditor (Perspective 7) | | | ☐ |
| Final sign-off | | | ☐ |

---

**Next:** Proceed to Deliverable 16 (Milestone-Based Manuscript Execution Plan).
