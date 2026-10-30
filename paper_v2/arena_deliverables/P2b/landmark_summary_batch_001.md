# Landmark literature register - batch 001

## Scope and status

This batch contains ten records: five for thermodynamic admissibility of generalized heat-conduction and thermoelastic models, and five for layered-media/interface waves. Topic 1 comprises Coleman-Gurtin 1967, Gurtin-Pipkin 1968, Chen-Nunziato 1974, and Green-Naghdi 1991 and 1993. Topic 2 comprises Rayleigh 1885, Love 1911, Stoneley 1924, Scholte 1947, and Barnett et al. 1985. The records were selected as foundational primary articles/books, with one metadata-only R1 paper and several R2 papers. No R3 claim is made. Batch 002 was not started.

## Verification counts

- Register rows: 10 total; topic 1: 5; topic 2: 5.
- R2: 6; R1: 3; R1-noDOI: 1; R0 in register: 0.
- Abstracts inspected: 6. Metadata-only/no-abstract records: Gurtin-Pipkin 1968, Rayleigh 1885, Scholte 1947, and Love 1911 (book page description/front matter used instead of an abstract).
- Full text accessible in checked sources: 4 (Green-Naghdi 1991 and 1993 Drive PDFs, Stoneley 1924 Royal Society PDF, Scholte 1947 OUP PDF). No full-text sections were used to claim R3.
- Independence: independent_by_authors 10; own_group 0; unknown 0. Every printed author was compared with all six supplied group names; this is a name-based assessment and does not infer independence from institutions. Author initials are retained where the publisher byline does not expand given names; all listed authors are included, not shortened to et al.

## Duplicate and BibTeX accounting

The duplicate check was read-only against refs.bib, refs_extra.bib, and refs_new.bib inside paper_v2/paper_sources.zip. The archive contained 150, 34, and 141 BibTeX entries, respectively. Duplicate rules used DOI and normalized title. In the match/verify CSV, title_match, doi_match, and full_author_match report confirmation against the opened source record; existing_bibliography_match and duplicate_status report the local duplicate check.

- Green-Naghdi 1991 is a DOI/title duplicate of refs.bib key Green1991.
- Green-Naghdi 1993 is a DOI/title duplicate of refs.bib key Green1993.
- Rayleigh 1885 is a normalized-title duplicate of refs_extra.bib key Rayleigh1885; that existing entry has no DOI.
- The remaining seven records had no DOI or normalized-title match in the three files.
- refs_landmark_batch_001.bib therefore contains seven nonduplicate verified records, each with a unique LM1_ key. It contains no duplicate DOI.

## Source and citation-chain notes

Publisher/journal/society pages were opened for the AIP Coleman-Gurtin article, Springer Gurtin-Pipkin and Chen-Nunziato articles, Royal Society Green-Naghdi, Stoneley, and Barnett articles, OUP Rayleigh and Scholte records, and the Cambridge Love book/reprint. The Green-Naghdi 1991 and 1993 Drive PDFs were searched/read for their first-page citations and abstracts. The Green-Naghdi 1993 PDF reference list was checked and points to the already-registered Green-Naghdi 1991 paper; the Chen-Nunziato Springer reference list includes Gurtin-Pipkin 1968 and Cattaneo 1948. Cattaneo remains an unverified discovery lead and was not registered.

External-page access test: successful for the listed AIP, Springer, Royal Society, OUP citation-export/PDF, and Cambridge sources. Some full-text pages are paywalled. The official GeoscienceWorld page for Haskell's 1953 multilayered-surface-wave paper returned HTTP 403; no direct Drive PDF was identified, so that discovery lead was not promoted into the register or BibTeX. OUP's Rayleigh landing page/PDF was access-restricted, although its publisher citation export was readable. No Crossref access is claimed.

## Limits and unresolved items

- Gurtin-Pipkin 1968 is R1 metadata-only: the Springer page exposes no abstract and full text was not available in the checked sources; no contribution claim is made in the register.
- Love 1911 is a book. The Cambridge publisher page and front matter identify the original 1911 work and a 2015 paperback reprint; the full book was not accessed. The contribution sentence is attributed to the publisher description, not presented as a read abstract.
- Rayleigh 1885 metadata is verified from the OUP citation export, but the article/PDF and abstract were not accessible; it remains in the register as a duplicate of an existing key.
- Scholte 1947 metadata is verified from the OUP citation export and the linked PDF was fetchable, but the extracted text did not expose an abstract. No contribution claim is made.
- Haskell 1953 is an unresolved discovery lead only, not an R0 register row. Its search-result metadata was not treated as evidence.
- No existing .tex, .bib, script, PDF, or Blueprint file was modified; only the five requested P2b deliverables were created. No LaTeX compilation, manuscript-novelty review, or citation changes to main.tex are claimed.

## QA record

- The three CSV headers were read from /tmp/p2b_batch001_headers.txt and used verbatim.
- CSV parsing passed: 10 register rows, 17 evidence rows, and 10 match/verify rows; each header and field count matches the supplied header.
- ASCII-only and control-character scans passed for all five files; no disallowed control characters were found.
- BibTeX validation passed: 7 records, 7 unique LM1_ keys, 6 unique DOI values (the book has no DOI), and balanced braces.
- Branch: arena/06654118-le. Pre-batch HEAD: 2ce39cd85acea410c854f88c326d87b7537df0fb. Merge-base with origin/main: fad98f923e76563e3fe4e8852d85cd68fc7c6fc5. The existing comparison merge-base with origin/review-paper-v2 is 340328c5fc46bc80067c4d7638f6fd73c7bd6257.
