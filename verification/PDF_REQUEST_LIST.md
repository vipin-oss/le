# PDF request list — independent verification of the AMR review

**Task item:** B7a (`control/BRAVE_B7.md`, `origin/claude/control` @ `fafb778`).
**Prepared:** 2026-10-22. **Author:** independent verifier (this session).
**Companion files:** `PDF_REQUEST_LIST.csv` (machine-readable, same 33 rows, full text of every
"why" and "what to check" field), `V-B7a_pdf_request_list.md` (verification sheet),
`V-B7b_oa_fulltext_upgrade.md` (what I could read myself).

---

## 1. What this list is

33 papers, ranked. These are the papers whose **full text** decides a specific claim, table cell
or displayed equation in the manuscript. I have verified the DOI, journal, volume and pages of
each row against Crossref or the publisher page this session; where a name in the brief did not
resolve, that is stated rather than guessed (see §5).

The list is deliberately **not** a reading list for the whole field. 428 records are in
`LITERATURE_BASE.csv`; 33 of them carry a decision. Priority 1 items each block a HIGH-risk claim
in `CITATION_MAP.csv` or a printed equation.

**Please send PDFs in rank order when convenient. Partial batches are fine — send in rank order
and I will report on whatever has arrived.** Files named `<rank>_<firstauthor><year>.pdf` save me
a step; anything legible is fine.

## 2. Ranked list

Priority 1 = decides a HIGH-risk claim or a printed equation · 2 = decides a table cell,
attribution or bibliographic fact · 3 = background needed to position the review.
"Route" is the legal access path I could identify; **institutional login is the intended route for
every closed row.**

