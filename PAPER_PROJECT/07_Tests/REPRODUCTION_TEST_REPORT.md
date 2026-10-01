# REPRODUCTION_TEST_REPORT (MASTER_PROMPT §75)

Date 2026-10-01 07:39:06 · environment: Python 3.13.14, numpy 2.3.5 · wall 38 s (2 vCPU) · script `08_Experiments/reproduce.py`
Scope: one verification case, one convergence/error study, one principal result, one principal figure, one table — re-computed from the frozen code and compared with stored outputs.

| item | expected / stored | recomputed | rel. difference | tolerance | status | note |
|---|---|---|---|---|---|---|
| V8 steady-gradient error 48x24 (stored value, 4 digits) | 0.0063 | 0.006311160626976627 | 1.77e-03 | 0.01 | PASS |  |
| V8 steady-gradient error 96x48 (stored value, 4 digits) | 0.0016 | 0.00161370515169918 | 8.57e-03 | 0.1 | PASS | stored value has 4 digits |
| closed-form steady wall hoop (Pa/K) | -1234746.0535908495 | -1234746.0535908495 | 0.00e+00 | 1e-12 | PASS |  |
| V11 reference peak (Pa/K) | 985689.4485743708 | 985689.4485743708 | 0.00e+00 | 1e-12 | PASS |  |
| V11 peak error 48x24 | 0.0116 | 0.011593578977993233 | 5.54e-04 | 0.05 | PASS | stored 4 digits |
| V11 peak error 96x48 | 0.0027 | 0.0027484576755259634 | 1.79e-02 | 0.05 | PASS | stored 4 digits |
| principal result: ellipse phi=90 peak (interp, Pa/K) re-computed vs stored | -961654.3309977308 | -961654.3309977308 | 0.00e+00 | 1e-09 | PASS |  |
| principal result: nodal peak | -959287.0616127604 | -959287.0616127604 | 0.00e+00 | 1e-09 | PASS |  |
| analysis script re-run (exit code 0) | 0 | 0 | 0.00e+00 | 0 | PASS |  |
| table phi_sweep_ellipse.csv: sha256 before vs after regeneration from the stored raw data | 9675e0d3b0ca6f8261cf441986335de4bd225fdcea0c694c3c275a07deb45f52 | 9675e0d3b0ca6f8261cf441986335de4bd225fdcea0c694c3c275a07deb45f52 | 0.00e+00 | 0 | PASS | byte-identical required |
| principal figure fig2 regenerated (exit code 0) | 0 | 0 | 0.00e+00 | 0 | PASS | wrote /home/user/PAPER_PROJECT/11_Figures/fig2_phi_sweep.png |

Overall: 11 PASS, 0 FAIL.
