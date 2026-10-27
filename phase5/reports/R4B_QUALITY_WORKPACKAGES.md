# R4B quality work packages Q1–Q5

**State:** sequenced after the targeted Section 10 pass; Q1 is active. Initial equation-level substitution checks are recorded as OCL-470–OCL-473 (Class V), but the unified notation, source-by-source reduction map, and comparison table remain incomplete. The order below is intentional. The targeted Section 10 energy-partition/matrix derivation is complete for its stated one-dimensional welded model; it does not close the remaining generalized-family or interface questions. No page-count target applies.

## Governing evidence rule

Every new substantive manuscript statement must map either to a Class A ledger row with `resolved_by` and claim-specific source anchors, or to a reproducible derivation/check under `phase5/verification/` recorded as Class V with its script path. Model-dependent and unresolved material must be labelled with the exact model/scope and retained as B/C where evidence is incomplete; hedging alone is not closure. New bibliography DOIs must be verified against the source paper or a saved Crossref response. Do not store source PDFs, copied prose/tables, private Drive identifiers, or private Drive links in the repository.

## Q1 — Unified synthesis (active)

**Progress note:** `phase5/verification/verify_unified_reductions.py` currently passes checks for LS-to-Fourier, first-order DPL-to-LS/Fourier, TPL-to-DPL, the displayed MGT heat-flux law-to-Fourier, derivative-level GN-III/GN-II compatibility, selected integer-order Caputo monomials, and the displayed nonlocal Helmholtz/dispersion local limits (OCL-470–OCL-473). These are equation-level substitutions only. They do not verify source transcription, solution convergence, complete model equivalence, or stability/admissibility. GL and GN-I reductions, the unified notation/template, the source-by-source reduction map, and the theory-comparison table remain open.

**Deliverables**

1. Establish a unified notation and common constitutive/field-equation template for Lord–Shulman (LS), Green–Lindsay (GL), Green–Naghdi I/II/III, dual- and triple-phase-lag (DPL/TPL), Moore–Gibson–Thompson (MGT), fractional, and nonlocal variants. Define variables, fluxes, operators, sign/time conventions, and admissible parameters before comparing models.
2. State the exact substitutions, parameter limits, or operator replacements that reduce one displayed formulation to another. Do not treat a family acronym as a unique model: identify variants and assumptions explicitly.
3. Verify each claimed reduction either symbolically with a saved script in `phase5/verification/` or against the exact cited source equation with page/equation anchors. Do not invent a unifying equation where formulations are not equivalent.
4. Add a structured theory-comparison table with columns for assumptions, state variables, heat-flux law, wave speeds/finite-speed property, stability/well-posedness, and dissipation. Every cell must be Class A with a source-anchored row or explicitly labelled **model-dependent** with its variant and reason; unresolved cells remain open in the ledger.

**Completion check:** reduction checks pass; notation is internally consistent with the manuscript; the comparison table has scope labels and ledger coverage; no blanket stability, finite-speed, or dissipation claim is inferred from a theory name alone.

## Q2 — Derivation quality

**Status:** Section 10's remote-plane versus local-interface residual, steady control-volume loss split, double-counting explanation, and welded 1D two-amplitude/two-condition matrix are verified in `phase5/verification/verify_interface_energy.py` (OCL-465–OCL-468, Class V). The interface-chapter pass remains open.

**Remaining deliverables:** harmonize the Section 9 interface derivations with Section 10; state assumptions and define incident/reflected/transmitted quantities at explicit reference planes; derive each interface matrix dimension from independent boundary/matching conditions and unknowns; distinguish amplitude ratios, flux-weighted power ratios, local interface residuals, and remote-plane absorption; and script-check every algebraic partition used as a benchmark. Include all model-specific energy channels and avoid counting the same bulk loss twice.

## Q3 — State of the field

For each Q1 family, document separately what is established, disputed/model-dependent, and open. Give the exact source/equation or result anchor, parameter and boundary-condition limits, and the reason an item is disputed or open. Include attribution conflicts, known ill-posed formulations/counterexamples, restrictions on parameters, and gaps caused by unavailable primary papers. A metadata match or search result is not claim verification; preserve conflicting source anchors instead of choosing one without evidence.

**Completion check:** each family has scoped established/disputed/open entries linked to ledger rows; unresolved disagreements and inaccessible papers remain visible rather than being converted to consensus statements.

## Q4 — Narrative and practical usefulness

Revise the introduction and contribution/scope statements only after Q1–Q3 evidence is stable. Add a conditional theory-selection guide (inputs, assumptions, and limitations); a list of validated analytical/numerical benchmarks that distinguishes script-verified identities from source-verified published results; and a research roadmap whose items derive directly from the Q3 open/disputed register. Do not call a result a benchmark unless its model, parameters, boundary conditions, and validation path are recorded.

**Completion check:** novelty and scope claims are evidence-mapped, the decision guide does not rank theories universally, and each roadmap item traces to a documented gap.

## Q5 — Presentation

Standardize symbols, subscripts, sign/time conventions, and abbreviation lists. Keep figures only where the depicted relations are verified; prefer script-generated diagrams or plots from verified formulas. Every figure caption must state the governing assumptions and scope, and each figure/table claim must have ledger coverage. Check final-size legibility and consistency between figure labels, equations, and text.

**Completion check:** notation and abbreviations are reconciled; figure sources/scripts and assumptions are recorded; visual review is completed at final PDF scale.

## Subsequent work, in the requested order

After Q1–Q5, continue WP3 reference hygiene (including Kumar2017 and the required Crossref re-check), WP4 equation audit, WP6 mock referee, WP7 journal-pack drafts, WP8 final consistency, and the Drive-based ledger/source-note work. The remaining WP2 source-backed section work (Section 4 beyond the targeted Tzou pass, Sections 11 and 13, then 14–17) remains open and must be scheduled against this sequence without overstating completion.

## Final report acceptance

The final report must enumerate Q1–Q5 deliverables and their verification state; list the verified unified-framework reductions and their exact script/source anchors; report current Class A and Class V row counts; and identify the five weakest remaining sections with a concrete reason for each. Also state what remains unresolved and distinguish successful engineering builds from scientific verification.
