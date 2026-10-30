# Paper A (Sumit): tests, tolerances, internal numbers

Internal only. No number on this page goes into a scholar document.

## Hard tests, in the order of the plan

| Step | Test | Tolerance | Status |
|---|---|---|---|
| 1 | Elastic isotropic plate limit, both families, Rayleigh limit at large fd | rel 1e-3 on c | Rayleigh reference 2909.73 m/s from cL 6197.8 and cT 3122.0 for the aluminium set (mu 2.6316e10, lambda 5.1084e10) |
| 1 | Elastic roots cross-check | 1e-6 | fd 10/100/1000: S0 5393.9053 / 5393.1719 / 5308.5887; A 311.6377 / 954.2341 / 2326.6431; A0 at fd 3e4 = 2909.7314 |
| 2 | Piezoelectric branch ordering and decoupled family | qualitative + sign of shift | open |
| 3 | Adiabatic/isothermal bracket | width of order thermoelastic coupling; Delta_E = 3.06e-3 (beta_1), 2.01e-3 (beta_3) | open |
| 4 | MGT saturation, peak shift, plateau rescaling | rel 1e-6 against 1D reduction | plateau tau_T^2/(tau_T-tau_q)^2; peak at 1/|tau_T-tau_q| |
| 4 | Visibility crossing | (2h)* = pi sqrt(kappa tau_q); trust band limit 2h >~ 40 nm | Sigma maps: tau_q 2.09e-11 / 8.36e-11 / 3.34e-10 s give 2h* 4.57 / 14.44 / 45.66 nm |
| 5 | Switching-off, every coupling | rel 1e-6 on k_r and k_i, all sampled modes | 1e-4 is a warning, not a pass |
| 6 | Size length sweep | l_nl/h and l_g/h over the quoted range | open |

## Numbers we hold, for the internal record

- Thermal: k_th 60 gives tau_T 5.687e-13 s, kappa 2.113e-5 m2/s; k_th 1.2 gives 1.137e-14 s, 4.225e-7 m2/s.
- Bulk attenuation peak: fd 251.4 Hz m, k_i 1.83e3 m^-1, k_i/k_r 7.7e-4 at 2h = 132 nm.
- Cutoffs of the elastic plate: A1 1561, S1 3099, S2 3122, A2 6198 Hz m.
- ZnO Set L (primary): c 209.7/121.1/105.4/211.2/42.4 GPa, e -0.57/1.32/-0.48, eps11 8.54 eps0,
  eps33 10.2 eps0, rho 5680; cbar11 157.100 GPa, ebar31 -1.2287, v_short 5259.13, v_open 5509.57,
  K2(0) 0.08884, k31 0.1957, d31 -5.447, d33 11.686 pC/N. All k-values UNVERIFIED.
- Set B and Set A are sensitivity sets; a conclusion that does not survive them is not reported.

## Known failure modes, do not repeat

- Viktorov approximation rejected; minus-sign undivided determinant is a dead end.
- LU with partial pivoting only; Leibniz-expanded determinants give garbage.
- Pre-scale columns by D before any 6x6 determinant; hard-coded u3' or Phi' rows give wrong signs.
- Golden-section plus bisection for roots; sign scans miss A roots.
