# What is still missing, and what to send if it cannot be found

*2026-11-01. Nine records: the three outstanding items, and one or two verified substitutes for each. Every DOI
below was opened against a Crossref record today; the one item with no book-level record says so plainly.
Rows: `BOOKS_OUTSTANDING_2026-11-01.csv`; checked by `check_books_outstanding.py`.*

---

## First: nothing else is needed

The shelf is otherwise complete. Of the thirteen rows of the earlier wish list, **ten arrived as usable books**,
one arrived as a single chapter, and one arrived as a one-page review of the book. So the answer to "do you
need any other book" is **no** - the three below are the whole list, and two of them are alternatives to each
other rather than additions. Nothing on this page is a request for a second copy of something already held.

---

## Need 1 - for BK-15, the only book that closes an atlas invariant

| role | # | Author (year) | Title | DOI |
|---|---|---|---|---|
| **send this** | 1 | **Eringen and Maugin (1990)** | *Electrodynamics of Continua I: Foundations and Solid Media*, Springer | **10.1007/978-1-4612-3226-1** |
| if not findable | 2 | **Eringen and Maugin (1990)** | *Electrodynamics of Continua II*, Springer | **10.1007/978-1-4612-3236-0** |
| if neither | 3 | **Maugin (1988)** | *Continuum Mechanics of Electromagnetic Solids*, North-Holland | **10.1016/c2009-0-08748-0** |

**What it buys:** BK-15 is six multifield atlas cases with no invariant *by design*, because inventing a
coupled electro-magneto-elastic constitutive law would produce numbers about no real material. This book
supplies the law, so coverage goes **34/40 -> 40/40**.

**Why the last delivery did not count:** what arrived was a **one-page review** of volume I in the *Journal of
Applied Mechanics* - no equations. What is needed is the **436-page book**. Volume II carries the same
equations by the same authors in the same year, so it substitutes; Maugin's 1988 monograph is the single-author
original of the same theory and also has a chapter on elastic dielectrics and piezoelectricity.

---

## Need 2 - for the fractional-thermoelasticity sentences

| role | # | Author (year) | Title | DOI |
|---|---|---|---|---|
| **send this** | 4 | **Povstenko (2015)** | *Fractional Thermoelasticity*, Springer | **10.1007/978-3-319-15335-3** |
| newer edition | 5 | **Povstenko (2024)** | *Fractional Thermoelasticity*, 2nd ed., Springer | **10.1007/978-3-031-64587-7** |
| if neither | 6 | **Povstenko (2015)** | *Linear Fractional Diffusion-Wave Equation for Scientists and Engineers*, Springer | **10.1007/978-3-319-17954-4** |

**Why the last delivery did not count:** what arrived was **Chapter 1 only** ("Essentials of Fractional
Calculus", 11 pages). The model chapters are the point. Either edition is fine - the 2024 second edition
supersedes the 2015 one; only page numbers in a citation would differ.

---

## Need 3 - optional, the only row of thirteen that never arrived

| role | # | Author (year) | Title | DOI |
|---|---|---|---|---|
| **send this** | 7 | **Achenbach (1973)** | *Wave Propagation in Elastic Solids*, North-Holland | **10.1016/c2013-0-04485-4** |
| if not findable | 8 | **Miklowitz (1978)** | *The Theory of Elastic Waves and Waveguides*, North-Holland | **10.1016/c2009-0-08749-2** |
| if neither | 9 | **Graff (1975)** | *Wave Motion in Elastic Solids*, Ohio State University Press | **no DOI recorded** |

**What it buys:** a classical, citable anchor for the Rayleigh/Lamb/interface material and a modern standard to
replace three bibliography rows that currently name older printings. **This one is optional** - it strengthens
the references, it does not close anything.

**Honest note on the two alternatives:** Miklowitz is stronger on waveguides and transients, weaker on exactly
the surface-wave derivations the manuscript cites. Graff has **no Crossref book record at all** - the only
Crossref hit for the title is a 1979 book review, which must not be cited as the book - so if Graff is chosen,
there will be no DOI on the row and the citation has to be print-only.

---

## Summary table for a quick look

| # | Author (year) | Title | DOI |
|---|---|---|---|
| 1 | Eringen and Maugin (1990) | Electrodynamics of Continua I | 10.1007/978-1-4612-3226-1 |
| 2 | Eringen and Maugin (1990) | Electrodynamics of Continua II | 10.1007/978-1-4612-3236-0 |
| 3 | Maugin (1988) | Continuum Mechanics of Electromagnetic Solids | 10.1016/c2009-0-08748-0 |
| 4 | Povstenko (2015) | Fractional Thermoelasticity | 10.1007/978-3-319-15335-3 |
| 5 | Povstenko (2024) | Fractional Thermoelasticity, 2nd ed. | 10.1007/978-3-031-64587-7 |
| 6 | Povstenko (2015) | Linear Fractional Diffusion-Wave Equation | 10.1007/978-3-319-17954-4 |
| 7 | Achenbach (1973) | Wave Propagation in Elastic Solids | 10.1016/c2013-0-04485-4 |
| 8 | Miklowitz (1978) | The Theory of Elastic Waves and Waveguides | 10.1016/c2009-0-08749-2 |
| 9 | Graff (1975) | Wave Motion in Elastic Solids | no DOI recorded |

```bash
python3 check_books_outstanding.py    # PASS all checks (9 rows, 3 needs, 8 DOIs verified, 1 print-only)
```
