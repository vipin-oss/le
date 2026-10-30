# Sumit (Paper A): internal verification

Internal only. No number in this file appears in a scholar file; the constants
are placeholders at physical scale and are listed at the end.

## 1. Parity of det M(eta) — corrected

The first attempt at this test evaluated det M at +eta and -eta in floating
point and compared. That test is worthless here: the matrix entries span about
forty decades, so the odd part of the determinant disappears in cancellation
and the verdict follows the size of the coupling constants, which is nonsense.
Parity of a polynomial cannot depend on how big its coefficients are.

Two methods are used instead, and they agree on every case in the table.

- **Structural.** Every entry is a polynomial in eta whose parity is exact.
  Signs sigma_i (rows) and tau_j (columns) with s_ij = sigma_i tau_j are sought
  by a union-find with parity; the product over the matrix is +1, so an
  assignment exists exactly when det M is even. This is independent of every
  constant.
- **Exact.** The determinant is expanded over the 120 permutations in exact
  rational arithmetic on the equilibrated matrix, and the odd coefficients are
  read off. Row and column scaling multiply det by a non-zero number, so the
  degree and the vanishing of the odd part are untouched.

Parity table for the full matrix (+ even, - odd, . zero):

```
          u_x   u_z   phi     n   theta
  u_x      +     -     -     .     +
  u_z      -     +     +     .     -
  phi      -     +     +     +     -
  n        .     .     +     +     +
  theta    +     -     -     +     +
```

The forced assignment is sigma = tau = (+1,-1,-1,-1,+1). Two entries fail it:

- M45 = -beta_th L, the thermodiffusion (Soret) term in the carrier equation;
- M54 = f(-i omega q Pi_th + E_g/tau_R), the Peltier and recombination terms in
  the heat equation.

Both sit on the carrier column and the heat row, and both are even where the
matching needs them odd.

Sweeping the four couplings that can matter, with the piezoelectric constants,
the free charge and the thermal expansion all present (16 combinations, both
methods agreeing in all 16):

```
                       det M even?
  p3  beta_th  Pi_th  E_g
   0     0       0     0     yes
   0     0       0     1     no
   0     0       1     0     no
   0     0       1     1     no
   0     1       0     0     no
   0     1       0     1     no
   0     1       1     0     no
   0     1       1     1     no
   1     0       0     0     yes
   1     0       0     1     no
   1     0       1     0     no
   1     0       1     1     no
   1     1       0     0     no
   1     1       0     1     no
   1     1       1     0     no
   1     1       1     1     no
```

**Result.** det M is even, and the two families split, if and only if
beta_th = 0, Pi_th = 0 and E_g = 0 together. The pyroelectric constant p3 makes
no difference either way: its two entries M35 and M52 are both odd, so they fit
the matching. The earlier statement that p3 breaks the split was wrong, and the
master has been corrected.

One refinement, recorded because it is easy to trip over: the sign-matching
condition is sufficient but not necessary. With q = 0 the carrier drops out of
the Gauss law, the conflicting cycles cannot be realised by any permutation,
and the determinant comes out even even though the matching still fails. Six
of the 64 combinations in the wider sweep behave that way. The exact test is
the one quoted.

## 2. Degree

Counted two ways, agreeing:

- row-by-row: 4 + 4 + 2 + 2 + 2 = 14 with l_g non-zero, 2 + 2 + 2 + 2 + 2 = 10
  with l_g = 0;
- exact determinant in mp precision: degree 14 with l_g = 3e-7, degree 10 with
  l_g = 0. The eta^14 coefficient is -3.9303908e-16, which matches the hand
  count -l_g^4 c44 c33 eps33 D_n k_th to all digits printed.

Note in passing, because it cost time: the size-effect entries are about 22
decades below the leading entries, so a double-precision determinant returns a
degree-10 polynomial and four roots are simply lost. Coefficients must be
formed at 120 digits or more.

The 14 roots at k = 1e4 1/m, f = 1 MHz, l_g = 3e-7 m, l_nl = 2e-7 m are

```
  6.5149e3   1.4703e4   2.3818e4   3.9368e5   3.3301e6   3.3335e6   2.9145e8
```

in magnitude, each in a +/- pair. The two pairs near 3.33e6 are the gradient
boundary layers: 1/l_g = 3.33e6 m^-1.

## 3. Section-8 tests

Full log: `internal/section8_tests.log`, produced by `section8_tests.py`.

