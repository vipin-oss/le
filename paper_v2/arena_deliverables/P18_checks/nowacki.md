# Nowacki: which book the bib entry is, and what the review should cite

**Task.** P18, item 2. **Date.** 2 November 2026.
**Question.** Find the book that matches the bib entry "Nowacki, *Thermoelasticity*, Pergamon, 1975", ISBN 9780080175238; read the title or copyright page of any library copy; report exact title, edition, year, publisher, ISBN; if no copy exists, say so; and say which Nowacki entry the review should cite.

---

## 1. Answer in one paragraph

**No copy of any Nowacki book is in the library** — the book inventory of P13 records the Nowacki slot as "NOT SUPPLIED", with nothing attributed to it, and the reference catalogue carries the key at level **R0** (author, title, publisher, year, ISBN and DOI all unverified). **The ISBN in the bib entry matches no registered book**: a Crossref ISBN query on both forms of 9780080175238 returns **0 records**. The only Nowacki *Thermoelasticity* with a registered record is the **Pergamon/Elsevier second English edition, print date 1986, ISBN 978-0-08-024767-0, author Witold Nowacki**. The review should therefore cite **Nowacki, W., 1986, *Thermoelasticity*, 2nd ed., Pergamon Press, Oxford, ISBN 978-0-08-024767-0** (or the chapter DOI of the part actually used), correct **"Nowacki, Z." to "Nowacki, W."**, and drop both the 1975 year and the ISBN 9780080175238 unless the author can produce a copy whose copyright page prints them.

---

## 2. What the library holds, and what the registers say

| Check | Result | Where |
|---|---|---|
| Any Nowacki file in the book library? | **No.** The books inventory has one Nowacki row, and it is the "not supplied" row | `P13_books/books_inventory.csv`: "Nowacki — not identified further … NOT SUPPLIED … No Nowacki file was added to the library; nothing in this deliverable is attributed to Nowacki" |
| Any Nowacki PDF in the paper library inventory? | No | `library_inventory_v2.csv`, `library_inventory_v3.csv`, `library_inventory_v2_part2.csv`: no Nowacki file |
| Catalogue level of the key | **R0** — `fields_no_list = author; title; publisher; year; isbn; doi` | `refs_catalogue_check.csv`, key `Nowacki1975`, batch 2 |
| The bib entry itself | `@book{Nowacki1975, author = {Nowacki, Z.}, title = {Thermoelasticity}, year = 1975, publisher = {Pergamon Press}, isbn = {9780080175238}}` | `src/refs.bib` line 755 |

So: **no title page and no copyright page could be read, because there is no copy.** Nothing in this file is a reading of a Nowacki book.

---

## 3. The ISBN, checked

| Query | Result |
|---|---|
| `api.crossref.org/works?filter=isbn:9780080175238` | **0 results** |
| `api.crossref.org/works?filter=isbn:0080175233` (the ISBN-10 form of the same number) | **0 results** |

Both queries were run on 2 November 2026. Crossref is not an ISBN registry, so "0 results" is not proof that the number was never printed on a book — but it is proof that **the number cannot be used to identify the book**, and that no edition of Nowacki's *Thermoelasticity* carries it in any registered record.

---

## 4. The book that does exist, and what identifies it

A Crossref bibliographic query for "Nowacki Thermoelasticity Pergamon" returns chapter-level records of one book, consistently:

* container title: **Thermoelasticity**
* author: **Witold Nowacki** (one chapter record gives "W. Nowacki")
* publisher: **Elsevier** (Pergamon is an Elsevier imprint; the records are Elsevier chapter DOIs)
* `published-print`: **1986**
* ISBN: **9780080247670** (i.e. 0-08-024767-0)
* chapter DOIs of the form `10.1016/b978-0-08-024767-0.500xx-x`, for example
  * `…50006-x` — "Basic relations and equations of thermoelasticity"
  * `…50011-3` — "Stationary plane problems of thermoelasticity"
  * `…50014-9` — "Thermal stresses in plates"
  * `…50016-2` — "Thermal stresses in viscoelastic bodies"
  * `…50004-6` — "**Preface to the first edition**"
