# P2-a batch 008 verification summary

## Candidate census and selection

Batch 007 left 14 one-name author-field candidates in the source-order remainder. Batch 008 selected all 14 and completed the final P2-a batch:

`Antaki2000, Quintanilla2008, Quintanilla2009, Chirita2017, Youssef2012, Shaw2019, Quintanilla2020, Biswas2020b, Chirita2012, Singh2020e, Biswas2020c, Abouelregal2011, Singh2013, Singh2015`

**Candidates remaining after batch 008: 0.** No batch 009 work was started.

## Source handling and method

The read-only `paper_v2/paper_sources.zip!refs_new.bib` supplied the original BibTeX fields and line ranges. The three exact CSV header lines copied from batch 001 in `/tmp/p2a_batch008_headers.txt` were used unchanged. Original BibTeX values and publisher observations are separate evidence rows; each observed publisher field has `matches_original` set to `yes` or `no`. Publisher citation exports, article pages, and issue tables were opened for citation metadata and accessible abstracts. No Crossref access is claimed; BibTeX source values were used only as comparison values.

Targeted Google Drive PDF-only DOI searches and exact-title PDF-only searches were used as leads, never as evidence of a match. All eight unique DOI-hit PDFs were opened and ruled out as false leads; additional title-search leads were opened where they appeared to be plausible. No target PDF was confirmed for any of the 14 candidates. Publisher pages supplied the metadata fallback. No Drive file was modified or deleted.

## Verification outcomes

| Level | Count | Meaning |
| --- | ---: | --- |
| R0 | 0 | No unresolved wrong-paper or incomplete-citation records; spelling questions are separately flagged for manual review. |
| R1 | 6 | Complete DOI/citation metadata, but no accessible publisher abstract. |
| R2 | 8 | Complete DOI/citation metadata and a publisher abstract inspected. |
| R3 | 0 | Not assigned. |
| **Total** | **14** | **14 selected records** |

R1 keys: `Antaki2000, Quintanilla2008, Quintanilla2009, Chirita2017, Singh2020e, Biswas2020c`. The AIAA article page for `Antaki2000` was opened for the pending abstract check; it is marked `No Access`, contains no accessible abstract text, and links a first-page preview image that could not be fetched. It remains R1.

R2 keys: `Youssef2012, Shaw2019, Quintanilla2020, Biswas2020b, Chirita2012, Abouelregal2011, Singh2013, Singh2015`.

## Drive PDF leads opened and ruled out

- `Antaki2000`: Drive ID `1W4iv7UQyucwTY0W4rjipQyzg9Xx08kH-` is a different 2025 paper, *Computational assessment of mechanical damage in a thermoelastic rod under hyperbolic two-temperature theory with nonlocal and memory effects* (DOI `10.1177/10567895251380193`).
- `Quintanilla2008`: Drive ID `1O9ciqiS6UN5Cufwe9WT74nbiJCOrRSCZ` is *Spatial behaviour of solutions of the three-phase-lag heat equation*, a different 2009 paper by R. Quintanilla (DOI `10.1016/j.amc.2009.03.005`). `Quintanilla2009` title-search leads `1xDTdw8cOwZ3PcGYkYasbZ99PrxDJDPsf` and `1RF_VFqTMh8iQ7f7OXv32WhJaLvAIr7E8` are unrelated 2020 Abouelregal papers.
- `Quintanilla2020`: DOI lead `1JnoD4gJmGPKBnX-xFEHg_cUcMpokyWAo` is an unrelated 2024 Acta Mechanica Sinica paper (DOI `10.1007/s10409-023-23419-x`). Title-search lead `1a506i3Zsj4K8uZe2CRLIBnTRz0whn8yY` is a different 2019 Mathematics and Mechanics of Solids paper by Ramon Quintanilla (DOI `10.1177/1081286519862007`).
- `Biswas2020b`: DOI leads `1BULnQy0gmttuhTpSr3qVoi7Cy__bxode`, `1nynWgpD_kdKwN49Uf1nCloEZixSH6ji9`, and `1LUPVa0U0g8d_ykqX95rN4w2_ogdPfG0v` are different 2026, 2026, and 2024 papers, respectively. Their first-page DOIs are `10.1007/s10999-026-09892-7`, `10.1108/HFF-11-2025-0930`, and `10.15625/0866-7136/19728`.
- `Chirita2012`, `Singh2020e`, and `Singh2015` also returned `1LUPVa0U0g8d_ykqX95rN4w2_ogdPfG0v`; its first page identifies the same unrelated 2024 Vietnam Journal of Mechanics paper by Baljeet Singh. A title-search lead for `Chirita2012`, `1ko-VpxDcTZUm-dkXkHIMXpZpZTFm3pCe`, is a different 1997 Journal of Thermal Stresses paper by S. B. Sinha and Khaled A. Elsibai (DOI `10.1080/01495739708956095`).
- `Biswas2020c`: DOI lead `1oOEDYn-09sxKcdjp2LEhbLKb6W5VJdFU` is a different 2024 *Physica Scripta* paper by Soumik Das et al. (DOI `10.1088/1402-4896/ad4829`).
- `Abouelregal2011`: DOI leads `1LUPVa0U0g8d_ykqX95rN4w2_ogdPfG0v`, `1zB4nJl6wZrAld9i8VXtQc6_0tvkvwtZM`, and `15iPLa4Dh3-yUJj7iz8nZd1t8fynG1kWa` are different 2024, 2025, and 2024 papers. `1hbErIqUcp-VGX6L_THsI49Nn2LFnngEt` contains the same unrelated 2025 Journal of Thermal Stresses paper as `1zB4...`; that duplicate false lead was not treated as a target match.

