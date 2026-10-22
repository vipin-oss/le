# Independent verification — Phase B1

Role: independent verifier. I did not see, and did not edit, the manuscript. Everything below was derived or checked from sources I could open; everything I could not check is listed under each file's "NOT verified" heading.

**Phase status: B1 complete (a, b, c) and revised after supervisor audit; B2 complete (a–m, z). B3 not started — awaiting go-ahead.**

## Phase B2 files

| File | Model | Overall status |
|---|---|---|
| `V-B2a_biot-fourier.md` | Fourier / Biot | usable |
| `V-B2b_lord-shulman.md` | Lord–Shulman | usable |
| `V-B2c_green-lindsay.md` | Green–Lindsay | **do not print GL equations without the 1972 paper (form not source-verified)** |
| `V-B2d_green-naghdi-I.md` | GN Type I | usable — establishes GN-I ≡ Biot |
| `V-B2e_green-naghdi-II.md` | GN Type II | usable |
| `V-B2f_green-naghdi-III.md` | GN Type III | usable with the variant problem stated |
| `V-B2g_dual-phase-lag.md` | DPL (Tzou) | usable; ill-posedness threshold verified |
| `V-B2h_triple-phase-lag.md` | TPL (Roy Choudhuri) | **needs the 2007 paper (form unresolved)** |
| `V-B2i_moore-gibson-thompson.md` | MGT (Quintanilla) | usable; γ = b − τc² > 0 independently verified |
| `V-B2j_memory-dependent-derivative.md` | MDD (Wang & Li) | usable with kernel stated |
| `V-B2k_caputo-fractional.md` | Caputo fractional | usable |
| `V-B2l_two-temperature.md` | Two-temperature | usable |
| `V-B2m_eringen-mindlin-nonlocal-gradient.md` | Eringen nonlocal + Mindlin gradient | usable |
| `V-B2z_comparison_table.md` | **comparison table + 14-entry mistakes catalogue** | the deliverable to read first |
| `V-B2_wave_speeds.py` | reproducible engine: all dispersion relations, 5 limit checks, numerics | runs standalone (needs numpy, sympy) |

**Headline B2 results:** (i) GN Type I *is* Biot — a nine-model list inflation; (ii) GL has no flux relaxation, contrary to a common description; (iii) DPL with τ_T < 0 is ill-posed above k_c = 1/√(κ|τ_T|), verified numerically; (iv) MGT's stability number γ = b − τc² > 0 independently reproduced, and positivity of τ, b, c² is not sufficient; (v) nonlocal and gradient elasticity differ by a factor 10⁶ at identical parameters; (vi) fractional/MDD models do **not** fix the infinite-speed problem; (vii) five symbolic limit checks pass — after they caught a sign error of mine.

## Files

| File | Contents | Confidence |
|---|---|---|
| `V-B1a_amr-landscape.md` | 13 AMR reviews 2018–2026 (metadata, refs, cites, page counts), descriptive statistics, AMR length/author policy with quotes, and the finding that AMR has no recent thermoelasticity review | HIGH on bibliographic + policy; MEDIUM on page statistics; figures/tables UNVERIFIED |
| `V-B1b_competing-reviews.md` | 14 existing reviews/primary sources across 5 sub-areas, coverage/omission assessment, honest "is the field covered?" verdict, ranked list of what a constructive review can add | HIGH on bibliography; MEDIUM on coverage judgements (no full texts read) |
| `V-B1c_most-cited.md` | 15 most-cited papers with Crossref **and** OpenAlex counts, runner-ups, index-dependent rank pairs flagged, and explicit statement that Google Scholar/Scopus/WoS were unavailable | HIGH as Crossref/OpenAlex counts; NOT a Google Scholar ranking |

**Revision log (after supervisor audit of B1):** (1) the "Length: open" quote in V-B1a now carries the exact URL, the exact sentence, the read date and a note that it is an ASME-wide page, not an AMR-specific one; (2) AMR digitisation caveat added for the 1998 Chandrasekharaiah DOI (print 1998, publisher page 2009); (3) the 2026 Research Square preprint is re-characterised in V-B1b from its verified 15-section list — overlap is partial, and it has **no** interface-partition, two-temperature, MDD, fractional or piezothermoelastic content; (4) OpenAlex counts added for all 15 rows in V-B1c, with the two index-dependent rank swaps flagged.

## Environment constraints (affect what "verified" means here)

