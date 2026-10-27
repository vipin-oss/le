# R4B-AUTO — Source findings and disposition history

**Scope.** Targeted verification for the R4B-1 baseline and WP2 Sections 4, 5, 7, 8, 9, and 12: Chester (1963); both Guyer–Krumhansl (1966) papers at *Physical Review* 148:766 and 148:778; Chandrasekharaiah (1998); Povstenko (2011), DOI `10.1080/01495739.2010.511931`, including Eq. (29); Dell’Oro–Pata, DOI `10.1007/s00245-016-9365-1`; the Povstenko book DOI; Gorenflo–Mainardi if available; Tzou (1995) and Quintanilla (2003); the cited Lata–Singh, Gupta et al., Li–He, Tung, and Zang nonlocal-model examples; Section 8’s Chadwick–Sneddon, Biot, Biswas, Marotti de Sciarra, and Hughes leads; and Section 9’s Kumar–Kansal, Sarkar, Singh, Aldandani, Kalkal, Das, and Kumar interface examples. Paper contents below are paraphrased; equations and printed page/equation anchors are given where checked.

**Method and access limits.** The available smaller Drive bundles and standalone PDFs were searched for the requested titles and identifiers. No source PDF, scan, extracted text, private Drive name, URL, or file ID is included in this repository. `pdftotext` was unavailable; a temporary PyMuPDF installation was used as a clearly identified fallback for targeted text extraction, with page-image checks for Chester, the p. 778 Guyer–Krumhansl paper, and selected 1998-review pages. No whole-paper text was added to the repository. The larger archives were not downloaded because the Drive download tool caps files at 100 MB, and the expressly excluded archive was not inspected or used. Findings explicitly described as prior-audit checks below come from the existing in-repository `scientific-audit.md`; those source PDFs were not reopened in this pass. The Section 7 paper copies that were located were checked through targeted text extraction at the cited equation anchors; their page images were not reviewed in that pass. For Section 8, the Biswas (2020) paper was read by targeted text extraction at its governing-equation anchor; its page image was not reviewed. The Chadwick–Sneddon, Marotti de Sciarra, and Hughes source copies were not located in the inspected set. For Section 9, Kumar & Kansal (2017) was checked at the coupled field equations and energy-intensity definitions, and the Kumar et al. (2022) abstract was checked; its detailed energy-matrix passage is carried from the earlier R3B read. Other Section 9 source anchors are carried from the saved R3B citation map; no page images were reviewed. Singh & Gupta (2020) was not located as an original paper. Achenbach and Nowacki books were not inspected.

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

**Disposition.** OCL-166–OCL-168 are now Class A with fresh source-page evidence. No discrepancy was found and no `CONTRADICTION-FIXED` row was required. Other Section 4 claims, including the distinct critical-case MGT result (OCL-046), remain outside this targeted pass. The missing-source register records the unlocated papers behind OCL-045, OCL-046, OCL-143–OCL-146, OCL-149, OCL-153–OCL-160, OCL-169–OCL-178; those claims were not upgraded by this Tzou check.

## WP2 — Section 5 targeted source-backing pass (2026-10-27)

### Mindlin (1974), *Equations of High Frequency Vibrations of Thermopiezoelectric Crystal Plates*

**CONFIRMED-IN-SOURCE.** Printed p. 625, Section 2 explicitly presents the classical three-dimensional linear thermopiezoelectric system. Equation (1) gives the momentum, charge-divergence, and entropy-balance equations. Printed p. 626, Eqs. (2)–(5) give the Fourier heat-flux relation and constitutive derivatives of the electric Gibbs function. The manuscript’s baseline paragraph matches these equations and identifies them as the system preceding Mindlin’s plate reduction. The checked pages support this classical linear model only; no generalized lag law is attributed to Mindlin.

### Biot (1956), *Thermoelasticity and Irreversible Thermodynamics*

**CONFIRMED-IN-SOURCE, WITH WORDING NARROWED.** The paper identity and DOI are printed on the source’s front matter. Printed p. 241, Eq. (2.2) includes a negative temperature-increment term in the stress law. Printed p. 242, Eqs. (3.3)–(3.4) give the conductivity-based heat-conduction equation and its coupling to deformation. The checked pages do not state the vector law `q_i = -k T_,i` in that form. Accordingly, Table T3 now summarizes thermal-stress coupling and a conductivity-based heat equation, without asserting a specific heat-flux vector or sign convention. No discrepancy remains in the revised table wording.

