# PROJECT_PROGRESS — `vipin-oss/le`

Branch: `arena/01a0f67f-le` · updated 2026-10-01 · source archive: `le.zip` (52,189,612 B,
sha256 `5e780e1fd6292690c1b56ad378dc35c9737e52cd873e4f18e610cfdf45bb0363`)

Full audit: **[`docs/PHASE1_AUDIT.md`](docs/PHASE1_AUDIT.md)**.

---

## What this project is

`PAPER_PROJECT` — *"verified continuum study of cavity thermoelasticity in monoclinic β-Ga₂O₃"*,
run under **MASTER_PROMPT v2.1** (90 sections). Transient coupled thermoelasticity around a
circular vs equal-area elliptical cavity (χ = 2) in the a–c plane of monoclinic β-Ga₂O₃;
Fourier / Lord–Shulman / two-relaxation-time conduction; frequency-domain mapped-grid FD solver +
**Bromwich inversion** for the single-pulse response; target journal IJHMT (user-owned).
`work/handoff/` = read-only input baseline (verified 303/303), `work/rerun/` = prior review area.

---

## Completed phases

| Phase | Status |
|---|---|
| **PHASE 1 — Repository audit** | **COMPLETE** (this file + `docs/PHASE1_AUDIT.md`) |
| Phase 0 (intake) | PARTIAL — done upstream; user profile info deliberately not invented |
| Phases 1–6 | deliberately NOT re-opened upstream (superseded by 04_Theory / 05_Numerical_Method) |
| Phases 7–12 | PASS upstream — verification (26 PASS/1 FAIL), R1–R9, convergence, gate, 150 production runs, analysis |
| Phase 13 | PARTIAL upstream — manuscript + audits + reproduction test (11 PASS) done; **final packaging not done** |

## Current phase

**PHASE 2 (consistency check) → then finish the Phase-13 tail (final packaging).**

## Files created / modified in this session

| File | Action |
|---|---|
| `docs/PHASE1_AUDIT.md` | created — full Phase-1 audit of the real project (replaces the earlier "empty repo" audit) |
| `PROJECT_PROGRESS.md` | created/rewritten — this record |
| `.gitignore` | created — excludes `work/handoff.zip` (redundant with verified `work/handoff/`), `PAPER_PROJECT/packages/` (regenerable via `make_packages.py`), `__pycache__/` |
| `PAPER_PROJECT/**`, `work/**` | **added unmodified** — extracted verbatim from `le.zip` |

## Tests performed (this session, all read-only)

| Test | Result |
|---|---|
| `le.zip` integrity (`git hash-object` vs blob id `297f5dcb`) | PASS — byte-exact |
| Handoff baseline vs `work/handoff/MANIFEST_SHA256.json` | **303 OK / 0 missing / 0 mismatch** |
| Production run count | 150 json + 150 npz (= 141 gate + 9 block F) PASS |
| `TEST_RESULTS.json` vs TEST_REPORT/VALIDATION_STATUS | 26 PASS / 1 FAIL, 28 cases PASS |
| Reproduction test record | 11 PASS / 0 FAIL PASS |
| `MANUSCRIPT_STATS.json` vs IJHMT limits (≤250-word abstract, ≤85-char highlights) | 231 words; 78/84/70/76/77 PASS |
| `amp_best` (manuscript 28.7% modulation) vs `ANALYSIS_V2.json` | 0.287495 PASS |
| Figure / table counts | 8 png / 5 csv PASS |
| Abstract "0.08% at the finest grid" vs `TEST_RESULTS.json` | consistent (V9d worst-law 192×96 = 0.08%; V11 = 0.07%) |
| `CODE_FREEZE_v2_gate.json` vs current files | 10 match / **5 mismatch** — all expected (documented block-F + P12-D001 additive changes) |
| `CODE_FREEZE_v2_blockF.json` vs current files | 21 match / **3 mismatch** — `13_Manuscript/{build_manuscript,ms_results,ms_static}.py` edited after the last freeze, no addendum |

## Validation status (inherited)

- **Verification:** VERIFIED for the quantities/grids listed in `07_Tests/TEST_REPORT.md` and
  `03_Validation/VALIDATION_RESULTS.md`; grid uncertainty quantified (u_num = 1.31 pp on the
  28.7% ellipse modulation). Independent references: 1-D Chebyshev (Laplace domain) and
  Crank–Nicolson (time domain) — no shared code with the 2-D solver.
- **Physical validation:** **APPLICABLE — EVIDENCE_UNAVAILABLE.** No experimental data exist;
  every claim is restricted accordingly in the manuscript.
- **Not yet done by me:** no re-computation yet (numpy/scipy/matplotlib/python-docx/openpyxl are
  not installed in this sandbox; PyPI is reachable). Phase 4 validation will install them and
  re-run the reproduction test (`08_Experiments/reproduce.py`).

## Unresolved issues

1. **Pending deliverables:** `packages/PACKAGE_PHASE_07…13.zip`, `PROJECT_STATE_FINAL.md`,
   `packages/RESEARCH_PROJECT_FINAL.zip` — none exist yet.
2. **P7-D002** (periodic-DFT synthesis → Bromwich inversion) is explicitly
   **FLAGGED FOR USER CONFIRMATION** and has not been confirmed.
3. Post-freeze edits to 3 manuscript builder scripts are undocumented (no freeze addendum).
4. 15 scripts hard-code `/home/user/PAPER_PROJECT` and `/home/user/work/handoff`, which do not
   exist in this checkout → must be resolved (symlink, not patching frozen files) before any run.
5. Sandbox has Python 3.11.2 and no scientific stack; recorded environment is Python 3.13.14 /
   numpy 2.3.5 / scipy 1.17.1 / matplotlib 3.10.9 → reproduction is allowed to differ bitwise
   (MP §75) but the version gap must be stated.
6. §74 items belonging to the non-re-opened phases (`RESEARCH_PROFILE.md`,
   `SCIENTIFIC_ACCEPTANCE_PLAN.md`, `NOVELTY_MATRIX.xlsx`) are absent — user decision, not to be
   invented.
7. User-owned open items: authors/affiliations/CRediT/funding/conflicts, AI-use declaration,
   repository DOI + licence, final journal, JCR verification, independent expert review.

## Exact next action

1. Create the compatibility symlinks `/home/user/PAPER_PROJECT → /home/user/le/PAPER_PROJECT`
   and `/home/user/work → /home/user/le/work` so the frozen scripts run unchanged (no file edits,
   so all code-freeze hashes stay valid).
2. Install the Python stack and run the **reproduction test** `08_Experiments/reproduce.py`
   (Phase 2/4) to confirm the delivered results reproduce in this environment.
3. Fix/document the 3 post-freeze manuscript-script changes (add `CODE_FREEZE_v2_final.json`
   addendum rather than reverting — the edits are the CORRECTIONS_LOG corrections).
4. Build the pending deliverables: `PROJECT_STATE_FINAL.md`, `PACKAGE_PHASE_07…13.zip`,
   `RESEARCH_PROJECT_FINAL.zip`; update `README.md`, `CHANGELOG.md`, `DECISION_LOG.md`.
5. Report the P7-D002 flag and the user-owned open items to the user.