| # | P | Paper | DOI | Route | Why full text / what to check |
|---|---|---|---|---|---|
| 1 | 1 | Quintanilla & Racke 2006, *A note on stability in DPL heat conduction*, IJHMT 49(7–8):1209–1213 | 10.1016/j.ijheatmasstransfer.2005.10.016 | ScienceDirect + login | The τ_θ/τ_q > ½ threshold and the "always stable at first order" conclusion are quoted in V-B2p from a **publisher preview only**; conclusion 3 and two printed intervals (√2−1, and (√3−2, ½)) were corrupted by HTML conversion and are marked UNVERIFIED. Check §1 definition of x, eq. (1.4)'s truncation order, all three conclusions verbatim, and the hypotheses of the theorem. |
| 2 | 1 | Green & Lindsay 1972, *Thermoelasticity*, J. Elasticity 2(1):1–7 | 10.1007/BF00045689 | SpringerLink + login | CL-006 is HIGH risk and open: this is the **only** authority for the printed GL energy equation, and no record in the base reproduces it. Check the constitutive pair (β_ij(T + t₁Ṫ)), the printed entropy/energy balance, the ordering τ₁ ≥ τ₀ > 0 (CL-023), and whether τ₀ enters the heat equation or only the stress. |
| 3 | 1 | Wang & Li 2011, *Surpassing the fractional derivative*, Comput. Math. Appl. 62(3):1562–1567 | 10.1016/j.camwa.2011.04.028 | ScienceDirect (OpenAlex marks it **bronze** OA but the PDF endpoint refused my session) | Manuscript eqs (6.7)–(6.8) at `sec06_transport.tex:92–105` print the MDD operator and the quadratic kernel but the text itself calls them "inherited candidate". I verified only that they match a verbatim reproduction in a secondary source. Check the definition, the kernel's stated bounds and the admissible τ range. |
| 4 | 1 | Green & Naghdi 1992, *On undamped heat waves in an elastic solid*, J. Thermal Stresses 15(2):253–264 | 10.1080/01495739208946136 | Taylor & Francis + login | **This paper is not in `LITERATURE_BASE.csv` at all** — a gap, since GN-II is a column of Table 12-B. Check whether it prints q = k\*α,ᵢ with α̇ = θ and whether ordinary conduction k is absent (absent ⇒ type II). |
| 5 | 1 | Green & Naghdi 1993, *Thermoelasticity without energy dissipation*, J. Elasticity 31(3):189–208 | 10.1007/BF00044969 | SpringerLink + login | The GN-II/GN-III attribution is contradictory in my sources: a secondary source read this session (Sci Rep 2023) labels the 1991/92/93 series GN-I/II/III **and** uses this same paper as the source of the *undamped* equations. Table 12-B rows at `sec12:101,108` depend on resolving it. |
| 6 | 1 | Lord & Shulman 1967, *A generalized dynamical theory of thermoelasticity*, JMPS 15(5):299–309 | 10.1016/0022-5096(67)90024-5 | ScienceDirect + login | CL-018 HIGH: the manuscript writes c_p = √((λ+2μ)/ρ) with the **isothermal** λ where the adiabatic one belongs. Check which modulus the LS dispersion relation uses and whether the paper distinguishes them. |
| 7 | 1 | Guyer & Krumhansl 1964, *Dispersion relation for second sound in solids*, Phys. Rev. 133(5A):A1411–A1417 | 10.1103/PhysRev.133.A1411 | APS + login (legacy archive) | The real second-sound anchor that replaced the fabricated "Guyer 1990" (V-B5b). CL-026 and §13's imaging argument rest on it and I have never read it. Check the dispersion relation, the crossover criterion, and whether a **measurement** is claimed (it is a theory paper). |
| 8 | 1 | Moore & Gibson 1960, *Propagation of weak disturbances in a gas subject to relaxation effects*, J. Aerospace Sci. 27:117–122/136 | 10.2514/8.8418 | AIAA (ARC) + login | MGT is named after this paper, but T1 dates MGT to 2019 (B6a defect) and CL-025 rests on the vanishing-relaxation limit. Check the equation as printed, which term carries τ, and whether it is a gas-only result. |
| 9 | 1 | Barak et al. 2023, *Energy transfer at the interface of monoclinic piezothermoelastic and thermoelastic half spaces with MDD*, J. Thermal Stresses 47 | 10.1080/01495739.2023.2253879 | Taylor & Francis + login | Carries §9.7 (`sec09_interfaces.tex:140–200`) together with the Sci Rep paper I did read. CL-013/014/015 — absorption coefficient definition, per-mode numerators, and the attribution of a **closed** energy identity — are decided here. Check the definition of A, whether Σ ratios = 1 is claimed exactly or numerically, and the secular equation's order in q. |
| 10 | 1 | Sinha & Elsibai 1997, *Reflection and transmission of thermoelastic waves at an interface*, J. Thermal Stresses 20(2):129–157 | 10.1080/01495739708956095 | Taylor & Francis + login | The lineage sentence before §9.7. A name search returns the **1996 half-space** paper (10.1080/01495739608946205) instead — do not substitute it. Check interface conditions (CL-021), the secular equation's degree, and whether energy ratios are per incident wave or summed. |
| 11 | 2 | Green & Naghdi 1991, *A re-examination of the basic postulates of thermomechanics*, Proc. R. Soc. A 432(1885):171–194 | 10.1098/rspa.1991.0012 | Royal Society + login | V-B2d records that even its volume/pages were "cited from memory". A secondary source read this session gives 432(1885):171–194; corroborate from the front matter, then §2–3 for the no-dissipation postulates. |
| 12 | 2 | Guyer & Krumhansl 1966, *Thermal conductivity, second sound, and phonon hydrodynamic phenomena in nonmetallic crystals*, Phys. Rev. 148(2):778–788 | 10.1103/PhysRev.148.778 | APS + login | Second of the two real second-sound anchors. §6 motivates a relaxation time from phonon hydrodynamics; check what GK actually derived vs postulated, and whether a ∇²q term is printed. |
| 13 | 2 | Tzou 1995, *A unified field approach for heat conduction from macro- to micro-scales*, J. Heat Transfer 117(1):8–16 | 10.1115/1.2822329 | ASME Digital Collection + login | Origin of the phase-lag law and of the Taylor-truncation practice that §4.7–4.8 is about. Check eqs (1)–(3) as printed, the n−m = 0/1 discussion, and any warning against second order in **both** lags. Note: Quintanilla & Racke quote a Tzou remark from a **different** 1995 paper (IJHMT 38(17), p. 3237) — keep the three Tzou 1995 papers separate. |
| 14 | 2 | Roy Choudhuri 2007, *On a thermoelastic three-phase-lag model*, J. Thermal Stresses 30(3):231–238 | 10.1080/01495730601130919 | Taylor & Francis + login | DOI identified only this session by bibliographic query; closed. Check the TPL law as printed, the definition of τ_v, and the paper's own statement of how TPL sits between DPL and GN-III. |
| 15 | 2 | Chandrasekharaiah 1986, *Thermoelasticity with second sound: a review*, AMR 39(3):355–376 | 10.1115/1.3143705 | ASME Digital Collection + login | The predecessor AMR review of this exact sub-field; the review must position itself against it. Crossref (queried this session): 835 citations, 1986-03-01. Check the bibliography's cut-off and what it treats as established. |
| 16 | 2 | Chandrasekharaiah 1998, *Hyperbolic thermoelasticity: a review of recent literature*, AMR 51(12):705–729 | 10.1115/1.3098984 | ASME Digital Collection + login | Second predecessor AMR review (Crossref: 1149 citations, 338 references, "a glance" at DPL). Check whether DPL is presented as a variant or a distinct theory and how GN-II/III are named. |
| 17 | 2 | Barak, Kumar, Kumar & Gupta 2023, *Energy analysis at the boundary interface of elastic and piezothermoelastic half-spaces*, Indian J. Phys. 97(8):2369–2383 | 10.1007/s12648-022-02568-w | SpringerLink + login | §9.7 citation; with the Sci Rep paper it defines the construction compared against. Check ratio definitions, closure claim, secular order. |
| 18 | 2 | Barak, Kumar, Kumar & Gupta 2023, *The effect of memory and stiffness on energy ratios at the interface of distinct media*, MMMS 19(3):464–492 | 10.1108/MMMS-10-2022-0209 | Emerald + login | §9.7 citation. Check the MDD treatment (kernel and order), the closure claim, and the stated number of partial waves. |
| 19 | 2 | Gupta et al. 2023, *Reflection/transmission … ideal fluid and nonlocal piezothermoelastic medium*, IJNMF 33(2):912–937 | 10.1108/hff-04-2022-0259 | Emerald + login | The only §9.7 paper coupling a **nonlocal length scale** to the interface problem — where §7 and §9 meet. Check whether the interface condition is applied to the nonlocal or the local stress (sharpens CL-020). |
| 20 | 2 | Gupta et al. 2023, *Energy analysis at the interface of piezo/thermoelastic half spaces*, IJNMF 33(6):2250–2277 | 10.1108/hff-11-2022-0654 | Emerald + login | Closest in scope to the Sci Rep paper I read (same group, no memory). Check the sign of the electric term in the flux (the manuscript leaves the piezothermoelastic flux **OPEN** at `energy_flux_derivations.tex:317–344`): is it −φḊ or +φḊ? |
| 21 | 2 | Kumar, Gupta, Pathania & Barak 2023, *Energy ratio response … elastic and dual-porous thermoelastic half-spaces*, Phys. Scr. 98(11):115211 | 10.1088/1402-4896/acfced | IOPscience — **I opened it and the access banner said my instance is not registered**; record is flagged hybrid CC-BY-NC-ND. Route: university login | §9.7 citation, and the only one of the group whose second medium is dual-porous. Also corroborates the Mindlin piezo anchors in its refs 14–16. |
| 22 | 2 | Mindlin 1974, *Equations of high frequency vibrations of thermopiezoelectric crystal plates*, IJSS 10(6):625–637 | 10.1016/0020-7683(74)90047-X | ScienceDirect + login | **This is the correct fulfilment of the brief's "Mindlin 1961 piezothermoelasticity anchors".** No 1961 Mindlin paper is in the base and the manuscript cites no Mindlin at all; the anchor its own citation chain uses is this 1974 paper, credited by the Sci Rep paper (read this session) as the origin of the piezothermoelectricity equations. Check the constitutive relations, the p_i T term in D_i, and what the plate approximation discards. |
| 23 | 2 | Quintanilla 2002, *Exponential stability in the dual-phase-lag heat conduction theory*, JNET 27(3):217–227 | 10.1515/jnetdy.2002.012 | De Gruyter + login | The ½ threshold is attributed **by** Quintanilla & Racke 2006 to this earlier paper; the original proof and full page range are unread. Drops to priority 3 if row 1 arrives. |
| 24 | 2 | Eringen 1983, *On differential equations of nonlocal elasticity …*, J. Appl. Phys. 54(9):4703–4710 | 10.1063/1.332803 | AIP + login | The abstract and §7 claim "a standard Eringen-type nonlocal dispersion relation has a bounded high-wavenumber frequency". That is my derivation from the differential form; check whether Eringen states it, and under what kernel condition the differential form is exact. |
| 25 | 3 | Quintanilla & Racke 2007, *Qualitative aspects in DPL heat conduction*, Proc. R. Soc. A 463(2079):659–674 | 10.1098/rspa.2006.1784 | Royal Society + login | Prints the threshold as τ_θ > τ_q — a **different** threshold from the 2006 paper's ½. Both texts are needed to state this without merging them. |
| 26 | 3 | Rukolaine 2014, *Unphysical effects of the dual-phase-lag model of heat conduction*, IJHMT 78:58–63 | 10.1016/j.ijheatmasstransfer.2014.06.066 | ScienceDirect + login | The review's DPL criticism is attributed here at metadata level only, and it is a **different** criticism from the truncation-dependent stability result in V-B2p. Check which truncation Rukolaine attacks and what the unphysical effect is. |
| 27 | 3 | Mindlin 1964, *Micro-structure in linear elasticity*, ARMA 16(1):51–78 | 10.1007/bf00248490 | SpringerLink + login | CL-016 quotes σ = Cε − ℓ²C∇²ε and its well-posedness from Mindlin 1964 + Tiersten 1962 + Eringen 1972, at metadata level. Check whether the printed theory has a Laplacian-of-strain term and how many extra boundary conditions it needs. |
| 28 | 3 | Mindlin & Tiersten 1962, *Effects of couple-stresses in linear elasticity*, ARMA 11(1):415–448 | 10.1007/bf00253946 | SpringerLink + login | CL-020: the manuscript derives σ_ij symmetry with no couple stress in a review with whole sections on micropolar media. Check the printed equilibrium and whether the stress is symmetric. |
| 29 | 3 | Eringen 1972, *Linear theory of nonlocal elasticity and dispersion of plane waves*, IJES 10(5):425–435 | 10.1016/0020-7225(72)90050-x | ScienceDirect + login | B6a defect D5: Table 12-B sources a **thermal** law ("Cattaneo", "τ (kernel)") to this paper, whose verified title is an isothermal theory. Check its contents so the cell can be re-sourced correctly. |
| 30 | 3 | Biot 1956, *Thermoelasticity and irreversible thermodynamics*, J. Appl. Phys. 27(3):240–253 | 10.1063/1.1722351 | AIP + login | CL-028: the Clausius–Duhem inequality and Coleman–Noll restrictions are marked UNVERIFIED in the equation register while being derived in the text. Check the entropy-production inequality as printed and the sign convention. |
| 31 | 3 | Tzou 1995, *Experimental support for the lagging behavior in heat propagation*, J. Thermophys. Heat Transfer 9(4):686–693 | 10.2514/3.725 | AIAA (ARC) + login | Cited twice this session (Chiriţă et al. 2017; Sci Rep 2023) for the n = p / n = p−1 relation. Check what experiment is claimed and at what scale. |
| 32 | 3 | Ackerman, Bertman, Fairbank & Guyer 1966, *Second sound in solid helium*, PRL 16(18):789–791 | 10.1103/PhysRevLett.16.789 | APS + login | The one paper in the set that reports a **measurement**. CL-026 ("second sound was measured") should rest on it, not on the 1964/66 theory papers. |
| 33 | 3 | Quintanilla & Racke 2008, *A note on stability in three-phase-lag heat conduction*, IJHMT 51(1–2):24–29 | 10.1016/j.ijheatmasstransfer.2007.04.045 | ScienceDirect + login | §4.8's TPL stability statements are bibliographic-only in V-B2h. Every §9.7 source is TPL or DPL, so a wrong TPL stability statement propagates into the interface section. |

