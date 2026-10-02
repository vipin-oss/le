# Evidence log — initial corpus reading

Checked date: 30 September 2026.

| Claim | Evidence | Status / boundary |
|---|---|---|
| Workbook contains 48 paper records | Loaded nonempty title rows 2–49 with openpyxl; saved source inventory | OBSERVED_INPUT_CONTENTS; not 48 verified publications |
| 47 distinct supplied DOI strings | Exact string deduplication of DOI hyperlinks | OBSERVED_INPUT_CONTENTS; record 47 DOI needs correction |
| Rows/IDs 36 and 41 duplicate a title and DOI | Original workbook values and hyperlinks | OBSERVED_INPUT_DUPLICATE |
| Record 47 correct article DOI is 10.1016/j.jppr.2026.02.007 | Retrieved P47 PDF p.1; publisher record https://www.sciencedirect.com/science/article/pii/S2212540X26000210 | METADATA_CORROBORATED; raw workbook not edited |
| Supplied ZIP contains eight PDFs, not source code | Actual zip central-directory inventory; safe extraction | OBSERVED_INPUT_CONTENTS |
| 12 Crossref metadata retrievals succeeded | Saved JSON records with HTTP 200 and matching titles | METADATA_VERIFIED_CROSSREF for those records only |
| 36 Crossref requests were rate limited | Saved HTTP 429 statuses | UNRESOLVED_ACCESS; does not prove invalid DOI/publication |
| Eight published sample PDFs retrieved | Download records, PDF signatures, parsed pages/checksums | OBSERVED_RETRIEVAL; section-level reading, not full scientific audit |
| Existing publication themes include coupled wave/thermoelastic/nonlocal/smart-material studies | Full inventory plus selected inspected PDF sections | CORPUS_DESCRIPTION; no fresh novelty claim |
| Existing unpublished FEM work covers anisotropic/internal-length/BFS/nonlinear/electromechanical themes | Eight local PDFs, abstracts and selected method/conclusion passages | SOURCE_TEXT_INSPECTED; findings/numbers unreproduced |
| FEM4 benchmark rates partly use source-reported norms | FEM_4_Paper.pdf Sec.4.1, pp.16–17 | SOURCE_TEXT_INSPECTED; recalculated rates are not solver reconstruction |
| FEM5 excludes optional flexoelectric contribution from quantitative results | FEM_5_Paper.pdf abstract and limitations/conclusions | SOURCE_TEXT_INSPECTED; implementation not inspected |
| GK inverse study uses synthetic experiments and no experimental inverse validation | GK_heat_Paper.pdf abstract, Secs.5 and 13 | SOURCE_TEXT_INSPECTED; empirical/model novelty not independently confirmed |
| QC study uses surrogate/composite parameters and configuration-specific electric decoupling | Quasi_crystal_Paper.pdf abstract, Sec.7.9, pp.25–26 | SOURCE_TEXT_INSPECTED; numerical claims not reproduced |
| Torsional draft title page does not list Vipin Gupta | paper_springer.pdf p.1 lists Annu Rani and M. S. Barak | OBSERVED_ATTRIBUTION; relationship awaits user clarification |
| No scientific simulation, code test or reproduction executed in this session | Activity consists of download, metadata inspection, PDF parsing and notes | NOT_RUN for scientific computation |
| Public repository exposure of supplied drafts | GitHub API returned private=false; public URLs downloaded without authentication | OBSERVED_ACCESS_STATUS; confidentiality/access choice belongs to user |

No current journal-quartile claim, comprehensive literature-gap claim, physical-validation pass, runtime benchmark, convergence result or independent reproduction is asserted by this log.
