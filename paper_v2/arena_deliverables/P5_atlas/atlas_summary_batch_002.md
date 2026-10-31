# P5 - Independent Full-Text Wave Problem Atlas, batch 002

Source: existing Google Drive library, eight bibkeys taken from `paper_v2/atlas_targets.csv`.
Task branch: arena/61348c2b-le, branched from origin/review-paper-v2.
Base SHA: 62b1a62ad9e8d07eed7af498ebbfdf26662743b1 (identical to `git merge-base HEAD origin/review-paper-v2`).
Mode: evidence-grounded problem extraction only. No .tex, .bib, script, PDF, zip, BLUEPRINT_v3.1.md or
atlas_targets.csv file was modified.

## 1. How each bibkey was located

`paper_v2/atlas_targets.csv` holds 74 target rows with the header `bibkey,doi,pdf_filename`. The eight
batch-002 bibkeys were read from it and the library was searched by file name. Where the library copy
carries a series prefix or a shortened name, the file was identified by a distinctive substring and the
identity was then confirmed from the first page of the PDF.

| bibkey | DOI (target list) | pdf_filename (target list) | file found | match basis |
|---|---|---|---|---|
| AboDahab2020 | 10.1016/j.rinp.2020.103270 | 1-s2.0-S221137972031737X-main.pdf | same name | exact file-name match, identity confirmed on page 1 |
| Mondal2020 | 10.1080/17455030.2020.1730480 | Piezo-thermoelastic media.pdf | same name | exact file-name match, identity confirmed on page 1 |
| Singh2020c | 10.1080/15397734.2020.1853566 | Singh, Gupta - 2023 - Wave reflection by the fr.pdf | B05-020__Singh, Gupta - 2023 - Wave reflection by the fr.pdf | series prefix added by the library; matched by distinctive substring, then title, authors and DOI read on page 1 |
| Yadav2022 | 10.1080/15376494.2022.2130484 | 23 PI- 13 MAMS Reflection hygrothermal Nonlocal.pdf | B03-003__23 PI- 13 MAMS Reflection hygrothermal Nonlocal.pdf | series prefix added by the library; matched by distinctive substring, then title, authors and DOI read on page 1 |
| Zhao2018 | 10.1007/s10704-018-0320-9 | hygro peizo.pdf | same name | exact file-name match, identity confirmed on page 1 |
| Ma2020 | 10.1080/15397734.2020.1852088 | 10.1080@15397734.2020.1852088.pdf | same name | exact file-name match, identity confirmed on page 1 |
| Li2019 | 10.1016/j.ijheatmasstransfer.2019.118664 | mdd + fractional.pdf | same name | exact file-name match, identity confirmed on page 1 |
| Guo2018 | 10.1080/01495739.2018.1522987 | 2019Amodifiedfractional-ordergeneralizedpiezoelectric_Guohuili.pdf | same name | exact file-name match; one duplicate copy of identical size exists in the library |

All eight PDFs were opened in this session and their text extracted page by page; no paper was judged
from metadata alone.

## 2. Eligibility decisions

Seven of the eight papers qualify and give seven accepted rows. Two papers use the same source twice
because they treat two distinct incidence configurations with two distinct result sets (AboDahab2020)
or two distinct incidence regimes (Singh2020c).

Three papers do not qualify as wave problems and are recorded as rejected candidates: Zhao2018 is a static
three-dimensional fracture study, Li2019 is a transient laser-heating study of a layered structure, and
Guo2018 is a one-dimensional transient thin-plate response whose only wave content is the position of the
thermal and elastic wave fronts. The reasoning for each is recorded in the rejected file and in section 5.

Own-group check: the printed author lists are S.M. Abo-Dahab, A.A. Kilany, Emad A.-B. Abdel-Salam,
A. Hatem; Sudip Mondal and Mohamed I. A. Othman; Baljeet Singh and Geetika Gupta; Anand Kumar Yadav,
Erasmo Carrera, Marin Marin and Mohamed Ibrahim Ahmed Othman; Yongbin Ma and Xiaoyu Duan. None of these
printed names is on the own-group list. Geetika Gupta is not Vipin Gupta, and Anand Kumar Yadav is not a
Rajesh Kumar; the decision was made by exact comparison of the printed names only.

