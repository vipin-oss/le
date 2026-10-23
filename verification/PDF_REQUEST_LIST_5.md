# PDF request list 5 — the supervisor's 69-paper EXTENDED_LIST

**Prepared:** 2026-10-23, independent verifier, batch **B19**.
**Source list:** `control/EXTENDED_LIST.csv` on `origin/claude/control` @ **`e09a127`** ("69 wish-list papers for Brave DOI verification — DOIs from memory, unverified"). 69 rows, tier ∈ {Must, Good}.
**What this file is:** an acquisition sheet. Nothing in it is a technical claim, and nothing here counts as a source that has been read. Metadata confirms *identity and access only*.

**Identifier check (Crossref, 2026-10-23):** every DOI in the list was resolved with `api.crossref.org/works?filter=doi:…` in batches of ten, `select=DOI,title,author,container-title,volume,issue,page,issued`, and the returned title, authors, journal, volume, issue, pages and year were compared with the citation as the supervisor wrote it. Where a listed DOI resolved to a *different* paper (five cases) the correct record was found by `query.bibliographic` + author/year matching; where resolution failed (two cases) no DOI is printed. **No DOI in this file comes from memory.** The raw verdict per paper is `verification/api_log/B19_extended_doi_checks.csv` (51 rows).

**Access check:** OpenAlex `open_access` for all 49 resolvable DOIs (four batched calls, `select=doi,open_access`) plus **Unpaywall** `api.unpaywall.org/v2/<doi>` for the four items where the OA verdict mattered most (n13 Quintanilla 2003, n18 Guyer–Krumhansl, n44 Chandrasekharaiah 1988, n47 Achenbach 1968). `closed` below means OpenAlex says closed and, where Unpaywall was consulted, Unpaywall agreed.

---

## 0. Counts

| group | n |
|---|---|
| rows in the supervisor's list | 69 |
| already in `LITERATURE_BASE` — **mapped below, not written up again** | 18 |
| verified this batch (new to the base) | 51 |
| … DOI as supplied, metadata matches | 41 |
| … DOI **corrected** (listed DOI is the wrong paper / unregistered) | 5 |
| … title matches but author field missing from the Crossref record | 1 (n28) |
| … end page differs from the list | 1 (n51) |
| … Crossref author list shorter than the list's | 1 (n58) |
| … **no DOI** (books) | 2 (n42, n43) |
| **Part A — open access, 9** · **Part B — paywalled, 40** · **Part C — no DOI, 2** | 51 |
| Must-have among the 51 | 17 |

This list **supersedes `PDF_REQUEST_LIST_4.md` only for the 69-paper extended list**. The 11 items still outstanding in LIST_4 (its Parts A, B, C) are unaffected and still stand.

---

## Part A — open access, request these first (9)

Everything below can be fetched without a subscription. "OA" is the OpenAlex `oa_status`; Unpaywall agrees where consulted.

