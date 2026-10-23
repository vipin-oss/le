# PDF request list 2 — the eleven sources behind `REFERENCE_GAPS.csv`

**Prepared:** 2026-10-22, independent verifier.
**Companion:** `REFERENCE_GAPS.csv` (16 rows) — this file covers the eleven gaps that need a document (twelve table rows: row 2b is the superseded 1997-book entry, kept so the correction is auditable), and leaves GAP-03/04/05/08 to `V-B13_gap_closeout.md` because the supervisor's findings already carry part of them.

**Verification method.** Every DOI below was resolved against the **Crossref REST API** on 2026-10-22 (`api.crossref.org/works/...` and bibliographic queries), and open-access status against **Unpaywall** (`api.unpaywall.org/v2/...`). Nothing here is from memory. Where Crossref holds no record, the row says **NO DOI** — it does not carry a plausible-looking identifier. Where a book exists in a later edition with a DOI, both facts are stated, because citing the 2014 DOI for a 1997 book would be a different citation.

---

## Priority 1 — blocks a section that cannot currently be written

| # | citation | journal / volume / pages | DOI | verified via | OA | serves |
|---|---|---|---|---|---|---|
| 1 | **Cattaneo, C. (1948).** Sulla conduzione del calore. | Atti del Seminario Matematico e Fisico dell'Università di Modena **3**, 83–101 | **NO DOI** | Crossref bibliographic query returns no record for the 1948 paper; the only hit is a one-page reprint entry in a 2011 Springer volume (`10.1007/978-3-642-11051-1_5`, p. 485), which is **not** the article and must not be cited as it | none found | GAP-01 |
| 2 | **Tzou, D. Y. (1995).** A unified field approach for heat conduction from macro- to micro-scales. | J. Heat Transfer **117**, 8–16 | `10.1115/1.2822329` | Crossref work record; **also opened by the supervisor** (`control/FULLTEXT_FINDINGS_04.md` F15, file `1.2822329.pdf`), who identifies it as the DPL paper | closed | GAP-06 |
| 2b | *(superseded row, kept for the record)* **Tzou, D. Y. (1997).** *Macro- to Microscale Heat Transfer: The Lagging Behavior.* | Taylor & Francis, Washington DC (book) | **NO DOI** | Crossref has **no 1997 record** for this book; the **2nd edition** is verifiable as Tzou, *Macro- to Microscale Heat Transfer*, Wiley 2014, `10.1002/9781118818275`. **This is a book, not the DPL journal paper.** Manuscript key `Tzou1997` (pp. 110–116) conflates the two — the DPL equations to be checked are in the 1995 *JHT* paper above | closed (2nd ed.) | GAP-06 |
| 3 | **Chen, P. J.; Gurtin, M. E. (1968).** On a theory of heat conduction involving two temperatures. | Z. Angew. Math. Phys. **19**(4), 614–627 | `10.1007/BF01594969` | Crossref work record (title, authors, volume, pages, 1968-07) | closed | GAP-10 |
| 4 | **Achenbach, J. D. (1973).** *Wave Propagation in Elastic Solids.* | North-Holland/American Elsevier, Amsterdam (book) | **NO DOI (book level)** | Crossref carries only **chapter-level** DOIs under `10.1016/b978-0-7204-0325-1.*` (Elsevier 1975 printing), and the front-matter chapters are marked WITHDRAWN; there is no monograph record | n/a | GAP-12 |
| 5 | **Povstenko, Y. (2015).** *Fractional Thermoelasticity.* | Springer, Solid Mechanics and Its Applications **219**; ISBN 978-3-319-15334-6 | `10.1007/978-3-319-15335-3` | Crossref work record (book, 2015, Springer Cham) plus Unpaywall | closed | GAP-09 |

**Note on rows 2/2b and 5 (rewritten 2026-10-22 after F15).** Row 2 is no longer a *request*: the DPL primary is **Tzou 1995, JHT 117:8–16**, and the supervisor has already opened it, so what is needed is the **printed equation numbers** for the two lag statements, nothing more. Row 2b is the 1997 book, which is a different document with no DOI; cite it as a book and only if a book is meant. Row 5 stands as before — `Povstenko2016` points at a **2015** Springer book (2nd ed. 2024, `10.1007/978-3-031-64587-7`), so the key year is wrong.

