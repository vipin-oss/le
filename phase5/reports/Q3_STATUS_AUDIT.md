# Q3 theory-status matrix — implementation and audit note

**Status:** Matrix implementation and internal ledger-link audit are complete; Q3's broader source-review deliverable remains **in progress**. No primary source was newly opened for this matrix pass. Statements below are cross-checked against the existing source findings, committed A/V rows, and B/C open-claim records; this note does not convert a previous targeted check into a full-text review.

## Scope and structural check

`Q3_THEORY_STATUS.csv` covers 14 requested families. Each row records an established state, a disputed/model-dependent state, a separate counterexample/ill-posedness status, an open question, the corresponding source/derivation anchor, and ledger IDs. The counterexample field separates source-anchored results from unverified B leads and from families not assessed for counterexamples; it does not imply well-posedness where no counterexample was reviewed. `verify_q3_status_matrix.py` checks all family names and columns, existing ledger IDs, A/V provenance or a live script for established rows, and preservation of the principal unresolved and counterexample statuses. It explicitly does not adjudicate source conflicts.

## Row-by-row evidence map reviewed

| Family | Bounded established evidence carried into matrix | Disputed or open boundary retained |
|---|---|---|
| Classical local Cauchy/Fourier | OCL-480 (V), local balance and positive-temperature Fourier entropy term | OCL-480 excludes generalized boundary-power terms; no transfer to higher-gradient, micropolar, or nonlocal models |
| Lord–Shulman | OCL-470 (V), displayed-form reduction only | OCL-011 and OCL-483 remain C/B; source equation convention and model-wide properties are not closed |
| Green–Lindsay | OCL-474 (A), printed p. 1 abstract scope only | OCL-481 (B); exact equations, state variables, parameter limits, and theorem hypotheses remain open |
| Green–Naghdi I | No equation-level property asserted | OCL-481 (B); exact primary source/equation mapping remains open |
| Green–Naghdi II | OCL-475 (A), abstract facts; OCL-471 (V), derivative-level displayed-form compatibility | OCL-491 (B) and OCL-483 (B); abstract claims do not establish the detailed equation or theorem hypotheses |
| Green–Naghdi III | OCL-476 (A), printed p. 255 scope/footnote; OCL-471 (V) | OCL-492 (B); type-II nondissipation is not transferred, and detailed coupled equations/energy statement remain open |
| Dual-phase-lag | OCL-444 (A) p. 8 and OCL-470 (V), bounded displayed formulation | OCL-445 (A) records stability for strict `>` and unstable solutions for strict `<` in the specified 1D problem; equality is unclassified. OCL-488 (B) preserves the unresolved first-page DOI reports |
| Triple-phase-lag | OCL-169 (A), cited first-order expansion; OCL-470 (V) for displayed substitution | Higher-order variants and family-wide admissibility remain open (OCL-123/OCL-483) |
| MGT | OCL-470 (V), displayed candidate substitution only | OCL-174/OCL-175 (B) and OCL-483 leave source identity, constitutive placement, and stability scope unresolved |
| MDD | OCL-478 (V), notation/displayed-operator checks only | OCL-402/OCL-483 (B); kernel, horizon, normalization, regularity, and energy law are not generalized from a family name |
| Fractional scalar / thermoelastic | OCL-321 (A), source-specific `zeta`/Caputo anchor; OCL-472 (V), displayed scalar algebra | OCL-403 (B) keeps coupled embedding, initial-data space, coefficient mapping, and admissibility open |
| Spatially nonlocal elasticity | OCL-257/OCL-260/OCL-261 (A), bounded paper-specific operator placements; OCL-473 (V), displayed local limit | OCL-258/OCL-480 retain kernel- and boundary-specific limits; no universal interface flux is inferred |
| Positive-gradient models | OCL-478 (V), displayed one-dimensional dispersion/notation algebra | OCL-480 (V) marks higher-gradient boundary power outside the local scaffold; no source-family law is inferred |
| Coupled multiphysics / piezothermoelastic | OCL-195/OCL-207 (A), Mindlin baseline and bounded Kumar numerical observation | OCL-300 (B), OCL-433 (C), and OCL-483 keep coupled interface flux, electrical jump, and common-closure claims open |

The Q3 table now explicitly carries the selected-problem instability result as a counterexample to a universal DPL stability reading, the unclassified critical equality, and the unresolved DOI source conflict. OCL-175's MGT instability statement is separately labeled as a B-class lead pending source verification, not as an established counterexample; the remaining families state when this pass did not assess counterexamples. It also distinguishes the Kumar article identity re-check from the earlier wrong-PDF concern: the DOI-matched *Phys. Scr.* p. 17 supports only its approximate numerical statement.

## Build and audit checkpoint

The status-matrix expansion commit `de1125a` passed CI `40488618346`; the strict-build PDF remained 119 pages. Artifact publication produced commit `57848ce`, which was integrated by rebase before the final audit-note commit `1f6a499`; the fixed-branch local and remote heads were then verified equal. CI reported undefined references/citations 0, privacy-token matches 0, internal-path matches 0, strict manuscript-tag matches 0, near-overfull boxes >0.5 pt 0, 18 figure PDFs rendered/16 master includes, and deletion-audit `NONE` rows 0; the >1 pt overfull gate passed. The hostile diff review found only the 14-family status CSV, its audit note, and the structural verifier changed; no manuscript, bibliography, or PDF source changed. Thus no manuscript claim was added or altered. The ten A/V rendered-text spot-check and page list remain in `B22_HANDOVER.md` and remain applicable to this unchanged PDF. Ledger validation passes at 492 rows (A=30, B=132, C=315, V=15).

## Audit limits and next work

The matrix is an evidence map, not a systematic literature review and not a proof of consensus across each family. Seven rows in B22's 26-row Class A sample were not checkable because the source was not held; these are not represented as absent. Unavailable primary equations and model-dependent properties remain B/C or explicitly open. Next, complete Q3's remaining source-specific checks and update each matrix row only when the exact source anchor is available; then proceed to Q4 and Q5. Current main ledger checkpoint is 492 rows (A=30, B=132, C=315, V=15); OCL-491 and OCL-492 separately record the GN-II/III equation-level gaps.
