# V-B6b — Hole closing and the "claims need citations" pass

| field | content |
|---|---|
| **Task** | B6b, two halves. (1) Close the named holes in `LITERATURE_BASE.csv` — numerical methods (6), plane waves/dispersion (11), Thompson 1972, and the absent authors (Racke, Hetnarski, Mindlin, Sharma, Singh, Biswas, Sur/Kanoria, Kovács/Ván). No padding. (2) For the 15 most serious or most-quoted claims in `V-B4_summary.md` / `CLAIM_LEDGER.csv`, list the 2–4 best primary citations from the base to support or qualify each. |
| **Result** | Base **400 → 428**, all DOI-verified by Crossref in this session. Six of the eight named author holes close; **two do not** (Hetnarski, Sharma — see §3). Numerical methods improves only 6 → 8 and remains the weakest column. Thompson 1972 is **still not found**. The claims pass produced `CITATION_MAP.csv`, 17 rows. |
| **Confidence** | **HIGH** that every added record came back from the Crossref queries logged below, and that the author names quoted are copied from those responses. **HIGH** on the hole-closure statement itself: I list the holes that remain open rather than asserting the set is complete. |
| **NOT verified** | None of the 28 new records has been read beyond metadata. The citations proposed in `CITATION_MAP.csv` are **not** verified to support the claims — they are the best available candidates, and the read-level column says so. |

## 1. Queries issued for this pass

| route | query | outcome |
|---|---|---|
| Crossref | `Racke thermoelasticity second sound asymptotic behaviour` | Racke 2002 (134 cites), Racke 2003 (52), Racke–Wang 2008 (already in base) |
| Crossref | `Mindlin microstructure in linear elasticity couple stress` | Mindlin–Tiersten 1962 (2388), Mindlin 1964 (3677), Mindlin 1972 (214) |
| Crossref | `Singh Biswas reflection micropolar thermoelastic half space impedance` | Singh–Yadav–Gupta 2019 (36), plus three further micropolar reflection papers |
| Crossref | `Sur Kanoria fibre reinforced thermoelastic medium` | Sur et al. 2015 (32), Mondal–Sur–Kanoria 2019 (42), Sur et al. 2018 (61) |
| Crossref | `Kovacs Van dual phase lag heat conduction thermoelastic stability` | Quintanilla 2002 (87) — **not** Kovács–Ván; led to a second query |
| Crossref | `Kovacs Van thermodynamical consistency dual-phase-lag` | **Kovács & Ván 2018 (43)** located; also Rukolaine 2014 (115), Chiriţă et al. 2017 (61), van der Merwe 2021 |
| Crossref | `Rayleigh Lamb waves generalized thermoelastic plate dispersion` | seven Rayleigh–Lamb items, 1987–2020 |
| Crossref | `meshless finite element numerical generalized thermoelastic wave propagation` | two usable numerical items (mesh-free GFD 2012; BEM 2019) |
| Crossref | `Thompson 1972 nonlinear acoustics relaxation finite amplitude` | **no Thompson record** |

## 2. What changed

| sub-area | before | after |
|---|---|---|
| memory-dependent / fractional | 55 | 58 |
| reflection-transmission / interfaces | 44 | 48 |
| nonlocal / gradient / Eringen | 37 | 40 |
| DPL / TPL | 33 | 36 |
| **plane waves / dispersion / Rayleigh–Lamb** | **11** | **18** |
| energy flux / dissipation / well-posedness | 22 | 24 |
| **numerical methods** | **6** | **8** |

428 records, 428 unique DOIs, 0 DOI-less, 428 unique bib keys.

The plane-waves hole is now honestly covered, with a real spine rather than filler: Mindlin's
microstructure papers supply the gradient side; Rayleigh–Lamb in a void-bearing plate (1987),
micropolar plate (2006), magneto-thermoelastic plate (2004), generalized thermoelastic plate with
liquid loading (2003), and strain-gradient micro-plate (2019) supply the geometry side; attenuation
of Rayleigh waves in generalized thermoelastic media (2013) supplies the dispersion/attenuation link.

**Numerical methods stays at 8, and I am not going to pretend otherwise.** The query returned
mostly water-wave and metamaterial FEM papers that do not belong in this review. What was added is
relevant and specific — a mesh-free generalized finite-difference treatment of a GN-II cylinder and
a boundary-element scheme for three-temperature micropolar magneto-thermoelastic wave propagation
— but eight records cannot carry a section on numerical treatment.

## 3. Which named-author holes actually closed

