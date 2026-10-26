# Phase 1 — Research Foundation

**Branch:** arena/40393d9f-le  
**Prepared:** 2026-10-21  
**Status:** Phase 1 deliverables 00–18 created; supporting files pending

## Directory structure

```
phase1/
├── 00_phase0_critical_audit.md
├── 01_registered_protocol_draft.md
├── 02_search_strategy.md
├── 03_search_execution_log.csv
├── 04_literature_master_database.csv
├── 05_screening_decisions.csv
├── 06_fulltext_extraction_matrix.csv
├── 07_foundational_theory.md
├── 08_energy_flux_framework.md
├── 09_interface_scattering_theory.md
├── 10_existing_review_saturation.md
├── 11_multidimensional_taxonomy.md
├── 12_research_gap_register.csv
├── 13_mathematical_verification_plan.md
├── 14_figure_blueprint.md
├── 15_manuscript_architecture.md
├── 16_journal_target_analysis.md
├── 17_seven_reviewer_audit.md
├── 18_phase1_final_report.md
└── README.md (this file)

../references/
├── library.bib
├── doi_verification.csv
└── source_provenance.csv

../figures/specifications/   (empty — pending)
../figures/svg/              (empty — pending)
../figures/tikz/             (empty — pending)
../mathematics/derivations/  (empty — pending)
../mathematics/symbolic_checks/ (empty — pending)
../mathematics/benchmarks/   (empty — pending)
../scripts/
├── validate_references.py
├── validate_database.py
└── validate_equations.py
```

## Scientific integrity rules (carried over from Phase 0)

1. Never invent citations, authors, DOIs, results, or journal metrics.
2. Clearly distinguish verified facts from hypotheses.
3. Provide source links and access dates.
4. Do not fabricate a systematic literature search that has not been executed.
5. Maintain a reproducible log of search sources and search queries.
6. Never claim to have read full text when only abstracts or metadata were accessible.
7. Stop after Phase 0; do not write the complete review article.
8. Do not claim a topic is novel merely because its title is different.
9. Do not estimate citation counts without documented basis; do not promise future citations.

## Readiness threshold (NOT YET REACHED)

Do NOT draft full manuscript text until:

1. Energy-flux derivations documented for LS, MGT, nonlocal, MDD media
2. Conservation check (ΣR + ΣT + A = 1) attempted on 3–5 representative papers
3. Broader literature search executed (Family F + citation chasing)
4. Full-text extraction of accessible papers completed
5. Validation scripts created and executed
6. Readiness threshold explicitly documented in 18_phase1_final_report.md

Current status: 0 of 6 conditions met.

## Validation

Run:
```
python3 scripts/validate_references.py
python3 scripts/validate_database.py
python3 scripts/validate_equations.py
```

## Key findings

- **Central gap:** No shared definition of energy flux across dissipative/memory-dependent/nonlocal/multiphysics media
- **Corpus:** 18 seed records (11 foundational + 7 researcher corpus)
- **Full-text access:** 17 abstract-only, 1 open access (RG-003), 0 extracted
- **Novelty claim:** UNCONFIRMED — no on-target review located in OpenAlex, but broader search pending
- **Top venues:** Applied Mechanics Reviews (ASME, h206), Continuum Mechanics and Thermodynamics (Springer, JIF 3.0)
