# Paper B (Neha): tests, tolerances, internal numbers

Internal only.

| Step | Test | Tolerance | Status |
|---|---|---|---|
| 1 | Elastic 1D hexagonal QC plate, branch count and ordering vs Zhang et al. (2021) | qualitative ordering; branch count exact | open |
| 1 | Phason limits: gamma = 0 gives a propagating branch, rho_p = 0 gives a diffusive branch | two independent assemblies agree to 1e-6 | open |
| 2 | Piezoelectric splitting vs Wang et al. (2025, 2022) | sign and ordering | open |
| 3 | Adiabatic/isothermal bracket; separately, the share of the phason work term | 1e-6 on the reduction, bracket width reported | open |
| 4 | Two cutoffs: thermal 1/|tau_T - tau_q| vs phason friction rate | crossover thickness located on a grid of 200 points | open |
| 5 | Coupling-off: R = 0, gamma = 0, rho_p = 0, thermal off | rel 1e-6 on k_r and k_i | open |
| 6 | Size length sweep | as Paper A | open |

## Numbers we hold

- MGT maps for the QC set: tau_q 2.09e-11 / 8.36e-11 / 3.34e-10 s give 2h* 0.70 / 2.22 / 7.02 nm;
  0.99 / 3.14 / 9.93 nm; 1.40 / 4.44 / 14.05 nm for the three conductivity sets, with fd_peak 79 / 157 /
  314 Hz m.
- Trust band of the continuum heat model: 2h above about 40 nm.
- The empty-window proof is in docs/04_scale_overlap_window.md; it is reused in the honest-note section.

## Standing rulings that apply here

- NSGT on the phonon stress only; the phason NSGT variant is a labelled sensitivity, never the main model.
- Lambda_ph must be sourced; a factor of two sensitivity is carried.
- The scholar computes her own branch count before any comparison; a mismatch is a stop, not a fit.
