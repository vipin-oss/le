# BLUEPRINT v3.1: Research Architecture FROZEN (blueprint level only)

Freeze scope: this freezes the research architecture and the verification rules. It is NOT a statement that the manuscript is ready. Manuscript readiness is assessed only after phases P1-P7. Section 9 defaults are the recommended ones; the author may change them before P0 closes.

Working title (recommended default, author to confirm):
**Coupled Wave Dynamics in Continuous Media: Constitutive Frameworks, Multiphysics Interactions, Model Admissibility, and Reproducible Benchmarks**

Author: Vipin Gupta (Gurugram University), formal corresponding contact for any journal. The author is responsible for every claim. AI assistance is disclosed (Section 8).

History: v1 reviewed independently (major revision) -> v2 -> second review (conditional approval, 5 corrections) -> v3 -> third review (conditional approval, 6 corrections and 1 refinement) -> this v3.1 implements them. Both reviews were by another AI model; they are advice, not authority. Journal facts below were reported by the second review and are to be re-checked by the author on the journals' own pages.

---

## 1. TARGET

A critical, physics-aware reference review of coupled wave dynamics in continua, with heat conduction as a major organising theme, that serves four purposes:
1. **Theory:** which model is mathematically and thermodynamically appropriate under which conditions.
2. **Model selection:** scientific basis for choosing among classical, generalized thermoelastic, nonlocal, porous, viscoelastic, piezoelectric, magnetic and multiphysics models (simplest physically justified model, not the most complex).
3. **Verification:** how to validate a new model, dispersion equation or solver (benchmark registry; code verification kept separate from physical validation).
4. **Research development:** what is established, conditional, disputed, unverified or open.

Not an encyclopedia of wave equations. No use of "first", "universal", "complete", "unprecedented".

## 2. NOVELTY (what must carry the paper)

Heat-law unification alone is not novel. Prior work exists and must be compared head-on in an originality matrix (not only cited historically):
- Shakeriaski et al., J. Comput. Des. Eng. 2021, DOI 10.1093/jcde/qwaa082 (review of generalized thermoelasticity; already in our bibliography).
- Critical review of non-Fourier bio-heating with phase lags, Int. J. Thermal Sci. (published 2026, DOI 10.1016/j.ijthermalsci.2025.110376; reports inconsistent phase-lag values).
- "On the phase-lag Green-Naghdi thermoelasticity theories", Appl. Math. Model., DOI 10.1016/j.apm.2016.01.010 (unified LS/GN/phase-lag formulation with thermodynamic restrictions).
- "On a multi-phase-lag model of coupled thermoelasticity", Int. Commun. Heat Mass Transfer, DOI 10.1016/j.icheatmasstransfer.2020.104722.
- Also: Chandrasekharaiah 1998 (AMR), Joseph and Preziosi 1989 (RMP).
Our distinguishing contributions must be: cross-theory comparison under one set of conventions, independently verified wave benchmarks, admissibility matrix, parameter-identifiability discussion, experimental validity assessment, and the model-selection guide. Status of these DOIs: the 2016 phase-lag Green-Naghdi paper was confirmed by the reviewers on public pages; all four still need R3 verification by full-text reading.

**Contribution map (required, links novelty to evidence):** for every distinct contribution claimed, one row with contribution_id, closest prior work (DOI), precise difference, supporting evidence (script, derivation, or R3 source), manuscript location, and the claim_id(s) in the claim register. A contribution without a filled row is not claimed in the paper.

## 3. MATHEMATICAL FRAMEWORK AND ITS CONDITIONS