* the presence of a "Preface to the first edition" chapter shows that the 1986 printing is a **later edition**, not a first printing.

That is as far as an external registry takes it: **edition number, place of publication and the translator's name are not printed in the Crossref record**, and no copy was available to read them. What can be stated without a copy is: title *Thermoelasticity*, author Witold Nowacki, publisher Pergamon (Elsevier), print year 1986, ISBN 978-0-08-024767-0, and that it is a later edition. What cannot be stated is: "second edition", the imprint place, and the translation credit — those need the copyright page.

---

## 5. The author initial is wrong, and the review's own list proves it

The bib entry says **Nowacki, Z.** The review's other Nowacki entry says **Nowacki, W.**:

* `[12]` in the printed list, `Nowacki1978`, verified in this session against Crossref:
  DOI **10.1080/01495737808926940**, title "SOME GENERAL THEOREMS OF THERMOPIEZOELECTRICITY", *Journal of Thermal Stresses* **1**(2), pp. 171–182, issued **1978-10**, author **W. Nowacki** — an exact match to the bib entry.

So the same author appears in one printed list under two initials, and the external record settles which is right: **W.** (Witold). This is the same point as M3 in the P17 referee report, now with the external check behind it.

---

## 6. What the review uses the Nowacki entry for, and what that implies

| Use in the manuscript | Page | What the citation has to support |
|---|---|---|
| "compact textbook accounts followed [Boley1960, Nowacki1975, Carlson1972]" | p. 7 | a textbook account of the classical dynamical theory |
| "Variational formulations and reciprocity theorems are available [Carlson1972, Nowacki1975]" | p. 23 | variational and reciprocity theorems for thermoelasticity |
| **Fig. 29: "Geometry after [22]: welded elastic interface at normal/oblique incidence"** | p. 61 | **a figure adapted from the book** |

Three consequences:

1. For the two text citations, the 1986 edition is the only registered candidate. Whether it actually carries the reciprocity and variational theorems the review attributes to it **was not verified here** — that is a chapter-level check that needs the copy, and it should be done before the citation is kept for that purpose.
2. For **Fig. 29**, an adapted figure needs a **specific edition and a specific figure number** in the permission request. The P17 report (finding R9) already flags the eight adapted figures; this one cannot even be requested until the edition is fixed.
3. The year matters for a fourth reason: if the review keeps "1975", a reader who looks it up finds the 1986 printing and no 1975 Pergamon *Thermoelasticity* with that ISBN. That is the kind of mismatch a copy-editor reports.

---

## 7. Recommendation, in the form the manuscript can use

**Replace** the bib entry with:

> Nowacki, W., 1986, *Thermoelasticity*, Pergamon Press, Oxford, ISBN 978-0-08-024767-0.

and, if a specific chapter is relied on rather than the book as a whole, cite that chapter's DOI (for example `10.1016/b978-0-08-024767-0.50006-x` for the basic relations and equations).

**Do not** keep the year 1975 and the ISBN 9780080175238 together: neither is supported by any record available here, and the pair cannot be matched to any book. If the author holds a 1975 Pergamon printing and its copyright page really prints that ISBN and year, then that copy is the authority — photograph the copyright page, correct the initial to W., and keep the rest; but the current entry cannot stand on the evidence.

**Other Nowacki entries in the list:** `Nowacki1978` ([12]) is correct and verified (DOI above). No other Nowacki entry exists in the bibliography — a search of all eight `.bib` files finds exactly these two keys.

---

## 8. Status of this deliverable

| Item | Status |
|---|---|
| Title, publisher, print year, ISBN of the 1986 edition | **VERIFIED EXTERNALLY** (Crossref, chapter records, 2 Nov 2026) |
| Author initial "W." | **VERIFIED EXTERNALLY** (both the 1986 chapter records and the 1978 article) |
| Edition number, imprint place, translator | **NOT ESTABLISHED** — needs the copyright page of a copy |
| The ISBN 9780080175238 and the year 1975 | **NOT MATCHED** — 0 records in Crossref for both ISBN forms; no library copy |
| Reading of a title or copyright page | **NOT DONE** — no copy exists in this environment |
