# Internal reviewer simulations — not peer review

**Important:** These are explicitly hypothetical, internal red-team scenarios. No real journal reviewer read this manuscript, and no review text or endorsement is being attributed to any person. They are issue-finding prompts based on the current incomplete phase5 source. They cannot substitute for independent external review.

## Simulated Reviewer 1 — continuum thermomechanics / mathematical consistency

### Recommendation: Major revision; reject any claim of completion pending derivation and build

1. The revised classical flux `J_i=q_i-sigma_ij v_j` is plausible under the stated symmetric Cauchy-stress and local-balance assumptions, but the paper has not shown that all appendices, tables, boundary conditions, and interface-normal conventions are consistent. It must include a short transparent derivation and a source sweep.
2. The draft still discusses GN-II/III, DPL/TPL, MGT, MDD, fractional and nonlocal theories without a model-specific balance for each. The authors appropriately avoid a universal flux formula, but a review cannot leave the central subject almost entirely open while using broad family labels. Choose a narrower claim and derive only what follows from each displayed constitutive set.
3. The GL, LS, and piezoelectric corrections are not source-verified. Provide the exact primary-source equations, notation map, assumptions, and page/equation references after inspecting the source. Do not use an inherited bibliography record as evidence of equation correctness.
4. The fractional diffusion-wave equation has been dimensionally repaired, but it is only a scalar equation. Explain how temperature, heat flux, and the mechanical field are coupled, which initial data are needed, and which parameter values retain a physical/thermodynamic interpretation—or clearly label it as a scalar illustration.
5. Strict CI now passes for phase5 and reports the repaired overfull boxes, but the uploaded final PDF/contact sheets remain unavailable for local inspection. The v1.0 PDF's appendix tables appeared to overrun the text block at overview scale. Inspect each table at readable scale and verify the final PDF/log and warning disposition.
6. For nonlocal and higher-gradient models, state the exact boundary power and additional traction terms before discussing an energy-flux ratio. A local Cauchy traction formula is not a universal substitute.

### Author response plan (status, not completed response)

| Point | Current response | Evidence status / action |
|---|---|---|
| Classical balance | Revised sign, indices, and harmonic average; local derivation described in audit | DERIVED; sweep all files, add/check explicit derivation, compile |
| Generalized model balances | No universal law claimed; several equations marked candidate or open | OPEN; primary-source derivations required |
| Primary equations | No original full texts checked in phase5 | UNVERIFIED; obtain and cite exact source equations |
| Fractional theory | Coefficient dimensions corrected and scalar scope narrowed | CONDITIONAL; coupled constitutive formulation still open |
| Tables/compile | Strict CI passed in run 39753968114; 146-page PDF and four contact sheets committed | Build PASSED; overview reviewed, full-size proof and scientific verification remain OPEN |
| Nonlocal boundary work | No universal correction asserted | OPEN; derive per kernel/domain/BC |

## Simulated Reviewer 2 — literature synthesis / editorial and reproducibility

### Recommendation: Major revision; scope and evidence chain are not yet auditable

1. The inherited literature database has 95 records while the local bibliography has 56 keys. Explain inclusion/exclusion, map every substantive claim to relevant primary sources, and distinguish a focused narrative review from a systematic search. The current evidence matrix honestly marks claims OPEN, but this is a work queue, not a literature synthesis.
2. Forty-seven of 95 inventory DOI cells are blank, and the populated DOI/full-text/access flags are inherited rather than rechecked. Resolve records against publisher/Crossref/registries; preserve exact metadata and mark unavailable items. Do not infer relevance from title or journal alone.
3. Several historical, taxonomy, application, and cross-family statements appear broad. Either support them with the original literature or present them as provisional classification rather than established consensus. The words “first,” “complete,” “standard,” and broad superiority claims require explicit evidence.
4. The article wrapper is generic. The target journal, scope, word limit, citation style, data policy, author statement, conflicts, funding, and supplementary-file rules are not known. Do not call the manuscript submission-ready.
5. Figure SVG licensing/authorship is not documented. Captions and equation/claim correspondence have not been verified; a vector PDF and contact-sheet thumbnail do not establish accuracy or legibility.
6. Make the version boundary visible. The repository baseline is 161 pages, whereas the reported 170-page artifact has not been supplied. Do not attribute the observed baseline-table defects or figure state to that separate file.

### Author response plan (status, not completed response)

| Point | Current response | Evidence status / action |
|---|---|---|
| Review method and corpus | 95-row inherited inventory recorded; no new systematic search claimed | OPEN; define protocol, databases, date range, screening, and exclusions |
| DOI and source validation | Evidence matrix labels all rows UNVERIFIED / OPEN | OPEN; re-resolve and inspect each source, then map claims |
| Broad historical/application claims | Selected language narrowed; many remain unverified | UNVERIFIED; line-by-line claim-source audit needed |
| Journal requirements | Generic wrappers only | NOT DONE; choose target only when requested/available; otherwise retain neutral format |
| Figure rights and accuracy | Register discloses source/licence unknown; conversions structurally checked | OPEN; document authorship/licence and review against claim/caption at final size |
| Artifact mismatch | Provenance report explicitly separates the 161- and 170-page PDFs | OPEN; obtain exact 170-page file if it is to be audited |

## Use limitation

These simulations are internal quality-control scaffolding only. They are not independent reviewer reports, do not establish acceptance or rejection likelihood, and should not be represented as external peer review in any package or correspondence.

## WP6 objection register

The 25-item register with locations, concrete fixes, and dispositions is `phase5/reports/WP6_MOCK_REFEREE_REGISTER.csv`. It supersedes the 12 numbered points above as the working list; the simulated reviewers remain internal and are not peer review.
