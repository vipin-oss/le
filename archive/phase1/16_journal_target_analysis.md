# Journal Target Analysis — Phase 1

**Prepared:** 2026-10-21  
**Status:** Partial — verified scope and metrics for primary targets; partial fit for others  
**Evidence standard:** `VERIFIED` (publisher pages) / `SNAPSHOT` (OpenAlex source metrics) / `PARTIAL` (publisher page partially fetched)

---

## 1. Target Journal Candidates

| # | Journal | Publisher | JIF (year) | h-index (OpenAlex) | Scope match | Fit | Status |
|---|---------|-----------|------------|-------------------|-------------|-----|--------|
| 1 | Applied Mechanics Reviews | ASME | Not individually verified | 206 | Solid mechanics, heat transfer, dynamics, biomechanics | STRONG | Verified scope page fetched |
| 2 | Continuum Mechanics and Thermodynamics | Springer | 3.0 (2025) | 124 | Continuum mechanics, thermodynamics, multiphysics | STRONG | Verified scope page fetched; invites review articles |
| 3 | Journal of Thermal Stresses | Taylor & Francis | Not verified | 124 | Thermal stresses, generalized thermoelasticity | GOOD | Prepared; page not fetched |
| 4 | Mathematics and Mechanics of Solids | SAGE | Not verified | 82 | Solid mechanics, mathematical methods | GOOD | Prepared; page not fetched |
| 5 | Heat and Mass Transfer (or Int. J. Heat Mass Transfer?) | Springer/Elsevier | Not verified | 89 | Heat transfer; HFF check partial | PARTIAL | Publisher page partially fetched |
| 6 | Mechanics of Time-Dependent Materials | Springer | Not verified | 86 | Time-dependent materials, memory effects | MODERATE | Prepared; page not fetched |

**Note:** HFF (Heat and Mass Transfer) scope verification is partial — the publisher page was not fully fetched. Fit assessment for HFF is preliminary.

---

## 2. Top Target: Applied Mechanics Reviews (AMR)

**Publisher:** ASME  
**Type:** Review journal  
**Scope (verified):** Solid mechanics, heat transfer, dynamics, biomechanics — publishes comprehensive review articles  
**h-index:** 206 (OpenAlex, 2026-10-21)  
**Fit:** STRONG — AMR publishes review-length articles on thermoelasticity and solid mechanics  
**Scope page:** https://www.asme.org/publications-submissions/journals/find-journal/applied-mechanics-reviews (fetched)

**Considerations:**
- Review journal — appropriate for a comprehensive synthesis
- High prestige (h206)
- No article processing charge information verified

---

## 3. Second Target: Continuum Mechanics and Thermodynamics (CMT)

**Publisher:** Springer  
**JIF:** 3.0 (2025)  
**h-index:** 124 (OpenAlex, 2026-10-21)  
**Scope (verified):** Continuum mechanics, thermodynamics; features invited review articles; hybrid OA  
**Scope page:** https://link.springer.com/journal/161 (fetched)  
**Fit:** STRONG — directly matches multiphysics interface thermoelasticity topic  
**Considerations:**
- Hybrid OA (article processing charge possible)
- Invited review articles — may require invitation or strong pre-submission inquiry

---

## 4. Alternative Targets

| Journal | Fit | Rationale |
|---------|-----|-----------|
| Journal of Thermal Stresses | GOOD | Direct thematic match; publishes generalized thermoelasticity |
| Mathematics and Mechanics of Solids | GOOD | Mathematical mechanics focus; suitable for energy-flux derivations |
| Mechanics of Time-Dependent Materials | MODERATE | Memory/MDD focus; narrower scope |

---

## 5. Journal Selection Criteria

| Criterion | Weight | Rationale |
|-----------|--------|-----------|
| Review scope | 0.25 | Must publish review/synthesis articles |
| Thematic fit | 0.20 | Must cover thermoelasticity/multiphysics interfaces |
| Prestige/impact | 0.15 | h-index, JIF where available |
| OA policy | 0.10 | Hybrid vs gold vs subscription |
| Accessibility | 0.10 | OpenAlex coverage, indexing |
| Submission feasibility | 0.10 | Unsolicited reviews accepted? |
| Cost | 0.10 | APC where applicable |

---

## 6. Next Steps

1. Fetch full scope pages for JTS, MAMS, HFF, MTDM
2. Verify JIF values for each journal (not all individually verified)
3. Check unsolicited review submission policy for each
4. Contact editors of top two targets for pre-submission inquiry
5. Record all findings in `source_verification_log.csv`
