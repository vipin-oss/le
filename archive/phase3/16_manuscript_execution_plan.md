# Deliverable 16 — Milestone-Based Manuscript Execution Plan

**Branch:** arena/40393d9f-le  
**Prepared:** 2026-10-21  
**Alignment:** Master Editorial Directive §20 (execution directive), §16 (journal strategy), §18 (quality control)

---

## 1. Execution Philosophy

Per Directive §20: **"Do not prematurely produce hundreds of pages without an approved scientific architecture."**

The execution plan follows a **milestone-based approach**:
1. Complete all 16 pre-manuscript deliverables (Phase 3a)
2. Derive unresolved energy fluxes (Phase 3b)
3. Write Version A manuscript (Phase 3c)
4. Submit to target journal (Phase 3d)
5. Prepare Version B as fallback (Phase 3e)

---

## 2. Phase 3a — Pre-Manuscript Deliverables (COMPLETED)

| Deliverable | File | Status |
|-------------|------|--------|
| 01 | Reference review structural analysis | `phase3/01_reference_review_structural_analysis.md` — COMPLETED |
| 02 | Revised scientific scope statement | `phase3/02_revised_scientific_scope_statement.md` — COMPLETED |
| 03 | Article title recommendations | `phase3/03_article_title_recommendations.md` — COMPLETED |
| 04 | Chapter-by-chapter outline | `phase3/04_chapter_by_chapter_outline.md` — COMPLETED |
| 05 | Mathematical content plan | `phase3/05_mathematical_content_plan.md` — COMPLETED |
| 06 | Literature acquisition strategy | `phase3/06_literature_acquisition_strategy.md` — COMPLETED |
| 07 | Source and equation selection criteria | `phase3/07_source_equation_selection_criteria.md` — COMPLETED |
| 08 | Scientific taxonomy proposal | `phase3/08_scientific_taxonomy_proposal.md` — COMPLETED |
| 09 | Figure-by-figure blueprint | `phase3/09_figure_by_figure_blueprint.md` — COMPLETED |
| 10 | Table-by-table blueprint | `phase3/10_table_by_table_blueprint.md` — COMPLETED |
| 11 | Author-publication consistency plan | `phase3/11_author_publication_consistency_plan.md` — COMPLETED |
| 12 | Journal suitability comparison | `phase3/12_journal_suitability_comparison.md` — COMPLETED |
| 13 | Manuscript length strategy | `phase3/13_manuscript_length_strategy.md` — COMPLETED |
| 14 | Scientific novelty assessment | `phase3/14_scientific_novelty_assessment.md` — COMPLETED |
| 15 | Editorial quality-control checklist | `phase3/15_editorial_quality_control_checklist.md` — COMPLETED |
| 16 | Manuscript execution plan | `phase3/16_manuscript_execution_plan.md` — THIS FILE |

---

## 3. Phase 3b — Critical Derivations (BEFORE WRITING)

These derivations must be completed before writing Section 10 (Energy and Dissipation), as they form the core mathematical contribution.

### 3b.1 Derivation schedule

| Milestone | Derivation | Target section | Est. effort | Dependency |
|-----------|------------|----------------|-------------|------------|
| 3b-1 | LS energy flux from relaxation equation | §10.3 | 1-2 weeks | EQ-007 (classical flux) |
| 3b-2 | DPL energy flux | §10.3 | 1-2 weeks | 3b-1 |
| 3b-3 | TPL energy flux | §10.3 | 1-2 weeks | 3b-2 |
| 3b-4 | MGT energy flux | §10.3 | 1-2 weeks | 3b-3 |
| 3b-5 | MDD hereditary energy flux | §10.3 | 2-3 weeks | 3b-4 |
| 3b-6 | Nonlocal integral-form energy flux | §10.3 | 2-3 weeks | 3b-5 |
| 3b-7 | GN II/III energy flux | §10.3 | 1-2 weeks | 3b-6 |
| 3b-8 | Electrical energy flux (piezoelectric) | §5.3 | 1 week | EQ-007 |

### 3b.2 Output location

`mathematics/derivations/` — one file per derivation:
- `ls_energy_flux.md`
- `dpl_energy_flux.md`
- `tpl_energy_flux.md`
- `mgt_energy_flux.md`
- `mdd_hereditary_flux.md`
- `nonlocal_integral_flux.md`
- `gn_energy_flux.md`
- `electrical_flux.md`

