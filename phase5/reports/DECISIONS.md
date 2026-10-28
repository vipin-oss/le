# R2 decisions and change log

Mission: produce a source-traceable review of wave mechanics in generalized continua. Round R2: mathematical and citation corrections requested in `control/ARENA_NEXT.md`; read-only control and verification files were not modified. The active session branch is `arena/40393d9f-le`.

## Scope and consequential decisions

| ID | Decision / disposition | Manuscript location | Evidence / ledger IDs |
|---|---|---|---|
| R2-01 | Replace the original Green–Lindsay energy equation with Fourier flux and no $\tau_0$ on strain-rate coupling; cite Yu et al. (2018) only as a modified strain-rate variant; do not conflate it with the original formulation. Bera remains unidentified and the requested Singh/Symmetry attribution is held pending metadata audit. State $\tau_1\geq\tau_0>0$ as a source-stated restriction, not a new derivation. | §4.4, Table 12-A, Appendix A | `EQ-015`; control `FULLTEXT_FINDINGS_01.md` F1; B6 `CL-006` |
| R2-02 | Attribute first-order TPL to Roy Choudhuri (2007), including $k^*\nabla v$ and $\dot v=T$. No $\tau_\nu/2$ term is used. A possible second-order $\tau_q^2/2$ form is identified only as a secondary Barak/Gupta extension, CONDITIONAL on that formulation's own stated admissibility/stability conditions. | §§1, 2, 4.8, Table 12-B, Table T1, Fig. 7, Appendix A | `EQ-019` (new Appendix A row); `FULLTEXT_FINDINGS_02.md` F6–F9; B8a §3 |
| R2-03 | Define $A_{\rm int}$ as the interface-local residual from the total-field flux difference on the two sides. Bulk dissipation is a volume integral and is not added as a third interface channel. The total-field definitions include all modal cross terms. A concrete V-B3d Biot steel/aluminium case at 4.46e11 Hz reproduces the total-field closure and the distinct reflected-sum/mode-diagonal discrepancies; closure alone is tautological, while independent half-space dissipation checks close to unity. | §§9.7, 10.5; Eqs. (9.10), (9.12), (10.11); `reports/V-B3d-cross-term-check.md` | B3d three-R finding; `CL-020`–`CL-023`; B9c; reproduced from read-only script at 3515358165023afcf3a5f8ac38543969593950d6 |
| R2-04 | Retain degree eight in Eq. (9.9) only for the specified 6mm medium, sagittal plane containing the c-axis, quasi-static electric closure, and stated retained field set, after the trivial quasi-static root is removed. No piezo-stiffened SH branch is claimed. | §9.5, Appendix A | `EQ-076`; `EQ-152`; control `ARBITRATION_B4.md` W2 |
| R2-05 | Replace the unsupported “simplified” MDD Fourier symbol with the finite-window multiplier derived for the displayed kernel and $e^{-i\Omega t}$ convention. | `energy_flux_derivations.tex`, Eq. `ef:mdd:4` | `MDD-01`; control `ARBITRATION_B4.md` W3 |
| R2-06 | Extend the equation register to Sections 6, 7, and 9; retain the original Section 3–5 and 10 rows. Add a separate Appendix-A ledger; do not change the read-only 176-row EQUATION_LEDGER or 53-row CLAIM_LEDGER. | Appendix A; `reports/APPA_LEDGER.csv` | `CL-027`, `CL-029`; control `BRAVE_B9.md` item 1 |
| R2-07 | Remove claims that the cited Barak/Gupta papers demonstrate a closed identity or specific energy-channel mechanisms unless full texts and conventions are checked. Retain the references as literature leads and mark their results unverified. | §9.7 and Table T6 note | `CL-021`, `CL-022`; `CLAIM_LEDGER.csv` read-only |
| R2-08 | State the actual assumption beside each CONDITIONAL register row and next to the relevant equation/prose. | Appendix A, §9, §10, Tables T4/T6/T12 | `APPA_LEDGER.csv`; relevant entries include `EQ-001`–`004`, `EQ-022F`, `EQ-10.4`–`10.12`, `EQ-9.9`–`9.12` |
| R2-09 | Apply the confirmed B6 corrections with ledger IDs: micropolar duplicate equation and scalar/vector notation; fractional units and kernel; GN-II/GN-III and nonlocal table cells; MGT spatial order and chronology; Rayleigh ratio; inventory overlap/decade counts; and thermal-wave imaging. | §§5, 11–14; Tables T1/T4/T12; Appendix A | `EQ-147`, `EQ-157`, `EQ-160`, `EQ-165`, `EQ-166`, `EQ-168`, `EQ-171`, `EQ-173`; `CL-030`, `CL-032`, `CL-040`, `CL-042`, `CL-045`, `CL-048`, `CL-049` |
| R2-10 | Correct the title-page date to 22 October 2026. Existing author names are unchanged. | Title page | R4 constraint |
| R2-11 | Keep the disputed bibliography entries; mark legacy DOI “YES” claims UNVERIFIED until a raw response and comparisons are saved. Add a manually triggered Crossref workflow that stores raw responses and an audit log. | `references/doi_verification.csv`, method report, enrichment workflow | UPDATE 1–2; read-only reference audit |
| R2-12 | Correct TPL and MGT bibliography links; remove the unrelated Abdalla cosmology citation from the conclusion without deleting its bibliography entry. Moore & Gibson (1960) is added with its Crossref DOI; Thompson (1972) remains explicitly UNVERIFIED because the source record was not located in the read-only literature base. | §§2, 4, 17; T1; local bibliography | `EQ-173`; `CL-030`; `REFERENCE_AUDIT.csv` read-only |
| R2-13 | Correct GN numbering: type II is Green–Naghdi 1993 (*J. Elasticity* 31:189–208); type III is Green–Naghdi 1992 (*J. Thermal Stresses* 15:253–264). Correct type-specific citations in Sections 2/4/12, T1/T2, and the appendices. | §§1, 2, 4.5–4.6, 12; T1/T2; energy-flux appendix | `FULLTEXT_FINDINGS_04.md` F13; `FULLTEXT_FINDINGS_05.md` F16–F17 |
| R2-14 | Correct GN-II alpha-form coupling to $\dot u_{i,i}$ and unify symbols: $\kappa^*$ is the thermal-displacement coefficient, $\kappa$ the temperature-rate coefficient. Correct the GN-III temperature equation and register EQ-016. | §4.5–4.6; Appendix A EQ-016; energy-flux appendix | `FULLTEXT_FINDINGS_05.md` F16–F17 |
| R2-15 | Keep Tzou (1995) as the DPL article; retain Tzou (1997) only as a separately identified book. Remove the fabricated Guyer1990 active BibTeX entry and manuscript citations; retain only the DOI-audit/literature-provenance rows as historical UNVERIFIED trail. | §§2, 4.7; local bibliography; DOI method note | `FULLTEXT_FINDINGS_04.md` F15; `FULLTEXT_FINDINGS_03.md` F10–F12 |
| R2-16 | Add the GK phonon-Boltzmann result and $\lambda^2=c^2\tau_N\tau_z/5$ with $\tau_z$ defined as the Ziman-averaged R-process time. Cite Tzou 1995 Eqs. 15 and 17 only as secondary continuum law/mapping, under their stated approximation. | §4.7 paragraph; §2; local bibliography | `FULLTEXT_FINDINGS_03.md` F10–F12; `FULLTEXT_FINDINGS_05.md` F18 |
| R2-17 | State Moore–Gibson 1960 as the origin of a third-order relaxing-gas acoustic equation, not a heat-conduction law; later MGT thermoelastic models are analogues. Keep model-specific equations conditional. | §§1, 4.9, 12; T1/T2 | `FULLTEXT_FINDINGS_04.md` F14 |
| R2-18 | Preserve the original GL (4.9) equation with Fourier flux and explicitly identify the uniform-$\tau_0$ strain-rate form as an LS/GL hybrid variant. Verify each CONDITIONAL row is adjacent to its applicable model, coefficient, geometry, or boundary assumptions. | §4.4; §10; T4; Appendix A; APPA_LEDGER | `FULLTEXT_FINDINGS_01.md` F1; `APPA_LEDGER.csv` (conditions) |

