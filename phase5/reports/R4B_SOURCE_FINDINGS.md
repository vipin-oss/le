# R4B-AUTO — Source findings and disposition history

**Scope.** Targeted verification for the R4B-1 baseline and the appended WP2 Section 12 pass: Chester (1963); both Guyer–Krumhansl (1966) papers at *Physical Review* 148:766 and 148:778; Chandrasekharaiah (1998); Povstenko (2011), DOI `10.1080/01495739.2010.511931`, including Eq. (29); Dell’Oro–Pata, DOI `10.1007/s00245-016-9365-1`; the Povstenko book DOI; Gorenflo–Mainardi if available; and the Tzou (1995) unified-field and Quintanilla (2003) sources added for Section 12. Paper contents below are paraphrased; equations and printed page/equation anchors are given where checked.

**Method and access limits.** The available smaller Drive bundles and standalone PDFs were searched for the requested titles and identifiers. No source PDF, scan, extracted text, private Drive name, URL, or file ID is included in this repository. `pdftotext` was unavailable; a temporary PyMuPDF installation was used as a clearly identified fallback for targeted text extraction, with page-image checks for Chester, the p. 778 Guyer–Krumhansl paper, and selected 1998-review pages. No whole-paper text was added to the repository. The larger archives were not downloaded because the Drive download tool caps files at 100 MB, and the expressly excluded archive was not inspected or used. Findings explicitly described as prior-audit checks below come from the existing in-repository `scientific-audit.md`; those source PDFs were not reopened in this pass.

## Findings by source

### Chester (1963), *Second Sound in Solids*

**CONFIRMED-IN-SOURCE.** The primary paper identifies Marvin Chester and *Physical Review* 131, printed pp. 2013–2015 (1963). On p. 2014, Eq. (5) gives a relaxation-flux form; Eqs. (6)–(7) give its damped thermal-wave equation and model speed. On p. 2015, Eq. (8) relates that speed to phonon speed only under an idealized, dispersionless phonon-gas assumption. The same page supplies a critical-frequency relation in Eq. (11) and a relaxation-time relation in Eq. (12); the conclusion describes experiments as prospective rather than completed evidence. The scan’s p. 2013 also contains an unrelated article fragment, which was not used. The Chester bibliography entry therefore omits a DOI not printed in the inspected copy.

**Inference.** These pages support a qualified historical account of Chester’s phenomenological model, not universal microscopic proof, a general continuum thermoelastic law, or experimental validation.

### Guyer–Krumhansl (1966), *Solution of the Linearized Phonon Boltzmann Equation* (p. 766 paper)

**CONFIRMED-IN-SOURCE (prior in-repository source audit).** The existing audit records inspection of the primary source’s printed pp. 766 and 773. Eq. (57) defines the Ziman-limit time `tau_z`; Eq. (59) contains the source-specific kinetic coefficient. With the definitions and rapid-normal-scattering restrictions stated around the equation—including `N* >> R*`, `Omega tau_N << 1`, and `Omega tau_R >> 1`—the relation `lambda^2 = c^2 tau_N tau_z / 5` follows. The current-pass accessible small-bundle member lists did not include this paper, so the source pages were not independently reopened. The prior audit’s source-derived result is retained as such, not represented as a new extraction.

**Inference.** The coefficient is limited to that phonon-kinetic regime; it is not a universal continuum thermoelastic constitutive law. Do not transfer this equation to the p. 778 companion paper.

### Guyer–Krumhansl (1966), *Thermal Conductivity, Second Sound, and Phonon Hydrodynamic Phenomena in Nonmetallic Crystals* (p. 778 paper)

**CONFIRMED-IN-SOURCE.** The inspected first page begins the distinct p. 778 article and identifies Guyer and Krumhansl. Its abstract describes macroscopic equations developed from the linearized phonon Boltzmann equation and discusses phonon-gas conductivity, Poiseuille flow, and second-sound phenomena. Printed p. 782, Eq. (17) gives a source-specific dispersion relation; the accompanying text attributes damping of second sound to second viscosity and momentum-loss scattering. Only the title page and selected passages were examined. The scanned source does not print a DOI; the existing DOI field is metadata provenance, not a DOI claim verified from the paper itself.

**Inference.** The p. 778 article is distinct from the p. 766 kinetic-theory article. Its damping discussion cannot be used to substantiate Eq. (59) of the p. 766 paper.

### Chandrasekharaiah (1998), *Hyperbolic Thermoelasticity: A Review of Recent Literature*