Replace "one polynomial" by a hierarchy: balance laws; constitutive transfer functions G(s); wave operators; characteristic determinants det D(k, omega; mu) = 0; geometry-specific secular equations.
Must state the assumptions each step requires:
- Linear, time-invariant, homogeneous media: Fourier-Laplace transform gives an algebraic characteristic relation.
- Exact delays (exponentials), fractional powers, hereditary kernels: not polynomial; transcendental or multivalued.
- Layered and periodic media: transfer operators, Bloch/Floquet conditions.
- Spatially variable, time-varying and nonlinear problems: no global algebraic dispersion relation from a simple Fourier-Laplace transform; separate formulations.
- Finite-domain and heterogeneous problems generally require boundary-value, operator eigenvalue, or discretized formulations; they are not necessarily characterized by the homogeneous bulk dispersion relation.
Explicit distinctions throughout: constitutive law vs conservation law; bulk dispersion vs surface/interface secular equation; temporal stability vs spatial attenuation; thermodynamic admissibility vs causality; exact delays vs truncated approximations; local vs nonlocal; well-posedness vs merely finding roots; code verification vs model validation.
Branch tracking by continuation of eigenvalues together with eigenvector or subspace information, residual checks and physical mode criteria where applicable (not by sorting phase speed, and not by eigenvector matching alone, which can fail near degeneracies, exceptional points, repeated eigenvalues and strongly non-normal coupled operators); group-velocity caveats in dissipative media; Stoneley/Scholte need decay/radiation conditions, a determinant root alone is not a physical mode.

## 4. SCOPE POLICY (exclusion and stopping rule)

Every candidate topic must directly serve at least one of the four purposes in Section 1. Three levels:

| Level | Meaning | Topics (initial assignment) |
|---|---|---|
| Full coverage (derivation, verified check, comparison, and sufficient independently verified primary literature to support the technical analysis) | Core to purposes 1-3 | Thermodynamic admissibility; Love/Stoneley/Scholte and layered media; Biot poroelasticity; viscoelastic and fractional viscoelastic waves; experimental validation and parameter identification; existing thermal-wave models, Rayleigh, Lamb, reflection, nonlocal, piezo |
| Brief comparative coverage (1-2 pages, key results and references) | Adds context | Micropolar and couple-stress; phononic/Bloch; rotation, pre-stress, gravity; scattering and Green's functions; semiconductor/photothermal; inverse problems and uncertainty quantification |
| Scope boundary only (a paragraph) | Outside focus | Nonlinear waves and solitons; PINNs and neural operators (include a comparison only if done fairly on cost, accuracy, generalisation) |

New topics are added only by a written decision recording which purpose they serve.

## 5. EVIDENCE SYSTEM

**5.1 Reference register** (one row per bibliography entry): key, DOI, full authors, metadata check, level R0-R3.
- R0 unverified or incomplete: not admissible at submission.
- R1 DOI, full authorship, metadata verified: bibliographic record only.
- R2 abstract inspected, claim matched: limited background claims.
- R3 relevant full-text section, equation or figure inspected: technical comparison and benchmark claims.

**5.2 Claim register** (one row per technical claim that cites a source): claim_id, manuscript_location, claim_text, source_doi, source_page_or_equation, verification_level, verifier, status. A reference can be R3 while a claim about it is wrong, so claims are tracked separately.

**5.2b Links between registers:** contribution map (Section 2) -> claim register -> reference register. Every contribution row points to claim_ids; every claim_id points to a reference row or to an in-paper derivation or script.

**5.3 Controversy classification** for every major scientific issue in the synthesis sections, justified by evidence and not applied automatically:
Established / Conditional (explicit assumptions or regimes) / Disputed (credible studies disagree; compare assumptions, boundary conditions, measurement regimes) / Unverified (predicted, no adequate independent confirmation) / Open (clear unresolved problem).
Example: reported phase-lag values are inconsistent across studies; the right conclusion is a discussion of identifiability and validity, not that every phase-lag model is invalid.

**5.4 Evidence classes for results:** analytic; numerically reproduced; independently reproduced; controlled experiment; limited-regime support; proposed but not experimentally established.

**5.5 Literature search methodology** (short subsection): sources searched, strings, dates, inclusion and exclusion criteria, duplicate handling, citation-chain expansion. No "systematic review" or PRISMA claim unless it is actually done.

**5.6 Independence:** no fixed percentage. Each major topic needs independent supporting literature where it exists; the group-level share of references is reported transparently. The author's own earlier results stay, compared fairly and without promotional framing.

## 6. VERIFICATION, VALIDATION AND UNCERTAINTY RULES