## Change details for the B6 defect set

| Defect | Ledger row | Applied disposition |
|---|---|---|
| Micropolar force-stress display duplicated void law and used an undefined scalar gradient | `EQ-147` | Replaced with an isotropic linear micropolar law using the microrotation vector; the displayed specialization remains UNVERIFIED against primary full text. |
| Electric potential / void-fraction symbol collision | `CL-032` | Renamed the void scalar to $\eta$ in §5.4 and its notation row; electric potential remains $\phi$. |
| Fractional diffusivity units | `EQ-157` | Replaced $a$ with $a_\alpha$ and stated $[a_\alpha]=\mathrm{m^2s^{-\alpha}}$. |
| Fractional hereditary kernel | `EQ-160` | Replaced the erroneous product with $(t-\tau)^{\alpha-1}/\Gamma(\alpha)$. |
| GN-II/GN-III and nonlocal thermal-law rows | `EQ-165`, `EQ-166` | Corrected the two GN flux laws; marked Eringen nonlocal elasticity as having no thermal law. Also separated temporal MDD window from nonlocal length. |
| MGT spatial order | `EQ-168` | Changed to second order in space; the named prototype is third order in time. |
| Rayleigh speed | `EQ-171` | Replaced 0.87 with 0.9194 at $\nu=0.25$ and noted 0.874 at $\nu=0$. |
| Inventory family totals | `CL-048` | Clarified 95 unique records but 96 overlapping family assignments; shares use 96 assignments. |
| 1970s count | `CL-049` | Changed 17 to 9 and removed the unsupported “bimodal” inference. |
| MGT chronology | `EQ-173` | Changed the milestone to 1960/1972, distinguished the 2019 thermoelastic treatment, and marked the Thompson source details UNVERIFIED. |
| Micropolar priority overclaim | `CL-030` | Removed “earliest”; now says no priority claim is made. |
| Fractional Cattaneo limit | `CL-040` | Removed the GN-II interpolation claim; scoped the alpha=1 reduction to the displayed Cattaneo/LS form. |
| Universal absence of limit theorems | `CL-042` | Narrowed to uneven coverage across model pairs/variants. |
| Thermal-wave imaging | `CL-045` | Replaced the false finite-speed requirement with the Fourier diffusion-depth scale and a regime-specific finite-speed qualification. |

## Evidence and non-claims

- R1 remains the historical pass only; no R2 pass is claimed until the strict build and output publication complete.
- Metadata match does not establish that a paper supports a scientific claim. The raw Crossref workflow verifies bibliographic fields only.
- Green–Lindsay is marked primary-source-checked on the basis of the handler-supplied 1972 full-text findings. The R2 manuscript does not infer that status from the DOI metadata row.
- The micropolar display, MGT lineage beyond the Moore–Gibson record, and cited Barak/Gupta energy results are not claimed to be primary-source-verified in this work.
- No author names, read-only control files, or read-only verification files were edited.
