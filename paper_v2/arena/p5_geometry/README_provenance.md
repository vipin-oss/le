# P5 geometry sheet - provenance and reading notes

Output of this task: `geometry_sheet.csv` (14 rows, A1 to A14, 17 columns, ASCII only).
Branch: arena/61348c2b-le (the session branch; a separate branch name cannot be created for this
session). Nothing outside `paper_v2/arena/p5_geometry/` was written.

## 1. Where each PDF came from

`RP6.zip` and `RIP7.zip` were downloaded from the same Drive account and extracted outside the
repository, into /tmp. No PDF was committed.

| ID | paper | source found |
|----|-------|--------------|
| A1 | Agarwal 1978 | RP6.zip, `bf00052480.pdf` |
| A2 | Abd-Alla and Al-Dawy 2001 | RP6.zip, `01495730151078171.pdf` |
| A3 | Sharma 2014 (isothermal boundary) | RP6.zip, `s10950-013-9401-4.pdf` |
| A4 | Sharma 2014 (insulated boundary) | RP6.zip, `s10950-013-9401-4.pdf` |
| A5 | Collet, Destrade and Maugin 2006 | RP6.zip, `j.euromechsol.2006.01.007.pdf` |
| A6 | Zhang, Li and Yu 2018a (flat plate) | RP6.zip, `ma11071186.pdf` |
| A7 | Zhang, Liang, Han and Li 2018b (spherical curved plate) | RP6.zip, `ma11122363.pdf` |
| A8 | Abo-Dahab et al. 2020 (P incidence) | not in either zip; Drive library copy |
| A9 | Abo-Dahab et al. 2020 (SV incidence) | not in either zip; Drive library copy |
| A10 | Singh and Gupta 2020 (qP incidence) | not in either zip; Drive library copy |
| A11 | Singh and Gupta 2020 (qSV incidence) | not in either zip; Drive library copy |
| A12 | Yadav, Carrera, Marin and Othman 2022 | not in either zip; Drive library copy |
| A13 | Ma and Duan 2020 | not in either zip; Drive library copy |
| A14 | Mondal and Othman 2020 | not in either zip; Drive library copy |

RIP7.zip turned out to hold classic reference papers, not the recent ones: Coleman and Gurtin
(1967), Chen and Nunziato (1974), Stoneley (1924), Scholte (1947), Barnett, Lothe, Gavazza and
Musgrave (1985), Rayleigh (1885), Collet, Destrade and Maugin (2006, duplicate of the RP6 copy),
and a scanned copy of Love's Some Problems of Geodynamics with no text layer. None of these is
A8 to A14. Since the same five papers were present in the same Drive account, they were downloaded
and read there instead of writing "paper not available". If zip-only provenance is required,
delete rows A8 to A14 and they become "paper not available".

Every PDF was identified from its first page (title and authors), never from a citing paper.

## 2. Page references

Every cell carries a page reference. The PDF page index and the printed page are kept apart in
`page_numbers_used`. Offsets used:

- A1: printed page = PDF page + 170 (PDF p.1 is printed 171).
- A2: printed page = PDF page + 364 (PDF p.3 is printed 367).
- A3 and A4: printed page = PDF page + 60 (PDF p.1 is printed 61).
- A5: printed page = PDF page + 694 (PDF p.1 is printed 695).
- A6 and A7: printed page equals the PDF page index (MDPI pagination).
- A8 and A9: printed page equals the PDF page index.
- A10, A11, A12, A13, A14: the publisher cover pages are unnumbered, so printed page = PDF page - 1
  from PDF p.3 on.

## 3. Quotation note

The quote column holds a short quotation from the source, at most 15 words. Where the PDF text layer
inserts spurious spaces inside words (A2 in particular renders most words letter-spaced), the spacing
was normalised; the wording is unchanged. No quotation was paraphrased.

## 4. What "not stated" means here

"not stated" marks a column that the paper genuinely does not define for that problem, including
cases where the question itself does not apply: A1 to A7 and A10 to A12, A14 are free-surface,
guided or driven problems in which no wave is incident at an angle, so no incident angle exists.
"none" marks a physical feature that the paper explicitly does not include (for example a heat
source). The distinction is deliberate: "none" is a statement by the paper, "not stated" is a gap.

## 5. Reading notes worth a second look

- A8 and A9 name the boundary z = 0 in the incidence geometry, but write the traction conditions for
  quantities evaluated at (x, 0, t), and also call the region a quarter-space.
- A12 writes the depth coordinate as y in the potentials (53)-(54) and as z in the boundary
  conditions (55).
- A14 never uses the word half-space; the half-space reading rests on the statement that the solution
  of the depth equation is bounded as z tends to infinity.
- A11 contains an internal inconsistency: Section 5.2(b) attaches the 28 degree critical angle to the
  reflected qP wave, while conclusion (iii) attaches it to the reflected qSV wave. The sheet follows
  Section 5.2(b).
- A13 does not name its material, and the direction, position and speed of its moving heat source are
  not stated beyond the normal-mode form of Q.
