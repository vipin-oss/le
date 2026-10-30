# Theory-Specific Energy Flux — Phase 2 Milestone D

**Prepared:** 2026-10-21  
**Status:** Completed (framework established; derivations sketched)  
**Evidence standard:** DERIVED / SCHEMATIC / HYPOTHESIS  
**Source:** Independent derivation; verified against RG-003 full text (Eq. 45-46)

---

## 1. Overview

This document derives or sketches energy balances and energy flux definitions for each major continuum theory in the review scope. The classical derivation (from `07_continuum_balance_derivations.md`) establishes:

- Total stored energy: $\mathcal{E} = e + \frac{1}{2} v_i v_i$ (internal + kinetic)
- Classical total energy flux: $J_i = \sigma_{ji} v_i + q_i$
- Total energy balance: $\rho \dot{\mathcal{E}} = -J_{i,i} + \rho f_i v_i + \rho r$

For generalized theories, additional storage and flux terms appear. Each theory is analyzed below.

---

## 2. Classical Coupled Thermoelasticity (Fourier)

### 2.1 Governing equations

- Momentum: $\rho \ddot{u}_i = \sigma_{ji,j} + \rho f_i$
- Constitutive: $\sigma_{ij} = c_{ijkl}\varepsilon_{kl} - \beta_{ij}(T - T_0)$
- Heat conduction: $q_i = -k T_{,i}$ (Fourier's law)
- Energy: $\rho \dot{e} = \sigma_{ij}\dot{\varepsilon}_{ij} - q_{i,i} + \rho r$

### 2.2 Stored energy density

$$\mathcal{E} = \frac{1}{2}\rho v_i v_i + \frac{1}{2}c_{ijkl}\varepsilon_{ij}\varepsilon_{kl} - \beta_{ij}\varepsilon_{ij}(T-T_0) + \frac{\rho c_v}{2T_0}(T-T_0)^2$$

### 2.3 Energy flux

$$J_i = \sigma_{ji}v_i + q_i = \sigma_{ji}v_i - k T_{,i}$$

### 2.4 Total energy balance

$$\rho \dot{\mathcal{E}} = -(\sigma_{ji}v_i + q_i)_{,i} + \rho f_i v_i + \rho r$$

### 2.5 Dissipation

$$\mathcal{D} = \frac{k T_{,i}T_{,i}}{T} \geq 0 \quad \text{(for } k > 0\text{)}$$

### 2.6 Status

**DERIVED** — Standard continuum mechanics result.

---

## 3. Lord–Shulman Theory (Single Relaxation Time)

### 3.1 Governing equations

- Heat conduction: $q_i + \tau_0 \dot{q}_i = -k T_{,i}$
- Energy: $\rho \dot{e} = \sigma_{ij}\dot{\varepsilon}_{ij} - q_{i,i} + \rho r$

### 3.2 Stored energy density

The relaxation term introduces additional stored energy:

$$\mathcal{E}_{LS} = \mathcal{E}_{classical} + \frac{\tau_0}{2k} q_i q_i$$

where $\frac{\tau_0}{2k} q_i q_i$ represents energy stored in the heat-flux relaxation process.

### 3.3 Energy flux — UNRESOLVED

**Candidate 1:** $J_i = \sigma_{ji}v_i + q_i$ (same as classical)

**Candidate 2:** $J_i = \sigma_{ji}v_i + q_i + \text{relaxation correction}$

**Analysis:** From the LS heat equation:
$$q_i + \tau_0 \dot{q}_i = -k T_{,i}$$

Taking the time derivative of the energy balance and substituting is non-trivial. The question is whether the relaxation term $\tau_0 \dot{q}_i$ contributes to the energy flux or only to the storage term.

**Critical issue:** If $J_i = \sigma_{ji}v_i + q_i$ (classical form), then the total energy balance becomes:

$$\rho \dot{\mathcal{E}}_{LS} = -(\sigma_{ji}v_i + q_i)_{,i} + \rho f_i v_i + \rho r + \text{additional terms from } \tau_0\dot{q}_i$$

The additional terms must be identified. This is an **open derivation**.

### 3.4 Status

**SCHEMATIC** — Stored energy term proposed but not rigorously derived. Energy flux form unresolved.

---

## 4. Green–Lindsay Theory (Two Temperature/Ratio-Temp)

### 4.1 Governing equations

Two-temperature theory with temperature $T$ and conductive temperature $\phi$:
- Coupled equations for $T$ and $\phi$
- Two relaxation times

### 4.2 Stored energy density

$$\mathcal{E}_{GL} = \mathcal{E}_{classical} + \text{terms involving } (T - \phi)$$

### 4.3 Energy flux

**UNRESOLVED** — Same issues as LS theory. The two-temperature structure requires careful definition of what constitutes "heat flux."

### 4.4 Status

**SCHEMATIC** — Not derived.

---

## 5. Green–Naghdi Type II (Dissipationless)

### 5.1 Governing equations

No dissipation; thermal displacement gradient appears in constitutive relations:
$$q_i = -k^* T_{,i} \quad \text{(with modified conductivity)}$$
Entropy production: $\mathcal{D} = 0$

### 5.2 Stored energy density

$$\mathcal{E}_{GN-II} = \mathcal{E}_{elastic} + \frac{\rho c_v}{2T_0}T^2 + \frac{k}{2T_0}T_{,i}T_{,i} + \cdots$$

### 5.3 Energy flux

Since $\mathcal{D} = 0$, energy is conserved. The flux must include thermal displacement gradient terms.

**UNRESOLVED** — Exact form not standardized.

### 5.4 Status

**SCHEMATIC** — Not derived.

---

## 6. Green–Naghdi Type III

### 6.1 Governing equations

Temperature-rate coupling; different from Type II in the structure of the heat equation.

### 6.2 Status

**SCHEMATIC** — Not derived.

---

## 7. Dual–Phase–Lag (DPL) Theory

### 7.1 Governing equations

$$q_i(t + \tau_q) = -k T_{,i}(t + \tau_T)$$

Taylor expansion:
$$q_i + \tau_q \dot{q}_i + \frac{\tau_q^2}{2}\ddot{q}_i + \cdots = -k\left(T_{,i} + \tau_T \dot{T}_{,i} + \frac{\tau_T^2}{2}\ddot{T}_{,i} + \cdots\right)$$

### 7.2 Stored energy density

Two relaxation processes contribute:
$$\mathcal{E}_{DPL} = \mathcal{E}_{classical} + \frac{\tau_q}{2k}q_i q_i + \frac{\tau_T \rho c_v}{2k T_0}T_{,i}T_{,i}$$

### 7.3 Energy flux

**UNRESOLVED** — Two relaxation times require two correction terms. The precise form depends on the truncation order of the Taylor expansion.

### 7.4 Status

**SCHEMATIC** — Not derived.

---

## 8. Three–Phase–Lag (TPL) Theory

### 8.1 Governing equations

Adds thermal displacement gradient phase lag $\tau_v$:
$$q_i(t+\tau_q) = -k T_{,i}(t+\tau_T) - k^* T_{,i}(t+\tau_v)$$

### 8.2 Status

**SCHEMATIC** — Three relaxation parameters make energy flux even more complex than DPL.

---

## 9. Moore–Gibson–Thompson (MGT) Theory

### 9.1 Governing equations

Third-order-in-time heat equation:
$$\tau \ddot{q} + \dot{q} = -k\nabla^2 T - \cdots$$

### 9.2 Stored energy density

$$\mathcal{E}_{MGT} = \mathcal{E}_{classical} + \text{terms involving } \dot{q}_i \dot{q}_i$$

### 9.3 Energy flux

**UNRESOLVED** — Third-order time derivatives require careful treatment of energy storage.

### 9.4 Status

**SCHEMATIC** — Not derived.

---

## 10. Memory-Dependent Derivative (MDD) Theory

### 10.1 MDD operator

$$D_\tau f(t) = \frac{1}{\tau}\int_{t-\tau}^{t} \kappa(t-\zeta) f'(\zeta) \, d\zeta$$

Kernel function: $\kappa(t-\zeta) = 1 - \frac{2\beta}{\tau}(t-\zeta) + \frac{\alpha^2}{\tau^2}(t-\zeta)^2$

### 10.2 Stored energy density

History-dependent:
$$\mathcal{E}_{MDD}(t) = \mathcal{E}_{instantaneous}(t) + \int_0^t K(t-\xi) \mathcal{E}(\xi) \, d\xi$$

where $K$ is a memory kernel related to $\kappa$.

### 10.3 Energy flux

**UNRESOLVED** — Convolution makes instantaneous energy flux physically ambiguous. A hereditary (time-integral) flux formulation is required.

$$J_i^{MDD}(t) = \int_0^t M(t-\xi) J_i(\xi) \, d\xi$$

where $M$ is a memory kernel.

### 10.4 Status

**SCHEMATIC** — Not derived. This is a central open problem.

---

## 11. Nonlocal Elasticity (Eringen)

### 11.1 Governing equations

$$\sigma_{ij}(x) - (e_0 a)^2 \nabla^2 \sigma_{ij}(x) = c_{ijkl}\varepsilon_{kl}(x)$$

### 11.2 Energy flux — NONLOCAL FORM REQUIRED

The divergence theorem argument used in classical derivations fails for nonlocal stress:
$$\int_{\partial\mathcal{V}} \sigma_{ji} n_j \, dS \neq \int_{\mathcal{V}} \sigma_{ji,j} \, dV$$

The energy flux must be nonlocal (integral form):
$$J_i^{\text{nonlocal}}(x) = \int K(x-x') \sigma_{ji}(x') v_i(x') \, dx'$$

### 11.3 Status

**SCHEMATIC** — Integral form proposed but not standardized.

---

## 12. Piezoelectric Coupling

### 12.1 Constitutive relations

$$\sigma_{ij} = c_{ijkl}\varepsilon_{kl} - \beta_{ij}(T-T_0) - e_{kij}E_k$$
$$D_i = e_{ijk}\varepsilon_{jk} + \kappa_{ij}E_j$$

### 12.2 Electrical energy flux

**Candidate 1:** $J_i^{\text{elec}} = -\phi \dot{D}_i n_i$ (work done by electric field on displacement current)

**Candidate 2:** $J_i^{\text{elec}} = -D_i \dot{\phi} n_i$ (alternative form)

**RG-003 evidence:** Eq. (45) uses:
$$P = -\text{Re}(\sigma_{13}\overline{\dot{u}}_1 + \sigma_{33}\overline{\dot{u}}_3 - \phi\overline{\dot{D}}_3 + K_3\overline{T}_{,3}\frac{T}{T_0})$$

This includes the electrical term $-\phi\overline{\dot{D}}_3$ but only on the HPS (piezothermoelastic) side.

### 12.3 Status

**PARTIALLY VERIFIED** — RG-003 Eq. (45) provides an electrical flux term for piezothermoelastic media, but only for a specific 2D formulation and only on one side of the interface.

---

## 13. RG-003 Energy Flux — Verified from Full Text

### 13.1 HPS side (piezothermoelastic with MDD+TPL)

From RG-003 Eq. (45):
$$P = -\text{Re}\left(\sigma_{13}\overline{\dot{u}}_1 + \sigma_{33}\overline{\dot{u}}_3 - \phi\overline{\dot{D}}_3 + K_3\overline{T}_{,3}\frac{T}{T_0}\right)$$

Components:
- $\sigma_{13}\overline{\dot{u}}_1$: tangential mechanical power
- $\sigma_{33}\overline{\dot{u}}_3$: normal mechanical power
- $-\phi\overline{\dot{D}}_3$: electrical power
- $K_3\overline{T}_{,3}T/T_0$: thermal conduction power

### 13.2 TS side (elastic thermoelastic)

From RG-003 Eq. (46):
$$P^e = -\text{Re}\left(\sigma_{31}^e\overline{\dot{u}}_1^e + \sigma_{33}^e\overline{\dot{u}}_3^e\right)$$

Components:
- $\sigma_{31}^e\overline{\dot{u}}_1^e$: tangential mechanical power
- $\sigma_{33}^e\overline{\dot{u}}_3^e$: normal mechanical power

**CRITICAL FINDING:** The TS side energy flux OMITS the thermal heat flux term ($q_i n_i$) that the HPS side includes. This means:

1. The claimed energy conservation (Eq. 58: $\sum ES_s + E_{int} + E_{RP} + E_{RT} + E_{RS} = 1$) is for a **partial energy balance** that excludes thermal transport on the TS side.

2. The energy flux definitions are **asymmetric** between the two media at the same interface.

3. This asymmetry is consistent with GAP-001 (no consensus on energy flux definition) and GAP-002 (no conservation check).

### 13.3 Energy ratios

From RG-003 Eqs. (54)-(56):
$$E_{RP} = \frac{\langle P_{RP}^e\rangle}{\langle P_{IP}^e\rangle}, \quad E_{RT} = \frac{\langle P_{RT}^e\rangle}{\langle P_{IP}^e\rangle}, \quad E_{RS} = \frac{\langle P_{RS}^e\rangle}{\langle P_{IP}^e\rangle}, \quad ES_s = \frac{\langle P_s\rangle}{\langle P_{IP}^e\rangle}$$

### 13.4 Conservation claim

From RG-003 Eq. (58):
$$\sum_{s=1}^{4}\left(ES_s + E_{int} + E_{RP} + E_{RT} + E_{RS}\right) = 1$$

where $E_{int} = \sum_{s,t=1,s\neq t}^{4} E_{st}$ is interaction energy between refracted waves.

**Status:** Claimed by authors; NOT independently verified. The asymmetric flux definition casts doubt on whether this holds for total energy.

---

## 14. Cross-Theory Comparison

| Theory | Storage terms | Flux terms | Dissipation | Status |
|--------|--------------|------------|-------------|--------|
| Classical (Fourier) | $\frac{1}{2}\rho v^2 + \frac{1}{2}c\varepsilon^2 + \cdots$ | $\sigma v + q$ | $k T_{,i}^2/T$ | DERIVED |
| Lord–Shulman | + $\frac{\tau}{2k}q^2$ | $\sigma v + q$ + ? | Relaxation | SCHEMATIC |
| Green–Lindsay | + two-temp terms | ? | ? | SCHEMATIC |
| GN Type II | + $\frac{k}{2T_0}(\nabla T)^2$ | ? | 0 | SCHEMATIC |
| GN Type III | ? | ? | ? | SCHEMATIC |
| DPL | + $\frac{\tau_q}{2k}q^2 + \frac{\tau_T}{2k}(\nabla T)^2$ | ? | ? | SCHEMATIC |
| TPL | + 3 relaxation terms | ? | ? | SCHEMATIC |
| MGT | + $\dot{q}^2$ terms | ? | ? | SCHEMATIC |
| MDD | Hereditary integral | Hereditary integral | ? | SCHEMATIC |
| Nonlocal | Integral form | Integral form | ? | SCHEMATIC |
| Piezoelectric | + electrical terms | $\sigma v + q + \phi\dot{D}$ | ? | PARTIAL (RG-003 Eq. 45) |

---

## 15. Next Steps

1. **Derive LS energy flux** from first principles using the relaxation equation
2. **Derive MGT energy flux** from the third-order heat equation
3. **Derive nonlocal energy flux** in integral form
4. **Derive MDD hereditary flux** in convolution form
5. **Verify RG-003 conservation claim** by checking if $\sum = 1$ with symmetric flux definitions
6. **Test BM-1 benchmark** (classical elastic interface) — see `phase2/15_mathematical_benchmark_results.md`
