# Mathematical Benchmark Results — Phase 2 Milestone F

**Prepared:** 2026-10-21  
**Status:** Completed (BM-1 derived analytically; BM-2 through BM-5 specified)  
**Evidence standard:** DERIVED (analytical) / SPECIFIED (pending numerical implementation)  
**Source:** Independent derivation; no external code execution

---

## 1. Overview

This document presents mathematical benchmarks for verifying energy-balance and conservation identities at multiphysics interfaces. BM-1 (classical lossless elastic interface) is derived analytically. BM-2 through BM-5 are specified but not yet numerically implemented.

---

## 2. BM-1: Classical Lossless Elastic Interface

### 2.1 Problem statement

Two isotropic elastic half-spaces bonded at $x_3 = 0$:
- Medium 1 ($x_3 < 0$): density $\rho_1$, Lamé parameters $\lambda_1, \mu_1$
- Medium 2 ($x_3 > 0$): density $\rho_2$, Lamé parameters $\lambda_2, \mu_2$

Incident P-wave from medium 1 at angle $\theta_0$.

### 2.2 Governing equations

Navier equations:
$$\rho_m \ddot{u}_i = (\lambda_m + \mu_m)u_{j,ji} + \mu_m u_{i,jj}, \quad m = 1,2$$

### 2.3 Wave speeds

P-wave speed: $c_{P,m} = \sqrt{(\lambda_m + 2\mu_m)/\rho_m}$
SV-wave speed: $c_{S,m} = \sqrt{\mu_m/\rho_m}$

### 2.4 Wave decomposition

**Incident P-wave (medium 1):**
$$\mathbf{u}^{inc} = A_0 \begin{pmatrix} \sin\theta_0 \\ -\cos\theta_0 \end{pmatrix} e^{ik_1(-x_1\sin\theta_0 - x_3\cos\theta_0) + i\omega t}$$

**Reflected P-wave:**
$$\mathbf{u}^{ref,P} = A_1 \begin{pmatrix} \sin\theta_1 \\ \cos\theta_1 \end{pmatrix} e^{ik_1(-x_1\sin\theta_1 + x_3\cos\theta_1) + i\omega t}$$

**Reflected SV-wave:**
$$\mathbf{u}^{ref,SV} = B_1 \begin{pmatrix} \cos\theta_2 \\ \sin\theta_2 \end{pmatrix} e^{ik_1(-x_1\sin\theta_2 + x_3\cos\theta_2) + i\omega t}$$

**Transmitted P-wave:**
$$\mathbf{u}^{trans,P} = A_2 \begin{pmatrix} \sin\theta_3 \\ -\cos\theta_3 \end{pmatrix} e^{ik_2(-x_1\sin\theta_3 - x_3\cos\theta_3) + i\omega t}$$

**Transmitted SV-wave:**
$$\mathbf{u}^{trans,SV} = B_2 \begin{pmatrix} \cos\theta_4 \\ \sin\theta_4 \end{pmatrix} e^{ik_2(-x_1\sin\theta_4 - x_3\cos\theta_4) + i\omega t}$$

Snell's law:
$$\frac{\sin\theta_0}{c_{P,1}} = \frac{\sin\theta_1}{c_{P,1}} = \frac{\sin\theta_2}{c_{S,1}} = \frac{\sin\theta_3}{c_{P,2}} = \frac{\sin\theta_4}{c_{S,2}}$$

### 2.5 Interface conditions (perfect bonding)

At $x_3 = 0$:
1. $u_1^{(1)} = u_1^{(2)}$ (tangential displacement)
2. $u_3^{(1)} = u_3^{(2)}$ (normal displacement)
3. $\sigma_{31}^{(1)} = \sigma_{31}^{(2)}$ (tangential traction)
4. $\sigma_{33}^{(1)} = \sigma_{33}^{(2)}$ (normal traction)

### 2.6 Energy flux

For elastic media, the mechanical energy flux is:
$$J_i = \sigma_{ji}v_i$$

Normal component at interface:
$$J_3 = \sigma_{31}v_1 + \sigma_{33}v_3$$

