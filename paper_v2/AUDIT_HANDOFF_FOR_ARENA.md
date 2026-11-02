# Independent critical audit: handoff for Arena (full read required)

Paper: "Waves in Thermoelastic and Multiphysics Continua: Generalized Heat Conduction, Coupled Fields and Size Effects" (target: Applied Mechanics Reviews, ASME).
Files: `submission/main_clean.pdf` (155 pp), `submission/main_submission_lineno.pdf` (line numbers), `overleaf_package.zip` (LaTeX sources), `paper_sources.zip`.

## Task for Arena
Read the ENTIRE manuscript (all sections and appendices, not a sample), as a critical AMR reviewer. Do not edit sources. Produce a report with: (1) errors (equation, sign, number, cross-reference, citation), each with page/line number and a suggested fix; (2) internal contradictions between text, summary boxes, tables and captions; (3) claims stronger than the evidence; (4) missing literature (give verified DOI for each suggestion); (5) structure/length issues; (6) a ranked top-10 list for the author. Verify numbers by recomputation, not by pdf text extraction alone (bracket glyphs get dropped; check LaTeX source).

## Already found by Claude (do not just repeat; confirm or refute, then go beyond)
Verified independently (OK): Eq. 21 (Re G), Eq. 24 (Routh-Hurwitz), EIT identity (Eq. 12-13), DPL stability thresholds (variant ii: tau_T = tau_q/2, growth 0.571 at 0.3; variant iii: 2-sqrt3; variant i stable), Table 3 f* for Al/Cu/steel.

Found problems:
1. Eq. 20 (sum rule, sections/s03c_prelim.tex) prints (v0 - v_inf)/vbar, but v0 (isothermal) < v_inf (adiabatic), so RHS is negative while LHS is positive; the Debye example uses the correct sign. Fix: (v_inf - v0).
2. Experiments section: body says pump-probe measures an electron-phonon coupling time, not tau_q; the Summary box says pump-probe and ultrasonic damping "can determine lags independently". Contradiction.
3. Experimental evidence is thin (about 1.2 pages) relative to the title ("size effects", "multiphysics"); resonator-Q subsection has no citations; absent authors in refs: Straughan, Kovacs, Van, Cimmelli, Minnich, Johnson, Duwel, Kaltenbacher.
4. Literature tilt towards one author cluster (Kumar, Barak, Biswas, Abouelregal, Singh); 46/416 self-citations.
5. Length (155 pp) and meta-heavy text ("how to discount this review", evidence protocol) for AMR; Appendix D catalogue ~5,500 words.
6. Review type: not systematic; no database/search protocol stated.
7. Table 3 material data unsourced; fused-silica epsilon printed as "7.2e-06"; silicon c1 = 8854 m/s averaging not verified.
8. Novelty claims (five-axis taxonomy, availability functional, verification register) read as research inside a review; "validated against exact solutions" in abstract may overstate (code verification only).
9. AI-use declaration (computations written/run with generative AI): check ASME policy wording.
10. Minor: overfull hbox 14.7 pt (pp. 87-89), overfull vbox (p. 93); "after 1990" vs "from 1990 onward".

Not covered by Claude (please cover): sections 5-9 beyond skim, interfaces and Rayleigh/Lamb sections, size-effect section, multiphysics section, all appendices, every table and figure, cross-references, nomenclature consistency, reference-list accuracy.