### Barak et al. (2023), *Behavior of higher-order MDD on energy ratios at the interface of thermoelastic and piezothermoelastic mediums*

**CONFIRMED-IN-SOURCE, WITH TERMINOLOGY CORRECTED.** The first page prints the article identity and DOI. Printed p. 3 gives the coupled model equations and nomenclature: the paper calls its `eta`/`epsilon` terms piezothermal moduli and identifies `p_i` as pyroelectric constants. Table T3 now uses that source terminology rather than attributing a generic `e_{kij}` piezoelectric tensor to this example. The row remains illustrative and does not claim a universal constitutive law.

### Kumar et al. (2023), *Energy ratio response at the interface of elastic and dual-porous thermoelastic half-spaces*

**CONFIRMED-IN-SOURCE.** The first page identifies an elastic/dual-porous thermoelastic interface paper and prints its DOI. Printed p. 17 reports that the total energy-ratio sum approximates unity. The manuscript now names the correct model family and describes the value only as a reported numerical observation, not an exact identity or general conservation theorem.

### Source availability and Section 5 dispositions

Targeted DOI/title searches and member-name checks did not identify the original full texts for Eringen (1966), Tauchert–Claus–Ariman (1968), Nunziato–Cowin (1979/1983), Iesan (1986), Gupta et al. (2022), or Gupta et al. (2023). Search hits were later citing papers or bundles, not proof that the source is absent from uninspected material. The Iesan (2013) monograph was not read or inspected as a whole; its existence/uniqueness attribution remains unverified. These limits are recorded separately in `MISSING_SOURCES.csv`.

OCL-195, OCL-404, OCL-405, and OCL-207 are Class A on fresh page evidence. OCL-405 and OCL-207 record `CONTRADICTION-FIXED` dispositions for source-terminology/model-family mismatches. Unsupported Gupta-specific statements OCL-205 and OCL-206 were removed from the active text and remain recorded as source leads for any future reinstatement. OCL-406–OCL-408 and other unrelated Section 5 claims remain open; this pass does not certify the whole section.

## WP2 — Section 7 targeted source-backing pass (2026-10-27)

### Lata & Singh (2020), *Effects of nonlocality and two temperature in a nonlocal thermoelastic solid due to ramp type heat source*

**CONFIRMED-IN-SOURCE, WORDING NARROWED.** Printed p. 359, Eq. (2) gives a conductivity-based heat equation for the cited two-temperature nonlocal model; Eq. (3) relates conductive and thermodynamic temperatures. The displayed heat equation contains no phase-lag or Green–Naghdi term. The manuscript now describes this as a conductivity-based example rather than attributing a specific vector Fourier/Biot flux law.

### Gupta et al. (2024), *Rayleigh wave in nonlocal piezo-thermo-electric semiconductor medium with fractional MGT model*

**CONFIRMED-IN-SOURCE.** Printed p. 7, Eqs. (17)–(19) place the spatial operator in the constitutive stress, electric-displacement, and entropy relations; Eq. (22) carries it in the inertial term. Equation (25) applies the spatial/fractional operator to the heat-flux relation and includes temperature-gradient, thermal-displacement-gradient, and carrier-related terms. The manuscript now names the operator placements without claiming that they are exclusive or universal.

### Li & He (2018), *Investigation of generalized piezoelectric-thermoelastic problem with nonlocal effect and temperature-dependent properties*

**CONFIRMED-IN-SOURCE.** Article p. 4, Eq. (7) specifies a modified-Bessel `K_0` kernel, and Eq. (8) gives the associated differential nonlocal relation. The manuscript now explicitly limits the correspondence to that kernel rather than implying a general integral/differential equivalence.

### Lazar & Agiasofitou (2022), *Nonlocal elasticity of Klein–Gordon type: Fundamentals and wave propagation*

**IDENTITY VERIFIED; CLAIM NOT VERIFIED.** The title and DOI are present in the reference list, but an exact title/DOI search and an author-name search did not locate the source full text in the inspected set. The former claim about operator placement in both constitutive and motion equations was narrowed to title-level identification only. This bounded search result does not establish absence from uninspected material; OCL-259 remains Class B and its operator-placement detail is not certified.

