# The books arrived: what is actually on the shelf

*2026-11-01, step 35. Twelve items arrived against the thirteen-row wish list. Each one was opened, and
its identity was taken from its own title and copyright pages - not from a file name, and not from the wish
list. `BOOKS_HELD_2026-11-01.csv` is the record; `check_books_held.py` re-reads it and re-tests the claims
made here.*

---

## The count, before anything else

| | |
|---|---|
| items received | **12** |
| usable books | **10** |
| usable only in part | **1** - Povstenko: **Chapter 1 only**, 11 pages |
| **not the book at all** | **1** - Eringen and Maugin: a **one-page book review** of it |
| still missing | **1** - Achenbach, *Wave Propagation in Elastic Solids* (rank 12) |

So the shelf is real, and the phrase "almost all" is accurate - but it is worth being exact about the two
misfires, because one of them was the top recommendation:

**Eringen and Maugin is still not held.** The file that arrived under that title is one page: a review in
the *Journal of Applied Mechanics* by Y. E. Pak, which opens by naming the book, its publisher, its year and
its length ("436 pages"), and contains no equations from it. A review cannot supply a constitutive theory.
**BK-15 therefore stays open**, the six multifield atlas cases still have no invariant, and coverage stays
**34/40** - not 40/40. That was the whole reason it was ranked first, and the ranking has not changed; only
the delivery has.

**Povstenko arrived as one chapter** (Chapter 1, "Essentials of Fractional Calculus"). It is usable for the
definitions of the fractional operators and nothing else. Every sentence in the manuscript about fractional
thermoelastic *solutions* needs the model chapters, which are not in the file.

---

## The ten usable books, with the year as printed

| rank | book | printed year and edition | ISBN on the copy | pp. |
|---|---|---|---|---|
| 2 | Coussy, *Poromechanics* | 2004, Wiley | 978-0-470-84920-7 | 315 |
| 3 | Gorenflo, Kilbas, Mainardi and Rogosin, *Mittag-Leffler Functions...* | 2014, Springer | 978-3-662-43930-2 | 454 |
| 5 | Hetnarski and Eslami, *Thermal Stresses - Advanced Theory* | 2019, **2nd ed.** | 978-3-030-10436-8 | 657 |
| 6 | Muller and Ruggeri, *Rational Extended Thermodynamics* | 1998, **2nd ed.** | 978-1-4612-7460-5 | 404 |
| 7 | Jou, Casas-Vazquez and Lebon, *Extended Irreversible Thermodynamics* | 2010, **4th ed.** | 978-90-481-3074-0 | 484 |
| 8 | Mainardi, *Fractional Calculus and Waves in Linear Viscoelasticity* | 2010, Imperial College Press | 978-1-84816-329-0 | 368 |
| 9 | Eringen, *Nonlocal Continuum Field Theories* | **2002** (wish list said 2004), Springer | 0-387-95275-6 | 386 |
| 10 | Eringen, *Microcontinuum Field Theories I* | 1999, Springer | 978-1-4612-0555-5 | 336 |
| 11 | Brekhovskikh, *Waves in Layered Media* | 1980, **2nd ed.**, Academic Press | 0-12-130560-0 | 508 |
| 13 | Ewing, Jardetzky and Press, *Elastic Waves in Layered Media* | 1957, McGraw-Hill | no ISBN in a 1957 printing | 400 |

Two corrections to the wish list, both from the books' own pages rather than from a catalogue:

- **Eringen, *Nonlocal Continuum Field Theories*: the copyright page says (c) 2002**, not 2004. The
  catalogue year is the online release; the book's own page wins, and the correction is recorded rather than
  the old year repeated.
- **Muller and Ruggeri: the printed ISBN is 978-1-4612-7460-5**, while the wish list carried the eBook ISBN
  978-1-4612-2210-1 (the DOI `10.1007/978-1-4612-2210-1` is the eBook's). Both numbers are recorded together
  so nobody has to guess which one a library will match on.

---

## What has already been done with them

The first pass is not a shelf-inventory pass; it is **one claim closed and read properly**:
[`ML_TAIL_READ_2026-11-01.md`](ML_TAIL_READ_2026-11-01.md) reads Gorenflo et al. pages 25-27, 47, 208 and
219 and turns the last mandatory gap of **CR046** - the one the register said "was not located in the front
matter" - into five printed statements plus a numerical proof.

The queue that the shelf now unblocks, in the order the work will be done:

1. **BK-11 with Coussy** - the porous benchmark measured against a real constitutive model. This is the
   strongest remaining structural job, and it is the only tier-A item that actually arrived.
2. **CR127 with Muller and Ruggeri** - the claim that has been unjudgeable for the whole project because the
   book was never in the library.
3. **CR182 and the micropolar sentences with the two Eringen books.**
4. **The named-theory attributions with Hetnarski and Eslami** - the single largest gap class in the 34-row
   partly-supported sheet (12 wrong-or-loose attributions).
5. **BK-13 and BK-14 with Brekhovskikh**, as an anchor independent of my own closed forms.
6. **The EIT sentences with Jou et al.**

```bash
python3 check_books_held.py      # PASS all checks (12 arrivals, 10 usable, BK-15 still open)
```
