# R4B-B14 completion audit

**Status:** B14 is complete; WP4 is unblocked but has not been started. The 19 Kumar-dependent claims remain B/C.

## Commits, CI, and build gates

- Section 5 source corrections: `a74aa0f02fe0eb8c6ac03f8ff2fd8269142430b2`; CI `40531241673` passed. Self-audit caught that the build reads the phase-level Figure 9 SVG, not only the master mirror. The source and vector PDFs were synchronized in `3bbdb659ccb26730d057863fc9a3d0ecc66f9a87`; CI `40538052545` passed. The final rendered PDF now shows “Void-material models (§5.4)” on printed manuscript p. 41 (PDF page 42).
- Section 7–10 and ledger refresh: `558242f25cdb3fd5145f2fbe3022703f81ca416d`; CI `40536299860` passed.
- Final artifact publication: `84434885867ed7d173a82f204765cf1332c35474` (remote head verified before this report-only commit).
- Final strict build: 122 pages; undefined references/citations **0**; forbidden privacy-token, internal-path, and manuscript-tag counts **0**; 18 rendered figure PDFs; 16 figure includes; near-overfull boxes **0**. Six strict-tag text matches were classified by CI as false positives, not forbidden tags. Claim-ledger provenance validation passed.

## Ledger and source reconciliation

| Ledger | Before B14 refresh | After |
|---|---:|---:|
| Open claims (499 rows) | A 43 / B 125 / C 313 / V 18 | A 48 / B 123 / C 310 / V 18 |
| Sanitized source ledger | 115 rows | 115 rows |
| Missing-source leads | 17 rows | 6 rows |

Class changes in this refresh: OCL-145 A→B; OCL-205 C→A; OCL-406–408 B→A; OCL-078 C→A; OCL-259 B→A; OCL-291 C→B. OCL-045 wording was corrected without changing its A status. The claim-ledger validator confirms 499 rows and the final class totals above.

Eleven matched leads were removed from `MISSING_SOURCES.csv`: legacy Eringen1968b (now Tauchert–Claus–Ariman 1968), Nunziato1979, Cowin1983, Iesan1986, legacy Iesan2013 (verified as Iesan2004), Gupta2023IJNMF, LazarAgiasofitou2022, Marotti2013, Hughes1980, Singh2020c, and IvanovSavova1991. The remaining leads are Gorenflo1997, GorenfloKilbasMainardiRogosin2014, Eringen1966a, Gupta2023Energy, ChadwickSneddon1958, and Green1991-GN-I. The Indian Journal of Physics companion was not attached to Gupta2023Energy. The sanitized ledger has no Drive IDs, links, folder paths, or nonempty file-location fields.

## Source-bounded changes

- **OCL-078 (A):** reinstated only Ivanov–Savova’s printed-p. 564 result for their surface thermoelastic half-space waves: the kinetic/internal-energy flux is not parallel to the surface, its direction varies with depth, and its magnitude has the stated depth and surface-direction decay. No universal flux law is inferred.
- **OCL-259 (A):** Lazar–Agiasofitou’s printed-p. 10 Eqs. (29)–(30) derive the stress relation by applying the differential operator to the nonlocal constitutive relation and show it acting on inertia and body force in the motion equation; the Klein–Gordon specialization is separately anchored to p. 12 Eqs. (39)–(40). The manuscript does not call this a “nonlocal balance law.”
- **OCL-291 (B):** corrected to Singh–Gupta’s free-boundary microstructured-flexoelectric half-space and the plotted energy-ratio observation in printed p. 10, Sec. 5.2. Printed p. 11 is a figure page. The class remains B as directed.
- **OCL-446 (B):** active prose stays cautious; p. 1 supports only the paper’s quasi-static type-II Green–Naghdi structural model, variational formulation in the complete state-variable set, mixed formulations, and a suitably formulated uniqueness condition. No detailed admissible-space/boundary-class comparison is claimed.
- **OCL-262 (B):** Chadwick–Sneddon is identified by title only; it is not used as equation-level support for mode classification or attenuation values.

## Non-promotions and holds

- **OCL-058 (C/partial):** Nunziato–Cowin p. 177 verifies the displayed nonlinear void-theory balances and entropy inequality, but not “non-conducting heat” or void change as internal dissipation; p. 125 and Iesan p. 67 do not establish a universal fast/slow/shear mode count.
- **OCL-145 (B):** Green–Lindsay p. 5 Eq. (4.11) is coefficient-restricted and includes temperature-rate and temperature-gradient terms; that page shows no heat-flux evolution equation and does not support unrestricted Fourier-only wording.
- **OCL-160 (B):** Green–Naghdi 1993 p. 202 restrictions apply to the cited type-II system and are not transferred to type III.
- **OCL-176 (B):** Quintanilla 2019 defines the thermal displacement by \(\dot\alpha=\theta\); the alleged notation discrepancy remains unestablished and may be OCR-related.
- **OCL-177 (B):** no promotion; follow Bazarra et al.’s printed p. 2 condition \(\bar\kappa=\kappa-\tau\kappa^*>0\), not the conflicting earlier note.
- **OCL-206 (C):** the exact Gupta2023Energy article remains missing; no result is attached from the distinct Indian Journal of Physics companion.
- **OCL-427 (B):** generic finite-element claim remains deleted. Hughes p. 1413 supports a specific selective-integration/mean-dilatation procedure for nearly-incompressible media under stated hypotheses, not the generic row.
- **OCL-448 (C):** the generic finite-element table row remains citation-free; the located Hughes paper is not a general-method source.
- **OCL-481 (B):** GN-I remains unassigned pending exact equation/model mapping; the reviewed scan pages do not establish the candidate law.
- **OCL-485 (B):** no universal generalized-interface mode count or matrix dimension is inferred; numeric counts remain limited to selected local isotropic examples.

## Contradictions recorded

1. **Bazarra vs. earlier notes:** the p. 2 positivity condition for \(\bar\kappa\) is printed in the paper, contrary to the earlier note; OCL-177 remains B while the source page governs the wording.
2. **Quintanilla vs. manuscript Eq. (4.18):** Quintanilla 2019 Eq. (2.4) prints positive conductivity-gradient terms; Eq. (4.18) uses negative signs. The text now states that the sign conventions differ and does not call them identical.
3. **Singh–Gupta page locator:** the energy-ratio sentence is on p. 10; p. 11 contains figures. The prior p. 11 locator is recorded as a mismatch; OCL-291 remains B.
4. **Gupta HFF energy wording:** p. 912’s abstract reports that the authors justify interface energy conservation; p. 924 separately reports a transmitted-wave interaction-energy ratio. The latter is not described as a conservation-balance term.
5. **Green–Lindsay flux scope:** p. 5’s restricted Eq. (4.11) contradicts the earlier unrestricted Fourier-only phrasing; the manuscript is narrowed and OCL-145 remains B.
6. **Iesan monograph scope:** contents pp. v–vi list chapter/section headings on void materials, Cosserat continua, existence, and uniqueness; no particular theorem is inferred.

The Section 5 table and the rendered Figure 9 were visually checked after the source-of-truth SVG was synchronized. Sections 7–10 claim pages and the compiled pages containing their revisions were also visually checked. No WP4 work has begun.