Five gate groups (replacing the 15 gates):
1. **Mathematics:** dimensional analysis, signs, units, notation, limiting cases, stability, convergence, at least one independent re-derivation or second implementation for key results; completeness of physical boundary and interface conditions; the admissible parameter domain of each constitutive model; passivity where applicable; admissibility of every modal root (decay or radiation conditions, correct branch). Especially for interface, coupled and nonlocal problems.
2. **Evidence:** reference register and claim register complete; every critical technical claim at R3 or independently derived; search audit documented.
3. **Reproducibility:** every number from versioned code with inputs and environment; clean-environment run; archive with checksums, licence and DOI.
4. **Benchmarks:** for each record the quantity tested, reference solution, error measure, parameter domain, precision, and why the tolerance was chosen. A 1e-10 elastic-limit match verifies that limit only; a Kramers-Kronig check does not prove admissibility. Every parameter is labelled known, fitted, assumed or numerical setting, with sensitivity or uncertainty where meaningful. Code verification and physical validation are reported separately.
5. **Editorial and review:** journal fit confirmed, template, declarations; author audit of all critical claims; two or three independent expert readers.

## 7. STRUCTURE (planning ranges, not requirements)

| Part | Content | Pages |
|---|---|---|
| I | Scope, research questions, originality matrix vs prior reviews, search methodology | 12-16 |
| II | Fundamental theory: balances, constitutive theory, thermodynamics, causality, dimensional analysis, admissibility matrix | 18-22 |
| III | Thermal-wave constitutive models: classical, LS, GL, GN, Cattaneo, DPL/TPL, MGT, GK, fractional, memory | 20-24 |
| IV | Mathematical wave framework: operators, conditions of validity, branches, attenuation, stability, boundaries, interfaces | 16-20 |
| V | Wave geometries: bulk, surface, interface, guided, layered (Love/Stoneley/Scholte), periodic, scattering | 23-28 |
| VI | Coupled material physics: piezoelectric, magnetic, porous, viscoelastic, micropolar, nonlocal, semiconductor | 24-28 |
| VII | Verification and evidence: analytic, numerical, convergence, experiments, parameter identification and uncertainty, inverse problems | 16-20 |
| VIII | Critical synthesis: model-selection guide, problem atlas and benchmark registry, controversy table, open problems | 16-20 |
| Appendices | Derivations, tables, parameter register, code, supplementary bibliography | extra |

Part II establishes the physical and mathematical criteria (admissibility, causality, stability, dimensional analysis); Part IV applies the operator and spectral machinery. Do not duplicate stability, causality and dispersion material between them.

Total planning range 150-180 pages (up to 200 only with editorial agreement). Custom 12pt pages differ from journal pages. Verification and admissibility come before the model catalogue.

**Problem atlas** (replaces the 17-row table): fields = ID, wave family, constitutive model, geometry, couplings, assumptions, governing formulation, verification, parameters and units, reported result, limitations, sources (original and independent), reproducibility (script, inputs, expected output, tolerance). Aim about 40-60 evaluated representative cases; the number follows feasible verification. Separate **benchmark registry** for solver validation.

## 8. POLICIES

- **AI declaration:** disclose substantial AI assistance in drafting, coding, literature organisation and technical checking; author keeps full verification responsibility; use the journal's required wording.
- **Code and data:** archive code and redistributable data with a versioned Zenodo DOI, subject to licensing.
- **Not accepting unverified output:** nothing produced by any tool is merged without a build and the relevant register check.

## 9. DECISIONS TO CONFIRM (author)

1. Title and scope: confirm the working title above (heat conduction as a major theme, not the only one).
2. Journal: Applied Mechanics Reviews as first practical target; Physics Reports as high-ambition option requiring an accepted proposal (author as formal contact). Progress in Materials Science only with a materials-science emphasis. Re-check each journal's current author guidelines.
3. Full-coverage topics as listed in Section 4.
4. Expert readers: one continuum thermodynamics specialist, one elastic or guided-wave specialist, one numerical or experimental wave specialist (named by the author).
5. Journal wording for the AI declaration.
6. Code and data release.

## 10. PHASES