## 3. Accepted problem rows

| problem_id | source | configuration | wave family | rows of evidence |
|---|---|---|---|---|
| P5-101 | AboDahab2020 | P wave incident on the free surface of a half-space, three reflected waves (T, p, SV) | reflected | 15 |
| P5-102 | AboDahab2020 | SV wave incident on the same free surface, three reflected waves | reflected | 13 |
| P5-103 | Singh2020c | qP wave incident on the free boundary of a flexoelectric half-space, reflected qP and qSV | reflected | 15 |
| P5-104 | Singh2020c | qSV wave incident on the same boundary, reflections only below the 28 deg critical angle | reflected | 15 |
| P5-105 | Yadav2022 | P wave incident on the free surface of a nonlocal hygro-thermoelastic half-space, four reflected waves (P, TD, mD, SV) | reflected | 16 |
| P5-106 | Ma2020 | normal-mode wave field in a fiber-reinforced half-space under a moving heat source, magnetic field and gravity | bulk half-space field, not an incidence problem | 14 |
| P5-107 | Mondal2020 | normal-mode plane wave in a piezo-thermoelastic half-space driven by a prescribed harmonic surface stress, LS/DPL/TPL with memory-dependent derivatives | bulk plane wave in a half-space, driven surface | 17 |

Accepted rows per paper: AboDahab2020 2, Mondal2020 1, Singh2020c 2, Yadav2022 1, Ma2020 1.

Five of the seven rows are incidence and reflection problems (P5-101 to P5-105). P5-106 and P5-107 are
half-space wave-field problems and are labelled as such. P5-106 is the weakest of the seven as a wave
problem: the field is harmonic along the boundary with a wave number and decays into the half-space, but
the paper defines no wave speed, no dispersion relation and no reflection coefficient, and its reported
results are distributions of displacement, temperature and stress against depth. A reviewer who wants
only incidence and reflection geometry can drop P5-106 without affecting the other six.

## 4. Evidence coverage and page offsets

105 evidence rows, every non-key field of every accepted row covered at least once. Printed page and PDF
page index are recorded separately:

- AboDahab2020: printed page equals the PDF page index (PDF p.1 is printed p.1), 16 pages.
- Mondal2020: PDF p.1 is the publisher cover and PDF p.2 is article page 1 without a printed number; printed = PDF - 1 from PDF p.3 on, 19 pages (printed 1 to 18).
- Singh2020c: PDF p.1 is the publisher cover; printed = PDF - 1 from PDF p.3 on, 24 pages (printed 1 to 23).
- Yadav2022: PDF p.1 is the publisher cover; printed = PDF - 1 from PDF p.3 on, 15 pages (printed 1 to 14).
- Ma2020: PDF p.1 is the publisher cover; printed = PDF - 1 from PDF p.3 on, 25 pages (printed 1 to 24).
- Zhao2018, Li2019, Guo2018: no evidence rows, since no problem row was created.

## 5. Not accepted

| candidate | reason |
|---|---|
| R-201 Zhao2018, hygro peizo.pdf | static three-dimensional steady-state general solution applied to a crack; the string "wave" does not occur anywhere in the extracted text |
| R-202 Li2019, mdd + fractional.pdf | transient thermomechanical response of a two-layered structure under a non-Gaussian laser pulse, Laplace transform and numerical inversion; no wave field and no reflection or transmission analysis |
| R-203 Guo2018, 2019Amodifiedfractional-ordergeneralizedpiezoelectric_Guohuili.pdf | one-dimensional transient thermoelectromechanical response of a thin piezoelectric plate under a thermal shock; the only wave content is the position of the thermal and elastic wave fronts (Eqs. (66)-(67)), used to bound the time window and compared with a published front position |
| Ma2020, 10.1080@15397734.2020.1852088.pdf | not rejected: kept as P5-106 with an explicit caveat, although it reports no wave speed, dispersion or reflection result |

## 6. Field conventions used