### Tung (2019), *Dispersion equation of Rayleigh waves in transversely isotropic nonlocal piezoelastic solids half-space*

**CONFIRMED-IN-SOURCE, WITH CONTRADICTION FIXED.** Printed p. 365, Eqs. (3)–(4) define nonlocal stress and electric-displacement relations and place a corresponding spatial factor in the motion balance. The governing system contains no thermal field or heat equation. The previous “inertia-only” description contradicted these displayed constitutive relations; OCL-260 now records `CONTRADICTION-FIXED`, and the manuscript distinguishes this model-specific combination.

### Zang et al. (2014), *Longitudinal wave propagation in a piezoelectric nanoplate considering surface effects and nonlocal elasticity theory*

**CONFIRMED-IN-SOURCE, SCOPE NARROWED.** Printed p. 147, Eq. (1) is the one-dimensional wave equation for the piezoelectric nanoplate; its scale-dependent terms occur in the inertia contributions. The abstract and the same equation identify a longitudinal-wave dispersion study with surface effects. The manuscript confines the statement to this model and does not present it as a general nonlocal placement rule.

### Section 7 disposition

OCL-256, -257, -258, -260, and -261 are Class A on fresh primary-source equation anchors; OCL-260 is the contradiction fix. OCL-259 remains Class B because only bibliographic identity/title was verified. The class totals are 445 ledger rows (A=25, B=124, C=296). The deleted/rejected stronger energy-flux and table claims OCL-245–OCL-255 were not revived or upgraded; the section continues to state that flux terms are model-specific and that no universal correction is asserted. The source PDFs were checked by targeted text extraction only, not page-image review.

## WP2 — Section 8 targeted source-backing pass (2026-10-27)

### Biswas (2020), *Surface waves in piezothermoelastic transversely isotropic layer lying over piezothermoelastic transversely isotropic half-space*

**CONFIRMED-IN-SOURCE.** The article’s first page identifies the DOI and describes a layered piezothermoelastic Rayleigh-wave analysis under Green–Naghdi type III. Section 2, Eq. (3), gives the GN-III heat-conduction equation; the displayed relation contains conductivity and additional gradient terms. The manuscript now confines the example to that model and does not infer an energy-partition result. OCL-075 is Class A on this primary-source equation anchor.

### Chadwick & Sneddon (1958), *Plane waves in an elastic solid conducting heat*

**IDENTITY ONLY; CLAIM NOT VERIFIED.** The bibliography identifies the article and DOI, but exact DOI/title searches and author-name filename searches did not locate the original paper in the inspected set. The active text is narrowed to title-level identification; the previous claims about S-, P-, and thermal-mode dispersion/attenuation are not asserted. OCL-063 and OCL-262 remain Class B. The bounded search does not establish absence from uninspected material.

### Marotti de Sciarra (2013), *Some variational principles for coupled thermoelasticity*

**IDENTITY ONLY; CLAIM NOT VERIFIED.** The title and DOI are in the reference list, but exact DOI/title searches did not identify the source copy in the inspected set. The active paragraph now gives only the title-level scope and does not attribute differences in admissible spaces, boundary conditions, or solution classes. OCL-446 remains Class B; the source is listed in `MISSING_SOURCES.csv`.

### Transform-reduction and Section 8.10 wording

The specific claim that the classical transient thermoelastic problem universally reduces to a pair of second-order normal-coordinate equations with closed-form solutions was removed; Achenbach (1973) and Nowacki (1975) were not inspected as whole books. Section 8 now says that transform outcomes and closed-form availability depend on the specified model, geometry, and boundary conditions. The broader hyperbolic/parabolic classification was also removed. The narrower coupled-system statement cites the Biot pp. 241–242 finding already documented in the Section 5 pass; no fresh Biot page read or new Class A upgrade is claimed. Sequential/quasi-static validity and harmonic attenuation/coupling language are now explicit methodological cautions, not universal criteria.

### Section 8 method-table source attribution

The generic scattering-matrix row no longer cites Barak2023, whose source is an interface energy-ratio paper rather than an inspected scattering-matrix formulation. The generic finite-element row no longer cites Hughes1980, whose title concerns selective integration in anisotropic/nonlinear media; the exact source paper was not located. The method rows now use “Standard method” where no source-specific example is checked. The Achenbach/Nowacki books were not read; the specific Section 8 closed-form claim was removed, while any remaining citations elsewhere await their later section passes.

