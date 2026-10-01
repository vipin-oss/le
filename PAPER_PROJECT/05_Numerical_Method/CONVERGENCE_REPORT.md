# CONVERGENCE_REPORT — Phase 9 (2026-10-01)

Verification, not validation (§39). Grid families (γ = 5): radial R48/M/R192 = 48×96, 96×96, 192×96 and angular T48/M/T144 = 96×48, 96×96, 96×144. Production grid M. Richardson with the observed order bounded to [1, 3].

## 1. Mesh-direction and clustering study (C4; ellipse φ = 30°, interpolated peak, MPa/K)

| N_r × N_θ | γ = 3.5 | γ = 5 | γ = 6.5 |
|---|---|---|---|
| 96x48 | 1.4123 | 1.2447 | 1.2361 |
| 192x48 | 1.2894 | — | — |
| 96x96 | 1.4542 | 1.2617 | — |
| 96x144 | 1.4586 | — | — |
| 144x72 | — | 1.2471 | — |
| 192x96 | 1.3157 | — | — |

Reading: at γ = 3.5, doubling N_r changes the peak by −8.7% and doubling N_θ by +3.0%; γ = 5 at 96×48 lowers it by 11.9%; γ = 6.5 differs from γ = 5 by 0.7%. The near-wall radial resolution controls the tip stress → γ = 5 (P9-D001). With γ = 3.5 the handoff-family triplets 48×24/96×48/192×96 have observed orders 0.8–1.35 (`09_Raw_Data/convergence_gamma3p5/`, not asymptotic).

## 2. Production quantities (ellipse, 6 orientations, MPa/K)

| φ | M | radial p | radial corr. | angular p | angular corr. | extrapolated |
|---|---|---|---|---|---|---|
| 0 | 1.1496 | 2.12 | -0.07% | 1.91 | +0.48% | 1.1543 |
| 30 | 1.2617 | 1.43 | -2.04% | 2.17 | +0.39% | 1.2409 |
| 60 | 1.1595 | 1.46 | -1.60% | 2.19 | +0.26% | 1.1439 |
| 90 | 0.9659 | 1.23 | -0.32% | 2.26 | +0.12% | 0.9640 |
| 120 | 1.2481 | 1.5 | -1.82% | 2.11 | +0.36% | 1.2299 |
| 150 | 1.3220 | 1.47 | -2.03% | 2.18 | +0.44% | 1.3010 |

Amplitude A_φ (six orientations): grid M 30.06%, R192 29.02%, T144 30.23%, extrapolated 28.75%; twelve orientations on M 29.87%; **u_num = 1.31%**; frozen threshold max(5 u_num, 2%) = 6.56% → RESOLVABLE.

## 3. Circle

Radial family at φ = 0: [0.8517, 0.8536, 0.8539] MPa/K (R48, M, R192), observed order 3.072693574786767, extrapolated 0.8539 MPa/K; error of M -0.03%, of R192 -0.00%.

## 4. Bromwich-plan independence (C2; ellipse φ = 90°, 96×48)

| plan | peak change | series change | solves |
|---|---|---|---|
| T32_g0.6 | 2.85e-10 | 4.12e-10 | 42 |
| T16_g1.1 | 3.49e-10 | 7.15e-10 | 22 |

## 5. Outer-radius (echo) sensitivity (C3; circle, 96×48 and 191×48)

| a (nm) | echo round trip at R = 80a (t_th) | peak change R80→R160 | D(R80) | D(R160) | D change |
|---|---|---|---|---|---|
| a10nm | 8.14 | +0.29% | 1.569e-02 | 1.485e-02 | -5.4% |
| a50nm | 1.63 | +0.18% | 2.934e-04 | 2.827e-04 | -3.6% |

## 6. Verification-level convergence orders

V8 steady gradient load: order 1.9675283417378677; V11 single pulse: orders 2.0766318319713055, 2.0451058001284252; V9d dynamic coupled: min order 2.074617052416121.