For harmonic fields, time-averaged normal flux:
$$\langle J_3 \rangle_t = \frac{1}{2}\text{Re}[\widehat{\sigma}_{31}(-i\omega\widehat{u}_1^*) + \widehat{\sigma}_{33}(-i\omega\widehat{u}_3^*)]$$
$$= \frac{\omega}{2}\text{Im}[\widehat{\sigma}_{31}\widehat{u}_1^* + \widehat{\sigma}_{33}\widehat{u}_3^*]$$

### 2.7 Energy ratios

For incident P-wave:
$$R_P = \frac{|\langle J_3^{ref,P}\rangle_t|}{|\langle J_3^{inc,P}\rangle_t|}, \quad R_{SV} = \frac{|\langle J_3^{ref,SV}\rangle_t|}{|\langle J_3^{inc,P}\rangle_t|}$$
$$T_P = \frac{|\langle J_3^{trans,P}\rangle_t|}{|\langle J_3^{inc,P}\rangle_t|}, \quad T_{SV} = \frac{|\langle J_3^{trans,SV}\rangle_t|}{|\langle J_3^{inc,P}\rangle_t|}$$

### 2.8 Conservation identity

For a lossless elastic interface:
$$R_P + R_{SV} + T_P + T_{SV} = 1$$

### 2.9 Analytical solution

The reflection and transmission coefficients for P-SV scattering at an elastic interface are well-known (Achenbach 1975). The coefficients depend on the impedance contrast and angle of incidence.

**Special case: Normal incidence ($\theta_0 = 0$)**

Only P-waves (no mode conversion at normal incidence).

Reflection coefficient:
$$R = \frac{Z_2 - Z_1}{Z_2 + Z_1}, \quad Z_m = \rho_m c_{P,m}$$

Transmission coefficient:
$$T = \frac{2Z_1}{Z_1 + Z_2}$$

Energy ratios:
$$R_P = |R|^2 = \left|\frac{Z_2 - Z_1}{Z_2 + Z_1}\right|^2, \quad T_P = \frac{Z_1}{Z_2}|T|^2 = \frac{4Z_1Z_2}{(Z_1 + Z_2)^2}$$

Conservation check:
$$R_P + T_P = \frac{(Z_2 - Z_1)^2 + 4Z_1Z_2}{(Z_1 + Z_2)^2} = \frac{Z_2^2 - 2Z_1Z_2 + Z_1^2 + 4Z_1Z_2}{(Z_1 + Z_2)^2} = \frac{(Z_1 + Z_2)^2}{(Z_1 + Z_2)^2} = 1$$

**Conservation verified for normal incidence.** ✓

### 2.10 Numerical implementation status

| Task | Status |
|------|--------|
| Analytical derivation | COMPLETED |
| Symbolic verification (SymPy) | NOT DONE |
| Numerical solver (Python) | NOT DONE |
| Convergence test | NOT DONE |
| Comparison with published results | NOT DONE |

---

## 3. BM-2: Thermoelastic Interface (Lord–Shulman)

### 3.1 Problem statement

Two thermoelastic half-spaces with Lord–Shulman heat conduction bonded at $x_3 = 0$.

### 3.2 Governing equations

Medium $m$:
$$\rho_m\ddot{u}_i = (\lambda_m + \mu_m)u_{j,ji} + \mu_m u_{i,jj} - \beta_m T_{,i}$$
$$\rho_m c_{v,m}\dot{T} = k_m\nabla^2T - \beta_m T_0\dot{u}_{i,i} - \tau_0 \rho_m c_{v,m}\ddot{T} + \text{relaxation terms}$$

LS heat equation:
$$q_i + \tau_0\dot{q}_i = -kT_{,i}$$

### 3.3 Energy flux — UNRESOLVED

The total energy flux for LS theory includes mechanical + thermal + relaxation terms. The precise form is not yet derived (see `08_theory_specific_energy_flux.md`).

### 3.4 Conservation identity

$$\sum R_j + \sum T_k + A = 1$$