- Direct `curl` from the sandbox to the open internet is blocked (`asmedigitalcollection.asme.org`, `doi.org`, `scholar.google.com`, `api.crossref.org` all returned HTTP 000). The web-fetch and web-search tools *do* have access, so all lookups were routed through them.
- **Google Scholar is unreachable.** Scopus and Web of Science have no credentials. Citation counts therefore come from **Crossref** `is-referenced-by-count` and **OpenAlex** `cited_by_count`, plus **Semantic Scholar** for cross-checks. These are systematically lower than Google Scholar counts (see V-B1c).
- **No subscription access to ASME, Taylor & Francis, Elsevier, Springer or OUP full texts.** All PDF links redirect to paywalled abstract pages. Consequence: page counts are verifiable (printed on the publisher's abstract page), but **figure counts, table counts and section counts are not**, and no competing review's body text could be read.
- AMR stopped depositing page ranges to Crossref around 2018 and now uses article numbers (`040801`), so "number of pages" for recent AMR articles is only obtainable from the publisher's article page or the PDF.

## Conventions used

- Every factual claim about a paper carries DOI (or stable publisher URL) and the read level: *record only* / *abstract* / *body*.
- Negative results ("no review exists on X") are stated together with the search that produced them and the bound on their strength.
- Citation counts always name the index and the retrieval date (all 2026-10-22).
- Confidence labels in each file refer to that file's claims, not to the project as a whole.

## Standing open items for the handler

1. **Figures/tables/sections for the 13 AMR reviews** need ASME access; the DOIs are listed in V-B1a and the columns can be filled quickly once PDFs are available.
2. **The 2026 Research Square preprint** "Thermodynamic Admissibility, Finite-Speed Heat Transport, and Wave Stability in Generalized Thermoelasticity: A Critical Review with Analytical Proofs" (DOI 10.21203/rs.3.rs-10734164/v1) targets nearly the same scope as this project. It is unrefereed. Someone should track whether it is published.
3. **V-B1c must not be presented as a Google Scholar ranking.** Re-run with GS/Scopus if available.

## Phase B2 revisions (R1–R5) — 2026-10-22

Orders: `control/BRAVE_B2_REVISIONS.md` @ `origin/claude/control` `db71198`.

| File | Order | Outcome |
|---|---|---|
| `V-B2p_dpl-truncation-order.md` (+ `V-B2p_dpl_truncation_check.py`) | R1 | **Table cell was wrong.** DPL finite speed is truncation-dependent: T2 (2nd order τ_q, 1st τ_θ) **does** have finite speed c∞ = √(2κτ_θ)/τ_q; T1 infinite; T4 band-limited. Stability is **τ_θ > τ_q/2** — the recalled `τ_q > τ_T/2` has the **wrong direction** (Q&R 2006 + independent Routh–Hurwitz). |
| `V-B2c_green-lindsay.md` §R7 | R2 | Mapping to (τ₀,τ₁) given; found a **notation defect** in my own (τ₁,τ₂) scheme (two symbols, three slots); corrected GL's speed to **c_h = √(κ/τ₀)** (verified); ordering **not** asserted — GL stays **do not print**. 1972 still not opened. |
| `V-B2n_piezothermoelasticity.md` | R3 | Structure-level file: 5 ingredients, quasi-static E, what it neglects, stiffening β→β−ep/ε (verified), mode-count correction (quasi-static electric = **constraint, not a mode**), 8 pitfalls. **No primary full text.** |
| `V-B2o_guyer-krumhansl.md` | R4 | Depth-marked overview. GK has **no finite speed for ℓ>0** (band-limited second sound); ℓ=0 ⇒ Cattaneo. Factor-3 convention flagged. |
| `V-B2q_micropolar-porous-semiconductor.md` | R4 | Depth-marked overview. **Classification:** all three are kinematic/transport enrichments, *not* heat-law generalisations — they inherit the thermal speed. Semiconductor part **UNVERIFIED** (no source). |
| `V-B2z_comparison_table.md` | R5 | Two new columns (**primary source opened?** = *no* everywhere; **printable as-is?**), DPL and GL cells corrected, two new rows (piezothermoelastic, GK), grouping fact 1 corrected. |

**Read levels after the revisions:** primary full texts opened = **1** (Dreher, Quintanilla & Racke
2009, *Appl. Math. Lett.* 22:1374–1379 — full text via Elsevier open archive). Abstract/summary
level = 3 (Q&R 2006 IJHMT preview; Q&R 2007 RSPA abstract; Chandrasekharaiah 1988 abstract).
Everything else is bibliographic record or secondary. **No model's *originating* paper has been
read.**

## Phase B3 — energy balance, R/T/A, literature (2026-10-22)

Orders: `control/BRAVE_NEXT.md`.

| File | Content | Headline |
|---|---|---|
| `V-B3a_energy-balance-interface-flux.md` | Energy identity, flux and interface conditions **per model** (Biot, LS, GL, GN-II, GN-III, MGT) | **GN-II is the only model with a conserved energy** (D≡0, verified by substitution). LS flux carries $(1-i\omega\tau_0)^{-1}$; **GL's flux is plain Fourier** (its relaxation is in the stress/energy); GN-III needs **both** channels in $[q_n]$. **MGT: no canonical flux** — a third-order model has no unique energy functional, so its $R/T$ is undefined without stating a choice; it also needs **3** interface conditions, not 2. |
| `V-B3b_RTA-conditions.md` | Conditions (C1)–(C5) for $R+T+A=1$; numeric example | **A refuted hypothesis, logged:** $A=0$ to machine precision at an *ideal* interface for **all five** computed models, including the dissipative ones — because the flux amplitudes share a common phase, so bulk dissipation lives inside complex $k$ (i.e. inside $T$), not in $A$. $A\neq0$ requires Kapitza resistance ($A$ up to $8.0\times10^{-2}$, non-monotonic in $h$) or a phase mismatch ($A=1.2\times10^{-4}$ for $\tau_0$ mismatch). **Corollary for the review: a reported $R+T=1$ is a consequence of the interface conditions, not a validation.** |
| `V-B3c_reflection-transmission-literature.md` | Six Crossref-verified records + checklist | **Record-level only; no full text opened.** No paper was located that reports flux-based $R/T/A$; most located work is free-surface *amplitude* reflection. GN-II source paper now Crossref-verified (Green & Naghdi 1993, *J. Elasticity* **31**:189–208, `10.1007/BF00044969`, 2194 cites). Largest gap: **classical (Biot) interface $R/T$ citations**. |
| `V-B3_rta.py` | Solver + all numeric checks | Identical-media test $r=0,t=1,A=0$ **exactly** for all five models; $\lvert R+T+A-1\rvert=0$ ($\le10^{-16}$); $\omega\tau_0\to0$ recovers Biot; $A(h)\to0$ at both $h$ extremes. MGT excluded with the reason printed. |

**Coupled-system stability status (requested with B3a) remains UNVERIFIED** for every model — the
files state this explicitly rather than extrapolating the rigid-conductor results.
