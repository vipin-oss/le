# PDF request list 4 — after the 25-paper batch (FINDINGS_10)

**Prepared:** 2026-10-23, independent verifier, batch **B18**. Supersedes `PDF_REQUEST_LIST_3.md` for everything already supplied.
**Identifier check:** every DOI below was resolved at **Crossref on 2026-10-23** (`api.crossref.org/works?filter=doi:…`, batched up to ten DOIs per call, `select=DOI,title,author,container-title,volume,issue,page,issued,type`) and the returned title/authors/journal/volume/pages/year were compared with the citation in this file. **No DOI here is from memory.** Where Crossref returned a mangled author field, that is stated rather than silently corrected.
**Access check:** OpenAlex `open_access` for all 26 journal/chapter DOIs (two batched calls) plus **Unpaywall** (`api.unpaywall.org/v2/<doi>`, 2026-10-23) for the four items where the OA verdict mattered most (Honig–Hirdes, Dell'Oro–Pata, Mainardi, Povstenko 2011). `closed` below means both sources agree there is no free copy.

---

## Correction carried into this list (C1)

**"Nowacki 1984", *A temperature-rate-dependent theory of thermopiezoelectricity*, J. Thermal Stresses 7(3-4):293-306 is by D. S. CHANDRASEKHARAIAH.** Crossref confirms the author as `D.S. Chandrasekharaiah` on `10.1080/01495738408942213`. The old list (Part B, row B3) and `Papers_to_download.xlsx` both carried "Nowacki". Corrected here and in `LITERATURE_BASE` (`LIT-0521`).

---

## Part A0 — supplied and read (25 items)

All 25 were supplied to the supervisor and read in the F30–F49 batch of `control/FULLTEXT_FINDINGS_10.md` (control @ `f95cf21`). Each is in `FULLTEXT_FACTS` as a **SECONDARY-SOURCE** row: the equations were transcribed by the supervisor; **this verifier opened none of these PDFs.**

| # | citation (Crossref-verified) | DOI | OA (OpenAlex / Unpaywall) | facts key |
|---|---|---|---|---|
| 1 | **Nowacki, W. (1978).** Some general theorems of thermopiezoelectricity. *J. Thermal Stresses* **1**(2), 171–182 | `10.1080/01495737808926940` | closed | `Nowacki1978` |
| 2 | **Chandrasekharaiah, D. S. (1984).** A temperature-rate-dependent theory of thermopiezoelectricity. *J. Thermal Stresses* **7**(3–4), 293–306 | `10.1080/01495738408942213` | closed | `Chandrasekharaiah1984TPZ` |
| 3 | **Cowin, S. C.; Nunziato, J. W. (1983).** Linear elastic materials with voids. *J. Elasticity* **13**(2), 125–147 | `10.1007/BF00041230` | closed | `CowinNunziato1983` |
| 4 | **Nunziato, J. W.; Cowin, S. C. (1979).** A nonlinear theory of elastic materials with voids. *Arch. Rational Mech. Anal.* **72**(2), 175–201 | `10.1007/BF00249363` | closed | `NunziatoCowin1979` |
| 5 | **Ieşan, D. (1986).** A theory of thermoelastic materials with voids. *Acta Mechanica* **60**(1–2), 67–89 | `10.1007/BF01302942` | closed | `Iesan1986` |
| 6 | **Marchand, R.; McDevitt, T.; Triggiani, R. (2012).** An abstract semigroup approach to the third-order MGT PDE… *Math. Methods Appl. Sci.* **35**(15), 1896–1929 | `10.1002/mma.1576` | closed | `Marchand2012MGT` |
| 7 | **Durbin, F. (1974).** Numerical inversion of Laplace transforms: an efficient improvement to Dubner and Abate's method. *Comput. J.* **17**(4), 371–376 | `10.1093/comjnl/17.4.371` | closed | `Durbin1974` |
| 8 | **Honig, G.; Hirdes, U. (1984).** A method for the numerical inversion of Laplace transforms. *J. Comput. Appl. Math.* **10**(1), 113–132 | `10.1016/0377-0427(84)90075-x` | **bronze** (OpenAlex; publisher PDF) | `HonigHirdes1984` |
| 9 | **Stroh, A. N. (1958).** Dislocations and cracks in anisotropic elasticity. *Phil. Mag.* **3**(30), 625–646 | `10.1080/14786435808565804` | closed | `Stroh1958` |
| 10 | **Stroh, A. N. (1962).** Steady state problems in anisotropic elasticity. *J. Math. Phys.* **41**(1–4), 77–103 | `10.1002/sapm196241177` | closed | `Stroh1962` |
| 11 | **Chadwick, P.; Sneddon, I. N. (1958).** Plane waves in an elastic solid conducting heat. *J. Mech. Phys. Solids* **6**(3), 223–230 | `10.1016/0022-5096(58)90027-9` | closed | `ChadwickSneddon1958` |
| 12 | **Joseph, D. D.; Preziosi, L. (1989).** Heat waves. *Rev. Mod. Phys.* **61**(1), 41–73 | `10.1103/RevModPhys.61.41` | closed | `JosephPreziosi1989` |
| 13 | **Joseph, D. D.; Preziosi, L. (1990).** Addendum to "Heat waves". *Rev. Mod. Phys.* **62**(2), 375–391 | `10.1103/RevModPhys.62.375` | closed | `JosephPreziosi1990` |
| 14 | **Hetnarski, R. B.; Ignaczak, J. (1999).** Generalized thermoelasticity. *J. Thermal Stresses* **22**(4–5), 451–476 | `10.1080/014957399280832` | closed | `HetnarskiIgnaczak1999` |
| 15 | **Ivanov, Ts. P.; Savova, R. (1991).** Energy-flux vector of surface thermoelastic waves. *J. Thermal Stresses* **14**(4), 563–570 | `10.1080/01495739108927085` | closed | `IvanovSavova1991` |
| 16 | **Povstenko, Y. Z. (2009).** Thermoelasticity that uses fractional heat conduction equation. *J. Math. Sci.* **162**(2), 296–305 | `10.1007/s10958-009-9636-3` | closed | `Povstenko2009` |
| 17 | **Gorenflo, R.; Mainardi, F. (1997).** Fractional calculus: integral and differential equations of fractional order. *CISM Courses and Lectures* **378**, 223–276 | `10.1007/978-3-7091-2664-6_5` | closed | `GorenfloMainardi1997` |
| 18 | **Gorenflo, R.; Kilbas, A. A.; Mainardi, F.; Rogosin, S. V. (2014).** *Mittag-Leffler Functions, Related Topics and Applications*. Springer Monogr. Math. | `10.1007/978-3-662-43930-2` | closed | `Gorenflo2014Book` |
| 19 | **Luchko, Yu. (2010).** Some uniqueness and existence results… generalized time-fractional diffusion equation. *Comput. Math. Appl.* **59**(5), 1766–1772 | `10.1016/j.camwa.2009.08.015` | **bronze** (ScienceDirect PDF) | `Luchko2010` |
| 20 | **Povstenko, Y. (2015).** *Fractional Thermoelasticity*. Springer, Solid Mech. Appl. **219** — **PREFACE ONLY supplied** | `10.1007/978-3-319-15335-3` | closed | `Povstenko2015Book` |
| 21 | **Wang, J.-L.; Li, H.-F. (2025).** Memory-dependent derivative versus fractional derivative (IV)… *Fractal Fract.* **9**(12), 794 | `10.3390/fractalfract9120794` | **gold** (MDPI) | `WangLi2025IV` |
| 22 | **van der Merwe, A. J.; van Rensburg, N. F. J.; Sieberhagen, R. H. (2021).** Comparing the DPL, Cattaneo–Vernotte and Fourier models using modal analysis. *Appl. Math. Comput.* **396**, 125934 | `10.1016/j.amc.2020.125934` | closed | `vanDerMerwe2021` |
| 23 | **Chiriţă, S.; D'Apice, C.; Zampoli, V. (2016).** The time differential three-phase-lag heat conduction model: thermodynamic compatibility and continuous dependence. *Int. J. Heat Mass Transfer* **102**, 226–232 | `10.1016/j.ijheatmasstransfer.2016.06.019` | closed | `Chirita2016` |
| 24 | **Chen, P. J.; Gurtin, M. E. (1968).** On a theory of heat conduction involving two temperatures. *ZAMP* **19**, 614–627 | `10.1007/BF01594969` | closed | `ChenGurtin1968` |
| 25 | **Gurtin, M. E.; Williams, W. O. (1966).** On the Clausius–Duhem inequality. *ZAMP* **17**(5), 626–633 | `10.1007/BF01597243` | closed | `GurtinWilliams1966` |

**Crossref quirks worth knowing (not corrected silently):** `10.1016/0022-5096(58)90027-9` lists the second author as **"Snedon"** (one *d*) — the printed paper and every citation have **Sneddon**; `10.1080/014957399280832` puts both authors in one string ("Richard B. Hetnarski, Jozef Ignacza"); `10.1007/978-3-7091-2664-6_5` carries the container title *Fractals and Fractional Calculus in Continuum Mechanics* (the CISM volume) rather than "CISM Courses and Lectures 378" — same book.

---

## Part A — open access, still outstanding (1 item)

| # | citation | DOI | OA | serves |
|---|---|---|---|---|
| A1 | **Dell'Oro, F.; Pata, V. (2016).** On the Moore–Gibson–Thompson equation and its relation to linear viscoelasticity. *Appl. Math. Optim.* **76**(3), 641–655 | `10.1007/s00245-016-9365-1` | **green** — Unpaywall: submitted version at Politecnico di Milano, `re.public.polimi.it/bitstream/11311/1026909/…` | s.4.9 / s.10 — the MGT ↔ viscoelasticity equivalence. **NOTE: two authors, Dell'Oro & Pata — not the three-author JDE 2016 paper (F26) and not Dell'Oro–Lasiecka.** |

## Part B — paywalled, still outstanding (3 items)

| # | citation | DOI | OA | serves |
|---|---|---|---|---|
| B1 | **Povstenko, Y. Z. (2011).** Fractional Cattaneo-type equations and generalized thermoelasticity. *J. Thermal Stresses* **34**(2), 97–114 | `10.1080/01495739.2010.511931` | closed (Unpaywall: no repository copy) | s.11 — **the only paper that can carry the manuscript sentence "a fractional Cattaneo-type law"**; Povstenko 2009 does not print one (correction C4) |
| B2 | **Povstenko, Y. (2015).** *Fractional Thermoelasticity*, Springer SMA **219** — **full book** (only the preface arrived) | `10.1007/978-3-319-15335-3` | closed | s.11 — book-level treatment; the Ch. 7 fractional telegraph/fractional Lord–Shulman development is currently known only from the preface |
| B3 | **Mainardi, F. (2010).** *Fractional Calculus and Waves in Linear Viscoelasticity*. Imperial College Press | `10.1142/p614` | closed (Unpaywall: no repository copy) | s.11 — the standard fractional wave/viscoelasticity bridge |

## Part C — print-era, no usable DOI (7 items)

| # | citation | identifier | serves |
|---|---|---|---|
| C1 | **Cattaneo, C. (1948).** Sulla conduzione del calore | *Atti Sem. Mat. Fis. Univ. Modena* **3**, 83–101 — **NO DOI** (no Crossref record found) | s.4.1 / s.4.2 — correction C2 fixes the manuscript's wrong journal/pages |
| C2 | **Vernotte, P. (1958).** Les paradoxes de la théorie continue de l'équation de la chaleur | *C. R. Acad. Sci.* **246**, 3154–3155 — **NO DOI** (a Crossref bibliographic query returned only unrelated items) | s.4.1 / s.4.2 — page range still unverified against the printed note |
| C3 | **Achenbach, J. D. (1973).** *Wave Propagation in Elastic Solids* | North-Holland — **NO DOI**; do not substitute the `10.1016/b978-0-7204-0325-1.*` chapter DOIs (1975 reprint, front matter WITHDRAWN) | s.9 / s.10 — the energy-flux definition |
| C4 | **Auld, B. A. (1973).** *Acoustic Fields and Waves in Solids*, vol. 1 | Wiley — **NO DOI** | s.10 — Poynting-type flux |
| C5 | **Tiersten, H. F. (1969).** *Linear Piezoelectric Plate Vibrations* | Plenum — **NO DOI** | s.5 — piezoelectric plate equations |
| C6 | **Mindlin, R. D. (1961).** On the equations of motion of piezoelectric crystals, in *Problems of Continuum Mechanics* | SIAM — **NO DOI** | s.5 — origin of the Mindlin piezothermoelastic plate theory |
| C7 | **Ignaczak, J.; Ostoja-Starzewski, M. (2010).** *Thermoelasticity with Finite Wave Speeds* | Oxford Univ. Press — **NO DOI confirmed** | s.10 / s.12 — energy identities, systematic comparison |

**Total still outstanding: 11 (1 open access, 3 paywalled, 7 print).**

---

## What changed since list 3

* **25 items moved to A0** (the whole F30–F49 batch plus Luchko 2010). The 29 outstanding of list 3 are now 11.
* **A6/A7/A12/B21** (Dubner–Abate, Stehfest, Honig–Hirdes, Durbin) are all supplied → A0.
* **B3 corrected** from "Nowacki 1984" to **Chandrasekharaiah 1984** (C1).
* **New on the list:** Povstenko 2011 (B1) — it did not exist on list 3 because the manuscript's fractional-Cattaneo sentence had not yet been tested against Povstenko 2009.
* **Dropped:** Moore & Gibson 1960 (already read, listed on 3 only for completeness); the four voids/thermopiezoelectric items; Stroh; Chadwick–Sneddon; Joseph–Preziosi; Hetnarski–Ignaczak; Ivanov–Savova; Gorenflo; Wang–Li 2025; van der Merwe.

## What I could **not** verify

1. **`Papers_to_download.xlsx` / the "Extended list" sheet with 69 DOIs was never available to me.** It is not in Drive under that name, is not among the 50 spreadsheets the connector lists, and is not in `2_Others_Papers`. So the DOI-by-DOI verification below covers the **26 identifiers this project actually carries** (25 supplied + Povstenko 2011), **not 69**. If the workbook appears, the same Crossref batch route will check 69 in about seven calls.
2. **No OA search beyond OpenAlex + Unpaywall.** A repository sweep (BASE, CORE, Google Scholar) was not run; `closed` means "no copy that OpenAlex or Unpaywall knows about", not "no copy anywhere".
3. **Printed page numbers of the print-era items** (C1–C7) are unverified; only C2's journal/volume come from a secondary bibliography.