where $A$ accounts for thermal dissipation.

### 3.5 Status

**SPECIFIED** — Problem defined; energy flux derivation pending.

---

## 4. BM-3: Piezoelectric Interface

### 4.1 Problem statement

Piezoelectric half-space bonded to elastic half-space at $x_3 = 0$.

### 4.2 Governing equations

Piezoelectric medium:
$$\sigma_{ij} = c_{ijkl}\varepsilon_{kl} - \beta_{ij}(T-T_0) - e_{kij}E_k$$
$$D_i = e_{ijk}\varepsilon_{jk} + \kappa_{ij}E_j$$
$$E_i = -\phi_{,i}$$
$$D_{i,i} = 0$$

### 4.3 Energy flux

Includes mechanical + thermal + electrical channels:
$$J_i = \sigma_{ji}v_i + q_i + J_i^{elec}$$

where $J_i^{elec}$ is the electrical energy flux (form pending — see `08_theory_specific_energy_flux.md`).

### 4.4 Conservation identity

$$\sum R_j + \sum T_k + A = 1$$

where $A$ accounts for all dissipation.

### 4.5 Status

**SPECIFIED** — Problem defined; electrical flux derivation pending.

---

## 5. BM-4: Memory-Dependent Derivative (MDD) Interface

### 5.1 Problem statement

Two media with MDD heat conduction bonded at an interface.

### 5.2 MDD operator

$$D_\tau f(t) = \frac{1}{\tau}\int_{t-\tau}^{t} \kappa(t-\zeta) f'(\zeta) \, d\zeta$$

### 5.3 Energy flux — UNRESOLVED

Convolution makes instantaneous energy flux ambiguous. Hereditary flux formulation required.

### 5.4 Status

**SPECIFIED** — Problem defined; hereditary flux derivation pending.

---

## 6. BM-5: Nonlocal/Porous/Semiconductor Interface

### 5.1 Problem statement

Nonlocal elastic or porous or semiconductor-coupled interface.

### 5.2 Challenges

- Nonlocal: divergence theorem fails; integral-form flux required
- Porous: pore-fluid energy channel
- Semiconductor: carrier diffusion energy channel

### 5.3 Status

**SPECIFIED** — Problem defined; multiple sub-cases pending.

---

## 7. Benchmark Implementation Plan

| Benchmark | Theory | Energy flux | Conservation check | Status |
|-----------|--------|-------------|-------------------|--------|
| BM-1 | Classical elastic | $\sigma v$ (derived) | $R+T=1$ (verified for normal incidence) | DERIVED |
| BM-2 | LS thermoelastic | $\sigma v + q +$ relaxation | $\sum R + \sum T + A = 1$ | SPECIFIED |
| BM-3 | Piezoelectric | $\sigma v + q + J^{elec}$ | $\sum R + \sum T + A = 1$ | SPECIFIED |
| BM-4 | MDD | Hereditary integral | $\sum R + \sum T + A = 1$ | SPECIFIED |
| BM-5 | Nonlocal/porous | Integral form | $\sum R + \sum T + A = 1$ | SPECIFIED |

---

## 8. Code Repository Structure (planned)

```
mathematics/benchmarks/
├── bm1_elastic_interface/
│   ├── bm1_analytical.py       # Analytical solution
│   ├── bm1_numeric.py          # Numerical verification
│   ├── bm1_test.py             # Unit tests
│   └── bm1_results.md          # Results report
├── bm2_ls_thermoelastic/
│   ├── ...
├── bm3_piezoelectric/
│   ├── ...
├── bm4_mdd/
│   ├── ...
└── bm5_nonlocal_porous/
    └── ...
```

---

## 9. Next Steps

1. Implement BM-1 numerical solver in Python
2. Verify conservation $R_P + R_{SV} + T_P + T_{SV} = 1$ for arbitrary incidence angles
3. Derive LS energy flux and implement BM-2
4. Derive piezoelectric electrical flux and implement BM-3
5. Derive MDD hereditary flux and implement BM-4
6. Document all benchmark results with quantitative residuals
