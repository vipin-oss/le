# Seven Reviewer Audit — Phase 1

**Prepared:** 2026-10-21  
**Status:** Not started (anticipated reviewer critiques prepared; no actual review conducted)  
**Purpose:** Pre-emptively identify likely reviewer objections and document responses

---

## Reviewer 1 — Novelty and Gap Claim

**Likely objection:** "The claimed gap (no review on interface energy flux) is not established. A broader literature search may reveal existing reviews."

**Evidence available:**
- OpenAlex search slices (12 slices, zero on-target reviews located)
- Type:review classification acknowledged incomplete/noisy
- No backward/forward citation chasing executed yet

**Response plan:**
- Execute Family F alternative-terminology searches
- Execute citation chasing from Chandrasekharaiah 1986/1998 and Shakeriaski 2021
- If access becomes available, search Scopus/Web of Science/Dimensions
- Frame the gap claim as "no on-target review located in searched databases" rather than "no review exists"
- Acknowledge OpenAlex type:review limitations explicitly

**Residual risk:** Moderate — gap claim is the central justification; if an on-target review is found, the novelty argument collapses.

---

## Reviewer 2 — Full-Text Access

**Likely objection:** "Most corpus records are abstract-only. You cannot claim to have analyzed full text."

**Evidence available:**
- 06_fulltext_extraction_matrix.csv: 17 of 18 records abstract-only; RG-003 open access but not yet extracted
- All extraction decisions labeled ABSTRACT_ONLY or NOT_YET_EXTRACTED
- No full-text claims made

**Response plan:**
- Explicitly distinguish metadata screening from full-text extraction
- Extract RG-003 (open access, Scientific Reports) as proof of concept
- Attempt DOI landing pages and institutional repositories for remaining corpus
- Label all abstract-only claims as "metadata-based inference"
- Do not claim to have read any inaccessible full text

**Residual risk:** High — corpus is mostly abstract-only; limits the depth of energy-flux analysis.

---

## Reviewer 3 — Mathematical Rigor

**Likely objection:** "The energy-flux definitions are schematic, not derived from first principles for each theory."

**Evidence available:**
- 07_foundational_theory.md and 08_energy_flux_framework.md contain schematic equations only
- 13_mathematical_verification_plan.md specifies benchmarks but none executed
- No derivations in `mathematics/derivations/` yet

**Response plan:**
- Derive total energy flux for LS theory from first principles
- Derive total energy flux for MGT theory
- Derive nonlocal energy flux (integral form)
- Derive MDD hereditary flux
- Test each against representative interface papers
- Document where unification succeeds and fails

**Residual risk:** High — mathematical framework is the core contribution; schematic-only content is insufficient.

---

## Reviewer 4 — Corpus Bias

**Likely objection:** "The corpus is dominated by one researcher's publication series (Barak/Das/Dutta/Sur/Gupta/Ahmad). This is not a representative literature base."

**Evidence available:**
- OpenAlex co-author grouping: Barak 29, Das 23, Dutta 9, Sur 9, Ahmad 9 joint records with Gupta
- RG-001 through RG-007 all from the same research programme
- Crossref-verified foundational works (FW-001 through FW-011) provide external anchor

**Response plan:**
- Explicitly document corpus bias as a limitation
- Treat each own-series paper as one contribution among many, not as independent evidence
- Expand search beyond own-series authors (Family F alternative terminology)
- Backward/forward citation chasing to find external interface papers
- Frame findings as "within this corpus" rather than "generally in the field"

**Residual risk:** High — corpus bias is a real limitation that cannot be fully mitigated without broader search access.

---

## Reviewer 5 — Citation and Metrics Claims

**Likely objection:** "Citation counts are OpenAlex snapshots only; no cross-database verification; no Scholar metrics."

**Evidence available:**
- All citation counts labeled as OpenAlex snapshots (2026-10-21)
- Google Scholar reCAPTCHA blocked; no Scholar metrics quoted
- Biomedical homonym (ORCID 0000-0002-0607-5543) explicitly excluded
- No citation estimates or promises made

**Response plan:**
- Maintain OpenAlex-only citation claims with explicit source and date
- Do not extrapolate, estimate, or promise future citations
- Cross-check key DOIs via Crossref where feasible
- Document limitations of single-database citation data

**Residual risk:** Low — integrity rules are explicitly followed; risk is mainly perception.

---

## Reviewer 6 — Reproducibility

**Likely objection:** "The search strategy is documented but not executed beyond Phase 0 baseline; no reproducible code provided."

**Evidence available:**
- 03_search_execution_log.csv: 42 Phase 0 baseline records logged
- 02_search_strategy.md: 6 query families A–F with database-specific syntax (prepared but unexecuted)
- search_log/queries.csv: Phase 0 queries logged
- scripts/validate_workspace.py: offline integrity checks

**Response plan:**
- Execute Family F searches (OpenAlex) and log results
- Execute citation chasing and log results
- Add validation scripts: validate_references.py, validate_database.py, validate_equations.py
- Maintain reproducible log format throughout
- Make all search queries and results reproducible

**Residual risk:** Moderate — search execution is partially complete; validation scripts pending.

---

## Reviewer 7 — Scope and Boundaries

**Likely objection:** "The review scope is ambiguous — is it about energy flux, interfaces, multiphysics coupling, or generalized thermoelasticity?"

**Evidence available:**
- 01_registered_protocol_draft.md: RQ1–RQ8, scope and eligibility criteria defined
- Inclusion/exclusion criteria documented
- Kill criteria defined

**Response plan:**
- Maintain explicit RQ1–RQ8 with scope boundaries
- Document eligibility criteria (PICO-style where applicable)
- State kill criteria clearly
- Distinguish in-scope vs out-of-scope topics explicitly
- Update protocol as searches execute (versioned)

**Residual risk:** Low — scope is documented; risk is scope creep during writing.

---

## Summary of Residual Risks

| Risk | Level | Mitigation status |
|------|-------|-------------------|
| Novelty claim unconfirmed | Moderate | Family F searches pending; citation chasing pending |
| Full-text access limited | High | RG-003 extraction planned; metadata-only labeling |
| Mathematical rigor insufficient | High | Derivations not yet executed |
| Corpus bias | High | Documented as limitation; expansion searches pending |
| Citation metrics limited | Low | OpenAlex-only with explicit labeling |
| Reproducibility incomplete | Moderate | Validation scripts pending |
| Scope ambiguity | Low | Protocol documented |

**Overall assessment:** Phase 1 deliverables provide a solid foundation, but the central contributions (energy-flux derivations, conservation checks, broader literature search) remain to be executed before manuscript drafting.