# Source and page-count reconciliation (v1.0 baseline → phase5 working build)

## Observed page counts and limits

- Baseline PDF: 161 pages (`phase4/manuscript/main.pdf`, byte-identical to `phase5/master/v1.0-baseline.pdf`).
- Latest independent rebuild reported by the control status: 144 pages for the manuscript source at `6e81d2b`. The corresponding latest Actions run, `39735068142`, built `d424434` (the same manuscript TeX source; the subsequent `6e81d2b` commit changed reports/packages only), also reported a transient 144-page PDF. That run failed the strict overfull-box gate and its PDF was not uploaded, so this report does **not** claim visual/page-by-page comparison.
- Difference: 17 fewer pages in the transient build. This is not equivalent to 17 whole pages of content being deleted. TeX page breaks and float placement are global and can shift when prose, tables, front matter, and line breaks change. A causal “pages saved by section” allocation cannot be made from source token deltas alone.
- Source-structure check: both main files include the same 17 numbered section files and the same seven appendix files; all eight table-source files have direct phase4/phase5 pairs. No complete section or appendix input was removed. Some inherited claims/material were deliberately withdrawn or narrowed, as listed below; that is not a claim that every underlying topic was fully audited.
- The comparison counts word-like source tokens using `scripts/reconcile_page_count.py`. It includes comments and LaTeX commands and is **not a prose word count** or page estimator. It is reproducible evidence of source-level size changes only.

## Section-by-section source changes

| File | v1.0 source tokens | v1.1 source tokens | Delta | Change/reconciliation |
|---|---:|---:|---:|---|
| `sec01_scope.tex` | 1632 | 1330 | -302 | Reframed the Fourier “infinite-speed” paradox as a property of the idealized model; softened universal claims about generalized theories and narrowed the scope objectives. |
| `sec02_literature.tex` | 2590 | 2380 | -210 | Condensed literature-strategy language; retains the inherited inventory and its non-systematic-search limitation. |
| `sec03_foundations.tex` | 3335 | 3418 | +83 | Expanded the directly checked classical balance/flux derivation and corrected index/sign conventions (+83 source tokens). |
| `sec04_thermoelastic.tex` | 3146 | 2538 | -608 | Removed or narrowed legacy family-wide descriptions; replaced unsupported equation/status assertions with explicitly conditional or unverified wording. |
| `sec05_multiphysics.tex` | 2856 | 2565 | -291 | Condensed the overview and narrowed statements about added fields, modal counts, and interface conditions to model-specific claims. |
| `sec06_transport.tex` | 2839 | 2158 | -681 | Condensed family-level transport claims; withdrew universal operator/limit/admissibility generalizations not established for every model. |
| `sec07_nonlocal.tex` | 2765 | 2378 | -387 | Condensed and bounded nonlocal/gradient dispersion and flux claims to displayed models and stated assumptions. |
| `sec08_mathematical_methods.tex` | 2625 | 2343 | -282 | Condensed method survey; no entire section removed. |
| `sec09_interfaces.tex` | 2468 | 2477 | +9 | Nearly unchanged by source-token count; section remains included. |
| `sec10_energy.tex` | 2996 | 1849 | -1147 | Largest section reduction: withdrew unverified generalized-family flux/conservation claims and retained the scoped classical result plus explicit open items. |
| `sec11_advanced.tex` | 2460 | 2440 | -20 | Nearly unchanged; section remains included. |
| `sec12_comparative.tex` | 3369 | 3051 | -318 | Condensed and reorganized comparisons; wide comparison tables were split/reflowed, not deleted. |
| `sec13_applications.tex` | 2500 | 2503 | +3 | Retained and slightly expanded the application/evidence discussion. |
| `sec14_taxonomy.tex` | 3816 | 3820 | +4 | Retained the taxonomy discussion and inventory analysis; source-token count is essentially unchanged. |
| `sec15_challenges.tex` | 2874 | 2813 | -61 | Light condensation of challenge/future-problem prose. |
| `sec16_future.tex` | 1810 | 1676 | -134 | Condensed future-work prose; research directions remain represented. |
| `sec17_conclusions.tex` | 2106 | 1767 | -339 | Replaced broad “established” claims with a narrow “derived in this revision” list and explicit open status; duplicate historical figure use replaced by a reference to the existing figure. |

