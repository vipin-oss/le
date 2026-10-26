# Recommended Research Direction

**Prepared:** 2026-10-21 · **Evidence cut-off:** 2026-10-21
**Status:** Phase 0 complete — recommendation only; no review article written.

---

## 1. Recommendation (one paragraph)

**Pursue Topic T1:** a review of energy flux and energy-ratio partitioning at interfaces of
generalized thermoelastic, piezoelectric and poroelastic media. It has the highest weighted score
(4.37 / 5.00) on the decision matrix ([`topic_comparison_matrix.csv`](topic_comparison_matrix.csv)),
ranks first under every sensitivity variant tested (equal weights, no author-fit, doubled gap
weight, saturation-neutral), and targets the largest verified gap: zero located reviews synthesize
energy-flux definitions and conservation across dissipative, memory-dependent, nonlocal,
multiphysics interfaces.

---

## 2. Transparent rationale

| Criterion | T1 score | Why |
|---|---|---|
| Gap size | 5/5 | Zero reviews located on interface energy flux; theory reviews (Chandrasekharaiah, Shakeriaski) stop at bulk media. |
| Review saturation | 5/5 | Zero located reviews with piezo-thermoelastic + interface; absence recorded as database absence, not proof. |
| Mathematical depth | 5/5 | Explicit governing equations, secular determinants, energy identities — appropriate for mechanics-thermodynamics venues. |
| Primary literature | 5/5 | ≥7 corpus energy-ratio papers + 686 reflection/thermoelastic and 1,036 nonlocal/thermoelastic works (OpenAlex counts). |
| Author-programme fit | 5/5 | Researcher's own multi-year energy-ratio series (elastic/piezo/thermo/porous/viscoelastic) is the closest match of any topic. |
| Differentiation | 5/5 | Shifts from theory review (existing) to interface conservation law (new); not a retitle. |
| Original taxonomy | 5/5 | 4-way E1–E4 energy-partitioning taxonomy crossed with dissipation × bonding classes. |
| Diagram opportunity | 5/5 | Sankey energy flows, flux decision tree, conservation audit table — original synthesis assets. |
| Journal fit | 4/5 | Applied Mechanics Reviews and Continuum Mechanics and Thermodynamics have verified review scope. |
| Long-term relevance | 5/5 | Energy conservation is foundational and time-independent. |
| Feasibility | 4/5 | Corpus is large but bounded by the interface+energy scope. |
| Self-referentiality risk | -4/5 | Researcher's own series dominates energy ratios; mitigated by independent sampling (see risk register). |

Scores are **ordinal analyst judgements on a 0–5 scale**, not measurements. Weighted score = 4.37;
next-best T2 = 3.53. Margin ≈ 0.84 points, robust across all four sensitivity variants.

---

## 3. Article architecture (proposed, not drafted)

1. **Introduction** — why interface energy matters; limitations of classical Fourier-coupled energy
   bookkeeping; scope and inclusion criteria.
2. **Theoretical foundations** — balance laws; heat-conduction hierarchy (LS, GL, GN II/III, DPL,
   TPL, MGT, MDD, fractional); piezoelectric/piezomagnetic/flexomagnetic coupling; porosity
   theories; nonlocal elasticity.
3. **The energy-flux problem** — what a flux functional must satisfy; why `q·n + σ·u˙ + D·E˙`
   fails under hyperbolic, nonlocal, memory-dependent, or imperfectly bonded conditions.
4. **Interface conditions and mode coupling** — perfect vs imperfect bonding; displacement,
   traction, temperature, heat flux, potential, electric displacement, pore pressure continuity.
5. **Energy ratios: computation and conservation** — amplitude-ratio → energy-ratio pipeline; do
   published ratios sum to unity?; conservation audit table of the corpus.
6. **Taxonomy** — E1–E4 energy-partitioning classes × dissipation × bonding; defining identity per
   cell.
7. **Open problems** — nonlocal flux, hyperbolic thermal flux, imperfect-bond storage, fractional
   instantaneous flux.
8. **Directions for future work** — experiments, numerical validation, open datasets.

Target length: 8,000–12,000 words; 10–15 figures/tables; 150–250 references. These are planning
figures, not commitments.

---

## 4. Risk register

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Self-referentiality (own series dominates) | Medium | High | Independently sampled corpus; own work = one contribution; declare in methodology. |
| No consensus flux exists | High | Medium | Frame review as proposing and comparing candidate flux functionals, not settling the issue. |
| Absence of located reviews ≠ none exist | Medium | Medium | Phrase as "no review located in OpenAlex/Crossref"; verify against Scopus/WoS in Phase 1. |
| High equation density limits readership | Low | Medium | Target mechanics-thermodynamics venues; add conceptual summaries and figures. |
| Citation counts drift / are young | Medium | Low | Report as snapshots with access dates; never promise impact. |
| Journal desk-rejects as too narrow | Low | Medium | AMR and CMT explicitly publish review articles; prepare tier-2 fallback (J. Thermal Stresses, MAMS). |

---

## 5. Kill criteria (stop if any is true in Phase 1)

1. A full-text systematic search finds an existing review that *already* synthesizes energy-flux
   definitions and conservation across dissipative/nonlocal/multiphysics interfaces — T1 would then
   be a duplicate, not a gap.
2. Phase-1 sampling shows the energy-ratio literature is almost entirely the researcher's own
   series, making an independent synthesis impossible without self-citation dominance.
3. No suitable venue confirms review scope for the topic after checking AMR, CMT, J. Thermal
   Stresses, MAMS, and Mathematics and Mechanics of Solids.

---

## 6. Immediate next steps (Phase 1)

1. Register a scoping-review protocol (search strategy, databases, inclusion/exclusion criteria).
2. Execute full-text search in Scopus/Web of Science/Compendex to confirm or refute the T1 gap.
3. Sample the primary corpus independently of the researcher's own co-authorship network.
4. Draft the energy-flux definitions and test them against 3–5 representative interface papers.
5. Contact target-journal editors to confirm review scope before writing.

---

## 7. Verification standard

All claims traceable to [`source_verification_log.csv`](source_verification_log.csv) and
[`search_log/queries.csv`](search_log/queries.csv). Scores are analyst judgements; citation counts
are OpenAlex/Crossref snapshots accessed 2026-10-21. No citation count is presented as a promise of
future impact.
