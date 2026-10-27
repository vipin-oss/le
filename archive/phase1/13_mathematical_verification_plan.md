# Mathematical Verification Plan — Phase 1

**Prepared:** 2026-10-21  
**Status:** Not started  
**Evidence standard:** `DERIVED` / `VERIFIED` / `PENDING`

---

## 1. Purpose

Independently verify key mathematical identities and limiting cases from the corpus. Distinguish:

- **Original numerical experiments** (new computations)
- **Published benchmark reproduction** (reproducing published results)
- **Symbolic analytical verification** (hand/computer algebra)
- **Hypothetical future experiments** (planned, not executed)

No planned experiment is presented as completed.

---

## 2. Benchmark Problems

### Benchmark BM-1 — Classical elastic interface (limiting case)

**Purpose:** Verify that energy ratios sum to unity in the lossless elastic limit.

| Element | Specification |
|---------|---------------|
| Governing equations | Navier equations: ρ ü_i = ∂σ_ji/∂x_j, σ_ij = λ δ_ij ε_kk + μ (ε_ij + ε_ji) |
| Interface | Perfectly bonded elastic/elastic half-spaces |
| Incident wave | P-wave at angle θ |
| Expected result | ΣR + ΣT = 1 (energy conservation) |
| Energy flux | J_n = (1/2) Re[σ_ji v_j* n_i] |
| Verification method | Symbolic derivation + numerical evaluation |
| Status | NOT STARTED |

### Benchmark BM-2 — Generalized thermoelastic interface

**Purpose:** Test energy conservation with Lord–Shulman thermal coupling.

| Element | Specification |
|---------|---------------|
| Governing equations | LS thermoelasticity (verified: DOI 10.1016/0022-5096(67)90024-5) |
| Interface | Thermoelastic/thermoelastic half-spaces, perfect bonding |
| Incident wave | Coupled P-T wave |
| Expected result | ΣR + ΣT + A = 1, where A = thermal dissipation |
| Energy flux | J_n = mechanical + thermal (total flux to be derived) |
| Verification method | Symbolic derivation |
| Status | NOT STARTED |

### Benchmark BM-3 — Piezoelectric interface

**Purpose:** Test energy conservation with electrical coupling.

| Element | Specification |
|---------|---------------|
| Governing equations | Piezoelectric elasticity (verified: D = e·ε + κ·E) |
| Interface | Piezoelectric/elastic half-spaces |
| Incident wave | Elastic P-wave |
| Expected result | ΣR + ΣT + A = 1, including electrical flux channel |
| Energy flux | J_n = mechanical + thermal + electrical |
| Verification method | Symbolic derivation |
| Status | NOT STARTED |

### Benchmark BM-4 — Nonlocal interface

**Purpose:** Test whether nonlocal energy flux can be defined at interface.

| Element | Specification |
|---------|---------------|
| Governing equations | Eringen nonlocal elasticity (verified: DOI 10.1016/0020-7225(72)90050-x) |
| Interface | Nonlocal/local elastic half-spaces |
| Expected result | Nonlocal flux requires integral form; conservation may fail locally |
| Verification method | Symbolic derivation |
| Status | NOT STARTED |

### Benchmark BM-5 — MDD interface

**Purpose:** Test whether instantaneous energy flux is meaningful in MDD media.

| Element | Specification |
|---------|---------------|
| Governing equations | MDD heat conduction (verified: DOI 10.1016/j.camwa.2011.04.028) |
| Interface | MDD thermoelastic/elastic half-spaces |
| Expected result | Hereditary (convolution) flux required |
| Verification method | Symbolic derivation |
| Status | NOT STARTED |

---

## 3. Verification Methods

| Method | Description | Tools | Status |
|--------|-------------|-------|--------|
| Symbolic derivation | Hand/computer algebra of balance laws | SymPy, Mathematica (planned) | NOT STARTED |
| Numerical evaluation | Compute fluxes for benchmark parameters | Python/NumPy (planned) | NOT STARTED |
| Conservation check | Verify ΣR + ΣT + A = 1 within tolerance | Python (planned) | NOT STARTED |
| Limiting-case check | Verify classical limits recovered | Symbolic | NOT STARTED |

---

## 4. Verification Criteria

A derivation is considered verified when:

1. All steps are documented and reproducible
2. Dimensional consistency is checked
3. Classical limits are recovered
4. Conservation holds (or the failure mode is identified)
5. Results are independent of arbitrary normalization

---

## 5. What Is NOT Part of This Plan

- Full-text systematic review of all 49 corpus papers (too large for manual verification)
- Experimental validation (no experimental capability in this sandbox)
- Finite-element implementation (beyond current scope; planned as future work)
- Pooled statistical analysis (literature unsuitable for meta-analysis)

---

## 6. Deliverables

- `mathematics/derivations/` — symbolic derivations (text/LaTeX)
- `mathematics/symbolic_checks/` — computer algebra verification scripts
- `mathematics/benchmarks/` — benchmark specifications and results

All derivations must trace to verified sources (DOIs in `source_verification_log.csv`).