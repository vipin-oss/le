# Interface Scattering Matrix Derivations — Phase 2 Milestone E

**Prepared:** 2026-10-21  
**Status:** Completed (framework derived; theory-specific matrices pending)  
**Evidence standard:** DERIVED / VERIFIED (RG-003 Eq. 44)  
**Source:** Independent derivation; verified against RG-003 full text (Eqs. 36-44)

---

## 1. General Interface Scattering Problem

### 1.1 Geometry

Two half-spaces bonded at interface $x_3 = 0$:
- Medium 1: $x_3 < 0$ (incident side)
- Medium 2: $x_3 > 0$ (transmission side)

### 1.2 Wave decomposition

Each medium supports multiple wave modes:
- Propagating modes: real phase velocity, possibly attenuated
- Evanescent modes: imaginary phase velocity, exponentially decaying

For medium $m$ with $N_m$ modes, the total field is:
$$\mathbf{u}^{(m)} = \sum_{j=1}^{N_m} A_j^{(m)} \mathbf{U}_j^{(m)} e^{i(\mathbf{k}_j^{(m)}\cdot\mathbf{x} - \omega t)}$$

where $A_j^{(m)}$ are modal amplitudes and $\mathbf{U}_j^{(m)}$ are polarization vectors.

---

## 2. Interface Conditions

### 2.1 Perfect bonding

| Quantity | Condition |
|----------|-----------|
| Displacement | $u_i^{(1)} = u_i^{(2)}$ at $x_3 = 0$ |
| Traction | $\sigma_{j3}^{(1)} = \sigma_{j3}^{(2)}$ at $x_3 = 0$ |
| Temperature | $T^{(1)} = T^{(2)}$ at $x_3 = 0$ |
| Heat flux | $q_3^{(1)} = q_3^{(2)}$ at $x_3 = 0$ |
| Electric potential | $\phi^{(1)} = \phi^{(2)}$ at $x_3 = 0$ |
| Electric displacement | $D_3^{(1)} = D_3^{(2)}$ at $x_3 = 0$ |

### 2.2 Imperfect bonding (spring-type)

$$u_i^{(2)} - u_i^{(1)} = K_i^u t_i \quad \text{(displacement jump proportional to traction)}$$
$$T^{(2)} - T^{(1)} = K^T q_3 \quad \text{(thermal contact resistance)}$$
$$\phi^{(2)} - \phi^{(1)} = K^\phi D_3 \quad \text{(electrical contact resistance)}$$

---

## 3. Scattering Matrix Formulation

### 3.1 Amplitude system

The interface conditions yield a linear system relating incident, reflected, and transmitted amplitudes:

$$\boldsymbol{\Delta} \mathbf{X} = \mathbf{Q}$$

where:
- $\boldsymbol{\Delta}$ = interface condition matrix (dimension $N_{eq} \times N_{modes}$)
- $\mathbf{X}$ = unknown modal amplitudes (reflected + transmitted)
- $\mathbf{Q}$ = known incident wave coupling vector

### 3.2 RG-003 verification (from full text)

From RG-003 Eq. (44):

$$\boldsymbol{\Delta} \mathbf{X} = \mathbf{Q}$$

where $\boldsymbol{\Delta}$ is a $7 \times 7$ matrix with entries $\Delta_{ij}$, $\mathbf{X} = [X_1, \dots, X_7]^T$ contains normalized modal amplitudes, and $\mathbf{Q}$ contains the incident wave coupling terms.

The matrix structure (from RG-003):

$$\Delta_{1i} = -\frac{c_{13}}{\beta_1 T_0 c} - \left(\frac{c_{33}W_i}{\beta_1 T_0} + \frac{\eta_{33}}{\eta_{31}}\Phi_i\right)q_i - \frac{c_{11}\beta_3}{i\omega\beta_1^2 T_0}\Theta_i$$
$$\Delta_{2i} = -\frac{c_{55}W_i}{\beta_1 T_0 c} - \frac{c_{55}q_i}{\beta_1 T_0} - \frac{\eta_{15}\Phi_i}{c\eta_{31}}$$
$$\Delta_{3i} = 1, \quad \Delta_{4i} = W_i, \quad \Delta_{5i} = \Theta_i$$
$$\Delta_{6i} = -\left[K_3^*(1 + \tau_v\Gamma(\tau,b)) + K_3(1 + \tau_T\Gamma(\tau,b))i\omega\omega_1\right]\Theta_i q_i$$
$$\Delta_{7i} = -\frac{c_{11}\eta_{31}}{\beta_1 T_0\eta_{33}c} - \frac{c_{11}q_i W_i}{\beta_1 T_0} + \frac{c_{11}\varepsilon_{33}}{\eta_{33}\eta_{31}}q_i\Phi_i + \frac{p_3 c_{11}^2}{i\omega\eta_{33}\beta_1^2 T_0}\Theta_i$$

for $i = 1-4$ (transmitted modes), and:

