# PDF request list 3 — the missing theory sources (s.5, s.8, s.10, s.11, s.12, s.4.9)

**Prepared:** 2026-10-23, independent verifier. **Batches:** B16b (list), B17 (supplied items removed after F23–F27).
**Why this list exists:** the B16 batch-1 audit showed that none of the must-read rows for sections 5, 8, 10, 12 and 4.9 / 4.11 is in the Drive library, and that the library holds ~300 applied papers rather than theory primaries (`V-B16_batch1_applications.md`, gaps `GAP-17`…`GAP-25`). No amount of further reading in that library will close those sections. This is the shopping list.

**How every entry was checked.** Identifiers were resolved against the **OpenAlex API on 2026-10-23** (`api.openalex.org/works?filter=doi:…`), one query per batch of DOIs; the returned record supplied title, year, volume/first–last page and the OA verdict (`open_access.is_oa`, `oa_status`, `oa_url`). Where OpenAlex returned nothing for a DOI I had guessed, the item is **not** in the list on the strength of that guess — it is either resolved by a title search or left out. **No DOI below is from memory.** Bibliographic details for the five print-era items in Part C could not be machine-verified and say so.

**Order.** Part A0 is what has already arrived. Part A is the remainder with an open-access copy — the handler can download those directly. Part B is paywalled but DOI-verified. Part C is print-era material with no usable DOI. **29 items are still outstanding: 4 open access, 20 paywalled, 5 print.**

---

## Part A0 — already supplied and read (6 items, no longer requested)

These were on the original list; the handler supplied them and the supervisor read them, so they are recorded in `FULLTEXT_FACTS` and are **no longer requests**.

| was | item | facts key | status |
|---|---|---|---|
| A1 | Caputo 1967, *Geophys. J. R. Astron. Soc.* **13**, 529–539, `10.1111/j.1365-246X.1967.tb02303.x` | `Caputo1967` | **SUPPLIED (F23)** — definition (5), purpose; operator came from viscoelasticity, not heat conduction |
| A2 | Sherief, El-Sayed & Abd El-Latief 2010, *IJSS* **47**, 269–275, `10.1016/j.ijsolstr.2009.09.034` | `Sherief2010Fractional` | **SUPPLIED (F24)** — (2.29) fractional flux, (2.37) energy |
| A3 | Wang & Li 2021 (I), *JCAM* **384**, 112923, `10.1016/j.cam.2020.112923` | `WangLi2021I` | **SUPPLIED (F25)** — MDD vs FD, conceptual only |
| A5 | Shakeriaski et al. 2021 review, *JCDE* **8**, 15–35, `10.1093/jcde/qwaa082` | `Shakeriaski2021Survey` | **SUPPLIED (F27)** — secondary survey for s.12 |
| A8 | Lasiecka & Wang 2015, *JDE* **259**, 7610–7635, `10.1016/j.jde.2015.08.052` | `LasieckaWang2015MGT` | **SUPPLIED (F26)** — abstract MGT with memory, decay |
| A9 | Dell'Oro, Lasiecka & Pata 2016, *JDE* **261**, 4188–4222, `10.1016/j.jde.2016.06.025` | `DellOroLasieckaPata2016MGT` | **SUPPLIED (F26)** — critical case αβ = γ |

*(A11, Quintanilla 2019, was listed only so its OA link was on record; it has been read since F19 and is likewise not a request.)*

## Part A — open access, download first (4 items)