## 3. Mandatory items from the brief — coverage

| Brief item | Row(s) | Note |
|---|---|---|
| Green & Lindsay 1972 | 2 | |
| Roy Choudhuri 2007 | 14 | DOI resolved this session |
| Quintanilla & Racke 2006 (typeset) | 1 | exactly the missing typeset; V-B2p §7.2 already lists what is corrupted in the preview |
| Sinha & Elsibai 1997 | 10 | **1997** interface paper, not the 1996 half-space paper |
| Moore & Gibson 1960 | 8 | |
| Lord & Shulman 1967 | 6 | |
| Green & Naghdi 1991–1993 | 4, 5, 11 | 1992 is **missing from the base**; 1993's type-II/III role is contradictory across my sources |
| Tzou 1995 | 13, 31 | two different 1995 papers; a third is quoted second-hand — not merged |
| Wang & Li 2011 | 3 | bronze-OA but the PDF endpoint refused me |
| Guyer & Krumhansl 1964/1966 | 7, 12 | 1964 = the anchor that replaced the fabricated "Guyer 1990" |
| Chandrasekharaiah 1986 and 1998 AMR | 15, 16 | both Crossref-confirmed this session (39(3):355–376; 51(12):705–729) |
| Barak/Gupta interface papers cited in §9.7 | 9, 17, 18, 19, 20, 21 (+ Sci Rep 2023 already read) | seven citations in `sec09_interfaces.tex:140–200`; the Sci Rep one is gold OA and is **not** a request row |
| Mindlin 1961 piezothermoelasticity anchors | 22 | **the 1961 reference did not resolve**; the anchor actually used is Mindlin 1974 (DOI verified). See §5. |

