# SELF-AUDIT CHECKLIST (30 Sep 2026) — AI self-audit; NOT peer review (recorded)

| Item | Status | Evidence |
|---|---|---|
| Pre-registered criteria frozen before outputs | YES | logs/PLAN_FREEZE.json + SCIENTIFIC_ACCEPTANCE_PLAN.md |
| All V-criteria re-earned after operator change | YES | data/VERIFY.json (final) + superseded copies preserved |
| Failed attempts preserved | YES | root CHANGELOG, REJECTED_IDEAS.md, logs/verify_rerun_v3 |
| Negative result reported (H3 strong form) | YES | ANALYSIS.json T2_status NOT-SUPPORTED; manuscript §4.2 |
| Post-hoc analyses labelled exploratory | YES | fig5 + ANALYSIS_EXPLORATORY_SCALING.json labels |
| Degenerate metric replaced + documented | YES | T3 wall→r≈2a probe note |
| Deviations pre-registered | YES | DECISION_LOG D015 (before production outputs) |
| Numbers traceable | YES | data/NUMBERS_AUDIT.csv |
| Deterministic reproduction | YES | double-run IDENTICAL (analysis) |
| Environment + code freeze | YES | ENVIRONMENT.json, CODE_FREEZE.json |
| Copyright respected | YES | no third-party PDFs in RECOVERY; paths/hashes only |
| Physical validation claims | NONE MADE | PHYSICAL_VALIDATION_PLAN.md |
| Limitations disclosed | YES | manuscript §5 + phase docs |
| Independent expert review | RECOMMENDED, NOT DONE | see below |

## What an independent expert should check (recommendation, recorded)
1. Continuum formulation: plane-strain monoclinic blocks + β rows (MATHEMATICAL_FORMULATION.md).
2. Conservative operator derivation & patch identities (src/cg_ops.py vs §3).
2a. Pre-registration integrity: mtime-based check NOT possible in-sandbox (timestamps normalized); session action log attests D015-before-production ordering.
3. Pre-registration integrity (external logs): DECISION_LOG timestamps vs data/PROD/ file mtimes.
4. Whether η_d=0.05 is acceptable for the intended journal's standards.
5. Novelty wording vs the full texts we could not read (R2.3 gate rows at abstract level).
6. Statistical/exploratory labelling of the collapse tests.
AI self-audit cannot substitute for peer review (constraint recorded).