### 3b.3 Entry criteria for Phase 3c

All 8 derivations completed and documented in `mathematics/derivations/` before Section 10 writing begins.

---

## 4. Phase 3c — Version A Manuscript Writing

### 4.1 Writing schedule (target: 60-90 pages)

| Month | Activity | Sections | Est. pages |
|-------|----------|----------|------------|
| M1 | Front matter + §1-2 | Title, abstract, notation, acronyms, scope, literature strategy | 9 |
| M2 | §3-4 | Foundations, thermoelastic theories | 27 |
| M3 | §5-7 | Multiphysics continua, transport, nonlocal | 33 |
| M4 | §8-10 | Methods, interfaces, energy | 35 |
| M5 | §11-12 | Advanced, comparative synthesis | 25 |
| M6 | §13-17 | Applications, taxonomy, challenges, future, conclusions | 36 |
| M7 | Figures and tables | Create Priority 1 and 2 figures/tables | — |
| M8 | References + review | Compile references; self-review | 10 |
| M9 | Quality control | Seven-perspective audit (Deliverable 15) | — |
| M10 | Presubmission + submit | Journal inquiry; submission | — |

**Total writing: 6 months; Total to submission: 10 months**

### 4.2 Writing standards (Directive §17)

| Standard | Implementation |
|----------|---------------|
| Formal academic English | No contractions; precise terminology |
| No exaggeration | Avoid "groundbreaking," "revolutionary," "first-ever" |
| Coherent argument | Each section has introduction, body, summary |
| Equations through physical meaning | Introduce equation, state it, interpret it |
| Concise section summaries | 2-3 paragraphs at end of each major section |
| Tables/figures independently interpretable | Captions self-contained |
| No repetitive novelty claims | Novelty stated once in introduction and conclusions |

---

## 5. Phase 3d — Submission Strategy

### 5.1 Journal priority order

| Priority | Journal | Version | Reason |
|----------|---------|---------|--------|
| 1 | JMPS | A | Premier mechanics journal; strong fit |
| 2 | IJSS | A | Strong mechanics fit; broad readership |
| 3 | Wave Motion | A | Wave propagation focus |
| 4 | CMT | A | Thermodynamics focus; targeted audience |
| 5 | Royal Society A | B (if invited) | Prestigious; comprehensive treatment |

### 5.2 Presubmission inquiries

Send to JMPS and IJSS editors simultaneously (Month 4.5 of writing schedule).

**Inquiry template** (from `phase3/12_journal_suitability_comparison.md` §6).

### 5.3 Submission decision matrix

| Outcome | Action |
|---------|--------|
| JMPS accepts | Submit Version A to JMPS |
| JMPS declines; IJSS accepts | Submit Version A to IJSS |
| Both decline; CMT accepts | Submit Version A to CMT |
| All Tier 1/2 decline | Prepare Version B; approach Royal Society A |
| Royal Society A also declines | Consider special issue or monograph |

---

## 6. Phase 3e — Version B Fallback (IF NEEDED)

### 6.1 When to trigger

- All Tier 1 and Tier 2 journals decline Version A
- Or target journal requests expanded treatment

### 6.2 Expansion plan

| Component | Version A | Version B | Additional effort |
|-----------|-----------|-----------|-------------------|
| Main text | 60-90 pages | 100-150 pages | 4-6 months |
| Figures | 10-15 | 25-40 | 2-3 months |
| Tables | 8-10 | 14-16 | 1 month |
| References | 150-200 | 300-400 | 1 month |
| Appendices | Minimal | Full (A-F) | 1-2 months |

**Total additional effort: 8-12 months**

---

## 7. Resource Requirements

### 7.1 Personnel

| Role | Responsibility | Time commitment |
|------|---------------|-----------------|
| Lead author | Writing, synthesis, coordination | 100% during writing phase |
| Mathematical auditor | Equation verification (Perspective 1) | 10% during writing |
| Continuum mechanics auditor | Physical validity (Perspective 2) | 10% during writing |
| Thermodynamics auditor | Energy/dissipation (Perspective 3) | 10% during writing |
| Figure creator | TikZ/SVG illustrations | 20% during months 7-8 |
| Reference manager | Bibliography maintenance | 5% throughout |

