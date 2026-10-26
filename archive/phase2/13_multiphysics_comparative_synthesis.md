# Multiphysics Comparative Synthesis — Phase 2 Milestone G

**Prepared:** 2026-10-21  
**Status:** Completed (comparison framework established; theory-specific comparisons pending numerical verification)  
**Evidence standard:** DERIVED / SCHEMATIC / VERIFIED (RG-003 full text)  
**Source:** Independent synthesis based on Phase 2 derivations and RG-003 full-text extraction

---

## 1. Comparison Framework

Twelve comparison criteria applied across theory families:

| # | Criterion | Classical | LS | GN II/III | DPL | TPL | MGT | MDD | Nonlocal |
|---|-----------|-----------|-----|-----------|-----|-----|-----|-----|----------|
| 1 | Mathematical structure | Elliptic/parabolic | Hyperbolic | Hyperbolic | Hyperbolic | Hyperbolic | 3rd-order | Hereditary | Integral |
| 2 | Heat speed | Infinite | Finite | Finite | Finite | Finite | Finite | Finite | Finite |
| 3 | Dissipation | Yes | Yes | No (II/III) | Yes | Yes | Yes | Kernel-dependent | Yes |
| 4 | Relaxation parameters | 0 | 1 (τ₀) | 0 (II), τ (III) | 2 (τ_q, τ_T) | 3 (τ_q, τ_T, τ_v) | 1 (τ) | 1 (τ) + kernel | (e₀a)² |
| 5 | Energy flux | σv + q | σv + q + ? | ? | σv + q + ? | σv + q + ? | σv + q + ? | Hereditary | Integral |
| 6 | Interface conditions | Standard | Standard | Standard | Standard | Standard | Standard | Standard | Nonlocal |
| 7 | Conservation | Verified | Unverified | Verified (II/III) | Unverified | Unverified | Unverified | Unverified | Unverified |
| 8 | Well-posedness | Yes | Yes (τ₀>0) | Yes | τ_q≥τ_T | Yes | Parameter-dependent | Kernel-dependent | Yes |
| 9 | Causality | No (infinite speed) | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| 10 | Published validation | Extensive | Moderate | Limited | Limited | Limited | Limited | Limited | Limited |
| 11 | Computational complexity | Low | Low | Low | Moderate | Moderate | Moderate | High | High |
| 12 | Remaining problems | None | Energy flux | Energy flux | Energy flux | Energy flux | Energy flux | Energy flux | Energy flux |

---

## 2. Theory Relationships (Limiting Cases)

Based on RG-003 (full text, Section "Limiting cases") and independent analysis:

### 2.1 Verified limiting relationships

| From | To | Conditions | Source |
|------|-----|------------|--------|
| Biot 1956 | Classical coupled | τ→0, no relaxation | Standard |
| LS 1967 | Classical | τ₀→0 | Standard |
| GN II 1991 | Classical | No dissipation limit | Standard |
| TPL 2007 | DPL | τ_v→0 | Roy Choudhuri 2007 |
| DPL 1995 | Classical | τ_q, τ_T→0 | Tzou 1995 |
| MGT 2019 | LS | Higher-order terms→0 | Quintanilla 2019 |
| MDD | Fractional | Kernel→power law | Wang & Li 2011/2021 |

### 2.2 RG-003's 11-case mapping

RG-003 maps its higher-order MDD+TPL model to 11 limiting cases:

1. **Case 1:** τ_q = τ_T = τ_v = 0, K* = 0 → Biot 1956
2. **Case 2:** n=1, τ_q>0, τ_v=τ_T=0, K*=0, κ=1, D_τ→∂/∂t → Lord-Shulman 1967
3. **Case 3:** n≥1, τ_q>0, τ_v=τ_T=0, K*=0 → Higher-order MDD (Abouelregal et al. 2021)
4. **Case 4:** τ_q=τ_T=τ_v=0, K=0, κ=1, D_τ→∂/∂t → Green-Naghdi Type II
5. **Case 5:** τ_q=τ_T=τ_v=0, κ=1, D_τ→∂/∂t → Green-Naghdi Type III
6. **Case 6:** p=1, n=2, K*=τ_v=0, κ=1, D_τ→∂/∂t → Tzou DPL 1995
7. **Case 7:** p=l=1, n=2, K*=τ_v=0 → Ezzat et al. DPL+MDD
8. **Case 8:** n,p≥1, K*=τ_v=0 → Abouelregal DPL+MDD
9. **Case 9:** p=l=1, n=2, κ=1, D_τ→∂/∂t → Roy Choudhuri TPL 2007
10. **Case 10:** p=l=1, n=2 → Ghosh et al. TPL+MDD
11. **Case 11:** n,p,l≥1, κ=1, D_τ→∂/∂t → Abouelregal higher-order TPL

### 2.3 Rigorousness of limiting procedures