| n | tier | sec. | citation (Crossref-verified) | DOI | OA + free copy | note |
|---|---|---|---|---|---|---|
| 21 | Good | 12 | Huberman, S.; Duncan, R.A.; Chen, K.; Song, B.; Chiloyan, V.; Ding, Z.; Maznev, A.A.; Chen, G.; Nelson, K.A. (2019). Observation of second sound in graphite at temperatures above 100 K. *Science* **364**(6438):375–379 | `10.1126/science.aav3548` | **green** — arXiv:1901.09160 (`https://arxiv.org/abs/1901.09160`) | the accepted-manuscript version; page numbers in any quote must come from the published PDF, not the preprint |
| 38 | Good | 11 | Ezzat, M.A. (2011). Theory of fractional order in generalized thermoelectric MHD. *Appl. Math. Model.* **35**(10):4965–4978 | `10.1016/j.apm.2011.04.004` | **bronze** — free at the publisher (`https://doi.org/10.1016/j.apm.2011.04.004`) | |
| 41 | Good | 11 | Atangana, A.; Baleanu, D. (2016). New fractional derivatives with nonlocal and non-singular kernel: theory and application to heat transfer model. *Thermal Science* **20**(2):763–769 | `10.2298/TSCI160111018A` | **gold** — `http://www.doiserbia.nb.rs/ft.aspx?id=0354-98361600018A` | list title omits the subtitle; OpenAlex holds a second, duplicate record for the same DOI with a green location — same paper, do not count it twice |
| 53 | Good | 9, 10 | Stoneley, R. (1924). Elastic waves at the surface of separation of two solids. *Proc. R. Soc. Lond. A* **106**(738):416–428 | `10.1098/rspa.1924.0079` | **diamond** — free at the Royal Society | |
| 54 | Good | 9, 10 | Lamb, H. (1917). On waves in an elastic plate. *Proc. R. Soc. Lond. A* **93**(648):114–128 | `10.1098/rspa.1917.0008` | **diamond** — free at the Royal Society | |
| 60 | Must | 4 | Quintanilla, R.; Racke, R. (2003). Stability in thermoelasticity of type III. *Discrete Contin. Dyn. Syst. B* **3**(3):383–400 | `10.3934/dcdsb.2003.3.383` | **green** — KOPS, Univ. Konstanz (`https://kops.uni-konstanz.de/server/api/core/bitstreams/c317437e-58ee-465a-8355-e67c1973b3d4/content`) | repository copy — check it is the published version before quoting a page |
| 66 | Good | 8 | Weideman, J.A.C.; Trefethen, L.N. (2007). Parabolic and hyperbolic contours for computing the Bromwich integral. *Math. Comp.* **76**(259):1341–1356 | `10.1090/S0025-5718-07-01945-X` | **hybrid** — AMS PDF (`https://www.ams.org/mcom/2007-76-259/S0025-5718-07-01945-X/S0025-5718-07-01945-X.pdf`) | |
| 67 | Good | 8 | Crump, K.S. (1976). Numerical inversion of Laplace transforms using a Fourier series approximation. *J. ACM* **23**(1):89–96 | `10.1145/321921.321931` | **bronze** — ACM PDF (`https://dl.acm.org/doi/pdf/10.1145/321921.321931`) | |
| 68 | Good | 12 | Cahill, D.G.; Ford, W.K.; Goodson, K.E.; Mahan, G.D.; Majumdar, A.; Maris, H.J.; Merlin, R.; Phillpot, S.R. (2003). Nanoscale thermal transport. *J. Appl. Phys.* **93**(2):793–818 | `10.1063/1.1524305` | **bronze** — OpenAlex points at `aip.scitation.org/doi/pdf/…` | that host is the retired AIP platform; the free-to-read copy may need the new `pubs.aip.org` URL. Treat as *probably* free, verify on fetch |

---

## Part B — paywalled (40), in tier order

"Must" rows are the ones that block a section that is otherwise ready. All titles/volumes/pages below are the Crossref record, not the list.

### B-I. Must — 16