### Section 8 disposition

OCL-075 is Class A on the fresh Biswas Eq. (3) anchor. OCL-063/-262 remain B at title-level only; OCL-446 remains B; OCL-447–OCL-457 record removed or narrowed source attributions and unsupported universal method claims, including fixed secular-order/root-count assertions and the claim that any extra retained root necessarily breaks the energy-conservation identity. The ledger now has 457 rows (A=26, B=127, C=304). No whole book was inspected, no source-page images were reviewed, and no unsupported mode, transform-reduction, variational, or finite-element attribution was promoted.

## WP2 — Section 9 targeted source-backing pass (2026-10-27)

### Kumar & Kansal (2017), *Reflection and Refraction of Plane Harmonic Waves at an Interface Between Elastic Solid and Magneto-thermoelastic Diffusion Solid with Voids*

**TARGETED PRIMARY-SOURCE CHECK.** The direct paper copy was checked by text extraction around its constitutive/thermal field equations and energy-intensity definitions. The displayed field equations contain relaxation-time terms in the thermal/coupled relations; the interface analysis defines source-specific amplitude and energy ratios for the stated elastic/magneto-thermoelastic-diffusion/void model. Section 9 now describes only its LS-type relaxation terms and does not use its modal energy formulas as a universal total-field identity. Exact equation text is not copied into this report. The detailed anchors also remain documented in the saved R3B source map.

### Kumar et al. (2022), *Wave propagation at the welded interface of an elastic solid and unsaturated poro-thermoelastic solid*

**TARGETED PRIMARY-SOURCE CHECK.** The direct source’s first page and abstract identify the DOI and the elastic/unsaturated-poro-thermoelastic welded-interface model. The abstract describes interaction energies as part of the model-specific balance. The Section 9 sentence is limited to that model-specific use; the detailed energy-matrix passage is carried from the full targeted read recorded in `R3B_CITATION_MAP.csv` and was not re-extracted in this pass.

### Singh & Gupta (2020), DOI `10.1080/15397734.2020.1853566`

**IDENTITY CHECK; CONTENT NOT VERIFIED.** The saved bibliographic record identifies *Wave reflection by the free boundary of a microstructured flexoelectric half-space*. Exact DOI/title Drive searches did not locate the original article in the inspected set. The earlier “TPL interface” energy-bound attribution did not match the identified paper scope and has been removed; OCL-291 is marked `CONTRADICTION-FIXED`, remains Class C, and the source is recorded in `MISSING_SOURCES.csv`. No claim about the paper’s detailed constitutive model or energy bound is made.

### Interface equations and model scope

The modal expansion now includes the tangential phase factor already set by the geometry. The spring-interface equation was corrected so that the named stiffness, traction law, and limiting cases are internally consistent; it is explicitly presented as one model-specific linear law. Ideal mechanical/thermal/electrical matching conditions now state their no-surface-force, perfect-contact, and no-free-charge assumptions. The fixed degree-eight 6mm secular-polynomial assertion was removed in favor of the generic determinant condition; no source-supported degree or mode count was available. The boundary-condition count text now notes that a square system alone does not prove well-posedness. The notation summary identifies `A_int` as an interface-local residual, not an absorption coefficient.

### Memory and nonlocal interfaces

The former universal statements about memory flux histories, nonlocal traction, and a first-order length/wavelength approximation were narrowed to conditional guidance: interface laws must be derived for the chosen constitutive kernel, boundary treatment, and history data. No universal interface law or error order is asserted. The graded-interface question remains an open, model-specific question without a claim that no reviewed paper addresses it.

### Carried source checks and disposition

Other source-specific examples retained in the Section 9 summary remain Class B and are carried from the targeted reads recorded in `R3B_CITATION_MAP.csv` (including the equation anchors recorded there for Sarkar2019, Singh2020, Aldandani2026, Kalkal2020, and Das2008). Singh2020b remains partial; its numerical observation is explicitly distinguished from a symbolic identity. Kumar2019 is described only as approximate; Kumar2022 is model-specific. No Class A promotion was made in this Section 9 pass. No source PDF or extracted publisher text was added to the repository, and no whole book was inspected.

