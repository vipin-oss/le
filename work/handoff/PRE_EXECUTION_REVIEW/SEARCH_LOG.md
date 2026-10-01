# Search log — pre-execution published-journal/benchmark screen

Date: 30 September 2026. User authorized published-journal/reference inspection before execution and supplied FINAL MASTER PROMPT v2.1. This screen does not confirm novelty or complete a formal closest-five investigation.

## Exact queries (no external filters)

1. `"New insights on generalized heat conduction and thermoelastic coupling models" pdf`
2. `"generalized thermoelasticity" "circular cavity" "analytical" "International Journal of Heat and Mass Transfer"`
3. `"generalized thermoelasticity" "benchmark" "analytical solution" "thermal shock"`
4. `"Ga2O3" "thermal conductivity tensor" "300" "1275"`
5. `"Bagri" "Eslami" "2007" "1325" thermoelasticity`
6. `"Transient heat conduction in a medium with two circular cavities" pdf`
7. `"Klimm" "2200204" pdf`
8. `"Applied Mathematics and Mechanics English Edition" "Science Citation Index Expanded" quartile 2025`
9. `"International Journal of Heat and Mass Transfer" "2025" quartile SCIE`
10. `"International Journal of Mechanical Sciences" site:scimagojr.com/journalsearch.php`
11. `"Jiang" "232105" "049902" erratum`
12. `"Erratum" "Three-dimensional anisotropic thermal conductivity tensor"`
13. `site:scimagojr.com/journalsearch.php "International Journal of Heat and Mass Transfer" "SJR 2025"`
14. `site:scimagojr.com/journalsearch.php "Applied Mathematics and Mechanics" "SJR 2025"`
15. `"A unified generalized thermoelasticity; solution for cylinders and spheres" "10.1016"`
16. `site:link.springer.com/journal/10483 "Science Citation Index Expanded"`
17. `site:sciencedirect.com/journal/international-journal-of-heat-and-mass-transfer/about/insights "Science Citation Index Expanded"`
18. `site:sciencedirect.com/journal/international-journal-of-mechanical-sciences/about/insights "Science Citation Index Expanded"`

Queries 16–18 returned no search results. The corresponding publisher pages had already been retrieved directly and contained indexing lists; no-result search output does not invalidate those directly inspected pages.

## Retained source roles

- Huang et al. 2025, DOI10.1007/s10483-025-3280-7: recent-model anchor. Metadata/abstract verified; exact equations/BCs not inspected.
- Bagri/Eslami2007, DOI10.1016/j.ijmecsci.2007.04.004: candidate coupled cylinder/sphere limit. Publisher preview inspected, not full case reconstruction.
- Gordeliy/Crouch/Mogilevskaya2008, DOI10.1016/j.ijheatmasstransfer.2007.10.021: heat-only classical cavity candidate. Publisher metadata/abstract/introduction preview inspected; full series/examples not obtained.
- Klimm et al. online2022/issue2023, DOI10.1002/crat.202200204: full five-page public PDF retrieved from https://d-nb.info/1274779782/34 and read. Relevant tensor/coordinate/experimental sections inspected in text and rendered pages2–3.
- Jiang et al.2018, DOI10.1063/1.5054573: material reference requiring correction. Publisher parent record and indexed abstract/method excerpts inspected; full main article not audited.
- Jiang et al.2019 Erratum, DOI10.1063/1.5088513: publisher metadata and correction main text inspected, including Eq4 sign correction and updated interpretation/Fig2b.

## Direct journal records inspected

1. https://www.scimagojr.com/journalsearch.php?q=25178&tip=sid — AMM English; 2025 Q1 rows for Applied Mathematics, Mechanical Engineering, Mechanics of Materials.
2. https://www.scimagojr.com/journalsearch.php?q=20448&tip=sid — IJHMT; 2025 Q1 rows for Fluid Flow and Transfer Processes, Mechanical Engineering, Condensed Matter Physics.
3. https://www.scimagojr.com/journalsearch.php?q=50170&tip=sid — IJMS; chunks0–1 included 2025 Q1 rows for Mechanical Engineering and Mechanics of Materials.
4. https://link.springer.com/journal/10483 — scope, SCIE/Scopus indexing list, hybrid model and explicitly labelled2025 JIF.
5. https://www.sciencedirect.com/journal/international-journal-of-heat-and-mass-transfer/about/aims-and-scope and /about/insights — scope, publisher indexing list and publishing options.
6. https://www.sciencedirect.com/journal/international-journal-of-mechanical-sciences/about/insights — publisher indexing list/publishing options; scope also inspected in SCImago.

Quartiles above are SCImago/SJR2025, not JCR. Independent primary Clarivate MJL/current JCR category verification not performed. No final journal selected.

## Access attempts and limits

- Public official AMM alternate URL http://www.amm.shu.edu.cn/EN/Y2025/V46/I8/1533: fetch errorHTTP500. Earlier HTTPS failures are recorded in the prior exploration log. No authentication/paywall bypass attempted.
- Three OpenAlex DOI location lookups returned200: Huang2025, Bagri2007 and Gordeliy2008. No OA PDF location was resolved in this attempt. Responses stored in OPEN_ACCESS_LOCATION_CHECKS.json. This is not proof that no public author copy exists anywhere.
- Klimm main PDF: downloaded successfully, actualPDF5pages; checksum/source in SOURCES/KLIMM_2023_SOURCE.json.
- Supporting file URLs constructed from the publisher-visible filename: Python403 for two case variants; alternate fetch displayed404/errorHTML. No supplement saved/inspected. Publisher metadata confirms a supplement exists; exact retrieval unresolved, not evidence of absence.
- Publisher-linked2019 APL erratum retrieved directly; correction body read. Parsed matrix formatting is compressed, so corrected numerical matrix import is not certified here.

## Exclusions / cautions

- Natural-convection/nanofluid cavity papers: different governing physics; not suitable for the proposed solid-conduction/thermoelastic case.
- A heat-only calculation is not a full coupled stress benchmark.
- Orthotropic axisymmetric disk/cylinder/sphere sources are possible backup references only after frame/BC review; cannot be assumed to represent fixed-Cartesian monoclinic/orthorhombic crystals.
- Nanobeam benchmark hits: geometry and small-scale assumptions differ; do not automatically reuse atomic-scale thicknesses as a physical continuum validation case.
- Third-party journal-metric aggregators had mixed years/values; primary SCImago/publisher records were used instead. Similar-name Chinese/English/Advances journals were distinguished.
- Publication in a reputable venue, another paper's word 'validated', and source-reported agreement are not independent evidence that our unexecuted model is correct.

## Outcome

Verification candidates identified; exact reconstruction not completed. Physical material evidence exists but full new transient thermoelastic validation is not established. No numerical computation or gap confirmation occurred. Stop before execution pending source access, exact direction/evidence-route approval and a scoped plan.