### Rayleigh-Lamb, both families (tolerance 1e-5)

The 4x4 free-face system of the elastic limit, at fd = 1000, 3000 and 10000
Hz m, against `common/rayleigh_lamb.py`. Largest relative difference over all
branches of both families: **2.6e-14**. Thick-plate limit at fd = 2e4: both
lowest branches give 2909.73164 m/s against the exact Rayleigh speed
2909.73139 m/s, relative 8.3e-08. Speeds: c_L 6197.8243 (target 6197.82,
6.9e-07), c_T 3121.95271 (target 3121.95, 8.7e-07), c_R 2909.73139 (target
2909.7, 1.1e-05).

### Couplings one at a time, against Calculation H

- Piezo stiffening of the bulk shear wave: K^2 = e15^2/(c44 eps11) =
  7.1865e-02; the (u_z, phi) block of M(0) vanishes at the stiffened speed to
  2.8e-37 relative.
- Zener thermoelastic damping of the bulk longitudinal wave, Q^-1 =
  Delta_E (omega tau)/(1 + (omega tau)^2) with Delta_E = T0 beta1^2/(rho c_p
  c11) = 2.1409e-07 and tau = rho c_p/(k_th k^2): relative differences
  2.1e-11, 5.4e-08 and 2.1e-07 at omega tau = 0.1, 1 and 10. Peak of Q^-1 at
  omega tau = 1 equals Delta_E/2 to 0 digits of difference.
- Hutson-White: complex k from the (u_z, phi, n) block against the closed form
  with eps_eff = eps11 (1 + i omega_c/omega), omega_c = q b_n n0/eps11 =
  4.2374e10 s^-1: real and imaginary parts agree to 1e-16 at omega/omega_c =
  0.01, 1, 100. With the coupling scaled down by 1e3 (K^2 -> 7e-8) the loss
  per wavelength peaks at omega/omega_c = 1.0000. At the physical K^2 the peak
  sits at 0.9661, an O(K^2) shift that the weak-coupling statement does not
  claim to cover.

### l_g and l_nl to zero, and the direction of the shift

Bulk longitudinal speed, k = 1e4 1/m:

```
  l_g k = 1e-4 .. 1e-2 :  (c - c_local)/c_local = +4.99999995e-09, +4.99999875e-07, +4.999875e-05
  l_nl k = 1e-4 .. 1e-2:  (c - c_local)/c_local = -4.99999995e-09, -4.99999625e-07, -4.999625e-05
```

against the predicted +0.5 (l_g k)^2 and -0.5 (l_nl k)^2 (residuals below
1e-6 relative). **l_g stiffens, l_nl softens.** The relative change of det M
falls by 99.99995 when l_g falls by 10, i.e. it is quadratic, as it should be.
The four extra roots run off like 1/l_g, so they leave the physical window as
l_g goes to zero while the ten matched roots stay put.

### Roots against conditions, and det B

- degree of det M: 14 with l_g = 3e-7, 10 with l_g = 0 (both by the exact
  determinant and by polyroots, which returns 14 and 10 roots);
- B is 14 x 14: seven face conditions on each of the two faces;
- at f = 5 MHz, h = 1 mm, a mode sits near k = 1.1e4 1/m. The smallest singular
  value dips to 1.173e-06 against an off-mode level of 1.444e-04, 2.1 decades.
  The singular-value route and the determinant route put the zero at 10999.20
  and 11001.07 1/m: 1.9 grid spacings apart on a grid of spacing 1 1/m,
  relative 1.7e-04.

## 4. Placeholder constants

c11 209.7, c13 105.4, c33 211.2, c44 42.4 GPa; e31 -0.57, e33 1.32, e15 -0.48
C/m^2; eps11 8.54 eps0, eps33 10.2 eps0; beta1 1.7e6, beta3 1.5e6 Pa/K; p3 0.5
C/(m^2 K); rho 5680 kg/m^3; c_p 3.4e6 J/(m^3 K); k_th 60 W/(m K); T0 300 K;
D_n 1e-3 m^2/s; b_n 0.02 m^2/(V s); n0 1e21 m^-3; v_d 1e3 m/s; tau_R 1e-9 s;
beta_th 2.5e5, Pi_th 0.05, E_g 1.2e-19; q 1.602e-19 C; l_g 3e-7 m, l_nl 2e-7 m;
tau_q 1e-11 s. Plate half-thickness 1 mm for the plate tests.
