# Anu (Paper C): internal verification

Internal only. No number here appears in a scholar file; constants are
placeholders at physical scale, listed at the end.

## 1. Parity of det M(eta)

Same two methods as in `sumit_matrix_verification.md`: the exact parity of each
entry with a union-find sign matching, and the exact rational determinant. Both
are independent of the size of the coupling constants.

Parity table for the full matrix (+ even, - odd, . zero):

```
          u_x   u_z   phi   psi   theta
  u_x      +     -     -     -     +
  u_z      -     +     +     +     -
  phi      -     +     +     +     -
  psi      -     +     +     +     -
  theta    +     -     -     -     +
```

The assignment sigma = tau = (+1,-1,-1,-1,+1) closes: **no entry fails**. The
magnetoelectric entries M34 and M43 are both even (a33 eta^2 - a11 k^2), the
pyromagnetic and pyroelectric entries M35 and M45 are both odd, and the pattern
is the same in every row.

All 32 combinations of (e, h, alpha, p3, m3) switched on and off: the
determinant is **even in all 32**, and the sign matching closes in all 32. So
the plate modes split into a symmetric and an antisymmetric family whatever the
magnetoelectric, piezoelectric, piezomagnetic, pyroelectric and pyromagnetic
couplings are.

## 2. Degree and roots

Exact determinant, k = 1e5 1/m, f = 1 MHz:

- l_g = 3e-7: degree 14, 14 roots, magnitudes
  2.805e4 (x2), 1.042e5 (x4), 1.43e5 (x2), 3.143e6 (x2), 3.334e6 (x2), 1.025e9 (x2);
- l_g = 0: degree 10, 10 roots, the same eight plus 2.395e8 (x2).

The pairs near 3.1e6 and 3.33e6 are the gradient layers, 1/l_g = 3.33e6 m^-1.

## 3. Limits

- **Magnetoelectric stiffening of the bulk shear wave.** At eta = 0 the
  (u_z, phi, psi) block vanishes when rho omega^2 = k^2 (C44 + v^T A^{-1} v)
  with v = (e15, h15) and A = [[eps11, -a11], [-a11, mu11]]. Checked: the
  block determinant at that speed is 7.9e-53 relative.
- **alpha to zero.** The stiffening becomes the sum of the two independent
  ones, C44 + e15^2/eps11 + h15^2/mu11: agreement to 0 digits of difference.
- **Coupling factor.** kappa^2 = a11^2/(eps11 mu11) = 8.0892e-03 with these
  placeholders. The coupled stiffness is positive only for kappa^2 < 1; that is
  the thermodynamic bound the master quotes as a band on alpha, not a number.

## 4. Placeholder constants

C11 220, C13 110, C33 215, C44 45 GPa; e31 12, e33 15, e15 -4.5 C/m^2;
h31 200, h33 250, h15 100 N/(A m); a11 1.2e-9, a33 3.4e-9 s/m;
eps11 8.0 eps0, eps33 9.0 eps0; mu11 2.0 mu0, mu33 1.5 mu0; beta1 1.7e6,
beta3 1.5e6 Pa/K; p3 0.5 C/(m^2 K); m3 0.05; rho 5500 kg/m^3;
c_p 3.2e6 J/(m^3 K); k_th 6 W/(m K); T0 300 K; l_g 3e-7, l_nl 2e-7 m;
tau_q 1e-11 s.