### Section 9 disposition

OCL-291 records the removed TPL/interface energy-bound attribution as `CONTRADICTION-FIXED`, but remains Class C because the original paper was not located and only the bibliographic title/DOI was checked. OCL-458–OCL-464 record internal equation/notation corrections and narrowed universal claims; T6 OCL-429–OCL-433 now reflect the current table rather than the deleted stronger rows. No Class A promotion was made. The ledger now has 464 rows (A=26, B=126, C=312), and `MISSING_SOURCES.csv` has 22 bounded records.

## WP2 — Section 10 energy-partition and interface-derivation pass (2026-10-27)

### Source access and disposition

A targeted Drive search by the Ivanov–Savova (1991) title and DOI `10.1080/01495739108927085` found bibliographic metadata but did not identify a copy of the article in the indexed material inspected. OCL-078 therefore remains Class C; the detailed surface-wave flux direction/depth-decay claim was removed from active Section 10 and recorded in `MISSING_SOURCES.csv`. This bounded search does not establish absence from uninspected archives. The unsupported general zero-normal-flux statement for a single evanescent partial wave was also removed; no generic evanescent-mode result is now asserted.

### Reproducible derivation

`phase5/verification/verify_interface_energy.py` symbolically derives the two-amplitude/two-condition matrix for normal-incidence longitudinal waves at a welded one-dimensional interface, checks its determinant and positive-impedance uniqueness, solves the amplitude ratios, and verifies the real-impedance power partition. The script also checks the time-averaged incident/reflected cross-term cancellation in that one-dimensional example, the definition-level total-field identity, and the steady control-volume split between bulk-left, interface-local, and bulk-right dissipation. It shows algebraically why a remote-plane absorption residual already includes the bulk losses and why appending those same bulk terms again double-counts them. The benchmark is restricted to the stated one-dimensional lossless welded model; it does not establish a generalized-multiphysics or multidimensional interface law.

### Section 10 disposition

OCL-465–OCL-468 are Class V and point to the verification script; OCL-469 records the withdrawn evanescent-mode assertion. The Section 10 ledger additions bring the register to 469 rows (A=26, B=126, C=313, V=4). The missing-source register now has 23 bounded records. No generalized-family flux or dissipation identity was promoted by this pass.

## Q1 — Initial equation-level reduction checks (2026-10-27)

`phase5/verification/verify_unified_reductions.py` passes symbolic substitutions for the explicitly displayed LS, first-order DPL/TPL, and MGT heat-flux residuals; it also checks a derivative-level GN-III/GN-II residual compatibility, selected integer-order Caputo monomial identities, and the displayed nonlocal Helmholtz/1D-dispersion local limits. OCL-470–OCL-473 are Class V and identify the corresponding script ranges. At this initial-check stage, no GL or GN-I reduction, family-wide template, or theory-comparison table had yet been established; the ledger snapshot was 473 rows (A=26, B=126, C=313, V=8), with 23 missing-source records. The later Q1 additions below supersede that snapshot. The checks validate algebra of the displayed equations only; they do not validate source transcription, solution convergence, thermodynamic admissibility, stability, or equivalence of complete initial-boundary-value problems.

### Q1 — Primary-source abstracts and scope distinctions

A fresh text extraction of Green and Lindsay's 1972 paper confirms the printed p. 1 abstract's limited description: a linearized thermoelastic generalization, symmetric linear heat-conduction tensor, allowance for second-sound effects, and a stated uniqueness theorem (OCL-474). The detailed displayed formula extraction is OCR-garbled; no GL field equation, parameter restriction, or reduction has been established from that read. Green and Naghdi's 1993 paper, printed p. 189 abstract, identifies its type-II system as nondissipative, permits finite-speed thermal waves, obtains the entropy-flux and stress constitutive equations from a shared potential, and states a uniqueness theorem (OCL-475). Green and Naghdi's 1992 paper, printed p. 255 introduction, scopes its later coupled development to type-III thermoelasticity and finite-speed thermal waves; the same printed-page footnote limits the nondissipation distinction to type II in the stationary-rigid-solid comparison, so that property is not transferred to type III (OCL-476). These are source-bounded abstract/introductory anchors, not a substitute for equation-level transcription needed for Q1's common template.