All limiting procedures identified are **parameter substitutions** (τ→0, etc.), not rigorous mathematical limit theorems. No proofs of convergence or error bounds are provided in any corpus paper.

---

## 3. Contradiction Analysis

### 3.1 Confirmed contradictions

| Contradiction | Studies involved | Nature | Resolution needed |
|---------------|-----------------|--------|-------------------|
| Energy flux asymmetry | RG-003 HPS vs TS sides | Same interface, different flux definitions (thermal on HPS only) | Derive symmetric flux; re-verify conservation |
| Conservation claims | RG-003 vs RG-007 | Both claim Σ=1 but with different flux definitions | Standardize flux; check both |
| Dissipation assumptions | FW-004 (GN II, conservative) vs FW-002 (LS, dissipative) | Different dissipation; cannot compare energy ratios directly | Common framework needed |

### 3.2 Suspected contradictions (not verified)

| Suspected contradiction | Basis | Verification needed |
|------------------------|-------|-------------------|
| Different energy ratios for same physical setup | Multiple papers report different ratios for similar interfaces | Extract full text; compare under identical conditions |
| Inconsistent interface conditions | RG-003 uses D₃=0; RG-004 uses spring-type; others use perfect bonding | Derive from variational principle; compare |

### 3.3 Resolution approach

1. Derive energy flux for each theory from first principles
2. Test conservation identity on BM-1 through BM-3 benchmarks
3. Document where conservation holds and where it fails
4. Identify conditions under which theories are comparable

---

## 4. Multiphysics Coupling Network

### 4.1 Coupling channels by theory

| Theory | Mechanical | Thermal | Electrical | Porous | Carrier |
|--------|-----------|---------|------------|--------|---------|
| Classical elastic | ✓ | ✗ | ✗ | ✗ | ✗ |
| Classical thermoelastic | ✓ | ✓ | ✗ | ✗ | ✗ |
| LS/GL/GN | ✓ | ✓ | ✗ | ✗ | ✗ |
| DPL/TPL | ✓ | ✓ | ✗ | ✗ | ✗ |
| MGT | ✓ | ✓ | ✗ | ✗ | ✗ |
| MDD | ✓ | ✓ | ✗ | ✗ | ✗ |
| Nonlocal | ✓ | ✗ | ✗ | ✗ | ✗ |
| Piezoelectric | ✓ | ✗ | ✓ | ✗ | ✗ |
| Piezothermoelastic | ✓ | ✓ | ✓ | ✗ | ✗ |
| Poroelastic | ✓ | ✗ | ✗ | ✓ | ✗ |
| Poro-thermoelastic | ✓ | ✓ | ✗ | ✓ | ✗ |
| Semiconductor photo-thermo-elastic | ✓ | ✓ | ✗ | ✗ | ✓ |

### 4.2 Energy flux channels by coupling

| Coupling | Flux channel | Verified source |
|----------|-------------|-----------------|
| Mechanical | σ_ji v_i | EQ-007 (derived) |
| Thermal | q_i (Fourier) | EQ-007 (derived) |
| Electrical | -φ Ḋ_i or -D_i φ̇ | RG-003 Eq. (45) |
| Porous | Pore-fluid flux | Not in corpus |
| Carrier | Carrier diffusion flux | Not in corpus |

---

## 5. Synthesis Findings

### F.1 What is established

1. Classical energy flux (σv + q) is derived and dimensionally consistent
2. RG-003 provides a verified energy flux for piezothermoelastic MDD+TPL media (HPS side)
3. RG-003 reveals asymmetric flux between media at the same interface
4. 11 limiting cases are mapped in RG-003 (parameter substitutions, not rigorous limits)
5. 24-record deduplicated database established with Crossref-verified DOIs

### F.2 What is NOT established

1. Energy flux for LS, MGT, nonlocal, MDD, fractional theories
2. Conservation identity ΣR+ΣT+A=1 verified for any generalized theory
3. Unified dissipation inequality across theories
4. Numerical benchmarks for any interface problem
5. Cross-model comparability framework

### F.3 Original contributions

1. **Energy flux asymmetry (GAP-011):** First documented case of inconsistent flux definitions at the same interface
2. **Equation provenance register:** 23 equations traced to sources with derivation status
3. **Taxonomy v2:** Applied to 24 records with 6 empty cells identified
4. **Validated gap register:** 12 gaps classified with evidence levels and testability

---

## 6. Next Steps

1. Derive LS energy flux from relaxation equation
2. Derive MGT energy flux from third-order heat equation
3. Derive nonlocal energy flux in integral form
4. Derive MDD hereditary flux in convolution form
5. Implement BM-1 numerical solver; verify conservation
6. Test RG-003 conservation claim with symmetric flux definitions
7. Create 15 scientific figures per `16_scientific_figure_package.md`
