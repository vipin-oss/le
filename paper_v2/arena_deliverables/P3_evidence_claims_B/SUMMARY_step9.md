# Step 9 - second, harder check of Drive: is any of these PDFs already there?

Date: 2026-11-01. Scope: all 87 works that were still on the request list after step 8.

## Why this was done again

The user did not believe the list was clean: "check once more, properly, that none of these PDFs is
already in Drive". A plain listing of the drive was not usable - it holds well over a thousand files and
the listing is capped and truncated - so the drive was searched work by work instead, and every match
was opened before it was believed.

## What was searched, and how

| Probe | Count | Purpose |
|---|---|---|
| first-author surname queries | ~40 | the library keeps most files as `authorYEAR.pdf` or `Author - Year - Title.pdf` |
| DOI-tail queries | 10 (76 DOIs batched ~8 per query) | catches files kept under their DOI, e.g. `bf01597243.pdf` |
| title-token queries | 12 | rows whose file would be named from the title, not the author |
| book-title queries | 6 | the four books on the list plus two near-misses |
| full-text probes | 4 | recall only - the drive's `fullText` matching is loose and cannot be used to prove absence |
| PDFs opened and read on page 1 | 12 | every candidate before anything was called held |
| archive containers downloaded and opened | 6 | two more rows were hiding inside archives |

Known limit: two drive archives (127 MB and 114 MB) are above the 100 MB download cap and could not be
opened here. A work stored only inside one of them would still appear on the list.

## Found: seven works are already in the drive

Each was opened and identified on its own title page or first page before it was removed from the
request list. Recorded, with the page-1 evidence, in `drive_held_sources_2026-11-01.csv`.

1. Abouelregal 2020, Indian J. Physics 94, 1949-1963 - three-phase-lag model with higher-order
   time-fractional derivatives (DOI 10.1007/s12648-019-01635-z).
2. Eringen, *Nonlocal Continuum Field Theories* - 386-page book, title page and preface read; the copy
   is the 2004 Springer printing, so the year caveat on that row stands.
3. Gurtin and Williams 1966, ZAMP 17, 626 - page 1 opens at "626 MORTON E. GURTIN and WILLIAM O.
   WILLIAMS ZAMP".
4. Muller and Ruggeri, *Rational Extended Thermodynamics* - 404-page Springer Tracts in Natural
   Philosophy vol. 37, author page and preface read.
5. Povstenko, *Fractional Thermoelasticity* - 261-page book, title page read.
6. Rayleigh 1885, Proc. London Math. Soc. s1-17, 4-11 - OCR text layer of the 1885 proceedings page.
7. Sarkar, De and Sarkar 2019, J. Thermal Stresses 42:9 - publisher cover page reads title, three
   authors and "42:9"; a second copy of the same file is also there.

## Look-alikes deliberately left on the list

These are in the drive but are *not* the cited works, so the rows stay:

- Quintanilla 2002 (J. Non-Equilib. Thermodyn. 27, 217-227, exponential stability) - not the 2002
  *Applied Mathematical Modelling* paper the register cites.
- Povstenko 2011, "Fractional Cattaneo-type equations and generalized thermoelasticity" (J. Thermal
  Stresses 34:2, 97-114) - not the Dirichlet-problem paper on the list.
- Chandrasekharaiah 1998 review (Appl. Mech. Rev.) and 1988 piezoelectric paper - not 1984 or 1997.
- Hetnarski and Ignaczak 2000, "Nonclassical dynamical thermoelasticity" - not the 1999 review.
- Gurtin and Pipkin 1968, "A general theory of heat conduction with finite wave speeds" - not Gurtin
  and Williams 1966.
- Mindlin 1965 and 1968 - not Mindlin 1974.
- Ezzat 2011, Ezzat and El-Bary 2016 (thermoelectric MHD), Ezzat 2015 - not the three 2016 rows.
- Biswas 2020 (state-space approach, porous medium) - not the 2020 *Acta Mechanica* layer paper.
- Kumar 2017 (AAM plate resonators) - not Kumar, Devi and Sharma 2017.
- Sur and Kanoria 2018 and Mondal/Sur/Kanoria 2019 - not Sur and Kanoria 2012.
- Wang and Li 2021, part (I) of the memory-dependent-derivative series - not part (IV) 2025.
- Joseph and Preziosi 1989 review (Rev. Mod. Phys. 61, 41) - the list asks for the 1990 addendum,
  Rev. Mod. Phys. 62, 375.

## Result

The request list went from 87 to **80 works** (76 titled, 4 with no title asserted; 70 DOIs =
69 verified + 1 wrong; 10 with no DOI). The pdf, the markdown twin, the CSV and the checker were all
regenerated; `check_pdfs_needed.py` prints PASS and exits 0, and it now also fails if any work recorded
as held in Drive is still on the request list.

No drive id, link or source-library folder name is stored in any file in this repository.
