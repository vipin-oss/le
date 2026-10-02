# AUDIT — pre-manuscript (MASTER_PROMPT §49, §70–71) · 2026-10-01

Question: are model, verification, convergence, baselines/ablations, production results and the central story stable enough to write the manuscript? Format: PASS / PARTIAL / FAIL / ACTION REQUIRED. Self-audit, not peer review (§84).

| Gate | Status | Evidence / remark |
|---|---|---|
| Model and admissibility | PASS | `04_Theory/FORMULATION_ADDENDUM.md`; U0, U1, U3, V3–V5, V12 |
| Verification | PASS | 26 PASS, 1 FAIL (V0 on the handoff grid family, explained; V0b on production grids PASS), 1 exploratory; test power shown for the rotation bug |
| Physical validation | APPLICABLE — EVIDENCE_UNAVAILABLE | no experiment; every claim restricted to the verified continuum model |
| Convergence / uncertainty | PASS | radial and angular families; amplitude uncertainty 1.3 percentage points; circle converged to 0.03%; inversion plan independent (3e-10); outer radius insensitive (≤ 0.3% peak) |
| Baselines / ablations | PASS | Fourier, CV, MCV3, quasi-static, feedback off, isotropic control, K/C/α ablations, expansion set, pulse width |
| Production | PASS | 150 runs (141 gate + 9 block F), all RUN_SUCCESS, provenance table |
| Central story | PASS | `00_Project_Control/CENTRAL_STORY.md` |

## Claims that the manuscript may make (claim → evidence → limit)
1. Single-pulse response by Bromwich inversion is verified → U4–U8, V9d, V11 → undamped linear model, window t ≤ 14.5 t_th.
2. Circle peak orientation-invariant to round-off, 0.854 MPa/K → T1 (4.6e-15), radial extrapolation → parameters as in Table 1 (α-dependent scale).
3. Ellipse orientation modulation ≈ 29% (28.7% extrapolated; 29.9% on M; u_num 1.3 pp) → T4 RESOLVABLE → one cavity shape (axis ratio 2), a = 10 nm, Fourier conduction, plane strain.
4. Modulation arises from competing expansion and stiffness anisotropy; conductivity anisotropy minor → block E (exploratory, 96×48, six orientations).
5. Thermal memory: D ≤ 6.4% (≤ 1.6% for a ≥ 10 nm), peak shift ≤ 1.4%; quasi-static collapse exact; dynamic residual 52% from O(ε²) inertia → blocks B/BQS/B2 → circular cavity only; τ hypothetical.
6. Feedback below 5δ → T3 → probe-based (wall temperature is Dirichlet).
7. Stress scale uncertain by a factor ≈ 16 between two expansion sets; modulation unchanged → block E1 (sensitivity-only set constructed from an abstract-level statement).

## Claims removed or limited relative to the handoff / my earlier hypotheses
- "Locality explains the ellipse orientation modulation": **not supported** — the pulse-width test (A₂ 24.8–32.0%) leaves the thin-layer limit untested; the manuscript states a non-local interaction of the heated region with the cavity shape.
- "(Λ, ε) two-parameter map" as a finding: replaced by D = D_QS(Λ) + O(ε²).
- Absolute stresses, "33–37%" and the handoff numbers: superseded (CORRECTIONS_LOG).
- Any statement of validity of Fourier/CV conduction at 5–50 nm: not made.

## Open items before submission (user-owned)
Authors, affiliations, CRediT, funding, competing interests; confirmation/edit of the AI-use declaration; public repository + licence + DOI; journal decision (IJHMT vs alternatives, `JOURNAL_FIT.md`); JCR verification; independent expert review; privacy decision on the public GitHub repository holding unpublished manuscripts.
