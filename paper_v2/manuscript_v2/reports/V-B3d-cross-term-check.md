# V-B3d total-field cross-term check

**Status:** Executed, arithmetic reproduction only; not an independent materials validation.
**Read-only source:** `verification/V-B3d_coupled_interface.py` and `verification/V-B3d_coupled-interface-rta.md` at commit `3515358165023afcf3a5f8ac38543969593950d6`.
**Execution:** Python 3.11 with NumPy 2.2.6; script run from a temporary copy, no edits to `verification/`.

## Concrete case

Biot/Fourier coupled thermoelastic interface; steel-like medium 1 and aluminium-like medium 2; 1-D, normal incidence, perfect contact; harmonic frequency `4.46e11 Hz`, selected where the script reports the thermal/elastic wavenumber-magnitude ratio as 1.00. Material values are illustrative arithmetic inputs, not a database claim.

| quantity | reproduced value |
|---|---:|
| Total-field reflection `R_flux` | 0.212026 |
| Reflected-sum `R_ref` (cross terms between reflected modes retained, incident removed) | 0.211074 |
| Diagonal-only `R_mode` | 0.211592 |
| Total-field transmission `T` | 0.787974 |
| `A_flux = 1 - R_flux - T` | 2.22e-16 |
| `R_ref + T - 1` | -9.5e-4 |
| `R_mode + T - 1` | -4.34e-4 |
| transmitted-side dissipation check `D2/(T J_i)` | 1.00000 |
| reflected-side dissipation check `D1/(R_ref J_i)` | 1.00000 |

## Interpretation and limits

The closure `R_flux + T + A_flux = 1` follows from the chosen total-field flux definitions and `A_flux := 1 - R_flux - T`; it is not independent evidence of energy conservation. The concrete calculation shows that the reflected-sum and diagonal-only ratios differ from total-field accounting when complex-wavenumber modes interfere. The independent checks in the read-only case compare the computed powers with bulk dissipation integrals and close to unity; they are the meaningful numerical checks. Do not transfer these Biot results to LS, GL, GN-II, or the rigid-conductor V-B3b problem.