**CONFIRMED-IN-SOURCE.** The first page identifies the article as a review and states that it covers work from roughly the preceding decade on hyperbolic thermoelasticity, including thermal-relaxation and temperature-rate-dependent theories. Selected discussion on printed pp. 722–724 was also recorded in the existing source audit. The article is a secondary review, not a primary derivation of the constitutive equations treated in the manuscript. The inspected scan does not print its DOI.

**Inference.** It is appropriate for historical or review context, but not as sole evidence for an equation or theorem.

### Povstenko (2011), DOI `10.1080/01495739.2010.511931`

**CONFIRMED-IN-SOURCE (prior in-repository source audit).** The existing audit records the source identity from its first page and targeted reading of printed pp. 97–104 and 109–110, with Eq. (29) visually checked on p. 101 and Appendix A checked on p. 113. Eq. (29) uses the source coefficient `zeta` in a related fractional Cattaneo flux law for `0 < alpha <= 1`; Appendix A identifies the derivative as Caputo while omitting a superscript `C`. No mapping from `zeta` to `tau^alpha / Gamma(1+alpha)` is printed or established. The article is distinct from the `.511929` Dirichlet-problem paper associated with the separate `Povstenko2011` bibliography key. The source was not reopened in this pass; the page-specific result is inherited from the in-repository audit, not guessed from metadata.

**Inference.** Keep Eq. (29) in its source-specific `zeta` form. The Gamma-normalized expression may be retained only as a separately identified manuscript convention, not attributed to this source.

### Povstenko, *Fractional Thermoelasticity* (2015 book)

**CONFIRMED-IN-SOURCE (prior in-repository source audit).** The supplied copy’s unnumbered copyright leaf (PDF leaf 5 in the earlier inspection) identifies the 2015 book, print ISBN `978-3-319-15334-6`, eBook ISBN `978-3-319-15335-3`, and DOI `10.1007/978-3-319-15335-3`. The current bibliography has the matching DOI and identifiers and records year 2015. Only front-matter identity was checked for this task; no mathematical chapter is used here.

**Inference.** The citekey `Povstenko2016` is retained for compatibility although its current bibliographic year is 2015; this is a key/year naming mismatch, not a DOI mismatch. No key rename is made.

### Dell’Oro–Pata (2016), DOI `10.1007/s00245-016-9365-1`

**CONFIRMED-IN-SOURCE.** The inspected first page prints the DOI, the two authors Dell’Oro and Pata, and the title *On the Moore–Gibson–Thompson Equation and Its Relation to Linear Viscoelasticity*. Its abstract relates the third-order MGT equation to linear viscoelasticity with an exponential memory kernel and reports a regularity-preservation result for a stated class of initial data. Only the first page and abstract were used for identity and scope; no stability theorem was taken from it. The new bibliography entry includes the DOI because it is printed on that page.

**Inference.** This two-author paper is not the three-author Dell’Oro–Lasiecka–Pata article cited for the critical-case stability statement in Section 4. It cannot substantiate that different article’s stability claim.

### Gorenflo–Mainardi (1997), and the 2014 Gorenflo–Kilbas–Mainardi–Rogosin monograph

**NOT-FOUND.** No identifiable full-text copy of the requested Gorenflo–Mainardi record, or of the cited 2014 monograph, was found among accessible individual Drive files or the smaller inspected archive member lists. Search hits from later papers citing these names do not identify the requested source. The larger archives were not fetched. No definition, theorem, or equation is inferred from the citation metadata; the related ledger statements remain at reference level and hedged.

## Source/manuscript discrepancies — highest priority first

1. **P0 — Dell–Pata identity boundary.** The requested DOI `.9365-1` identifies the two-author MGT/linear-viscoelasticity article. Section 4’s critical-case stability sentence cites a different, three-author Dell’Oro–Lasiecka–Pata paper with DOI `10.1016/j.jde.2016.06.025`. The requested source does not verify that stability sentence. This is a distinct-source boundary, not proof that the separate JDE claim is false; the JDE paper itself was not checked in this pass.
2. **P1 — Povstenko key distinction.** The Eq. (29) paragraph correctly cites the dedicated `.511931` key and now names `zeta`; the separate `Povstenko2011` key points to `.511929`, a different Dirichlet-problem article. Do not merge those records. The requested Gamma-normalized mapping remains unsupported.
3. **P1 — Guyer–Krumhansl distinction.** The bibliography and Section 2 retain separate p. 766 and p. 778 entries. Eq. (59) belongs only to the p. 766 source; the p. 778 paper’s second-sound discussion is cited separately. Neither source’s DOI is printed in the inspected 1966 scan, so the existing DOI values remain metadata-sourced.
4. **P2 — Mainardi availability.** The reference-level background claim has no located full text in the accessible source set. It remains unexpanded; no source-specific statement is promoted.
5. **P2 — other open equations.** The Tzou (1995) printed p. 10, Eqs. (15) and (17), were freshly inspected during the Section 12 pass, but the Section 4 claim-to-source correspondence and any needed correction remain for that section’s dedicated pass; OCL-166–OCL-168 remain open in the meantime. The broader Green–Naghdi chronology in the Section 2 paragraph is also not resolved by this source set.