| Phase | Work | Exit condition |
|---|---|---|
| P0 | Scope and originality: research questions, originality matrix and contribution map vs prior reviews, mathematical conditions of validity, exclusion policy, journal choice. Two separate documents: (a) Applied Mechanics Reviews editorial inquiry (describe article, current length, intended contributions, expected expansion; do not assume 150-180 custom LaTeX pages is suitable); (b) Physics Reports proposal (the 1,000-word limit with an identified editor is specific to that journal) | Section 9 answered; matrix done; both documents drafted |
| P1 | Integrity audit of the existing 134 pages: equations, signs, notation, assumptions, the 35 scripts, independent re-derivation of the central results, rewrite of the overbroad unification wording | Audit report; fixes merged; build clean |
| P2 | Evidence registers: reference register R0-R3 for all 323 entries, claim register for technical claims, fix 32 memory-typed and 41 truncated records, search protocol, missing landmark works | No R0 entries; critical claims at R3 |
| P3 | Full-coverage expansions: admissibility, Love/Stoneley/Scholte and layered, Biot, viscoelastic, parameter identification and experiments | Each with equations, verified checks, sources, evidence classes |
| P4 | Integration: common conventions, cross-model limits, mode tracking, benchmark registry, independent second implementations | Registry published in repository |
| P5 | Critical synthesis: model-selection guide, controversy table, rebuilt atlas, research agenda | Tables complete |
| P6 | Two or three expert reviews; resolve findings | Responses logged |
| P7 | Journal submission package: template, declarations, figures, archive DOI, cover letter | Submitted |

No new chapters are written before the P1 audit confirms the central derivations and conventions are internally consistent.

## 11. FREEZE AND APPROVAL CHECKLISTS

### 11a. Blueprint freeze (design level, this document)

Blueprint-level pass criteria for the five gate groups:

| Gate | Pass criterion at blueprint level |
|---|---|
| Mathematics | All required checks defined; central conventions and validity assumptions specified |
| Evidence | Reference and claim register schemas finalised; verification rules documented |
| Reproducibility | Benchmark record schema, environment requirements, release policy defined |
| Benchmarks | Acceptance rules for accuracy, convergence, independent verification, physical validation documented |
| Editorial and expert review | Target journal strategy, responsibilities, expert assessment plan defined |

- [x] Scope and exclusion policy final (Section 4)
- [x] Mathematical framework and its conditions specified (Section 3)
- [x] Originality matrix and contribution map defined (Section 2); filled in P0
- [x] Reference, claim and contribution registers designed (Section 5)
- [x] Full-coverage topics approved (Section 4); no further major expansion now
- [x] Verification, validation and uncertainty rules final (Section 6)
- [x] Journal strategy defined (AMR inquiry first, Physics Reports proposal as alternative)
- [ ] Expert readers named by the author (three complementary specialists, P0/P6)
- [x] Code/data archive and AI declaration policies defined (exact AI wording after journal choice)

### 11b. Manuscript submission approval (NOT yet assessed; completed only after P1-P7)

Passing the gates means actually completing the checks, not defining them:
- [ ] P1 audit of the 134 pages, derivations and the 35 scripts complete
- [ ] Reference register has no R0 entries; critical claims at R3 or independently derived
- [ ] Contribution map filled and checked against prior reviews
- [ ] Benchmark registry complete, independent implementations done
- [ ] Two or three expert reviews received and resolved
- [ ] Journal fit confirmed, template, declarations, archive DOI complete

---

## 12. Implementation clarifications (from the final review; no revision of the architecture)

1. R0 handling in P2: references that are successfully verified move to R1 or higher; records that cannot be verified are excluded or replaced. An unverifiable reference is never forced to R1 to satisfy the exit condition.
2. Reproducibility scope: "every number from versioned code" applies to computed numerical results and generated figures. Values quoted from the literature are traceable to their verified original source and are not regenerated.
3. Expert readers: expertise requirements are fixed; names are identified during P0 or before P6 and do not delay P0-P2.
4. Scope changes after freeze go through the Section 4 procedure (written decision tied to a purpose), not through a new blueprint version.

STATUS: BLUEPRINT v3.1 - RESEARCH ARCHITECTURE FROZEN. Next: P0 (originality, AMR inquiry), P1 (manuscript and script audit with defect register), P2 (bibliography and claim verification).
