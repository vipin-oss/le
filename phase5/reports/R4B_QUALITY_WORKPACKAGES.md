# R4B quality work packages Q1–Q5

**State:** Q1 and Q2 are complete at their explicitly scoped, evidence-bounded levels. After B22 P1/P2 closure, Q3 is resumed: a 14-family status matrix and structural/source-map verifier are in place, with the source-review completion boundary recorded in `Q3_STATUS_AUDIT.md`. Q4 and Q5 remain next. Q1's Section 4 scaffold is limited to local Cauchy balances with non-universal closure placeholders (OCL-480, Class V); its matrix covers every requested family and comparison dimension while source-dependent claims and open cells remain B/C (OCL-481, OCL-483), with structural coverage separately checked (OCL-482, Class V). The reduction map checks only displayed-equation substitutions for LS, GN-II/III derivative compatibility, DPL, TPL, MGT, fractional endpoints, and nonlocal local limits; GL/GN-I and MDD reductions remain open (OCL-479, Class V). OCL-169 is Class A only for the cited first-order TPL form; GL/GN source evidence remains limited to the exact pages in OCL-474–OCL-476. Q2 distinguishes interface-plane $R_{\Sigma},T_{\Sigma}$ from remote-plane ratios, includes separate left-bulk/interface/right-bulk losses, verifies selected 2x2/4x4/6x6 local matching examples, and leaves generalized-family counts/fluxes open (OCL-484–OCL-487). Latest content CI 40478413805 passed on `e1452a8ffa0ecb0bcaba360ef7936e1d3c3c2bce`; 119 pages, undefined references/citations 0, strict overfull boxes >1 pt 0, near-overfull >0.5 pt 0, forbidden privacy/tag matches 0, 18 figures rendered/16 master includes. Final-size pages 62–68 and the revised interface figure/table were reviewed. Q2 completion ledger checkpoint: 487 rows (A=30, B=128, C=314, V=15); `MISSING_SOURCES.csv` was at 23 at that checkpoint. These results establish engineering checks and selected algebra only, not generalized constitutive validity. No page-count target applies.

## Governing evidence rule

Every new substantive manuscript statement must map either to a Class A ledger row with `resolved_by` and claim-specific source anchors, or to a reproducible derivation/check under `phase5/verification/` recorded as Class V with its script path. Model-dependent and unresolved material must be labelled with the exact model/scope and retained as B/C where evidence is incomplete; hedging alone is not closure. New bibliography DOIs must be verified against the source paper or a saved Crossref response. Do not store source PDFs, copied prose/tables, private Drive identifiers, or private Drive links in the repository.

## Q1 — Unified synthesis (complete at evidence-bounded scope)

**Progress note:** The shared local-Cauchy balance scaffold, unified notation checks, comparison matrix, and reduction map are in place and passed CI 40463595470. `phase5/verification/verify_unified_reductions.py` checks displayed LS-to-Fourier, first-order DPL-to-LS/Fourier, TPL-to-DPL, candidate MGT-to-Fourier, derivative-level GN-III/GN-II compatibility, Caputo endpoints, and nonlocal local limits (OCL-470–OCL-473, OCL-479). These are equation-level substitutions only; GL/GN-I equation-level reductions, MDD limits, source-specific closures, and model-dependent stability/dissipation properties remain open at B/C in the ledger. The package is complete as a scoped evidence-bounded comparison, not as closure of those source gaps.

**Deliverables**

1. Establish a unified notation and common constitutive/field-equation template for Lord–Shulman (LS), Green–Lindsay (GL), Green–Naghdi I/II/III, dual- and triple-phase-lag (DPL/TPL), Moore–Gibson–Thompson (MGT), fractional, and nonlocal variants. Define variables, fluxes, operators, sign/time conventions, and admissible parameters before comparing models.
2. State the exact substitutions, parameter limits, or operator replacements that reduce one displayed formulation to another. Do not treat a family acronym as a unique model: identify variants and assumptions explicitly.
3. Verify each claimed reduction either symbolically with a saved script in `phase5/verification/` or against the exact cited source equation with page/equation anchors. Do not invent a unifying equation where formulations are not equivalent.
4. Add a structured theory-comparison table with columns for assumptions, state variables, heat-flux law, wave speeds/finite-speed property, stability/well-posedness, and dissipation. Every cell must be Class A with a source-anchored row or explicitly labelled **model-dependent** with its variant and reason; unresolved cells remain open in the ledger.

**Completion check:** reduction checks pass; notation is internally consistent with the manuscript; the comparison table has scope labels and ledger coverage; no blanket stability, finite-speed, or dissipation claim is inferred from a theory name alone.

## Q2 — Derivation quality (complete at selected-model scope)

**Status:** The selected, local benchmark work is complete and passed content CI `40478413805` on `e1452a8ffa0ecb0bcaba360ef7936e1d3c3c2bce`. Section 10 distinguishes the remote-plane residual from local interface loss, derives the steady control-volume split and double-counting consequence, and checks the welded 1D two-amplitude/two-condition system (OCL-465–OCL-468, OCL-486, Class V). Section 9 now uses $R_{\Sigma},T_{\Sigma}$ for interface-plane total-field bookkeeping and explicitly distinguishes them from R_rem/T_rem; the remote balance includes bulk-left, interface-local, and bulk-right losses. The selected 1D, plane-strain isotropic elastic, and classical Fourier thermoelastic examples have 2x2, 4x4, and 6x6 matching dimensions derived from checked modal counts and listed conditions (OCL-484, Class V). The V-B3d report's cross-term values remain audit-specific; because its saved summary lacks a reference-plane convention, they are not mapped to either ratio family (OCL-487, Class C). Final-size review covered PDF pp. 62–68; the interface schematic and notation summary were harmonized and checked.

**Open boundary:** no universal mode count, matrix rank, radiation admissibility, or family-wide energy flux is inferred for LS/GL/GN/phase-lag/MGT/fractional, piezoelectric, nonlocal, or memory-dependent systems. OCL-485 remains B pending exact-model dispersion roots, field closure, boundary conditions, and source/equation anchors. This package does not establish uniqueness or well-posedness for the selected square systems beyond the separately checked 1D positive-impedance determinant.

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
