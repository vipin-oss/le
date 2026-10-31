# P5 - Independent Full-Text Wave Problem Atlas, batch 001

Source archive: RP6.zip (single archive, exact-name search).
Task branch: arena/61348c2b-le, created from origin/review-paper-v2.
Base SHA: 62b1a62ad9e8d07eed7af498ebbfdf26662743b1 (git merge-base HEAD origin/review-paper-v2).
Mode: evidence-grounded problem extraction only. No manuscript, source, script, PDF, archive,
blueprint or target-list file was modified.

## 1. What the archive actually contains

`unzip -l` on RP6.zip reports six PDF entries and no directory entries:

| # | File inside RP6.zip | Bytes | Pages | Identity confirmed on page 1 |
|---|---------------------|-------|-------|------------------------------|
| 1 | bf00052480.pdf | 287,067 | 7 | Agarwal, On surface waves in generalized thermoelasticity, J. Elasticity 8(2):171-177 |
| 2 | 01495730151078171.pdf | 476,916 | 18 | Abd-Alla and Al-Dawy, Thermal relaxation times effect on Rayleigh waves..., J. Thermal Stresses 24(4):367-382 |
| 3 | s10950-013-9401-4.pdf | 652,981 | 19 | Sharma, Propagation and attenuation of Rayleigh waves..., J. Seismology 18:61-79 |
| 4 | j.euromechsol.2006.01.007.pdf | 189,820 | 12 | Collet, Destrade and Maugin, Bleustein-Gulyaev waves in some functionally graded materials, EJMA/Solids 25:695-706 |
| 5 | ma11071186.pdf | 4,470,769 | 16 | Zhang, Li and Yu, ...Evanescent Lamb Wave in Functionally Graded Piezoelectric-Piezomagnetic Plates, Materials 11:1186 |
| 6 | ma11122363.pdf | 13,568,313 | 17 | Zhang, Liang, Han and Li, ...Non-Propagating Lamb-Like Wave in a Functionally Graded Piezoelectric Spherical Curved Plate..., Materials 11:2363 |

Six PDFs were expected at most and six were found. Two papers named in the brief were **not** in the
archive (see section 5). The two Zhang papers are both present, and the brief allowed either one.

Page counts were taken from the PDF page objects; each PDF was opened and its text read in this
session. No paper was accepted from metadata alone.

## 2. Eligibility decisions

All six PDFs satisfied the eligibility rule, and all six printed author lists are independent of the
own group (Vipin Gupta, M. S. Barak, Soumik Das, Vijayata Pathania, Rajesh Kumar, Rachaita Dutta,
Meghana A. R., Abhik Sur). The printed names were compared as printed; no inference was made from
similar surnames.

One caveat is recorded rather than hidden: the 1978 Agarwal paper prints no DOI anywhere in the PDF.
Title, author, journal, volume and page range are printed on page 1 and match, and the filename
carries the Springer DOI suffix. That row is therefore marked "partial" for title/DOI match and
flagged for external DOI confirmation in `atlas_match_verify_batch_001.csv`.

## 3. Accepted problem rows

Seven rows, from six papers. One paper contributes two rows because it defines two genuinely
different boundary-value problems.

| Paper | Rows | Problem IDs | Wave family |
|-------|------|-------------|-------------|
| Agarwal 1978 | 1 | P5-001 | Rayleigh-type surface wave, half-space, LS and GL |
| Abd-Alla and Al-Dawy 2001 | 1 | P5-002 | Rayleigh wave, half-space, thermally insulated, CD/LS/GL |
| Sharma 2014 | 2 | P5-003, P5-004 | Rayleigh wave, half-space, isothermal surface / insulated surface |
| Collet, Destrade and Maugin 2006 | 1 | P5-005 | Bleustein-Gulyaev surface wave, FGM piezoelectric half-space |
| Zhang, Li and Yu 2018 | 1 | P5-006 | Lamb wave in an FGPPM plate, evanescent branches included |
| Zhang, Liang, Han and Li 2018 | 1 | P5-007 | Lamb-like wave in an FGPM spherical curved plate, non-propagating branches |

The two Sharma rows are justified by distinct conditions, not by a duplicated result: the isothermal
surface gives boundary conditions (17), an irrational dispersion equation (18) and a degree-7
polynomial (19) with a copper example; the insulated surface gives conditions (20), equation (21) and
a degree-9 polynomial (22) with a limestone example. Their conclusions differ in sign - for example
velocity falls with thermal conductivity at an isothermal surface and rises with it at an insulated
surface.

Two further candidate rows were deliberately not created, to avoid inflating the batch with
duplicates: the shorted-circuit case of P5-006 (used only to compute the coupling factor) and the SH
branch of P5-007 (explicitly excluded by the authors, who solve only the Lamb-like system). Both are
recorded in the rejected-candidates file as "no row" decisions with reasons.

## 4. Evidence coverage