- Unknown or unreported is written as `-`. No parameter, unit, tolerance or error bound was inferred.
- `verification` records only what the source demonstrates. AboDahab2020 shows nothing beyond the
  integer-order limit; Singh2020c shows an energy-sum check and claims qualitative agreement with
  Qi (2019); Yadav2022 shows an energy-sum check; Ma2020 shows nothing.
- No numerical prediction is described as an experimental finding. None of the seven accepted problem
  rows rests on experimental data; no paper in this batch reports an experiment.
- `reproducibility` records what the source supplies. Singh2020c states that a MATLAB program was used and
  Yadav2022 that Equations (51)-(52) were used in a FORTRAN program; in both cases no code is provided and
  no review-author script is claimed to exist.
- Evidence levels take two values only: `direct_read` and `direct_read_equation_text_garbled`.
- All text is in our own words. No abstract was pasted and no quotation exceeds 25 words; direct quotations
  are not used in the CSV files at all.

## 7. Quality caveats found while reading

- **AboDahab2020 names its surface inconsistently.** The incidence geometry of Fig. 1 refers to the z-axis,
  the region is called a quarter-space, the field is said to be independent of z, and the traction
  conditions (46) are written for quantities evaluated at (x,0,t). The atlas records this rather than
  guessing a coordinate.
- **AboDahab2020 Table 1 is partly unreadable in the text layer.** Only the entries that print cleanly
  (CE, mu, rho, g, T0) are recorded; the conductivity and expansion entries are not reconstructed.
- **Yadav2022 names its depth coordinate inconsistently.** The potentials (53)-(54) use y, the boundary
  conditions (55) use z. The text also mentions an isothermal surface option, but (55) contains only the
  insulated condition, so only that one is recorded.
- **Yadav2022 uses two different parameter sets.** The constant list gives T0 = 283 K and omega = 30 Hz,
  while the figure captions use T0 = 286 K and omega = 5, 10, 15 Hz. Both are recorded as printed.
- **Singh2020c contradicts itself on the critical angle.** Section 5.2(b) says the reflected qP wave does
  not exist beyond 28 deg, while conclusion (iii) attaches the same limit to the reflected qSV wave.
  P5-104 follows Section 5.2(b) and the discrepancy is flagged in the evidence notes.
- **Ma2020 does not name its material** and several constants print with ambiguous symbols; the values are
  listed in sequence without asserting which symbol each belongs to.
- **Mondal2020 never uses the word half-space.** The half-space reading of P5-107 rests on the statement
  that the solution of the depth equation is taken bounded as z tends to infinity (Eq. (36)); the paper
  is flagged for manual verification on that point.
- **All seven accepted rows are analytical or semi-analytical with graphical results only.** No tabulated
  values are available in any of them, so no numeric reproduction of a figure is possible from the papers.

## 8. Integrity checks performed

- Header lines of all four CSV files are byte-identical to the required headers, read from a /tmp scratch
  file before the build; column counts are 13, 10, 11 and 5 respectively.
- All four files parse as CSV with a consistent column count on every row; one record per row; CRLF line
  endings as in batch 001.
- ASCII-only scan: 0 non-ASCII bytes and 0 control characters in the CSVs and in this file.
- No double-quote character appears inside any cell; no cell contains a sentence-length quotation.
- Field coverage and evidence-to-problem referential integrity checked programmatically: every non-`-`
  field of every accepted row has at least one evidence row, and no evidence row points outside P5-101 to
  P5-106.
- No Drive IDs, URLs, links or folder names appear in any output; only file names are recorded.

## 9. Files created

- `problem_atlas_batch_002.csv` - 7 accepted problem rows (P5-101 to P5-107)
- `atlas_evidence_batch_002.csv` - 105 evidence rows
- `atlas_match_verify_batch_002.csv` - 7 rows, one per accepted problem
- `atlas_rejected_candidates_batch_002.csv` - 3 rows (R-201 to R-203)
- `atlas_summary_batch_002.md` - this file

## 10. Not done

- Batch 003 was not started and no other bibkey from atlas_targets.csv was touched.
- No manuscript text, citation sentence or abstract wording was produced.
- The three rejected papers were not re-read beyond the sections needed to establish the rejection.
- Where the text layer garbles an equation, the equation number and its role are recorded but no symbol
  was reconstructed.
