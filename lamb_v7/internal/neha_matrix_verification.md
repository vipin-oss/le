# Neha (Paper B): internal verification

Internal only. No number here appears in a scholar file; constants are
placeholders at physical scale, listed at the end.

## 1. Parity of det M(eta)

Same two methods as in `sumit_matrix_verification.md`: the exact parity of each
entry plus a union-find sign matching, and the exact rational determinant.
Both are independent of the size of the coupling constants, which is the point:
the first attempt at this test used floating-point evaluation of det M at +eta
and -eta and was meaningless at this conditioning.

Parity table for the full matrix (+ even, - odd, . zero):

```
          u_x   u_z    w    phi   theta
  u_x      +     -     -     -     +
  u_z      -     +     +     +     -
  w        -     +     +     .     -
  phi      -     +     .     +     -
  theta    +     -     -     -     +
```

The assignment sigma = tau = (+1,-1,-1,-1,+1) closes: **no entry fails**. The
thermo-phason coupling beta^w sits in M25 and M52, both odd, so it fits; the
phason does not couple to the electric field in this model, so M34 = M43 = 0.

All 32 combinations of (R, e, beta^w, beta_th, p3) switched on and off: the
determinant is **even in all 32**. In five of the degenerate combinations
(thermal expansion off, or the phason coupling off with p3 on) the sign
matching fails while the determinant is still even; the reason is that the
conflicting cycle cannot be realised by any permutation once the entry that
would carry it is zero. The exact test is the one quoted, and it says the
polynomial is even, so the plate modes split into a symmetric and an
antisymmetric family for every setting of the couplings.

## 2. Degree and roots

Exact determinant, k = 1e5 1/m, f = 1 MHz:

- l_g = 3e-7: degree 14, 14 roots, magnitudes
  1.134e4 (x2), 8.126e4 (x2), 1.039e5 (x4), 3.329e6 (x2), 3.335e6 (x2), 1.134e9 (x2);
- l_g = 0: degree 10, 10 roots, the same eight plus 1.079e9 (x2).

The two pairs near 3.33e6 are the gradient layers, 1/l_g = 3.33e6 m^-1. The
pair near 1.1e9 is the thermal layer.

## 3. Limits

- **Frozen phason.** As gamma grows the phason amplitude is forced to zero and
  the model must return the one with R = 0. Checked as det M(eta)/(i gamma w)
  against the determinant of the minor with the phason row and column removed,
  at gamma = 1e20 and five values of eta: worst relative difference 4.7e-05.
- **Phason operator.** M33 against K1 eta^2 - K2 k^2 + rho_p w^2 + i gamma w at
  gamma = 0, 1e8, 1e12, 1e20: exact agreement.
- **Phason off.** Setting R = 0 removes the phason from the phonon equations
  entirely and leaves a piezoelectric thermoelastic plate; that is the limit
  stated in Calculation H of the master.

## 4. Placeholder constants

C11 150, C13 60, C33 130, C44 40 GPa; K1 30, K2 20 GPa; R1 2, R2 3, R3 1.5 GPa;
e31 0.4, e33 1.1, e15 0.3 C/m^2; eps11 8.54 eps0, eps33 10.2 eps0;
beta1 1.7e6, beta3 1.5e6 Pa/K; beta^w 1.0e6; p3 0.5 C/(m^2 K); rho 4200,
rho_p 12 kg/m^3; gamma 1e8; c_p 2.9e6 J/(m^3 K); k_th 4 W/(m K); T0 300 K;
l_g 3e-7, l_nl 2e-7 m; tau_q 1e-11 s.