## Priority 2 — needed, but a section can stand without them for now

| # | citation | journal / volume / pages | DOI | verified via | OA | serves |
|---|---|---|---|---|---|---|
| 6 | **Vernotte, P. (1958).** Les paradoxes de la théorie continue de l'équation de la chaleur. | C. R. Acad. Sci. Paris **246**, 3154–3155 | **NO DOI** | no Crossref record for the 1958 note | none | GAP-02 |
| 7 | **Gurtin, M. E.; Williams, W. O. (1966).** On the Clausius–Duhem inequality. | Z. Angew. Math. Phys. **17**(5), 626–633 | `10.1007/BF01597243` | Crossref work record | closed | GAP-10 |
| 8 | **Chiriţă, S.; D'Apice, C.; Zampoli, V. (2016).** The time differential three-phase-lag heat conduction model: thermodynamic compatibility and continuous dependence. | Int. J. Heat Mass Transfer **102**, 226–232 | `10.1016/j.ijheatmasstransfer.2016.06.019` | Crossref work record; Unpaywall `oa_status: closed` | closed | GAP-07 |
| 9 | **Gorenflo, R.; Mainardi, F. (1997).** Fractional calculus: integral and differential equations of fractional order. | in *Fractals and Fractional Calculus in Continuum Mechanics* (CISM 378), Springer Vienna, 223–276 | `10.1007/978-3-7091-2664-6_5` | Crossref work record (chapter, 1997) | closed | GAP-09 |
| 10 | **Luchko, Y. (2010).** Some uniqueness and existence results for the initial-boundary-value problems for the generalized time-fractional diffusion equation. | Comput. Math. Appl. **59**(5), 1766–1772 | `10.1016/j.camwa.2009.08.015` | Crossref work record; Unpaywall `is_oa: true`, `oa_status: bronze`, free publisher PDF at `sciencedirect.com/science/article/pii/S0898122109005549/pdf` | **yes, free PDF** | GAP-09 |
| 11 | **Nowacki, W. (1975).** *Dynamic Problems of Thermoelasticity.* | Noordhoff/PWN, Leiden–Warsaw (book) | **NO DOI** | no Crossref record for the 1975 title; Crossref holds only chapter DOIs of the **1986** book *Thermoelasticity* (`10.1016/b978-0-08-024767-0.*`), which is a different work | n/a | GAP-13 |

**Luchko ambiguity, stated rather than hidden.** The manuscript key `Luchko2010` cannot be pinned from the record alone: the base has no row for it and the audit marks it SUSPECT. Two candidates verify — row 10 above (CAMWA, 2009 online / 2010 volume) and Luchko (2011), *Initial-boundary-value problems for the one-dimensional time-fractional diffusion equation*, Fract. Calc. Appl. Anal. **15**, 141–160, `10.2478/s13540-012-0010-7`. Row 10 is the more probable target for a fractional-thermoelasticity citation because it is the uniqueness/existence statement; **confirm the intended key before requesting.**

---

## What I am asking for, in order

1. **Rows 1–5** (P1). Rows 3 and 5 can be bought or borrowed through the library in minutes; rows 1, 2b and 4 are the ones that need a human — they are old books and an Italian 1948 proceedings volume with no DOI anywhere.
2. **Rows 6–11** (P2) whenever convenient.
3. For every item, the **pages that carry the equations**, not the whole document: Cattaneo the flux law itself; **Tzou 1995 the DPL statement and its equation numbers** (the 1997 book and its 2014 edition will not substitute — different equation numbering); Chen & Gurtin the two-temperature relation and the energy balance; Achenbach the energy-flux/average-intensity definition; Povstenko the fractional constitutive chapter.

## What I am *not* claiming

* That these are the only missing sources. `REFERENCE_GAPS.csv` has five more rows whose fix is reading or a decision rather than a document (GAP-03/04/05/08 in part, GAP-11, GAP-14/15/16).
* That a verified DOI means the paper says what the review needs. Row 8 is exactly this case: the tensor-form admissibility condition is attributed to it **second-hand** in `LIT-0477`, and until the paper is read that attribution is itself unverified.