`atlas_evidence_batch_001.csv` holds 98 rows. Every non-"-" field of every accepted atlas row has at
least one supporting evidence row, and every evidence row points at an existing problem_id. This was
checked mechanically, not by eye.

Each evidence row records the PDF page index and the printed page separately. The offsets are not
uniform, so they were established per file:

- Agarwal: PDF page 1 is printed page 171 (offset +170), 7 pages.
- Abd-Alla: PDF pages 1-2 are unnumbered publisher cover pages; printed numbering starts at 367 on
  PDF page 3 (offset +364), running to 382 on PDF page 18.
- Sharma: PDF page 1 is printed 61 (offset +60), 19 pages to 79.
- Collet et al.: PDF page 1 is printed 695 (offset +694), 12 pages to 706.
- Zhang et al. 2018a: printed page equals PDF page index (1 to 16).
- Zhang et al. 2018b: printed page equals PDF page index (1 to 17).

## 5. Not accepted

| Candidate | Reason |
|-----------|--------|
| Kumar, Paswan and Singh 2024, DOI 10.1080/15376494.2024.2303728 | Not present in RP6.zip. No PDF, so no first page, geometry, conditions or results could be checked. |
| Naik, Sahu and Kirti 2026, DOI 10.3103/S1541308X26700093 | Not present in RP6.zip. Same reason. |

No rejected file was a mis-filed unrelated paper: every PDF in the archive matched one of the expected
targets.

## 6. Field conventions used

- Unknown or unreported is written as `-`. No parameter, unit, tolerance or error bound was inferred.
- `verification` records only what the source demonstrates. The reductions used in P5-001, P5-003,
  P5-004 and P5-005 are limit reductions to known results and are labelled as such, not as
  validation. Only P5-006 and P5-007 compare against an independent published numerical method, and
  neither reports an error bound.
- No numerical prediction is described as an experimental finding. None of the six papers reports
  experimental data.
- `reproducibility` records what the source supplies: equations, coefficient sets, material tables and
  convergence tables. No review-author script is claimed to exist or to have run, and no LaTeX was
  compiled.
- Evidence levels take two values only:
  - `direct_read` - the page was read in this session and directly supports the observation.
  - `direct_read_equation_text_garbled` - the page was read, but the PDF text layer mangles the
    equation, so only structure and meaning confirmed by surrounding prose are recorded.
- All text is in our own words. No abstract was pasted. The longest cell in the atlas file is 112
  words of paraphrase; no quoted passage approaches the 25-word limit.

## 7. Quality caveats found while reading

- **Agarwal 1978 is a scanned PDF with a poor OCR layer.** Prose is usable but equations are mangled
  (Greek letters and subscripts collide). The sign in the radiation condition (2.10) is ambiguous in
  the OCR, so it is recorded structurally and not asserted. Equations were read, not reconstructed.
- **Both MDPI papers have a duplicated text layer.** Each page also contains a "FOR PEER REVIEW"
  copy of the same content, so the extracted text repeats itself. Both copies were read; the
  duplication is a rendering artefact of the files, not a second analysis.
- **Zhang et al. 2018b has garbled display equations (1)-(2).** These are the general spherical
  field equations, rendered as vertical character dumps. The coupled governing equations (7a)-(7d)
  are legible and were used.
- **Most results in these papers are graphical.** Agarwal gives none at all; Abd-Alla, Sharma and
  Collet present curves with a few numbers in the text. Only P5-006 offers a numeric table
  (Table 3). Reported results in the atlas are therefore mostly stated trends, not numbers, and are
  written that way.
- **All six are analytical or semi-analytical studies with no experimental validation.** No
  tolerance, error bound or benchmark table is reported anywhere in the batch.

## 8. Integrity checks performed

- Header lines of all four CSV files are byte-identical to the required headers (read from a scratch
  file) and contain no extra columns.
- All four files parse as CSV with a consistent column count on every row; one record per row.
- ASCII-only scan: 0 non-ASCII bytes and 0 control characters in all four files; each file also
  decodes as valid UTF-8.
- Diacritics were transliterated where needed: "Gerard" in the Collet citation and the "Lame"
  constants, with the note "diacritics removed" carried in the affected cells.
- No Drive IDs, URLs, links or folder names appear in any output. File names recorded are those
  inside RP6.zip only.
- Field coverage and evidence-to-problem referential integrity checked programmatically.

## 9. Files created

All under `paper_v2/arena_deliverables/P5_atlas/`:

- `problem_atlas_batch_001.csv` - 7 accepted problem rows
- `atlas_evidence_batch_001.csv` - 98 evidence rows
- `atlas_match_verify_batch_001.csv` - 7 verification-of-match rows
- `atlas_rejected_candidates_batch_001.csv` - 4 rows (2 absent papers, 2 no-row decisions)
- `atlas_summary_batch_001.md` - this file

No other file was created, edited, moved or deleted in the repository.

## 10. Not done

Batch 002 was not started. No manuscript text was edited and no citation sentence was drafted for
main.tex. No claim is made that any LaTeX compiled.