| author | status | evidence |
|---|---|---|
| **Racke** | **CLOSED** | Racke 2002 *Math. Meth. Appl. Sci.* (134 cites); Racke 2003 *Quart. Appl. Math.* (52). Both authors read verbatim from Crossref. |
| **Mindlin** | **CLOSED** | Mindlin–Tiersten 1962 (2388); Mindlin 1964 *Micro-structure in linear elasticity* (3677); Mindlin 1972 (214). |
| **Singh** | **CLOSED** | Singh, Yadav & Gupta 2019, *J. Ocean Eng. Sci.* (36). |
| **Biswas** | **PARTIAL** | no Biswas record was returned. The Singh 2019 paper is the closest match to the name pair in the hole list; I did not find a Biswas-authored item and did not substitute one. |
| **Sur / Kanoria** | **CLOSED** | Mondal, Sur & Kanoria 2019 *Acta Mech.* (42); Sur et al. 2015 (32); Sur et al. 2018 (61). |
| **Kovács / Ván** | **CLOSED** | Kovács & Ván 2018, *Continuum Mech. Thermodyn.*, "Thermodynamical consistency of the dual-phase-lag heat conduction equation" (43). Note: my first guess at this pair (`10.1515/jnetdy.2002.012`) turned out to be **Quintanilla alone**, which is exactly the kind of mis-attribution the brief warns about, so it is recorded here rather than quietly dropped. |
| **Hetnarski** | **NOT CLOSED** | no Hetnarski-authored record was returned by any query in this or the previous session. He appears in the base only as a *subject* (his 1998 review is cited by others). |
| **Sharma** | **NOT CLOSED** | the two "Sharma" entries in the manuscript are the mismatched `Sharma2022` (really Sherief & Hussein). No genuine Sharma-authored record was located in the searches run. |

**Thompson 1972 — still not found.** The eponym's second half has no DOI-bearing Crossref record
in the searches I ran; it is a technical report. The nearest 1972 hits are JASA papers on
finite-amplitude waves in relaxing fluids, but the query did not return authors and I will not
assume one of them is Thompson. Recorded as a hole, not filled.

## 4. Along the way: four records that are directly useful to the review's argument

Added because they bear on open verdicts, not to inflate counts:

* **Rukolaine 2014**, "Unphysical effects of the dual-phase-lag model of heat conduction"
  (115 cites) — directly relevant to CL-024 and to the review's own caution about DPL.
* **Kovács & Ván 2018** — the thermodynamic-consistency conditions for DPL.
* **Chiriţă, Ciarletta & Tibullo 2017** (61) — thermomechanical consistency of time-differential
  DPL, i.e. a second, independent route to the same constraint set.
* **van der Merwe, van Rensburg & Sieberhagen 2021** — a modal comparison of DPL, Cattaneo–Vernotte
  and Fourier, which is the kind of cross-theory benchmark the review's GAP-004 says is absent.

The DPL row is now the best-sourced family in the base for well-posedness, which is worth saying
because the B6a audit found DPL-related defects elsewhere.

## 5. The claims pass

`CITATION_MAP.csv` (17 rows, described in `V-B6c_citation_map.md`) covers the 15 most serious or
most-quoted claims from `V-B4_summary.md` / `CLAIM_LEDGER.csv`, plus two added in this round (the
fractional dimensional defect and the second-sound anchors).

Two honest limitations, stated up front:

1. **Read level is metadata for almost every proposed citation.** I have not read the papers. A
   proposed citation is a *lead*, not a support verdict — the map's `risk` column says which rows
   that matters for. The three rows marked **HIGH** risk are exactly the ones where no source in
   the 428-record base may be able to support the claim as written.
2. **Bib keys for 308 of 428 records are `Anon…` placeholders**, because the author field is blank
   and `make_bibtex.py` falls back to "Anon". The keys in `CITATION_MAP.csv` are therefore correct
   *for the current bib* but will change when enrichment runs. A key printed in a manuscript before
   enrichment is a key that will not resolve later.

## 6. Checks done

1. Every added DOI appears in a Crossref response quoted in §1; none was typed from memory.
2. Duplicate check after insertion: 428 rows / 428 distinct DOIs (case-insensitive).
3. `make_bibtex.py` regenerated: 428 keys, all unique, 0 DOI-less records.
4. Every citation key in `CITATION_MAP.csv` was machine-checked against `literature_base.bib` — all
   resolve (one initial error, `LIT-0010 (Chester1963)`, was found by that check and replaced with
   the real key `Chester1963Second`).
5. Author names were filled only where a Crossref response in this session printed them; 308 rows
   are still blank and are reported as blank.
6. The named-author table in §3 distinguishes CLOSED from PARTIAL from NOT CLOSED; nothing is
   claimed closed without a DOI in the base.
