# Phase 0 — Research Domain Identification and Landmark Review Opportunity Assessment

**Status:** Phase 0 complete. No review article has been written.
**Session date:** 2026-10-21 (UTC)
**Working branch:** `arena/40393d9f-le`

---

## 1. What this repository is

This is a reproducible Phase 0 research workspace for planning a theoretically deep review article
aligned with the verified research programme of **Vipin Gupta** (Department of Mathematics,
Gurugram University, India; ORCID [0000-0002-5238-1963](https://orcid.org/0000-0002-5238-1963)).

The workspace does four things:

1. **Resolves the researcher's identity** against homonyms and documents what can and cannot be verified.
2. **Maps the research landscape** (history, foundational theories, methods, competing views, maturity).
3. **Audits existing reviews** to measure saturation rather than assert novelty.
4. **Proposes and ranks five review topics**, recommending one with a transparent, sensitivity-tested rationale.

## 2. Headline finding

The verified corpus is a coherent, unusually concentrated programme on **wave propagation and
reflection–transmission in multiphysics continua**: generalized thermoelasticity, piezoelectric and
piezothermoelastic coupling, porosity (voids, single and double porosity), semiconductor
photo-thermo-elasticity, nonlocal/size effects, and memory-dependent or fractional heat transport.

The strongest under-served intersection is **energy-flux partitioning at interfaces** — the
bookkeeping of how incident wave energy is distributed among reflected and transmitted modes across
coupled mechanical, thermal, electrical, and pore-fluid channels. The corpus contains at least seven
papers explicitly on energy ratios; the landscape contains no dedicated synthesis of the concept.
The recommended topic is therefore **T1** (see [`recommended_research_direction.md`](recommended_research_direction.md)).

> This is a *bibliometric and scope-based* judgement. It is not a prediction of citations, impact, or
> acceptance, and it is not a claim that the topic is "novel" merely because no review with that title exists.

## 3. Deliverables

| # | File | Contents |
|---|------|----------|
| 1 | [`research_profile.md`](research_profile.md) | Verified identity, metrics, venues, themes, methods, collaborators, unverifiable items |
| 2 | [`domain_taxonomy.md`](domain_taxonomy.md) | Five-axis domain taxonomy, history, foundational theories, governing equations, methods, maturity |
| 3 | [`existing_review_analysis.md`](existing_review_analysis.md) | Verified review inventory, saturation map, gap statements, differentiation logic |
| 4 | [`five_candidate_topics.md`](five_candidate_topics.md) | Five fully specified review topics (13 required elements each) |
| 5 | [`topic_comparison_matrix.csv`](topic_comparison_matrix.csv) | Weighted decision matrix with per-criterion evidence and ranks |
| 6 | [`recommended_research_direction.md`](recommended_research_direction.md) | Recommendation, sensitivity analysis, article architecture, risk register, kill criteria |
| 7 | [`source_verification_log.csv`](source_verification_log.csv) | Every cited source: DOI, verification method, access date, verified fields, status |

### Supporting material

| Path | Purpose |
|------|---------|
| [`search_log/queries.csv`](search_log/queries.csv) | Reproducible log of every database query executed in this session |
| [`data/publications_verified.csv`](data/publications_verified.csv) | Work-level record for the 49 ORCID-linked publications with OpenAlex citation counts |
| [`data/review_inventory.csv`](data/review_inventory.csv) | Machine-readable version of the review inventory |
| [`figures/fig1_taxonomy_map.svg`](figures/fig1_taxonomy_map.svg) | Original five-axis domain taxonomy diagram |
| [`figures/fig2_saturation_map.svg`](figures/fig2_saturation_map.svg) | Review-saturation heat map across the five candidate topics |
| [`scripts/validate_workspace.py`](scripts/validate_workspace.py) | Offline integrity checks (DOIs, CSV schemas, cross-file consistency) |
| [`Makefile`](Makefile) | `make validate` |

## 4. Reproducibility

Every quantitative claim in this workspace is either (a) a field returned by the OpenAlex or
Crossref API, (b) a page retrieved from a publisher or registry, or (c) an explicitly labelled
analyst judgement.

- **Search queries:** recorded verbatim in `search_log/queries.csv`, with the full request URL,
  filters, and result counts.
- **Source records:** recorded in `source_verification_log.csv` with DOI, retrieval endpoint,
  access date, which fields were verified, and a status flag.
- **Offline checks:** `python3 scripts/validate_workspace.py` verifies schemas, DOI syntax,
  duplicate IDs, and that every source referenced in the matrix exists in the verification log.

**Network limitation.** In this sandbox, outbound HTTP from the shell was restricted; OpenAlex,
Crossref, ORCID and publisher pages were retrieved through the agent's page-fetch tool, not through
`curl`. The exact request URLs are preserved so the queries can be replayed from any networked
environment. Citation counts are snapshots and will drift.

**What was not done.** No full-text systematic review was executed. No PRISMA flow diagram is
claimed. Abstract- and metadata-level evidence is labelled as such throughout. Citation counts are
reported as database snapshots, not as impact estimates.

## 5. Integrity rules used in this workspace

1. No citation, author, DOI, result, or journal metric is invented.
2. Every DOI in a deliverable resolves to a record in `source_verification_log.csv`.
3. Verified facts, database snapshots, inferences, and hypotheses are labelled separately
   (`VERIFIED`, `SNAPSHOT`, `INFERRED`, `HYPOTHESIS`).
4. Absence of a review in a database is reported as *absence of evidence in that database*,
   never as proof that no such review exists.
5. No future citation counts, impact factors, or acceptance probabilities are promised.
6. Journal scope statements are quoted only where the publisher page was actually retrieved;
   otherwise the status is marked `PARTIAL` or `NOT VERIFIED`.
7. Where the Google Scholar profile was inaccessible, that is stated, and Scholar metrics are not quoted.

## 6. How to read the recommendation

Start with [`recommended_research_direction.md`](recommended_research_direction.md) §2 for the
one-page rationale, then use [`topic_comparison_matrix.csv`](topic_comparison_matrix.csv) for the
criterion-level evidence. The matrix is a **decision aid**, not a measurement: scores are ordinal
analyst judgements on a 0–5 scale, with the rationale written next to each score.

## 7. Scope discipline

Phase 0 stops here. The next phase would be a protocol-registered scoping review and full-text
coding of the primary corpus. No section of the review article itself has been drafted.
