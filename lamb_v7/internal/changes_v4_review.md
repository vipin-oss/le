# Round v4 review: change log

Reviewer: Dr. Vipin. Date of changes: 30 October 2026. Files touched: `reports/model_v4.tex`,
`deliver/src/*`, `internal/*`, `reports/packages_v4.tex`.

| # | Instruction | Change made | Status |
|---|---|---|---|
| 1 | NSGT in Lim form, equivalent momentum form, cite the equation number read | (N1) is now `(1 - l_nl^2 lap) t_ij = sigma_ij` with the gradient operator on `c:eps` only. (N2) added as the equivalent momentum form: `(1 - l_nl^2 lap) rho u_ij^ddot = sigma_ij,j`. Eq. numbers (18) and (19) of Lim-Zhang-Reddy are cited **through** Barretta & Marotti de Sciarra (IJES 130 (2018) 187, introduction), because the Elsevier PDF was closed to me. Marked [R, secondary] and the scholar is told to confirm (18) on the page. | done, with the secondary-source caveat stated in the document, not hidden |
| 2 | Piezo, piezomagnetic, thermal, phason terms local; state as a modelling choice | `(1-l_g^2 lap)` removed from A2, B3, C2, C3. It survives only on `c:eps` in (N1). A paragraph "Modelling choice, applied to all three papers" states the reason: D and B stay second order, extra conditions stay mechanical, no double counting. | done |
| 3 | A6: drop `-(E_g/q) dn/dt`; use the Onsager-reciprocal Peltier term; units of beta_th; sign for n-type; keep `E_g D_n/tau_R` only with finite tau_R | (A5) now carries `beta_th lap theta` with `beta_th = b_n n_0 S_n`, unit m^-1 s^-1 K^-1, negative for electrons. (A6) carries `-q Pi_th d(dn)/dt` with `Pi_th = T_0 S_n`, and (A7) states the Onsager ratio `Pi_th/beta_th = T_0/(b_n n_0)`. Recombination is an optional **pair**: `-dn/tau_R` in (A5) and `+E_g dn/tau_R` in (A6); both vanish as `tau_R -> inf`. A term-by-term dimension table for every term of (A5) and (A6) is in section 1. The notation table (section 0) now carries units for every symbol. | done |
| 4 | Remove or source: A "close at most one of the two", C "rarely retained", C "frequency-dependent alpha" | All three claims removed. Replaced by search statements with dates and named neighbours. Found and cited: Qu, Pan, Zhu, Jin & Roy, IJES 182 (2023) 103775 (a PSC continuum **with** Seebeck and Peltier, killing the A claim); Sharma, Pal & Chand, J. Therm. Stresses 27 (2004) 33 (piezothermoelastic plate Lamb waves with attenuation); Othmani, Takali & Njeh, Superlattices Microstruct. 106 (2017) 86 (PSC plate Lamb waves, isothermal); Kondaiah, Shankar & Ganesan, Coupled Syst. Mech. 2 (2013) 1 and Tocci Monaco et al., Nanomaterials 11 (2021) 87, which **do** keep pyro- and pyromagnetic coefficients (killing the C claim); Xiao, Han, Liu & Li, Compos. Struct. 153 (2016) 704 (guided waves in a graded MEE plate). No support found for frequency-dependent alpha, so it is gone. | done |
| 5 | Lubensky authors and phase; phason dynamics source | Corrected to Lubensky, Ramaswamy & Toner, Phys. Rev. B 32 (1985) 7444, **icosahedral**, cited for the relaxation mechanism only, with an explicit warning not to transfer its moduli. Added Agiasofitou & Lazar, IJSS 51 (2014) 923, Eqs. (26) and (30), for the telegraph phason balance (read in the arXiv version 1311.5095), and Baggioli & Landry, SciPost Phys. 9 (2020) 062, Eq. (17), for the diffusive-to-propagating crossover. | done |
| 6 | Distinct symbols | `q` = carrier charge magnitude, `h_kij` = piezomagnetic (was `q_kij`), `k` = wavenumber, `b_n` = mobility (was `mu_n`, to free `mu_ik` for permeability). Renamed consistently in all three sets and in the packages. | done |
| 7 | One sentence per plan on the order of the system | Present in section 6 of each research plan and in sections 1-3 of the model document: NSGT raises the order in z, so extra conditions are needed at the faces, and settling them is the scholar's task. | done |

## Things I could not do

1. Open Lim-Zhang-Reddy 2015 (Elsevier). Equation numbers are secondary. Logged in
   `internal/*_equation_source_log.md`.
2. Open Acta Mech. Solida Sin. 2026 (10.1007/s10338-026-00755-4), generalized thermoelastic Lamb waves in
   1D hexagonal QC nanoplates. This is a direct threat to Paper B's novelty; it is now week-one reading for
   Neha and is flagged in her plan.
3. Open Zhang et al. Acta Mech. 232 (2021) in full; only abstract and display equations were reachable.
4. Confirm the Ozgur ZnO review constants table entry by entry; the piezo range is known but not a single
   self-consistent measured set.

## v4.1 addendum: second review round

| # | Instruction | Change | Status |
|---|---|---|---|
| 8 | MGT is Moore-Gibson-Thompson | every "modified gradient" replaced in the six files and in the model document; first use in each file spells the name out; sentences rewritten around it | done |
| 9 | Sumit sign error: beta_th and the Peltier term | beta_th = -b_n n_0 S_n (>0) and the bracket entry +q Pi_th d(Dn)/dt; the Onsager ratio now written as -T_0/(b_n n_0); text rewritten so that carriers accumulate on the cold side; derivation in `internal/sumit_audit.md` | done, reviewer's version confirmed by independent derivation |
| 10 | sign and unit audit for Neha and Anu | `internal/neha_audit.md`, `internal/anu_audit.md`: every shared constant checked for reciprocity, every term checked for units, plus the two by-products (unit of alpha is s/m; gamma must be positive) | done |
| 11 | basics files expanded | 8840, 6440 and 6040 words; 23 sections each; every symbol of the matching plan tabulated with unit and rough size; a section on self-testing | done |
| 12 | zips rebuilt, milestone report updated with counts | three archives rebuilt, `reports/packages_v4.tex` rewritten with the new counts | done |
