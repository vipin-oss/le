# What is new, compared with earlier reviews — one page for the submission file

**Manuscript.** *Waves in Thermoelastic and Multiphysics Continua: Generalized Heat Conduction, Coupled Fields and Size Effects.*

**Status of this page.** The block in §1 is the quotable statement (120 words, within the 120-word limit). The table in §2 is a working note, not part of that block: it maps each claim to where it is delivered in the manuscript and to what the earlier reviews of the field contain. It exists so that an editor or referee can check the claims rather than take them on trust.

---

## 1. The statement (111 words)

> What is new here:
> (1) one heat-flux template with three lags, from which the named theories follow as parameter choices, regular and singular limits separated (Sec. 3.2.4, Table 4);
> (2) a dispersion polynomial in K = k² for rational heat laws, checked symbolically, permitting like-for-like comparison of speed, attenuation, damping (Eq. (34), App. B);
> (3) the dual-phase-lag stability threshold shown to depend on the Taylor truncation, three thresholds distinguished (Sec. 4.3.1, Fig. 10);
> (4) quantified limits of truncated lag laws against the exact delay (Sec. 4.4.2, Fig. 12);
> (5) a page-level provenance table separating checked from repeated attributions (Table 6);
> (6) a five-axis taxonomy, a pitfalls checklist and a decision guide (Sec. 10.1-10.2).

---

## 2. Working note: where each item is delivered, and what it goes beyond

| # | Claim | Delivered in | Verified by | Relationship to the earlier reviews [6]–[10], [158] |
|---|---|---|---|---|
| 1 | One template, three lags, named theories as parameter choices | Sec. 3.2.4, Eq. (14)–(15), Table 4 (p. 13–14); Sec. 4.2, Table 7 | `check_reductions.py`; reductions stated as exact or singular limits | The earlier reviews present the theories one at a time, in historical order ([6], [7]) or in a stability-and-uniqueness frame ([8]–[10]). The template with an explicit parameter vector, and the identification of τ_q → 0 at fixed τ_T as singular, is not, to the author's knowledge, in them. |
| 2 | Dispersion polynomial in K = k² valid for all rational laws | Eq. (34) (p. 23); Appendix B (p. 96) | `check_dispersion.py` (symbolic determinant equals the polynomial, difference zero); Eq. (28) checked against numerical roots to 10⁻¹⁰ | Chandrasekharaiah (1986) and Hetnarski–Ignaczak (1999) give dispersion relations model by model; no comparative polynomial in this form was found in them. |
| 3 | DPL stability threshold depends on the truncation | Sec. 4.3.1 (p. 30–31), Fig. 10; pitfall 1 of Sec. 10.1.4 | `fig_stability.py`: largest real part of the temporal roots, maximised over wavenumber | The three thresholds are individually in the literature ([43], [10, 158], [159]). The point that the commonly quoted condition belongs to one truncation, and that a paper applying it to another is applying the wrong condition, is the review's own. |
| 4 | Limits of truncated lag laws against the exact delay | Sec. 4.4 (p. 34–35), Fig. 12; the error table at ωτ_q = 0.05, 0.1, 0.3, 1 | `fig_lag_truncation.py`; the exact root k_w = √(ρcω/k)·exp(i(π/4 − ωτ_q/2)) | Tzou (2015) discusses the truncation as a modelling device; a tabulated error against the exact delay, and the ωτ_q ≈ 0.3 rule, were not found there. |
| 5 | Page-level provenance, with what each check does not cover | Sec. 2.4, item 4; Table 6 (p. 29) | The primary texts named, with page and equation numbers | None of the six reviews gives a per-attribution provenance table; the convention in the earlier literature is a citation without a page. |
| 6 | Five-axis taxonomy, pitfalls checklist, decision guide | Sec. 10.1.2, Table 14 (p. 85); Sec. 10.1.4, 17 items (p. 86); Fig. 40 (p. 87) | Internal consistency with Tables 15–16 and Section 11.1 | Ignaczak–Ostoja-Starzewski (2010) closes with open problems; Tzou (2015) with applications. A taxonomy in which a model is a point in a product of axes, and a decision sequence keyed to ωτ and ω/ω\*, is the review's own construction. |

---

### Notes for the author

* Item (3) must not go out until the papers that state τ_T ≥ τ_q/2 for the first-order model are cited (see `referee_report.md`, finding R4). The claim "the commonly quoted condition belongs to another truncation" needs its examples; without them the item should be softened to "the condition is sometimes quoted" and the word "demonstration" replaced by "analysis".
* Item (1) says "the named theories follow as parameter choices"; Green–Lindsay, fractional and memory-dependent laws do **not** follow from Eq. (14), and the statement above deliberately does not list them. The manuscript's abstract does list them, which is finding R12 of the referee report. Keep this page and the abstract consistent once the abstract is revised.
* The word counts above refer to the block in §1 only, as declared in the header.