$$\Delta_{15} = \frac{C_T\zeta_1 + k_1^2\rho^e(\alpha_1^{e2} - 2\alpha_2^{e2}\sin^2\theta_1)}{i\omega\beta_1 T_0}, \quad \Delta_{25} = -\frac{k_1^2\alpha_1^{e2}\rho^e\sin 2\theta_1}{i\omega\beta_1 T_0}, \dots$$

for $i = 5-7$ (reflected modes).

### 3.3 Verified interface conditions (RG-003 Eq. 38)

$$\sigma_{33} = \sigma_{33}^e, \quad \sigma_{31} = \sigma_{31}^e, \quad u_1 = u_1^e, \quad u_3 = u_3^e, \quad T = T^e$$
$$\left[K_3\frac{\partial}{\partial t}\left(1 + \sum_{m=1}^p \frac{\tau_T^m}{m!}D_{\tau_T}^m\right) + K_3^*\left(1 + \sum_{m=1}^l \frac{\tau_v^m}{m!}D_{\tau_v}^m\right)\right]\frac{\partial T}{\partial x_3} = K_e^*\frac{\partial T^e}{\partial x_3}, \quad D_3 = 0$$

**Key observation:** The electrical boundary condition is $D_3 = 0$ (insulated interface), not $D_3^{(1)} = D_3^{(2)}$. This is a specific modeling choice, not a general interface condition.

---

## 4. Secular Equation

### 4.1 Christoffel-type system

For each medium, substitution of harmonic plane wave form yields:

$$\Gamma_{ij}(\mathbf{n}, \omega) U_j = \rho\omega^2 U_i$$

where $\Gamma_{ij}$ is the Christoffel-type matrix depending on propagation direction $\mathbf{n} = \mathbf{k}/|\mathbf{k}|$.

### 4.2 Characteristic equation

Nontrivial solutions require:
$$\det[\Gamma_{ij} - \rho\omega^2\delta_{ij}] = 0$$

For RG-003 HPS medium, this gives the 8th-order polynomial (Eq. 27):
$$G_{11}q^8 + G_{12}q^6 + G_{13}q^4 + G_{14}q^2 + G_{15} = 0$$

Roots $q_1-q_4$ have positive imaginary parts (decaying in $+x_3$ direction), $q_5-q_8$ have negative imaginary parts.

### 4.3 Mode classification (RG-003)

- $q_4$: electric potential (eP) mode
- $q_1-q_3$: quasi-P (qP), quasi-T (qT), quasi-SV (qS) propagating modes

---

## 5. Number of Boundary Conditions

### Theorem 5.1 (Boundary condition count)

**Statement:** The number of independent boundary conditions must equal the number of unknown outgoing modal amplitudes.

**Proof:** For an interface between medium 1 ($N_1$ modes) and medium 2 ($N_2$ modes), with $N_{inc}$ incident modes:
- Unknown reflected amplitudes: $N_1 - N_{inc}$
- Unknown transmitted amplitudes: $N_2$
- Total unknowns: $N_1 - N_{inc} + N_2$
- Required independent boundary conditions: $N_1 - N_{inc} + N_2$

**RG-003 check:** 4 transmitted modes + 3 reflected modes = 7 unknowns; 7 boundary conditions in Eq. (38). ✓

---

## 6. Reciprocity and Energy Conservation

### 6.1 Reciprocity

For self-adjoint systems (lossless, no magnetic field, no rotation), the scattering matrix is symmetric:
$$S_{ij} = S_{ji}$$

For dissipative systems, reciprocity may still hold if the Onsager relations are satisfied.

### 6.2 Energy conservation

For a passive interface with no energy storage:
$$\sum_j R_j + \sum_k T_k + A = 1$$

where $A$ accounts for dissipation.

For an interface with energy storage:
$$\sum_j R_j + \sum_k T_k + A + \frac{\partial\mathcal{E}_{interface}}{\partial t} = 1$$

**RG-003 claim:** $\sum ES_s + E_{int} + E_{RP} + E_{RT} + E_{RS} = 1$ (Eq. 58)

**Critical issue:** The asymmetric energy flux definition (TS side missing thermal term) means this conservation law may not represent total energy conservation.

---

## 7. Complex Mode Handling

### 7.1 Evanescent modes

For purely evanescent modes in lossless media:
$$\langle J_n \rangle_t = 0$$

These modes don't contribute to net energy flux but affect the near-field.

### 7.2 Attenuating modes

For complex slowness $q = q_r + iq_i$:
- The mode carries energy while attenuating
- Energy flux must be computed using complex Poynting vector analogue

### 7.3 Modal normalization

For energy ratios to be meaningful, modes must be normalized such that:
$$\langle J_n \rangle_t = 1 \quad \text{for unit-amplitude propagating mode}$$

**Status:** SCHEMATIC — normalization procedure not standardized across theories.

---

## 8. Next Steps

1. Derive scattering matrix for BM-1 benchmark (classical elastic interface)
2. Derive scattering matrix for BM-2 benchmark (thermoelastic interface)
3. Test conservation identity $\sum R + \sum T + A = 1$ for each benchmark
4. Handle complex modes (evanescent, attenuating) consistently
5. Derive interface matrix for imperfect bonding conditions
