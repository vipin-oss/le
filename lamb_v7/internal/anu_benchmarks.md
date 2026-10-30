# Paper C (Anu): tests, tolerances, internal numbers

Internal only.

| Step | Test | Tolerance | Status |
|---|---|---|---|
| 1 | Elastic laminated plate limit and Rayleigh velocity | rel 1e-3 | Rayleigh 2909.73 m/s for the aluminium set, computed from cL 6197.8 and cT 3122.0 |
| 2 | MEE branch ordering vs Chen, Pan & Chen (2007) | sign and ordering | open |
| 3 | Adiabatic/isothermal bracket; separately, the change when m_i is removed | 1e-6 on reductions; bracket width reported | open |
| 4 | MGT saturation; peak at 1/|tau_T - tau_q|; plateau tau_T^2/(tau_T - tau_q)^2 | rel 1e-6 vs 1D reduction | open |
| 4 | Two homogenisation routes drawn as a band | band width vs thermal contribution, week 9 decision | open |
| 5 | Coupling-off: thermal, electric, magnetic, size effect | rel 1e-6 on k_r and k_i | open |
| 6 | Size length sweep, three thicknesses, two families | as Paper A | open |

## Numbers we hold

- MGT maps, CoFe2O4: tau_q 2.09e-11 / 8.36e-11 / 3.34e-10 s give 2h* 0.72 / 2.27 / 7.16 nm, fd_peak 82 Hz m.
- BaTiO3: 1.09 / 3.46 / 10.94 nm, fd_peak 191 Hz m. Composite: 0.59 / 1.86 / 5.88 nm.
- Thermal constants: CoFe2O4 k_th 0.6 W/mK, D 0.52 mm2/s (10.1007/s10854-022-09777-3); BaTiO3 rho
  5.84-5.94 g/cm3, c_p 0.41-0.43 J/(g K) (Thin Solid Films 2004, PII S0040603104000942).
- No measured magnetoelectric coefficient for the modelled stack; both routes must be shown.

## Standing rulings that apply here

- The paper is downgraded to Q2 by the earlier scorecard; the Q1 test is the ridge resolution at week nine.
- Step 4 monotonicity and floor-resolution are hard gates.
- Do not overwrite paper/problem_v2.md; scorecards are appended, never rewritten.
