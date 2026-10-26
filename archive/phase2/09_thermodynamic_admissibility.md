# Thermodynamic Admissibility — Phase 2 Milestone D

**Prepared:** 2026-10-21  
**Status:** Completed (framework established; theory-specific checks pending)  
**Evidence standard:** DERIVED / SCHEMATIC  
**Source:** Independent derivation from Coleman-Noll procedure

---

## 1. Dissipation Inequality (Coleman-Noll Form)

From `07_continuum_balance_derivations.md` Theorem 6.1, the local dissipation inequality is:

$$\mathcal{D} = \sigma_{ij}\dot{\varepsilon}_{ij} - \rho(\dot{\psi} + s\dot{T}) - \frac{q_i T_{,i}}{T} \geq 0$$

where:
- $\sigma_{ij}\dot{\varepsilon}_{ij}$ = stress power input per unit volume
- $\rho\dot{\psi}$ = rate of change of Helmholtz free energy
- $\rho s\dot{T}$ = entropy-temperature coupling
- $q_i T_{,i}/T$ = heat conduction contribution

---

## 2. Constitutive Restrictions

For a thermoelastic material with free energy $\psi = \psi(\varepsilon_{ij}, T, T_{,i})$:

$$\sigma_{ij} = \rho\frac{\partial\psi}{\partial\varepsilon_{ij}}, \qquad s = -\frac{\partial\psi}{\partial T}, \qquad \frac{\partial\psi}{\partial T_{,i}} = 0$$

The reduced dissipation inequality becomes:

$$\mathcal{D} = -\frac{q_i T_{,i}}{T} \geq 0$$

### Fourier conduction

$q_i = -k T_{,i}$ with $k > 0$:

$$\mathcal{D} = \frac{k T_{,i}T_{,i}}{T} \geq 0 \quad \text{(satisfied for } T > 0, k > 0\text{)}$$

---

## 3. Theory-Specific Admissibility Analysis

### 3.1 Lord–Shulman (Single Relaxation Time)

**Heat equation:** $q_i + \tau_0\dot{q}_i = -k T_{,i}$

**Dissipation analysis:**

From the heat equation:
$$q_i = -k T_{,i} - \tau_0\dot{q}_i$$

Substitute into dissipation:
$$\mathcal{D} = -\frac{q_i T_{,i}}{T} = \frac{k T_{,i}T_{,i}}{T} + \frac{\tau_0\dot{q}_i T_{,i}}{T}$$

The first term is non-negative for $k > 0$. The second term $\tau_0\dot{q}_i T_{,i}/T$ can be positive or negative depending on the phase relationship between $\dot{q}_i$ and $T_{,i}$.

**Condition for admissibility:** The relaxation term must not dominate the Fourier term:
$$\left|\frac{\tau_0\dot{q}_i T_{,i}}{T}\right| \leq \frac{k T_{,i}T_{,i}}{T}$$

This is not guaranteed for all processes. LS theory is **conditionally admissible** — admissible for sufficiently slow processes (small $\tau_0\dot{q}_i$) but potentially non-admissible for rapid transients.

**Status:** SCHEMATIC — condition derived but not verified against published analyses.

### 3.2 Green–Naghdi Type II (Dissipationless)

**Heat equation:** No dissipation by construction; thermal displacement gradient formulation.

**Dissipation:** $\mathcal{D} = 0$

**Admissibility:** Satisfied trivially (zero dissipation). However, the physical interpretation of "dissipationless heat propagation" requires careful justification — the second law allows $\mathcal{D} = 0$ only for reversible processes.

**Status:** SCHEMATIC — not independently verified.

### 3.3 Green–Naghdi Type III

**Dissipation:** Temperature-rate coupling introduces dissipation terms.

**Admissibility:** Depends on the sign of the temperature-rate coupling coefficient. Not independently verified.

**Status:** SCHEMATIC.

### 3.4 Dual–Phase–Lag (DPL)

**Heat equation:** $q_i(t+\tau_q) = -k T_{,i}(t+\tau_T)$

**Dissipation analysis:** For $\tau_q > \tau_T$, the DPL model can exhibit wave-like behavior with attenuation. For $\tau_q < \tau_T$, the model may be ill-posed or exhibit anti-dissipative behavior.

**Condition:** $\tau_q \geq \tau_T$ is typically required for stability and admissibility.

**Status:** SCHEMATIC — condition cited from literature but not independently derived.

### 3.5 Moore–Gibson–Thompson (MGT)

**Heat equation:** Third-order-in-time: $\tau\ddot{q} + \dot{q} = -k\nabla^2 T - \cdots$

**Dissipation analysis:** The MGT equation can be written as a damped wave equation. For appropriate parameter ranges, it is dissipative. However, the third-order time derivative can lead to instabilities for certain parameter values.

**Status:** SCHEMATIC.

### 3.6 Memory-Dependent Derivative (MDD)

**MDD operator:** $D_\tau f(t) = \frac{1}{\tau}\int_{t-\tau}^t \kappa(t-\zeta) f'(\zeta)\,d\zeta$

**Dissipation analysis:** The memory kernel $\kappa$ determines admissibility. For positive definite kernels, the MDD operator is dissipative. For oscillatory or sign-changing kernels, admissibility is not guaranteed.