## Appendix-by-appendix source changes

| File | v1.0 source tokens | v1.1 source tokens | Delta | Change/reconciliation |
|---|---:|---:|---:|---|
| `appA_equation_register.tex` | 1492 | 1243 | -249 | Replaced inherited VERIFIED/PARTIAL labels with DERIVED/CONDITIONAL/UNVERIFIED/OPEN; withdrew legacy equations that lack source/derivation support. |
| `appB_balance_derivations.tex` | 644 | 645 | +1 | Balance derivation retained; essentially unchanged. |
| `appC_benchmarks.tex` | 321 | 334 | +13 | Benchmark claims/status language remains limited; no benchmark is represented as independently reproduced. |
| `appD_figures.tex` | 1047 | 447 | -600 | Replaced claims of scientific validation with the 18-item source/status register and final-proof requirements; figure inventory retained. |
| `appE_tables.tex` | 394 | 324 | -70 | Condensed appendix table notes; tables remain listed in the source tree. |
| `appF_reproducibility.tex` | 482 | 385 | -97 | Removed legacy “all reproducible/PASSED” and obsolete pipeline/database claims; replaced with actual repository/build limitations. |
| `energy_flux_derivations.tex` | 2873 | 2352 | -521 | Converted purported family-wide “derivations” into explicitly open audit leads; retained only the classical local Cauchy-flux derivation as checked under stated assumptions. |

## Table-source changes

| File | v1.0 source tokens | v1.1 source tokens | Delta | Change/reconciliation |
|---|---:|---:|---:|---|
| `T1_historical_development.tex` | 418 | 230 | -188 | Condensed historical rows/notes. |
| `T2_generalized_thermoelastic.tex` | 316 | 231 | -85 | Condensed theory-family rows/notes; review remains incomplete. |
| `T3_coupled_multiphysics.tex` | 206 | 211 | +5 | Small terminology/layout edits; table retained. |
| `T4_wave_types.tex` | 228 | 234 | +6 | Small terminology/layout edits; table retained. |
| `T5_solution_techniques.tex` | 239 | 242 | +3 | Table retained; current edit is layout-only. |
| `T6_interface_configurations.tex` | 231 | 239 | +8 | Table retained; current edit is layout-only. |
| `T7_energy_transport.tex` | 297 | 241 | -56 | Condensed notes/claims; table retained. |
| `T8_applications_validation.tex` | 190 | 162 | -28 | Condensed notes/claims; table retained. |
| **Total** | **55565** | **49026** | **-6539** | Sections, appendices, and table sources only. |

## Explicitly visible content withdrawals / de-duplication

- **Section 10 and `energy_flux_derivations.tex`:** unsupported universal/generalized energy-flux claims were withdrawn or relabelled as open; the classical local flux remains stated with its explicit assumptions. This is the main deliberate content reduction and is documented in `CHANGELOG.md` and the equation audit.
- **Appendix A:** legacy equation statuses are not carried forward as evidence. Unsupported Green–Lindsay, TPL, MDD-kernel, MGT, and electrical-storage equations are marked unverified/open or withdrawn from the asserted register.
- **Appendix D:** the 18 figure entries remain, but prior assertions that all scientific content, dates, modal counts, and conservation identities were validated were replaced with source/render status and explicit open checks.
- **Appendix F:** removed inherited “all reproducible/PASSED” statements and obsolete pipeline/database descriptions that were not supported by current repository evidence.
- **Section 17:** overbroad “Established” list replaced by “Derived in this revision” and an explicit open list; an extra reuse of the historical overview figure was replaced with a reference to the existing figure.
- **Tables:** no table-source file was removed. Several inherited table notes/claims were shortened or made conditional; comparison tables were reflowed/split for layout.

## Remaining evidence needed for an exact page-level explanation

Runs `39739383577` and `39739833380` uploaded their PDFs, extracted text, metadata, and contact sheets, but artifact download from this environment returned EOF. The 144-page report is from the prior independent rebuild and run `39735068142`; the page count from `39739833380` has not been independently retrieved. Local text extraction and visual comparison against the 161-page baseline are still required to certify page-by-page correspondence and quantify float/reflow effects. The 17-page difference is observed and source-level changes are itemized, but a strict causal page allocation and final no-loss visual proof remain OPEN.