| n | sec. | citation (Crossref-verified) | DOI | why |
|---|---|---|---|---|
| 9 | 1, 12 | Hetnarski, R.B.; Ignaczak, J. (2000). Nonclassical dynamical thermoelasticity. *Int. J. Solids Struct.* **37**(1–2):215–224 | `10.1016/S0020-7683(99)00089-X` | companion review for s.1/s.12 |
| 10 | 3, 4 | Gurtin, M.E.; Pipkin, A.C. (1968). A general theory of heat conduction with finite wave speeds. *Arch. Rational Mech. Anal.* **31**(2):113–126 | `10.1007/BF00281373` | memory-type origin of finite-speed conduction |
| 12 | 3, 4 | Quintanilla, R.; Racke, R. (2008). A note on stability in three-phase-lag heat conduction. *Int. J. Heat Mass Transfer* **51**(1–2):24–29 | `10.1016/j.ijheatmasstransfer.2007.04.045` **(corrected)** | TPL stability; listed DOI was the wrong paper |
| 13 | 3, 4 | Quintanilla, R. (2003). A condition on the delay parameters in the one-dimensional dual-phase-lag thermoelastic theory. *J. Thermal Stresses* **26**(7):713–721 | `10.1080/713855996` **(corrected)** | the τ_T vs τ_q condition; supervisor's "year/DOI uncertain" flag now closed |
| 16 | 3, 4 | Tzou, D.Y. (1995). Experimental support for the lagging behavior in heat propagation. *J. Thermophys. Heat Transfer* **9**(4):686–693 | `10.2514/3.725` | experimental basis for the lags |
| 18 | 3, 12 | Guyer, R.A.; Krumhansl, J.A. (1966). Solution of the linearized phonon Boltzmann equation. *Phys. Rev.* **148**(2):766–778 | `10.1103/PhysRev.148.766` | **one of the three read comparisons GAP-22 needs for s.12** |
| 25 | 7 | Eringen, A.C. (1972). Nonlocal polar elastic continua. *Int. J. Engng Sci.* **10**(1):1–16 | `10.1016/0020-7225(72)90070-5` | nonlocal origin |
| 26 | 7 | Eringen, A.C.; Edelen, D.G.B. (1972). On nonlocal elasticity. *Int. J. Engng Sci.* **10**(3):233–248 | `10.1016/0020-7225(72)90039-0` | nonlocal origin |
| 32 | 7 | Aifantis, E.C. (1992). On the role of gradients in the localization of deformation and fracture. *Int. J. Engng Sci.* **30**(10):1279–1299 | `10.1016/0020-7225(92)90141-3` | gradient (Aifantis) theory |
| 37 | 11 | Compte, A.; Metzler, R. (1997). The generalized Cattaneo equation for the description of anomalous transport processes. *J. Phys. A* **30**(21):7277–7289 | `10.1088/0305-4470/30/21/006` | fractional Cattaneo origin |
| 44 | 5 | Chandrasekharaiah, D.S. (1988). A generalized linear thermoelasticity theory for piezoelectric media. *Acta Mechanica* **71**(1–4):39–49 | `10.1007/BF01173936` | s.5 core; supervisor's "could not resolve DOI" flag now closed — the DOI is good |
| 46 | 9, 10 | Deresiewicz, H. (1957). Plane waves in a thermoelastic solid. *J. Acoust. Soc. Am.* **29**(2):204–209 | `10.1121/1.1908832` | classical thermoelastic waves |
| 47 | 9, 10 | Achenbach, J.D. (1968). The influence of heat conduction on propagating stress jumps. *J. Mech. Phys. Solids* **16**(4):273–282 | `10.1016/0022-5096(68)90035-5` **(corrected)** | wave-front / stress-jump analysis |
| 50 | 9, 10 | Sinha, S.B.; Elsibai, K.A. (1996). Reflection of thermoelastic waves at a solid half-space with two relaxation times. *J. Thermal Stresses* **19**(8):749–762 | `10.1080/01495739608946205` | reflection (GL) |
| 51 | 9, 10 | Sinha, S.B.; Elsibai, K.A. (1997). Reflection and refraction of thermoelastic waves at an interface of two semi-infinite media with two relaxation times. *J. Thermal Stresses* **20**(2):129–145 | `10.1080/01495739708956095` | interface partition; core for s.10 — Crossref end page 145 vs list 146, settle on the PDF |
| 64 | 8 | Talbot, A. (1979). The accurate numerical inversion of Laplace transforms. *IMA J. Appl. Math.* **23**(1):97–120 | `10.1093/imamat/23.1.97` | inversion method |

### B-II. Good — 24