## R4B-1 initial manuscript and ledger disposition (historical baseline before WP2 Section 12)

- Section 2 now distinguishes Chester’s 1963 phenomenological model, the p. 766 Guyer–Krumhansl kinetic-theory result, and the separate p. 778 companion. The Chandrasekharaiah 1998 review is limited to contextual use.
- Section 11 cites Povstenko Eq. (29) at printed p. 101, identifies Caputo notation from Appendix A at p. 113, and explicitly avoids attributing the Gamma-normalized mapping.
- Section 12 adds a compact source-specific comparison and cites six distinct source records: Chester; Guyer–Krumhansl p. 766; Guyer–Krumhansl p. 778; Chandrasekharaiah 1998; Povstenko `.511931`; and Dell’Oro–Pata `.9365-1`. This is a count of distinct cited records, **not** a claim that six eligible primary sources satisfy any separate readiness threshold; Chandrasekharaiah is a review, and Mainardi remains not found.
- The new Chester bibliography entry omits a DOI not printed in the inspected source. The new Dell’Oro–Pata DOI is printed on the paper’s first page. The existing Guyer–Krumhansl entries remain separate; the current Povstenko book DOI is already source-confirmed.
- Ledger: before, 439 rows (A=0, B=144, C=295). After, 442 rows (A=10, B=138, C=294). Seven existing rows were promoted to A and three new source-specific rows were added; the broader Section 2 rows remain hedged where they include sources outside this check.

**Rows resolved to Class A:** OCL-125, OCL-137, OCL-164, OCL-165, OCL-321, OCL-322, OCL-326, and the three new source-specific rows OCL-440–OCL-442. **Rows still open or partial:** OCL-046 (the distinct three-author stability article was not checked); OCL-087 (the comparison with the 2009 source remains unverified); OCL-124 (Green–Naghdi chronology and dissipation scope remain outside this source check); OCL-127 (broad no-universal-energy limitation remains hedged); OCL-128 (the wider multi-review synthesis remains deleted/not re-established; no claim-level support is asserted); OCL-131 and OCL-327 (Mainardi-related full text not found); OCL-132 (the generic Povstenko2011 key denotes `.511929`, so `.511931` findings are not transferred); OCL-166–OCL-168 (Tzou printed p. 10 Eqs. (15) and (17) have since been inspected and were dispositioned in the later WP2 Section 4 pass below); and OCL-323 (the Gamma-normalized mapping is not source-supported). These remain B/C; metadata or title-page identification alone does not close them.

## WP2 — Section 12 source-backing pass (2026-10-26)

### Chester (1963), fresh targeted re-read

**CONFIRMED-IN-SOURCE.** Printed p. 2014, Eq. (5) adds relaxation to the heat-flux law and Eqs. (6)–(7) give the associated damped thermal-wave equation and speed. Printed p. 2015, Eq. (8) relates that speed to phonon speed under the paper’s idealized dispersionless phonon-gas assumption. The unrelated fragment on the scan’s p. 2013 was not used.

### Guyer–Krumhansl (1966), p. 766 article, fresh targeted re-read

**CONFIRMED-IN-SOURCE.** The title page identifies the distinct kinetic-theory article at *Physical Review* 148, p. 766. Printed p. 773, Eqs. (57) and (59) define the source-specific quantities and kinetic coefficient. The associated nonlocal-length interpretation is confined to the paper’s stated rapid-normal-scattering and phonon-regime restrictions; it is not a universal continuum thermoelastic coefficient.

### Guyer–Krumhansl (1966), p. 778 article, fresh targeted re-read

**CONFIRMED-IN-SOURCE.** The scanned first sheet contains an unrelated p. 788 fragment above the p. 778 article’s own title and abstract; only the correctly headed p. 778 article and its selected text were used. Printed p. 782, Eq. (17) gives the paper-specific dispersion relation, and the adjacent discussion attributes second-sound damping to second viscosity and momentum-loss scattering. These findings are separate from the p. 766 article’s Eq. (59).

### Chandrasekharaiah (1998), fresh selected-page check

