# Search and retrieval log — initial user-corpus reading

Date: 30 September 2026 (user local date). Scope: inspect user-supplied publications and manuscripts; not a systematic novelty/gap search.

## User-provided inputs

- https://github.com/vipin-oss/BFS-FEM-MATLAB/blob/main/Vipin_Research_Papers_06-Aug_2026.xlsx
- https://github.com/vipin-oss/BFS-FEM-MATLAB/blob/main/FEM_Total.zip

GitHub API file metadata was inspected before downloading. Download provenance and checksums are in `SOURCE_MANIFEST.json`. The repository root was listed only to understand available artifacts. Other code/research archives were not downloaded or executed.

## Exact published-literature web queries

### Q01
- Query: `"10.1038/s41598-023-44339-5"`
- Filter: none.
- Relevant retained results:
  - https://pubmed.ncbi.nlm.nih.gov/37821492
  - https://pmc.ncbi.nlm.nih.gov/articles/PMC10567774/
- Finding: title, DOI, article number and open full-text location for workbook record 2.
- Inspection: PubMed/PMC search excerpts and PMC first content chunk; actual article PDF retrieved and selected sections read locally.
- Related results were not screened as competing novelty evidence.

### Q02
- Query: `"Size-dependent analysis of surface wave in irregular fractured porous seabed"`
- Filter: none.
- Retained source: https://www.tandfonline.com/doi/full/10.1080/15376494.2024.2440131?af=R
- Finding: metadata/abstract corroborates the title and DOI duplicated in workbook records 36 and 41; online date and final issue year should be treated separately.
- Inspection: metadata and abstract from search result; full text not read.

### Q03
- Query: `"Fractal geometry-based Klein-Gordon model for heat and mass transfer"`
- Filter: none.
- Retained publisher source: https://www.sciencedirect.com/science/article/pii/S2212540X26000210
- Finding: publisher DOI `10.1016/j.jppr.2026.02.007`; volume 15, issue 1, pp. 179–196. Workbook record 47 DOI differs. Retrieved PDF first page agrees with publisher source.
- Inspection: publisher metadata/abstract from search output and selected local PDF sections.
- Other hits were not treated as confirmation of any new research gap.

## Crossref metadata retrieval

Endpoint pattern: `https://api.crossref.org/works/{DOI}` for the workbook's supplied DOI strings.

- 48 record requests were attempted.
- 12 returned HTTP 200 and metadata.
- 36 returned HTTP 429; no successful verification is claimed for those responses.
- HTTP 429 means the retrieval was rate limited, not that a DOI/paper is invalid.
- Actual records: `CROSSREF_METADATA_VERIFICATION.json`.

## Selected full-text retrieval

Attempted workbook IDs: 1, 2, 10, 21, 25, 29, 35, 38, 45, 47.

- Retrieved PDF IDs: 1, 2, 25, 29, 35, 38, 45, 47.
- IDs 10 and 21: PDF retrieval unresolved in this attempt.
- Actual locations/checksums/statuses: `PUBLISHED_FULLTEXT_RETRIEVAL.json`.

No unpublished manuscript text or unpublished research question was submitted to a web-search query. PDF parsing and note-taking were local. No Scopus/Web of Science subscription access, exhaustive recent scooping, journal quartile check, full correction/retraction review, code execution or numerical reproduction is claimed.