| n | sec. | citation (Crossref-verified) | DOI |
|---|---|---|---|
| 14 | 3, 4 | Fabrizio, M.; Lazzari, B. (2014). Stability and second law of thermodynamics in dual-phase-lag heat conduction. *Int. J. Heat Mass Transfer* **74**:484–489 | `10.1016/j.ijheatmasstransfer.2014.02.027` **(corrected)** |
| 20 | 12 | Jackson, H.E.; Walker, C.T.; McNelly, T.F. (1970). Second sound in NaF. *Phys. Rev. Lett.* **25**(1):26–28 | `10.1103/PhysRevLett.25.26` |
| 22 | 12 | Chen, G. (2021). Non-Fourier phonon heat conduction at the microscale and nanoscale. *Nature Reviews Physics* **3**(8):555–569 | `10.1038/s42254-021-00334-1` |
| 23 | 12 | Mitra, K.; Kumar, S.; Vedevarz, A.; Moallemi, M.K. (1995). Experimental evidence of hyperbolic heat conduction in processed meat. *J. Heat Transfer* **117**(3):568–573 | `10.1115/1.2822615` |
| 24 | 3 | Maxwell, J.C. (1867). On the dynamical theory of gases. *Phil. Trans. R. Soc. Lond.* **157**:49–88 | `10.1098/rstl.1867.0004` |
| 28 | 7 | *Nonlocal Continuum Field Theories* (book), Springer, 2004 — Crossref record carries **title and year only, no author**; the list's author (Eringen) is not confirmed by Crossref | `10.1007/b97697` |
| 30 | 7 | Mindlin, R.D. (1965). Second gradient of strain and surface-tension in linear elasticity. *Int. J. Solids Struct.* **1**(4):417–438 | `10.1016/0020-7683(65)90006-5` |
| 31 | 7 | Mindlin, R.D.; Eshel, N.N. (1968). On first strain-gradient theories in linear elasticity. *Int. J. Solids Struct.* **4**(1):109–124 | `10.1016/0020-7683(68)90036-X` |
| 33 | 7 | Aifantis, E.C. (2003). Update on a class of gradient theories. *Mech. Mater.* **35**(3–6):259–280 | `10.1016/S0167-6636(02)00278-8` |
| 34 | 7 | Lim, C.W.; Zhang, G.; Reddy, J.N. (2015). A higher-order nonlocal elasticity and strain gradient theory and its applications in wave propagation. *J. Mech. Phys. Solids* **78**:298–313 | `10.1016/j.jmps.2015.02.001` |
| 35 | 7 | Romano, G.; Barretta, R.; Diaco, M.; Marotti de Sciarra, F. (2017). Constitutive boundary conditions and paradoxes in nonlocal elastic nanobeams. *Int. J. Mech. Sci.* **121**:151–156 | `10.1016/j.ijmecsci.2016.10.036` **(corrected)** |
| 45 | 5 | Yang, J. (2018). *An Introduction to the Theory of Piezoelectricity* (book, 2nd ed.), Springer | `10.1007/978-3-030-03137-4` |
| 48 | 9, 10 | Nayfeh, A.; Nemat-Nasser, S. (1971). Thermoelastic waves in solids with thermal relaxation. *Acta Mechanica* **12**(1–2):53–69 | `10.1007/BF01178389` |
| 49 | 9, 10 | Puri, P. (1972). Plane waves in thermoelasticity and magnetothermoelasticity. *Int. J. Engng Sci.* **10**(5):467–477 | `10.1016/0020-7225(72)90052-3` |
| 52 | 9, 10 | Rayleigh, Lord (1885). On waves propagated along the plane surface of an elastic solid. *Proc. London Math. Soc.* **s1-17**(1):4–11 | `10.1112/plms/s1-17.1.4` |
| 55 | 2 | Coleman, B.D.; Noll, W. (1963). The thermodynamics of elastic materials with heat conduction and viscosity. *Arch. Rational Mech. Anal.* **13**(1):167–178 | `10.1007/BF01262690` |
| 56 | 2 | Coleman, B.D. (1964). Thermodynamics of materials with memory. *Arch. Rational Mech. Anal.* **17**(1):1–46 | `10.1007/BF00283864` |
| 57 | 2 | Liu, I-S. (1972). Method of Lagrange multipliers for exploitation of the entropy principle. *Arch. Rational Mech. Anal.* **46**(2):131–148 | `10.1007/BF00250688` |
| 58 | 3 | Jou, D.; Casas-Vázquez, J.; Lebon, G. (2010). *Extended Irreversible Thermodynamics* (book, 4th ed.), Springer — Crossref lists only Jou and Lebon | `10.1007/978-90-481-3074-0` |
| 59 | 3 | Müller, I.; Ruggeri, T. (1998). *Rational Extended Thermodynamics* (book, 2nd ed.), Springer | `10.1007/978-1-4612-2210-1` |
| 61 | 4 | Zhang, X.; Zuazua, E. (2003). Decay of solutions of the system of thermoelasticity of type III. *Commun. Contemp. Math.* **5**(1):25–83 | `10.1142/S0219199703000896` |
| 63 | 4 | Dafermos, C.M. (1968). On the existence and the asymptotic stability of solutions to the equations of linear thermoelasticity. *Arch. Rational Mech. Anal.* **29**(4):241–271 | `10.1007/BF00276727` |
| 65 | 8 | Abate, J.; Whitt, W. (2006). A unified framework for numerically inverting Laplace transforms. *INFORMS J. Comput.* **18**(4):408–421 | `10.1287/ijoc.1050.0137` |
| 69 | 12 | Majumdar, A. (1993). Microscale heat conduction in dielectric thin films. *J. Heat Transfer* **115**(1):7–16 | `10.1115/1.2910673` |