**CONFIRMED-IN-SOURCE.** The first page identifies a review of hyperbolic thermoelasticity. Printed pp. 722–724 discuss specific dual-phase-lag models and their stated assumptions. This remains review-level context, not a primary equation source or a family-wide admissibility result.

### Tzou (1995), *A Unified Field Approach for Heat Conduction From Macro- to Micro-Scales*

**CONFIRMED-IN-SOURCE.** The primary paper’s opening page (printed p. 8) describes the unified-field treatment as a high-rate heat-conduction model and relates the flux lag to small-scale temporal response and the temperature-gradient lag to small-scale spatial response. The bibliographic DOI already in the library belongs to this distinct unified-field article. Printed p. 10, Eqs. (15) and (17) were freshly inspected during the Section 12 work and then dispositioned in the dedicated Section 4 pass below; their formulas match the source-specific statements, with the pure-phonon scope retained.

### Quintanilla (2003), one-dimensional dual-phase-lag thermoelastic theory

**CONFIRMED-IN-SOURCE.** The paper’s first page prints the author initial, title, journal, volume, pages 713–721, year, and DOI `10.1080/01495730390203518`. The conclusion on printed p. 720 states exponential stability for the strict condition `tau_theta > tau_q/2` and the existence of unstable solutions for `tau_theta < tau_q/2`. The equality case is not characterized by that pair of statements. The new bibliography entry records the first-page fields and does not infer an issue number.

**Inference.** These results concern the paper’s specified one-dimensional problem; they do not provide a universal dual-phase-lag admissibility condition.

### Povstenko (2011), DOI `.511931`, fresh Eq. (29) and Appendix A check

**CONFIRMED-IN-SOURCE.** Printed p. 101, Eq. (29) uses the source coefficient `zeta` in a fractional Cattaneo flux law for `0 < alpha <= 1`. Printed p. 113 states that the Caputo derivative is used while the `C` subscript is omitted. The equation supplies no Gamma-normalized identification of `zeta`.

**Inference.** Keep the source law in its `zeta` form; do not attribute `tau^alpha / Gamma(1+alpha)` to this paper.

### Dell’Oro–Pata (2016), DOI `.9365-1`, fresh first-page check

**CONFIRMED-IN-SOURCE.** The first page prints the DOI, two authors, title, and an abstract describing the relation of the MGT equation to linear viscoelasticity with an exponential kernel. This is not the distinct three-author critical-case stability article.

### Section 12 result and ledger checkpoint

The focused source-backed comparison now uses **eight distinct records: seven primary papers** (Chester; Guyer–Krumhansl p. 766; Guyer–Krumhansl p. 778; Tzou; Quintanilla 2003; Povstenko `.511931`; Dell’Oro–Pata `.9365-1`) **and one review** (Chandrasekharaiah 1998). This clears the six-primary-source target for the focused Section 12 comparison; table-only citations are not counted as freshly source-checked evidence.

Ledger checkpoint: before this pass, 442 rows (A=10, B=138, C=294); after, 445 rows (A=13, B=138, C=294). New Class A rows OCL-443–OCL-445 cover the fresh Povstenko, Tzou, and Quintanilla anchors. Older carried-audit rows remain explicitly labelled as carried. OCL-166–OCL-168 remained open at the end of the Section 12 pass; they are resolved in the later dedicated Section 4 pass below.

## WP2 — Section 4 targeted Tzou source pass (2026-10-26)

### Tzou (1995), *A Unified Field Approach for Heat Conduction From Macro- to Micro-Scales*, printed p. 10

**CONFIRMED-IN-SOURCE.** Under the paper’s “Pure Phonon Field in Dielectric Crystals” subsection, Eq. (15) relates the time derivative and relaxation of the heat-flux vector to the temperature gradient and the phonon-scattering spatial operators. The coefficients in the manuscript’s displayed equation match the source’s Eq. (15). The paragraph now cites the paper at that equation and gives the printed page; it does not assign the continuum reduction to Guyer–Krumhansl.

**CONFIRMED-IN-SOURCE.** Equation (17) on the same printed page maps the pure-phonon case to `alpha = tau_R c^2/3`, `tau_T = 9 tau_N/5`, and `tau_q = tau_R`. The manuscript mapping matches those coefficients and is explicitly scoped to Tzou’s phonon approximation, not stated as a general DPL identity.

**Disposition.** OCL-166–OCL-168 are now Class A with fresh source-page evidence. No discrepancy was found and no `CONTRADICTION-FIXED` row was required. Other Section 4 claims, including the distinct critical-case MGT result (OCL-046), remain outside this targeted pass.