## Kumar2017 bibliography identity reconciliation (2026-10-27)

The inspected library article's title page identifies Rajneesh Kumar, Shaloo Devi, and Veena Sharma, with the title *Damping in Microscale Modified Couple Stress Thermoelastic Circular Kirchhoff Plate Resonators* (Applications and Applied Mathematics: An International Journal 12(2), Article 19, pp. 924–945). The saved Crossref response for DOI `10.12921/cmst.2016.0000036` instead identifies Rajneesh Kumar and Tarun Kansal's distinct CMST interface paper. The records are split in `references_local.bib`: `Kumar2017` is retained for the library article with no DOI and `verified={NO}` pending an independently established Crossref match; the Crossref-confirmed CMST paper is now `KumarKansal2017` with `verified={YES}`. Active Section 9 and Section 10 citations and current OCL source-key notes were updated to the latter key where they refer to Kumar & Kansal. No claim-verification class was promoted; all 19 dependent ledger rows (OCL-076 and OCL-278–OCL-295) remain at their existing B/C classifications. `phase5/verification/verify_kumar2017_reference_split.py` checks this key/metadata split against the saved Crossref response and asserts the B/C status of all 19 rows (OCL-477).

### Q1 — Notation audit (2026-10-27)

`phase5/verification/verify_q1_notation.py` checks the selected notation harmonization and the algebraic derivative/limits of the displayed one-dimensional nonlocal dispersion law (OCL-478). The MDD history window is now `\omega_M`, its kernel is labeled `K_{\mathrm{MDD}}`, and the time-integration dummy is `t'` to distinguish it from the spatial nonlocal length `\xi`. Section 7 uses `k_{\mathrm w}` for wave number to distinguish it from conductivity `k`; the Section 17 summary now labels `\tau_0` as an LS heat-flux relaxation time and uses `c_T` for the displayed thermal characteristic speed. These are notation and displayed-form checks only: they do not verify source transcription, a common constitutive template, or family-wide reductions. The ledger now has 478 rows (A=29, B=126, C=313, V=10); `MISSING_SOURCES.csv` remains at 23 records.

### Rendered-text spot-check — Q1 notation seed pass (CI 40460458977)

The green build at content commit `8097390b5dfe2b163b202bbdbe4e4241f1310a03` produced a 130-page PDF. Gate summary: undefined references/citations 0; privacy-token matches 0; forbidden manuscript-tag matches 0; near-overfull boxes (>0.5 pt) 0; 18 figure PDFs rendered, 16 included in the master. A ten-row A/V rendered-text spot-check matched the corresponding manuscript claims and locations: OCL-165–OCL-168 (PDF p. 34), OCL-440 (pp. 17–18), OCL-441 (p. 81), OCL-443 (p. 74), OCL-444–OCL-445 (p. 81), and OCL-478 (pp. 3 and 54). The ledger changed from A=29, B=126, C=313, V=9 (477 rows) to A=29, B=126, C=313, V=10 (478 rows); only OCL-478 was added, as a scoped algebra/notation verification. This is a spot-check, not a full-page proof or a closure of Q1.

### Q1 — Template, comparison matrix, and reduction map

Added a scoped local-Cauchy balance scaffold in Section 4.12, reusing the momentum/internal-energy balances and representing stress and heat-flux closures with explicitly non-universal placeholders. The updated classical-flux script also checks the Fourier entropy-production term for positive conductivity and absolute temperature (OCL-480). The new reduction map and its script cover only algebraic reductions of the displayed laws: LS to Fourier; first-order DPL to LS/Fourier; TPL to the displayed DPL residual; the displayed MGT candidate to Fourier; a GN-II/GN-III derivative-level identity; integer-order scalar Caputo endpoints; and the displayed nonlocal local limits. No solution-convergence or family-wide equivalence follows. GL and GN-I remain open rather than being inferred from neighboring theories (OCL-479, OCL-481).

The expanded Table T2 now covers assumptions/scope, state variables, heat-flux closure, finite-speed property, stability/well-posedness, and dissipation. Model-dependent conditions are explicitly tied to their selected problems; unverified cells are labelled not established. The table-coverage script checks the requested dimensions and open family rows only; scientific support remains attached to the individual ledger rows (OCL-482).