---

## Part C — no DOI (2), library / ILL only

Both are books the list itself marked "(book; library)". **Crossref returned no book-level record for either**, so there is no DOI to quote and none is invented here.

| n | citation | what Crossref does and does not have | what is needed |
|---|---|---|---|
| 42 | Podlubny, I. (1999). *Fractional Differential Equations*. Academic Press, Mathematics in Science and Engineering series | `query.author=Podlubny & query.title=… & filter=type:book` → **0 results**; bibliographic search returns only his journal/proceedings papers | the printed book (library). If a page-specific claim is to be made about the Riemann–Liouville/Caputo definitions, the request must name the chapter |
| 43 | Kilbas, A.A.; Srivastava, H.M.; Trujillo, J.J. (2006). *Theory and Applications of Fractional Differential Equations*. Elsevier, North-Holland Mathematics Studies **204** | chapter-level records exist under the book (e.g. the Preface, `10.1016/S0304-0208(06)80001-0`); the book itself has **no** book-level DOI that Crossref will return | the printed book, or the specific chapter DOI once the page is known |

---

## Part D — the 18 papers already in `LITERATURE_BASE` (map only, per B19 order 3)

These are **not** described again and **not** requested as new rows. If a PDF is wanted, it is because the *existing* row is below the read level its section needs — stated in the last column.

| n | list item | LIT id | current read_level | PDF still wanted? |
|---|---|---|---|---|
| 1 | Biot 1956, *J. Appl. Phys.* 27:240–253 | LIT-0001 | metadata only | no new request (one-line citation) |
| 2 | Lord & Shulman 1967 | LIT-0002 | FULL (text layer read) | no — done |
| 3 | Green & Lindsay 1972 | LIT-0003 | SECONDARY-SOURCE | no — counts as read under B11 #2; supervisor flag "(re-confirm)" needs no fetch |
| 4 | Green & Naghdi 1991 | LIT-0004 | metadata only | no new request this batch (scanned copy already held, no text layer) |
| 5 | Green & Naghdi 1992 | LIT-0430 | PRIMARY-SOURCE-CHECKED (supervisor-transcribed) | no — equations already transcribed with the qualifier |
| 6 | Green & Naghdi 1993 | LIT-0005 | PRIMARY-SOURCE-CHECKED (supervisor-transcribed) | no — same; (4.15) stays untranscribed by standing rule |
| 7 | Chandrasekharaiah 1986 review | LIT-0038 | metadata only | secondary — only if time allows |
| 8 | Chandrasekharaiah 1998 review | LIT-0039 | metadata only | **YES — GAP-22 comparison #3** |
| 11 | Quintanilla & Racke 2006 (DPL) | LIT-0413 | metadata only | no new request (s.4.7–4.8 already has DPL sources) |
| 15 | Kovács & Ván 2015 | LIT-0119 | metadata only | no new request |
| 17 | Chester 1963, *Phys. Rev.* 131:2013–2015 | LIT-0010 | metadata only | **YES — GAP-22 comparison #1** |
| 19 | Ackerman et al. 1966 | LIT-0011 | metadata only | no new request (s.12 has better experiments) |
| 27 | Eringen 1983 | LIT-0019 | metadata only | no new request |
| 29 | Mindlin 1964 | LIT-0404 | metadata only | no new request |
| 36 | Youssef 2010 | LIT-0106 | metadata only | no new request |
| 39 | Wang & Li 2011 | LIT-0029 | FULL | no — done |
| 40 | Yu, Hu & Tian 2014 | LIT-0286 | metadata only | no new request |
| 62 | Racke 2002 | LIT-0401 | metadata only | no new request |

**DOI status of these 18** was not re-verified in this batch (order 3: map only). B18 already Crossref-checked the ones that were active requests; the rest stand at whatever their base row records.

---

## Part E — s.12 / GAP-22: which three read comparisons are missing, and are they in this list?

