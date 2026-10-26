# Manuscript Architecture — Phase 1

**Prepared:** 2026-10-21  
**Status:** Architecture only — no manuscript text drafted  
**Scope:** 18 sections + appendices, ~12,000–15,000 words + 25–40 figures

---

## 1. Section Architecture

| Sec | Title | Approx. words | Figures | Tables | Key content |
|-----|-------|--------------|---------|--------|-------------|
| 1 | Introduction | 1,200 | 3 | 0 | Problem statement, gap, objectives |
| 2 | Historical development | 1,000 | 2 | 1 | Theory lineage, researcher corpus |
| 3 | Review methodology | 1,000 | 1 | 2 | Search, screening, extraction |
| 4 | Fundamental continuum principles | 1,000 | 3 | 1 | Balance laws, thermodynamics |
| 5 | Mathematical foundations of energy transport | 1,200 | 3 | 2 | Energy flux formulations |
| 6 | Generalized thermoelastic theories | 1,500 | 2 | 2 | LS, GL, GN II/III, DPL, TPL, MGT, MDD |
| 7 | Coupled multiphysics formulations | 1,000 | 1 | 1 | Piezoelectric, poroelastic |
| 8 | Wave dispersion, propagation, attenuation | 1,000 | 3 | 0 | Dispersion curves, attenuation maps |
| 9 | Interface and boundary theories | 1,000 | 3 | 1 | Boundary conditions, scattering matrix |
| 10 | Reflection and transmission formulations | 1,200 | 2 | 1 | Energy-partition taxonomy |
| 11 | Energy flux and thermodynamic consistency | 1,200 | 2 | 1 | Limiting cases, model assumptions |
| 12 | Original multidimensional taxonomy | 1,000 | 2 | 1 | 5-axis taxonomy application |
| 13 | Comparative critical synthesis | 1,500 | 3 | 2 | Literature evolution, contradictions |
| 14 | Model limitations and contradictory findings | 1,000 | 2 | 0 | Open problems, synthesis |
| 15 | Emerging mathematical challenges | 800 | 1 | 0 | Unsolved problems |
| 16 | Benchmark architecture | 500 | 0 | 1 | Proposed benchmarks BM-1 to BM-5 |
| 17 | Future research roadmap | 500 | 1 | 0 | Research priorities |
| 18 | Conclusions | 600 | 0 | 0 | Summary, implications |
| **Total** | | **~17,000** | **~27** | **~14** | |

---

## 2. Figure Plan

Approximately 25–40 original figures as specified in `14_figure_blueprint.md`. Highest priority:

- **F5.1** — Generalized energy-balance framework (central mathematical figure)
- **F9.1** — Incident/reflected/transmitted modal geometry (interface setup)
- **F10.1** — Energy-partition taxonomy (core conceptual contribution)
- **F11.2** — Model assumptions comparison (critical synthesis)

---

## 3. Technical Coherence

| Requirement | Status | How addressed |
|-------------|--------|---------------|
| Balance laws documented | Draft | Section 4 |
| Constitutive relations by theory | Draft | Sections 5–7 |
| Energy flux formulations | Draft | Section 5 |
| Interface boundary conditions | Draft | Section 9 |
| Limiting cases specified | Draft | Section 11 |
| Benchmark problems specified | Draft | Section 16 |
| Symbolic verification plan | Draft | `13_mathematical_verification_plan.md` |

---

## 4. Writing Order (Recommended)

1. Section 3 (methodology) — foundation for all claims
2. Section 4 (balance laws) — mathematical foundation
3. Section 5 (energy transport) — core contribution
4. Sections 6–8 (theories, coupling, waves) — literature synthesis
5. Sections 9–10 (interfaces, reflection/transmission) — core application
6. Section 11 (energy flux, thermodynamic consistency) — core contribution
7. Section 12 (taxonomy) — original classification
8. Sections 13–14 (synthesis, limitations) — critical analysis
9. Sections 1–2 (introduction, history) — written last
10. Sections 15–18 (challenges, benchmarks, future work, conclusions) — final

---

## 5. Risks and Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| Full-text access limited | Cannot verify energy-flux claims | Explicitly label metadata-only claims; classify as unverified |
| Novelty claim unconfirmed | Review may duplicate existing work | Family F searches; citation chasing; conservative framing |
| Mathematical derivation errors | Undermines credibility | Symbolic verification plan; independent check planned |
| Citation inflation | Overstates impact | OpenAlex snapshots only; no Scholar metrics; no estimates |
| Reviewer skepticism about gap | Challenge to central claim | Document search methodology; acknowledge limitations |

---

## 6. Stop Condition

Do NOT draft full manuscript text until:

- Energy-flux derivations are documented (Milestone E)
- Literature mapping is complete (Milestone C)
- Conservation check is attempted on representative papers
- Readiness threshold is explicitly documented