A saved primary-text review for Roy Choudhuri (2007) records Eqs. (3), (4), and (9), including the first-order three-lag expansion and its source-specific lag ordering; this is cross-indexed by APPA_LEDGER EQ-019 and CROSSREF_VERIFY LIT-0431. OCL-169 is now Class A only for that formulation. The unsupported second-order, universal admissibility, and broader TPL claims remain B/C. Its missing-source record was removed because the paper/equation source is present; the Green--Lindsay formula pages and GN-I source/equation mapping remain in the missing-anchor ledger. The library note for Green and Naghdi (1991) describes a postulates-methodology paper, not a specific GN-I material equation; no GN-I formula is inferred.

Current ledger: 483 rows (A=30, B=127, C=313, V=13); A+V=43. `MISSING_SOURCES.csv` contains 23 remaining source/anchor records. Candidate closures and unresolved theory properties retained in the comparison matrix remain B under OCL-483; table coverage is a separate structural V check under OCL-482. Q1 is still incomplete: the comparison framework and selected reductions are in place, but GL/GN-I equation-level anchors, the source-specific constitutive template across all families, and several model-dependent stability/dissipation cells remain open.

### Q1 — Source-anchored limits for GL, GN-I, and TPL

The Green–Lindsay primary abstract also identifies an entropy-production restriction in the Green–Laws framework; the manuscript table therefore records that framework-level fact but leaves the exact GL rate identity and equation-level closure open (OCL-474). The library note for Green and Naghdi (1991) treats that paper as a methodological examination of thermomechanical postulates, not a specific type-I material equation. No type-I equation, heat-flux closure, or reduction is inferred from its identity; the exact GN-I source mapping remains B/open (OCL-481).

For TPL, the saved full-text audit identifies Roy Choudhuri (2007), Eqs. (3), (4), and (9), as the source of the first-order three-lag form and its ordering. The evidence is recorded in `APPA_LEDGER.csv` (EQ-019) and `CROSSREF_VERIFY.csv` (LIT-0431; prior full-text read). OCL-169 is promoted only for that bounded first-order claim. The missing-source row was removed because the source/equations are present; later second-order variants, universal admissibility claims, and any shared stability/dissipation statement remain unverified.

### Q1 rendered-text audit — CI 40463595470

The Q1 package compiled on content commit `3fc1fec6879d6187efb27e62820d5429ba6ce071`; the workflow-generated PDF/output commit is `687f1f67c12da4bd4249731d50eec7e165cb9a4a`. The PDF has 118 pages. Gates: undefined references/citations 0; strict forbidden privacy-token matches 0; forbidden manuscript-tag matches 0; near-overfull boxes (>0.5 pt) 0; rendered figure PDFs 18, master figure includes 16; deletion-audit `NONE` rows 0. The strict build also passed its overfull-box gate (>1 pt: 0). Visual inspection of PDF pages 37–40 confirmed the three-page comparison matrix and reduction map are legible and unclipped; page 118 retains the final BM-5 appendix item.

Ten A/V rendered-text spot-checks matched the audited claims and locations: OCL-169 (PDF index p. 35; first-order TPL expansion and lag ordering); OCL-474 and OCL-475 (p. 37; source-limited GL abstract facts and GN-II finite-speed/nondissipation scope); OCL-476 (p. 38; GN-III finite-speed report without a transferred dissipation identity); OCL-478 (pp. 3 and 51; time-dummy notation); OCL-479 and OCL-470–OCL-472 (p. 40; requested coverage and displayed reductions); and OCL-480 (p. 37; non-negative Fourier entropy contribution). This spot-check is not a full-page proof. The ledger is 483 rows (A=30, B=127, C=313, V=13; A+V=43); `MISSING_SOURCES.csv` remains at 23 rows. Q1 is complete as a scoped deliverable; GL/GN-I equation-level cells and other source-/model-dependent questions remain open and ledgered, and Q2 is next.

### CI correction record

CI 40462918463 first stopped on an undefined `\\mathscr` command; replaced the placeholders with already-supported `\\mathcal` notation without adding a package. CI 40463181026 then reached the strict layout gate and reported six overfull table boxes (maximum 15.0 pt); widened/rebalanced the comparison columns, split the header, and shortened only the overflowing cell text. No gate was relaxed. CI 40463595470 passed all checks.

