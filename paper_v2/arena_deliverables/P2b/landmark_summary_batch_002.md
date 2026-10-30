# Landmark literature register - batch 002

## Scope and status

This batch contains ten verified records: five for Topic 3 (Biot poroelastic and thermo-poroelastic waves) and five for Topic 4 (viscoelastic and fractional viscoelastic waves, including causality and loss-model dispersion). Topic 3 includes Biot's 1956 low- and high-frequency papers, his 1962 porous-media mechanics/acoustic-propagation paper, Sharma 2008, and Carcione et al. 2019. Topic 4 includes Toll 1956, Futterman 1962, Caputo 1967, Kjartansson 1979, and Koeller 1984. The Caputo record is retained as a verified duplicate of an existing bibliography entry; it is not repeated in the new BibTeX file. Batch 003 was not started.

## Verification counts

- Register rows: 10 total; Topic 3: 5; Topic 4: 5.
- R2: 10; R1: 0; R1-noDOI: 0; R0 in register: 0; R3 claims: 0.
- Abstracts/summaries inspected: 10; Wiley labels the Caputo abstract a Summary. All contribution statements are paraphrases, not pasted text.
- Full text accessible in checked sources: 2. Carcione et al. 2019 is marked Free Access by Wiley/AGU. The OUP-linked Caputo 1967 PDF endpoint returned a signed publisher file, but extraction exposed only the download watermark; no article-body claims were made and the record remains R2. No full text was identified in Drive for the other eight records.
- Independence: independent_by_authors 10; own_group 0; unknown 0. Every printed author was compared by name with Vipin Gupta, M. S. Barak, Soumik Das, Vijayata Pathania, Rajesh Kumar, and Rachaita Dutta. M. D. Sharma was not conflated with M. S. Barak; no independence inference was made from institutions.

## Duplicate and BibTeX accounting

The read-only duplicate check covered refs.bib, refs_extra.bib, and refs_new.bib in paper_v2/paper_sources.zip, plus refs_landmark_batch_001.bib. Counts were 150, 34, 141, and 7 BibTeX entries, respectively. DOI and normalized-title matching was applied.

- Caputo 1967 is an exact DOI and normalized-title duplicate of refs.bib::Caputo1967. The source page uses the historical journal title Geophysical Journal of the Royal Astronomical Society; the existing entry uses the later title Geophysical Journal International.
- The other nine register records have no DOI or normalized-title match in the four checked bibliographies.
- refs_landmark_batch_002.bib contains nine verified, nonduplicate entries with unique LM2_ keys and nine unique DOIs. The duplicate Caputo record is not included; no duplicate DOI is present in the new file.

## Source and citation-chain notes

Publisher/journal pages were opened for all ten records: AIP (Biot 1956 Parts I/II and Biot 1962), Springer (Sharma 2008), Wiley/AGU (Carcione 2019, Futterman 1962, Kjartansson 1979), APS (Toll 1956), Wiley (Caputo 1967), and ASME (Koeller 1984). Abstracts (the Caputo page labels its abstract Summary) and publication metadata were visible on each source page. APS citation export supplied Toll's page range (1760-1770).

The AIP reference list for Biot 1962 cross-checks both 1956 JASA papers. The Springer Sharma page also points back to Biot's 1956 and 1962 work. The verified Drive PDF B13-008__SCSB23.pdf (Santos et al., 2023, "Wave propagation in thermo-poroelasticity: A finite-element approach," Geophysics 88(1), WA161-WA175, DOI 10.1190/GEO2022-0271.1) was read for its first-page metadata, abstract, and references; its reference list includes Sharma 2008, and its discussion cites the Carcione 2019 thermo-poroelastic simulation line. The verified Drive PDF B03-015__10.1080@15397734.2020.1852088.pdf was also checked as a fractional-calculus citation-chain source and cites Koeller 1984. These Drive papers provide discovery/citation context only; target records were verified from the publisher pages.

## Access tests and limits

Web access was re-tested successfully on AIP, Springer, Wiley/AGU, Wiley, APS, and ASME publisher pages. The earlier Futterman DOI-resolver request returned a Wiley verification challenge, but the direct AGU/Wiley page opened and exposed full metadata and the abstract. The Futterman and Kjartansson PDF links returned the abstract pages rather than article text; the AIP, Springer, APS, and ASME full-text pages require purchase, subscription, or authorization. The Caputo publisher PDF endpoint returned a signed file URL but only a watermark was extracted. Carcione et al. 2019 is the only page explicitly marked Free Access. Search-result snippets were treated only as discovery leads. No Crossref source or access is claimed.

This is a literature-register and source-verification batch only. No main.tex citation sentences, manuscript-novelty conclusions, or LaTeX compilation are included. No existing .tex, .bib, script, PDF, or Blueprint file was changed; only the five requested batch_002 deliverables were created. The pre-existing untracked google_drive/ directory was not staged.

## QA record

- The three CSV header lines were copied from /tmp/p2b_batch002_headers.txt and used verbatim.
- CSV parsing passed: 10 register rows, 16 evidence rows, and 10 match/verify rows; each row matches its header field count.
- All five files passed ASCII-only and disallowed-control-character scans.
- BibTeX validation passed: 9 records, 9 unique LM2_ keys, 9 unique DOI values, and balanced braces.
- Branch: arena/06654118-le (active and fixed). No branch was created or switched. Pre-batch HEAD: 500420044d4666b1d4441cdf7ce9bb6ee2e8cd93. Merge-base with origin/main: fad98f923e76563e3fe4e8852d85cd68fc7c6fc5. Merge-base with origin/review-paper-v2: 340328c5fc46bc80067c4d7638f6fd73c7bd6257.
- Exact remote line for origin/review-paper-v2 before the batch:

  `340328c5fc46bc80067c4d7638f6fd73c7bd6257	refs/heads/review-paper-v2`