### 7.2 Software and tools

| Tool | Purpose | Status |
|------|---------|--------|
| LaTeX (TeX Live) | Manuscript preparation | Available |
| TikZ/PGFPlots | Figure creation | Available |
| Python | Validation scripts | Available |
| BibTeX | Reference management | Available |
| Git | Version control | Available (arena/40393d9f-le) |

### 7.3 Computing

| Resource | Purpose | Status |
|----------|---------|--------|
| Local workstation | Writing, compilation | Available |
| Git repository | Version control, backup | arena/40393d9f-le |
| No numerical computation needed | All derivations analytical | N/A |

---

## 8. Risk Management

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Energy flux derivations take longer than expected | HIGH | HIGH | Start derivations immediately; parallelize where possible |
| Journal rejects review article | MEDIUM | HIGH | Presubmission inquiries; Version B fallback |
| Key paper paywalled | HIGH | MEDIUM | Cite from metadata; flag as limitation |
| RG citation cap difficult to maintain | LOW | MEDIUM | Track citations per section during writing |
| Length exceeds journal limit | MEDIUM | MEDIUM | Compression strategies ready (Deliverable 13) |
| Reviewer requests additional derivations | MEDIUM | MEDIUM | Mathematics/derivations/ directory ready |

---

## 9. Success Criteria

### 9.1 Milestone completion criteria

| Milestone | Completion criterion |
|-----------|---------------------|
| Phase 3a | All 16 deliverables completed (DONE) |
| Phase 3b | 8 energy flux derivations documented |
| Phase 3c | Version A manuscript complete (60-90 pages) |
| Phase 3d | Manuscript submitted to target journal |
| Phase 3e | Version B prepared (if needed) |

### 9.2 Quality criteria (from Deliverable 15)

| Criterion | Target |
|-----------|--------|
| All 30 pre-submission checks passed | 100% |
| Seven-perspective audit completed | All 7 perspectives |
| No adversarial language | 0 instances |
| All equations verified or flagged | 100% |
| All figures have source files | 100% |

### 9.3 Timeline criteria

| Milestone | Target | Status |
|-----------|--------|--------|
| Phase 3a complete | 2026-10-21 | COMPLETED |
| Phase 3b complete | 2026-12-21 | PENDING |
| Version A complete | 2027-04-21 | PENDING |
| Submission | 2027-06-21 | PENDING |

---

## 10. Directory Structure for Manuscript

```
manuscript/
├── main.tex              # Master LaTeX file
├── front/
│   ├── title.tex
│   ├── abstract.tex
│   ├── notation.tex      # Table 1
│   └── acronyms.tex      # Table 2
├── sections/
│   ├── sec01_scope.tex
│   ├── sec02_literature.tex
│   ├── sec03_foundations.tex
│   ├── sec04_thermoelastic.tex
│   ├── sec05_multiphysics.tex
│   ├── sec06_transport.tex
│   ├── sec07_nonlocal.tex
│   ├── sec08_methods.tex
│   ├── sec09_interfaces.tex
│   ├── sec10_energy.tex
│   ├── sec11_advanced.tex
│   ├── sec12_synthesis.tex
│   ├── sec13_applications.tex
│   ├── sec14_taxonomy.tex
│   ├── sec15_challenges.tex
│   ├── sec16_future.tex
│   └── sec17_conclusions.tex
├── figures/
│   ├── tikz/
│   └── svg/
├── tables/
├── references.bib
└── appendices/
    ├── appA_equation_register.tex
    ├── appB_balance_derivations.tex
    ├── appC_benchmarks.tex
    ├── appD_figure_specs.tex
    ├── appE_table_specs.tex
    └── appF_reproducibility.tex
```

---

## 11. Immediate Next Actions

| Priority | Action | Owner | Due |
|----------|--------|-------|-----|
| 1 | Commit Phase 3 deliverables to branch | Author | 2026-10-21 |
| 2 | Push to origin | Author | 2026-10-21 |
| 3 | Begin LS energy flux derivation | Author | 2026-11-01 |
| 4 | Create figures/tikz/ directory | Author | 2026-11-01 |
| 5 | Send presubmission inquiry to JMPS | Author | 2027-02-21 |

---

**Next:** Commit Phase 3 deliverables and push to branch `arena/40393d9f-le`.