For the seven candidates with zero DOI-query hits (`Antaki2000, Quintanilla2008, Quintanilla2009, Chirita2017, Youssef2012, Shaw2019, Singh2013`), exact-title searches were also run. Those results were citation-heavy and did not confirm any target PDF. File names and search snippets were not used to verify identity.

## Citation differences, author spelling, and own-group check

- Printed-year differences: `Chirita2017` (`year differs: bib=2017, printed=2018`); `Chirita2012` (`year differs: bib=2012, printed=2013`); `Singh2020e` (`year differs: bib=2020, printed=2021`); `Biswas2020c` (`year differs: bib=2020, printed=2021`); and `Singh2015` (`year differs: bib=2015, printed=2016`). Online-first dates are recorded separately in notes where the publisher displays them. No printed volume difference was found.
- `Singh2013`: the source BibTeX gives pages `1--6`; the Wiley citation export/current article page labels the journal `International Scholarly Research Notices` while the BibTeX says `ISRN Geophysics`. The publisher citation gives volume 2013, issue 1, and article ID `857937`, with no journal page range displayed. The register follows the publisher citation and records both the journal-title and page-field differences; the historical print-title relationship was not independently resolved. Publisher issue/supplement fields are added where displayed; no numbered issue is inferred where the publisher shows none, and no original BibTeX entry in this batch has an issue field. `Shaw2019` has no original BibTeX pages field; the ASCE publisher citation supplies article ID `04019003`. `Quintanilla2020` uses article ID `100006`, matching the numeric value in the source pages field.
- No unresolved author-spelling discrepancy requires manual review. Publisher spellings for Stan Chirita and Ramon Quintanilla are rendered in ASCII with `diacritics removed`. For `Quintanilla2008`, the publisher citation export provides only `R. Quintanilla`; no given name was inferred. No `et al.` is used for a full author list.
- Every printed byline was compared against Vipin Gupta, M. S. Barak, Soumik Das, Vijayata Pathania, Rajesh Kumar, and Rachaita Dutta. All 14 own-group flags are `no`.

## Deliverables and QA

Created only these four new files under `paper_v2/arena_deliverables/P2a/`:

- `reference_register_batch_008.csv` - 14 selected citation records.
- `reference_evidence_batch_008.csv` - original BibTeX values, publisher observations, abstract outcomes, own-source metadata comparisons, and Drive-search outcomes.
- `reference_match_verify_batch_008.csv` - 14 title/DOI/byline/verification checks; no manual spelling review required.
- `reference_summary_batch_008.md` - this summary.

The three CSV headers are byte-for-byte identical to the batch 001 headers copied in `/tmp/p2a_batch008_headers.txt`. All four deliverables are ASCII. CSV row counts, candidate order, evidence-field coverage, abstract quote lengths (maximum 25 words), author lists, and own-group flags were checked. No source file, manuscript, earlier batch, or Drive file was altered. The pre-existing untracked `google_drive/` directory remains unstaged. No LaTeX compilation was attempted or claimed.