s.12 stands at **3 of the 6** read sources it needs (Wang & Li 2025 — LIT-0307; van der Merwe et al. 2021 — LIT-0428; the Shakeriaski survey — LIT-0040). GAP-22 stays open until three more papers are **read**, not merely identified. **All three are in the supervisor's extended list** — that is the useful finding of this batch:

| # | paper | list n / tier | status in base | what it costs |
|---|---|---|---|---|
| 1 | Chester, M. (1963). Second sound in solids. *Phys. Rev.* **131**(5):2013–2015, `10.1103/PhysRev.131.2013` | **n17, Must**, sections "3, 12" | **LIT-0010, metadata only** | PDF only — no new base row. Paywalled (APS); Part D row |
| 2 | Guyer, R.A.; Krumhansl, J.A. (1966). Solution of the linearized phonon Boltzmann equation. *Phys. Rev.* **148**(2):766–778, `10.1103/PhysRev.148.766` | **n18, Must**, section 12 | **not in base** | PDF **and** a new LIT row after reading. Paywalled (APS), OpenAlex + Unpaywall both say closed — **Part B** |
| 3 | Chandrasekharaiah, D.S. (1998). Hyperbolic thermoelasticity: a review of recent literature. *Appl. Mech. Rev.* **51**(12):705–729, `10.1115/1.3098984` | **n8, Must**, sections "1, 12" | **LIT-0039, metadata only** | PDF only. Paywalled (ASME); also the AMR benchmark review this review will be judged against |

Secondary, only if time allows: n7 Chandrasekharaiah 1986 (`10.1115/1.3143705`, LIT-0038, metadata only) and n21 Huberman 2019 (Good, **not** in base, **open access** — Part A; the modern second-sound experiment, would strengthen rather than close GAP-22).

**Consequence for the plan:** two of the three GAP-22 items need no new `LITERATURE_BASE` row, only a PDF; one (Guyer–Krumhansl 1966) needs both. None of the three is free to read.

---

## Part F — the five DOI corrections (carry into every later citation)

| n | DOI in the supervisor's list | what that DOI actually is | correct DOI for the intended paper |
|---|---|---|---|
| 12 | `10.1016/j.ijheatmasstransfer.2007.05.009` | Chiu & Yan, *Mixed convection heat transfer in inclined rectangular ducts with radiation effects*, IJHMT 51(5–6):1085–1094 (2008) | `10.1016/j.ijheatmasstransfer.2007.04.045` |
| 13 | `10.1080/01495730306338` | not registered at Crossref | `10.1080/713855996` (Quintanilla, J. Thermal Stresses 26(7):713–721, 2003) |
| 14 | `10.1016/j.ijheatmasstransfer.2014.02.060` | Saleh et al., *Mixed convection stagnation flow towards a vertical shrinking sheet*, IJHMT 73:839–848 (2014) | `10.1016/j.ijheatmasstransfer.2014.02.027` |
| 35 | `10.1016/j.ijmecsci.2016.12.014` | Lalonde et al., *Modeling multilayered wire strands…*, Int. J. Mech. Sci. 126:281–296 (2017) | `10.1016/j.ijmecsci.2016.10.036` |
| 47 | `10.1016/0022-5096(68)90036-3` | not registered at Crossref | `10.1016/0022-5096(68)90035-5` |

Two of these (n14, n35) are the kind of error that survives a copy-paste citation chain: the wrong DOI resolves to a real, plausible-looking paper. Any bibliography built from this list **must** use the right-hand column.

---

## Part G — what this file does **not** establish

1. **No paper here has been read.** Metadata confirms identity and access only; every one of the 51 stays unknown as a source until a PDF is opened and a row is written from it.
2. The OA verdicts are 2026-10-23 snapshots from OpenAlex (and Unpaywall for four items). Repository copies move; the n68 AIP link is already suspected stale.
3. n28's authorship, n58's third author and n51's end page are **unresolved** — Crossref does not settle them. They must be settled from the printed article, not from this list.
4. n42/n43: no DOI located. This is a statement about Crossref, not proof that no DOI exists in the world.
5. Book records (n28, n45, n58, n59, n42, n43) are catalogue-level only: Crossref cannot confirm edition, ISBN, or pagination.