**Kernel conditions (from RG-003):**
- $0 < \kappa(t-\zeta) \leq 1$
- $\tau$ less than upper limit set by kernel for uniqueness and existence

**Specific kernels (Eq. 2 in RG-003):**
1. $\alpha = \beta = 0$: $\kappa = 1$ (uniform memory)
2. $\alpha = 0, \beta = 1/2$: $\kappa = 1 - (t-\zeta)/\tau$ (linear decay)
3. $\alpha = \beta = 1$: $\kappa = (1 - (t-\zeta)/\tau)^2$ (quadratic decay)

**Admissibility:** Kernels 1-3 are positive on $[0,\tau]$, so MDD with these kernels is dissipative.

**Status:** PARTIALLY VERIFIED — kernel positivity verified from RG-003 Eq. (2); full dissipation inequality not derived.

### 3.7 Fractional-Order Thermoelasticity

**Heat equation:** Fractional derivative (Caputo or Riemann-Liouville)

**Dissipation analysis:** Fractional derivatives introduce hereditary dissipation. Admissibility depends on the fractional order and the specific definition used.

**Status:** SCHEMATIC — not independently verified.

---

## 4. Stability and Causality

### 4.1 Stability conditions

| Theory | Stability condition | Source | Verified |
|--------|-------------------|--------|----------|
| Classical (Fourier) | $k > 0, c_v > 0, c_{ijkl}$ positive definite | Standard | YES |
| Lord–Shulman | $\tau_0 > 0$ | Standard | YES |
| GN Type II | No dissipation; stable by construction | Literature | SCHEMATIC |
| DPL | $\tau_q \geq \tau_T$ | Literature | SCHEMATIC |
| MGT | $\tau > 0$, appropriate damping | Literature | SCHEMATIC |
| MDD | Positive definite kernel | RG-003 Eq. (2) | PARTIAL |
| Nonlocal | $(e_0a)^2 > 0$ | Literature | SCHEMATIC |

### 4.2 Causality

For hyperbolic theories (LS, DPL, TPL, MGT), finite heat propagation speed implies causality. The maximum heat speed is:

- LS: $c_{heat} = \sqrt{k/(\rho c_v \tau_0)}$
- DPL: Depends on $\tau_q, \tau_T$
- MGT: Depends on $\tau$ and other parameters

**Status:** SCHEMATIC — formulas cited from literature but not independently derived.

---

## 5. Positive Energy

### 5.1 Condition

The total stored energy must be positive definite:
$$\mathcal{E} > 0 \quad \text{for all non-zero states}$$

### 5.2 Theory-specific checks

| Theory | Positive energy condition | Status |
|--------|--------------------------|--------|
| Classical | $c_{ijkl}$ positive definite, $c_v > 0$ | VERIFIED |
| LS | + $\frac{\tau_0}{2k}q_i q_i \geq 0$ | SCHEMATIC |
| GN II | + $\frac{k}{2T_0}T_{,i}T_{,i} \geq 0$ | SCHEMATIC |
| DPL | + relaxation terms $\geq 0$ | SCHEMATIC |
| MDD | Depends on kernel properties | SCHEMATIC |
| Nonlocal | Nonlocal energy may not be positive locally | SCHEMATIC |

---

## 6. Well-Posedness

### 6.1 Definition

A boundary-value problem is well-posed if:
1. A solution exists
2. The solution is unique
3. The solution depends continuously on the data

### 6.2 Theory-specific assessments

| Theory | Well-posedness | Known issues | Status |
|--------|---------------|--------------|--------|
| Classical | Well-posed | None | VERIFIED |
| LS | Well-posed for $\tau_0 > 0$ | None | SCHEMATIC |
| DPL | Ill-posed for $\tau_q < \tau_T$ | Paradoxical heat flow | SCHEMATIC |
| MGT | Well-posed for appropriate parameters | Third-order instabilities | SCHEMATIC |
| MDD | Well-posed for positive kernels | Kernel-dependent | PARTIAL (RG-003) |
| Nonlocal | Well-posed with appropriate integral kernels | Boundary layer effects | SCHEMATIC |

---

## 7. Critical Findings

### 7.1 Asymmetric dissipation at interfaces

RG-003 (full text extracted) uses different energy flux definitions on the two sides of the interface:
- HPS side: includes mechanical + electrical + thermal flux
- TS side: includes mechanical flux only

This means the dissipation inequality cannot be checked consistently across the interface — the thermal dissipation on the TS side is unaccounted for.

### 7.2 No unified dissipation inequality

Each theory (LS, GN, DPL, TPL, MGT, MDD) has its own dissipation structure. No common framework exists for comparing thermodynamic admissibility across theories.

### 7.3 Stability limits

Chiriţă et al. (cited in RG-003) show that $n \geq 5$ or $p \geq 5$ in higher-order MDD leads to unstable systems. This is an important constraint on admissible parameter ranges.

---

## 8. Next Steps

1. Derive LS dissipation inequality from first principles
2. Derive MGT dissipation inequality
3. Check RG-003 dissipation consistency across interface
4. Verify stability conditions for each theory against published analyses
5. Document which theories are thermodynamically admissible under which conditions
