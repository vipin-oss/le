# P2-a batch 007 verification summary

## Candidate census and selection

Before batch 007, **34** one-name author-field candidates remained after excluding batches 001, 005, and 006. The source-order census is:

`Ignaczak1985, Ignaczak1982, Bem1982, Scott2007, McCarthy1972, Sherief1992, Sherief1993a, Ignaczak1981, Bem1983, Ezzat2004, Hosseini2017, Quintanilla2002, Quintanilla2002a, Chandrasekharaiah1997, Ciarletta1999, Iesan1998, Youssef2011, Quintanilla1999, Quintanilla2002b, Rukolaine2014, Antaki2000, Quintanilla2008, Quintanilla2009, Chirita2017, Youssef2012, Shaw2019, Quintanilla2020, Biswas2020b, Chirita2012, Singh2020e, Biswas2020c, Abouelregal2011, Singh2013, Singh2015`

Selected the first 20 in source order (no matching Drive PDF was confirmed for any selected key):

`Ignaczak1985, Ignaczak1982, Bem1982, Scott2007, McCarthy1972, Sherief1992, Sherief1993a, Ignaczak1981, Bem1983, Ezzat2004, Hosseini2017, Quintanilla2002, Quintanilla2002a, Chandrasekharaiah1997, Ciarletta1999, Iesan1998, Youssef2011, Quintanilla1999, Quintanilla2002b, Rukolaine2014`

After batch 007, **14** one-name candidates remain:

`Antaki2000, Quintanilla2008, Quintanilla2009, Chirita2017, Youssef2012, Shaw2019, Quintanilla2020, Biswas2020b, Chirita2012, Singh2020e, Biswas2020c, Abouelregal2011, Singh2013, Singh2015`

No batch 008 work was started.

## Source handling and method

The read-only `paper_v2/paper_sources.zip!refs_new.bib` supplied original BibTeX values and line ranges. The exact CSV headers from batch 001 were copied to `/tmp/p2a_batch007_headers.txt` and used unchanged. Original field values and publisher observations are separate evidence rows; each observed field has `matches_original` set to `yes` or `no`. Full publisher bylines are retained, without `et al.`. Publisher issue/supplement labels are included only where visible; no numbered issue was inferred. ScienceDirect identifies Rukolaine2014 in volume 78, supplement C, which is recorded as `Suppl. C`. Article identifiers, if present, would be noted as identifiers; none of this batch uses an article identifier in place of pages.

Targeted Google Drive PDF-only DOI searches were used as leads, not evidence of a match. No target paper was confirmed in Drive. Publisher sources supplied the fallback: Taylor & Francis citation exports and article pages for its records; the Oxford Academic issue table for Scott2007; ScienceDirect article pages for its records, plus a publisher-hosted first-page preview for Chandrasekharaiah1997 and an issue table for Rukolaine2014; and De Gruyter article/issue pages for Quintanilla2002b. No Crossref access is claimed; BibTeX source values were treated only as the original values to compare.

## Verification outcomes

| Level | Count | Meaning |
| --- | ---: | --- |
| R0 | 0 | No unresolved wrong-paper or incomplete-citation records; spelling questions are separately flagged for manual review. |
| R1 | 13 | Complete DOI/citation metadata, but no accessible abstract on the opened publisher source. |
| R2 | 7 | Complete DOI/citation metadata and a publisher abstract inspected. |
| R3 | 0 | Not assigned. |
| **Total** | **20** | **20 selected records** |

R1 keys: `Ignaczak1985, Ignaczak1982, Bem1982, Scott2007, Ignaczak1981, Bem1983, Hosseini2017, Quintanilla2002a, Chandrasekharaiah1997, Ciarletta1999, Iesan1998, Youssef2011, Quintanilla1999`.

R2 keys: `McCarthy1972, Sherief1992, Sherief1993a, Ezzat2004, Quintanilla2002, Quintanilla2002b, Rukolaine2014`.

All 20 have no confirmed matching Drive PDF, so duplicate-of-target comparison was not applicable. The opened DOI leads for three selected keys were unrelated and were rejected:

- `Ignaczak1985`: B07-016__Analysis of plane wave propagation under the pu.pdf (Drive ID `1RWEvq-FQ87bml0ZPAFzl_02ZwJhQ`) is a different 2021 paper.
- `Hosseini2017`: B13-009__Shakeriaski_2021_Phys._Scr._96_125206.pdf (Drive ID `1saQAC68Nizzb7o1Zqh8Q3HmDg64D1w42`) is a different 2021 paper.
- `Youssef2011`: B09-010__crystals-12-01458-v3.pdf (Drive ID `1epJlSFtP3OY14OWf1AgSIykFHuFeX68w`) and B01-009__P09_2023_PhysScr_Energy-Ratio-Response-Interface-Elastic-Dual-porous-Thermoelastic.pdf (Drive ID `18sAl3_HC0sl7DSlN0nDWqWdGamMeVm92`) are different works.

The ScienceDirect first-page preview for Chandrasekharaiah1997 confirmed its title and printed byline. No Drive PDFs were modified or deleted.

## Citation differences, author spelling, and own-group check

- `Scott2007`: the OUP issue table gives the final printed issue citation as 2008, volume 73, issue 1, pages 123-136. The register uses 2008 and records `year differs: bib=2007, printed=2008`.
- `Quintanilla2002b`: De Gruyter gives print publication 2002-09-30 and online publication 2005-06-01; the register uses print year 2002, volume 27, issue 3, pages 217-227. The source BibTeX has no `pages` field, so the publisher page range is a new observation, not a claimed discrepancy.
- No selected record has a printed volume or page range that differs from its BibTeX value. Publisher issue values were added where present; the original BibTeX entries had no issue fields. Rukolaine2014 is in volume 78, supplement C (`Suppl. C`); no numbered issue is shown.
- Two name-spelling flags remain unresolved and require manual review: `Bem1983` (publisher citation export says `Zbigniew Bern`; original BibTeX says `Bem, Z.`) and `Iesan1998` (publisher export renders the surname as `Iesn` after diacritic removal; original BibTeX says `Iesan, D.`). Both are marked `manual_check_required=yes`; neither spelling was silently corrected.
- Publisher spellings with diacritics are rendered in ASCII with `diacritics removed`: `Jozef Ignaczak` (1981, 1982, 1985), `Ramon Quintanilla` (2002 and 2002a), and `D. Iesn` (1998; discrepancy also flagged). The Green-Naghdi en dash is rendered as an ASCII hyphen.
- Every printed author was compared against Vipin Gupta, M. S. Barak, Soumik Das, Vijayata Pathania, Rajesh Kumar, and Rachaita Dutta. All 20 own-group flags are `no`.

## Deliverables and QA

Created only these four new files under `paper_v2/arena_deliverables/P2a/`:

- `reference_register_batch_007.csv` - 20 selected citation records.
- `reference_evidence_batch_007.csv` - 340 evidence rows, with original BibTeX values, publisher metadata, abstract-access outcomes, and Drive PDF-search outcomes.
- `reference_match_verify_batch_007.csv` - 20 title/DOI/byline/verification checks; two spelling discrepancies require manual review.
- `reference_summary_batch_007.md` - this summary.

The three CSV headers are byte-for-byte identical to the batch 001 headers in `/tmp/p2a_batch007_headers.txt`. All four files are ASCII; CSV key counts and selected order were checked. No source, manuscript, earlier batch, or Drive file was altered. The pre-existing `google_drive/` directory remains unstaged. No LaTeX compilation was attempted or claimed.