## 4. Already open access — read by me, no request needed

These were in the candidate set and I read them myself; details in `V-B7b_oa_fulltext_upgrade.md`.

| Paper | Legal OA route used | Read level now |
|---|---|---|
| Barak, Ahmad, Kumar et al. 2023, Sci Rep 13, `10.1038/s41598-023-44339-5` | publisher gold OA (CC-BY) | **FULL** |
| Chiriţă, Ciarletta & Tibullo 2017, IJHMT 114:277–285, `10.1016/j.ijheatmasstransfer.2017.06.071` | arXiv:2103.10068 (submitted version) | **FULL** |
| Quintanilla 2019, *MGT thermoelasticity*, MMS 24(12):4020–4031, `10.1177/1081286519862007` | UPC repository `hdl.handle.net/2117/169798` | **FULL** |
| Kovács & Ván 2018, *Thermodynamical consistency of the DPL equation*, CMT, `10.1007/s00161-017-0610-x` | arXiv:1709.06825 | **FULL** |
| Kovács & Ván 2018, *Second sound and ballistic heat conduction: NaF experiments revisited*, IJHMT, `10.1016/j.ijheatmasstransfer.2017.10.041` | arXiv:1708.09770 | **FULL** |
| Bongarti, Charoenphon & Lasiecka 2021, *Vanishing relaxation time dynamics of the JMGT equation*, JEE, `10.1007/s00028-020-00654-2` | arXiv:2011.11141 | **FULL** (preprint of the journal paper) |