### Q2 — Selected mode counts, plane-consistent ratios, and rendered audit

Section 9 distinguishes interface-plane bookkeeping ratios $R_{\Sigma},T_{\Sigma}$ from remote-plane quantities. Section 10's normalized remote balance includes left-bulk, interface-local, and right-bulk losses; under the stated passive, steady, source-free, no-accumulation/no-unlisted-channel scope, $1-R_{\mathrm{rem}}-T_{\mathrm{rem}}$ already contains all three. The V-B3d cross-term report preserves its original $R_{\mathrm{flux}}/T_{\mathrm{flux}}$ labels because the saved summary does not identify reference planes sufficient to map them to either ratio family (OCL-486, V; OCL-487, C).

Selected matrix-size examples cover a 1D welded longitudinal system (2 unknowns/2 conditions/2x2), isotropic plane-strain elastic P--SV scattering (4/4/4x4), and the displayed classical Fourier thermoelastic plane-strain model (three generic branch pairs per side, 6/6/6x6). `verify_interface_mode_counts.py` checks the displayed characteristic determinant degree/factors and the dimensions from stated mode/condition counts; `verify_interface_energy.py` checks the 1D amplitudes and both energy partitions. Neither script establishes rank or radiation admissibility for the multidimensional examples. No count or flux identity is transferred to generalized/piezoelectric/nonlocal families (OCL-484 V, OCL-485 B). The current ledger is 487 rows (A=30, B=128, C=314, V=15; A+V=45), and `MISSING_SOURCES.csv` remains at 23.

### Q2 rendered-text audit — CI 40478413805

The final content commit is `e1452a8ffa0ecb0bcaba360ef7936e1d3c3c2bce`; workflow output commit `8b1b9f3139e92d0229ce7d08d9b818af2c24fdb3` contains the PDF/contact sheets. The PDF has 119 pages. Gates: undefined references/citations 0; strict forbidden privacy-token matches 0; forbidden manuscript-tag matches 0; near-overfull boxes (>0.5 pt) 0; strict overfull boxes (>1 pt) 0; 18 figure PDFs rendered/16 master includes; deletion-audit `NONE` rows 0. Ten A/V rendered-text spot-checks matched their anchors: OCL-125 (p. 18), OCL-321 (p. 72), OCL-445 (p. 76), OCL-477 (p. 115), OCL-478 (pp. 3 and 51), OCL-479 (p. 40), OCL-480 (p. 36), OCL-482 (p. 39), OCL-484 (pp. 62–63), and OCL-486 (pp. 63–68). OCL-487's caution is present on p. 65. This is a ten-row spot-check, not a full proof of every page or claim.

Visual inspection covered the final-size mode-count tables and surrounding text (pp. 61–64), interface accounting schematic (p. 62), remote control-volume derivation and welded benchmark (pp. 67–68), and the notation summary. The interface schematic's ratio notation, label positions, and font size were corrected; the figure sources and PDFs were regenerated. CI 40476454180 first exposed a 1.1-pt overfull notation-table symbol cell. The symbols were wrapped, not the layout gate relaxed; CI 40476895866 then passed. A subsequent visual audit found the schematic still used generic R/T labels, so OCL-486 was extended to cover the figure and verification script. CI 40477763908 passed the notation harmonization; the final legibility adjustment passed CI 40478413805. All final metrics above are from that last content run.

### B22 F11 re-check: Kumar et al. (2023), *Phys. Scr.* 98:115211

**CONFIRMED-IN-SOURCE; B22 anchor concern resolved.** The exact article identified by DOI `10.1088/1402-4896/acfced` was reopened. Its first page identifies *Energy ratio response at the interface of elastic and dual-porous thermoelastic half-spaces* and the author/title metadata. The PDF has 19 pages; printed p. 17 exists and contains Section 9, “Conclusion.” That page states that the total sum of energy ratios approximates unity for every angle of incidence. This supports the manuscript's bounded paraphrase as a reported numerical observation, not an exact conservation identity. B22's p. 17 concern relied on a different Kumar paper/PDF (identified there as a *PNAS I* article); it does not apply to the DOI-matched *Physica Scripta* article. OCL-207 therefore remains Class A with the p. 1 identity and p. 17 conclusion anchors.