| # | citation | journal / volume / pages | DOI | OA | serves |
|---|---|---|---|---|---|
| A4 | **Wang, J.-L.; Li, H.-F. (2025).** Memory-dependent derivative versus fractional derivative (IV): Space-dependent derivative for unsteady heat diffusion | Fractal Fract. **9**(12), 794 | `10.3390/fractalfract9120794` | **gold** (MDPI) | s.12 — the newest side-by-side comparison in the series |
| A6 | **Dubner, H.; Abate, J. (1968).** Numerical inversion of Laplace transforms by relating them to the finite Fourier cosine transform | J. ACM **15**(1), 115–123 | `10.1145/321439.321446` | **bronze**, ACM PDF | s.8 — the Laplace-inversion method actually used by the state-space papers the review cites |
| A7 | **Stehfest, H. (1970).** Algorithm 368: Numerical inversion of Laplace transforms | Comm. ACM **13**(1), 47–49 | `10.1145/361953.361969` | **bronze**, ACM PDF | s.8 — the other inversion algorithm in that literature |
| A10 | **Dell'Oro, F.; Lasiecka, I. (2016).** On the Moore–Gibson–Thompson equation and its relation to linear viscoelasticity | Appl. Math. Optim. **76**(3), 641–655 | `10.1007/s00245-016-9365-1` | **green** (PoliMi repository) | s.4.9 + s.10 — the MGT ↔ viscoelasticity correspondence. **Note: this is NOT the F26 paper.** F26 supplied Dell'Oro, Lasiecka & Pata 2016 (*JDE* **261**, 4188) — a different article. This one (Dell'Oro & Lasiecka, *Appl. Math. Optim.* **76**, 641) is still outstanding and is worth having for the viscoelasticity equivalence. |

## Part B — paywalled, DOI verified (20 items)

| # | citation | journal / volume / pages | DOI | serves |
|---|---|---|---|---|
| B1 | **Mindlin, R. D. (1974).** Equations of high frequency vibrations of thermopiezoelectric crystal plates | Int. J. Solids Struct. **10**(6), 625–637 | `10.1016/0020-7683(74)90047-X` | s.5 — **GAP-18**: the thermopiezoelectric plate equations |
| B2 | **Nowacki, W. (1978).** Some general theorems of thermopiezoelectricity | J. Thermal Stresses **1**(2), 171–182 | `10.1080/01495737808926940` | s.5 — reciprocity/uniqueness for the coupled piezo-thermal field |
| B3 | **Nowacki, W. (1984).** A temperature-rate-dependent theory of thermopiezoelectricity | J. Thermal Stresses **7**(3–4), 293–306 | `10.1080/01495738408942213` | s.5 — the GL-type extension for piezoelectric media |
| B4 | **Cowin, S. C.; Nunziato, J. W. (1983).** Linear elastic materials with voids | J. Elasticity **13**(2), 125–147 | `10.1007/BF00041230` | s.5 — the void parameter that section 5's "three-source" set already leans on |
| B5 | **Nunziato, J. W.; Cowin, S. C. (1979).** A nonlinear theory of elastic materials with voids | Arch. Rational Mech. Anal. **72**(2), 175–201 | `10.1007/BF00249363` | s.5 — its nonlinear parent |
| B6 | **Iesan, D. (1986).** A theory of thermoelastic materials with voids | Acta Mechanica **60**(1–2), 67–89 | `10.1007/BF01302942` | s.5 — the thermoelastic voids theory that most applied papers cite |
| B7 | **Stroh, A. N. (1958).** Dislocations and cracks in anisotropic elasticity | Phil. Mag. **3**(30), 625–646 | `10.1080/14786435808565804` | s.8 — the Stroh formalism every anisotropic wave paper silently uses |
| B8 | **Stroh, A. N. (1962).** Steady state problems in anisotropic elasticity | J. Math. Phys. **41**(1–4), 77–103 | `10.1002/sapm196241177` | s.8 — same formalism, the steady-state version |
| B9 | **Chadwick, P.; Sneddon, I. N. (1958).** Plane waves in an elastic solid conducting heat | J. Mech. Phys. Solids **6**(3), 223–230 | `10.1016/0022-5096(58)90027-9` | s.8 + s.10 — the classical attenuation/dissipation calculation |
| B10 | **Joseph, D. D.; Preziosi, L. (1989).** Heat waves | Rev. Mod. Phys. **61**(1), 41–73 | `10.1103/RevModPhys.61.41` | s.8 + s.10 — the review that frames hyperbolic heat conduction |
| B11 | **Joseph, D. D.; Preziosi, L. (1990).** Addendum to "Heat waves" | Rev. Mod. Phys. **62**(2), 375–391 | `10.1103/RevModPhys.62.375` | s.8 — must be cited with B10, not instead of it |
| B12 | **Hetnarski, R. B.; Ignaczak, J. (1999).** Generalized thermoelasticity | J. Thermal Stresses **22**(4–5), 451–476 | `10.1080/014957399280832` | s.8 + s.10 + s.12 — the standard review of the five generalizations |
| B13 | *(authors to be taken from the article page — not captured in my metadata query)* **Energy-flux vector of surface thermoelastic waves** (1991) | J. Thermal Stresses **14**(4), 563–570 | `10.1080/01495739108927085` | s.10 — a rare paper whose **title** is the energy-flux vector itself; verify before citing |
| B14 | **Povstenko, Yu. (2009).** Thermoelasticity that uses fractional heat conduction equation | J. Math. Sci. **162**(2), 296–305 | `10.1007/s10958-009-9636-3` | s.11 — **GAP-09**: the fractional thermoelasticity reference the section is missing |
| B15 | **Povstenko, Yu. (2015).** *Fractional Thermoelasticity* | Springer, Solid Mech. Appl. **219** | `10.1007/978-3-319-15335-3` | s.11 — book-level treatment; 2nd ed. 2024 `10.1007/978-3-031-64587-7` |
| B16 | **Mainardi, F. (2010).** *Fractional Calculus and Waves in Linear Viscoelasticity* | Imperial College Press | `10.1142/p614` | s.11 — the standard wave/viscoelasticity bridge |
| B17 | **Gorenflo, R.; Kilbas, A. A.; Mainardi, F.; Rogosin, S. V. (2014).** *Mittag-Leffler Functions, Related Topics and Applications* | Springer | `10.1007/978-3-662-43930-2` | s.11 — the special-function machinery behind fractional thermoelasticity |
| B18 | **Marchand, R.; McDevitt, T.; Triggiani, R. (2012).** An abstract semigroup approach to the third-order Moore–Gibson–Thompson PDE arising in high-intensity ultrasound | Math. Methods Appl. Sci. **35**(15), 1896–1929 | `10.1002/mma.1576` | s.4.9 + s.8 — well-posedness of the MGT equation (the "mathematical methods" side of s.4.9) |
| B19 | **van der Merwe, A. J.; van Rensburg, N. F. J.; Sieberhagen, R. H. (2021).** Comparing the dual phase lag, Cattaneo–Vernotte and Fourier heat conduction models using modal analysis | Appl. Math. Comput. **396**, 125934 | `10.1016/j.amc.2020.125934` | s.12 — side-by-side comparison, now a plan row (`LIT-0428`) |
| B20 | **Moore, F. K.; Gibson, W. E. (1960).** Propagation of weak disturbances in a gas subject to relaxation effects | J. Aerospace Sci. **27**(2), 117–127 | `10.2514/8.8418` | s.4.9 — the origin paper; **already identified and read by the supervisor** (F14). Listed for completeness, not for purchase |

## Part C — print-era, no usable DOI (5 items)

| # | citation | publisher | DOI | serves |
|---|---|---|---|---|
| C1 | **Mindlin, R. D. (1961).** On the equations of motion of piezoelectric crystals. In *Problems of Continuum Mechanics* (Musketi anniversary volume) | SIAM, Philadelphia | **NO DOI — printed source** | s.5 — the origin of the Mindlin piezothermoelastic plate theory that B1 extends. Page range not machine-verified; take it from the copy. |
| C2 | **Tiersten, H. F. (1969).** *Linear Piezoelectric Plate Vibrations* | Plenum, New York | **NO DOI — printed source** | s.5 — the standard reference for the piezoelectric plate equations |
| C3 | **Achenbach, J. D. (1973).** *Wave Propagation in Elastic Solids* | North-Holland, Amsterdam | **NO DOI — printed source** (chapter-level DOIs under `10.1016/b978-0-7204-0325-1.*` are Elsevier 1975 reprints and the front matter is marked WITHDRAWN; do not cite them as the book) | s.10 — the energy-flux / average-intensity definitions that section 10 needs |
| C4 | **Auld, B. A. (1973).** *Acoustic Fields and Waves in Solids*, vol. 1 | Wiley, New York | **NO DOI — printed source** | s.10 — the Poynting-type flux for piezoelectric media |
| C5 | **Ignaczak, J.; Ostoja-Starzewski, M. (2010).** *Thermoelasticity with Finite Wave Speeds* | Oxford University Press | **NO DOI confirmed** (no OpenAlex record matched the candidate DOI; do not cite a guessed one) | s.10 + s.12 — energy identities and the systematic comparison of the five theories |

---

## Coverage against the gaps

| gap | section | items in this list | note |
|---|---|---|---|
| GAP-18 | s.5 | **B1–B6**, C1–C2 | **Mindlin 1974 (B1) has since been supplied and read (F21)**; the remaining micropolar/void core is still paywalled or print, so s.5 has one eligible source of the six it needs. |
| GAP-19 | s.8 | **A6, A7, B7–B12** | the two inversion algorithms are free; the Stroh and Chadwick classics are not |
| GAP-20 | s.10 | **B9, B10, B12, B13, C3–C5** | mostly print-era; this is the section that will cost the most effort |
| GAP-21 / GAP-25 | s.11 | **B14–B17** (A1–A3 now supplied) | **GAP-25 is closed** — Caputo arrived (F23). Still open: Povstenko (B14, B15) and the fractional books (B16, B17) |
| GAP-22 | s.12 | **B12, B19** (A3–A5 now supplied) | s.12 has **one** eligible source (LIT-0040, secondary survey) and needs five more read comparisons |
| GAP-08 / s.4.9 | s.4.9 | **B18, B20** (A8–A11 now supplied/read) | **GAP-24 is closed as a labelling defect** — three s.4.9 rows are eligible; the six-source bar is not met |
| GAP-23 | s.13 | — | nothing here; s.13's second-sound primaries (Chester 1963, Sham 1967) were **not** searched for in this pass and are still open |

## What I did **not** do, and why

1. **Thompson (1972) is still not identified.** The supervisor's F14 names it alongside Moore–Gibson 1960, but neither OpenAlex nor the library surfaces a 1972 Thompson paper on relaxing-gas acoustics with a DOI. **Do not cite "Thompson 1972" until someone identifies the actual article**; the MGT lineage is defensible from B20 + A8–A11 + B18 alone.
2. **Chandrasekharaiah's 1988 piezoelectric thermoelasticity paper** is referenced in the plan as *LIT-0016*-adjacent material but I could not resolve a DOI in this pass (a guessed Acta Mechanica DOI returned an unrelated 1980 paper). It is **not** in the list rather than being listed with an unverified identifier.
3. **No OA search was run for the s.10 analysis papers beyond OpenAlex's flags.** A Unpaywall pass could find repository copies for B9/B10/B12; I did not run it because OpenAlex already reports `closed` for all three.
4. **No book was ordered twice:** B20, A11 and B15 are already in the base, and A5 is already a plan row. They appear here only so the handler sees the OA link or the duplicate.