Marked bronze/hybrid OA but **not** readable from this environment: Wang & Li 2011 (row 3) and
Kumar et al. 2023 Phys. Scr. (row 21). OA metadata is not reading; both stay request rows.

## 5. Two item-level corrections to the brief

1. **"Mindlin 1961 piezothermoelasticity anchors"** — no 1961 Mindlin paper exists in
   `LITERATURE_BASE.csv`, and a grep of every `.tex` file in the manuscript tree returns **zero**
   occurrences of "Mindlin" outside the bibliography rows at §7. The anchor that the manuscript's
   own citation chain actually uses is **Mindlin 1974**, IJSS 10(6):625–637,
   `10.1016/0020-7683(74)90047-X`, credited in Barak et al. 2023 (read this session) as the origin
   of the piezothermoelectricity governing equations. Row 22 is therefore that paper. I could not
   locate any 1961 Mindlin item, so none appears in the list.
2. **Green & Naghdi 1992** — the base holds 1991 and 1993 only. The 1992 J. Thermal Stresses paper
   (`10.1080/01495739208946136`, 15(2):253–264, verified in V-B2e against Crossref) is absent. I
   have **not** added it to the base: that changes the accepted count of 428, and the decision is
   Claude's. It is recorded as row 4 instead.

## 6. What I will do when PDFs arrive

Per paper: record authors/year/title/venue/pages/DOI/access date/access level; read only for the
specific item in the "what to check" column; write the result into the V-sheet that owns the claim
(`V-B2c`, `V-B2e/f`, `V-B2p`, `V-B6a`, …) rather than a new file per PDF; raise `read_level` to FULL
in `LITERATURE_BASE.csv` **only** for what I actually read; and state explicitly which verdicts in
`CLAIM_LEDGER.csv`/`EQUATION_LEDGER.csv` change. No verdict changes without the paper in hand.

## 7. NOT verified / open issues in this list

1. Two DOIs are quoted from a source I read but did not query at the registrar: Ackerman 1966
   (`10.1103/PhysRevLett.16.789`, from `LITERATURE_BASE.csv`) and Tzou's AIAA paper
   (`10.2514/3.725`, from Chiriţă et al. 2017's reference list, read this session). Both are
   consistent with the records I did see; neither was confirmed at Crossref in this session.
2. Page ranges for rows 9 and 14 carry a year-only or partial pagination: Barak et al. JTS is a
   2023-online / vol. 47 print item and I could not confirm the page range; Roy Choudhuri's pages
   (231–238) come from Crossref, which for this record omits the issue in one field.
3. Row 22 (Mindlin 1974) is included on the strength of a **secondary** attribution. Whether the
   manuscript *should* cite it at all is Arena's decision, not mine.
4. I have not checked whether the handler's institution subscribes to Taylor & Francis, Emerald,
   ASME, De Gruyter or APS. Those routes are inferred from the publisher, not from a
   subscription list.
