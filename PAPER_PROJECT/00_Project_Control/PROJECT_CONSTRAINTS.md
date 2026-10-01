# PROJECT_CONSTRAINTS — Phase 0 (2026-10-01)

## 1. Governing protocol
- MASTER_PROMPT v2.1 (§0–90), user-supplied. Priority order (§2): correctness > admissibility > evidence > verification > validation > significance > novelty > numerical robustness > reproducibility > journal fit > presentation.
- User control (§88): final research direction, major scientific assumptions, production-compute approval, major methodological changes, final journal, submission. None of these may be decided silently.

## 2. Authorization state
| Item | State |
|---|---|
| This session — Phase 0 | Started without an explicit phase instruction: the user pasted the prompt twice and skipped my phase-choice question. Treated as authorization for Phase 0 ONLY (P0-D001). Revocable. |
| This session — Phase ≥ 1 | **NOT authorized.** |
| Earlier approvals recorded in the handoff | D009 bounded pilot (Huang-2025 source case). D012 pragmatic directive ("full validation kabhi nahi hoga; limiting cases + source-jaisi curves; source galat ho to honestly document"). **D013 blanket authorization to proceed through phases 1→13 for the β-Ga₂O₃ cavity direction without repeated approval requests** — user-owned exceptions: compute > 4 CPU-h / 1 GPU-h / 5 GB, first-principle method changes, journal selection, final submission. D017 journal selection (IJHMT primary, MDSM fallback) on "yes go ahead". |
| D013 carry-over | **Not assumed.** It was given to a previous agent session. One-line user confirmation needed. |
| Working style observed | The user dislikes repeated questions and has skipped ask_user prompts several times (D013, D016, D017). → Ask only about user-owned decisions; batch questions; offer copy-pasteable one-line choices. |

## 3. Compute constraints
- Thresholds (§43; no `RESEARCH_PROFILE.md`, so defaults apply): production compute needs explicit approval if the estimate exceeds 4 CPU-hours, 1 GPU-hour or 5 GB generated data.
- Sandbox available to me: 2 vCPU (Xeon 2.60 GHz), 1,984 MB RAM, ≈20 GB free disk, no GPU (`TOOL_AVAILABILITY.md`). The user's own hardware: UNKNOWN.
- Recorded cost of the existing pipeline (handoff `COMPUTE_STATUS.md`, 2026-09-30): V0–V7 re-run 403 CPU-s; production 38 runs 1,039 CPU-s (≈13–17 s per run at 96×48); sensitivity + 192×96 spot checks ≈250 CPU-s (≈95 s per 192×96 run); debugging ≈400 CPU-s; day total ≈0.6 CPU-h; peak memory < 2 GB.
- My review runs on 2026-10-01: CPU-seconds not logged; the review artifacts span ≈22 min of sandbox wall-clock.
- Estimate for a corrected re-run: **NOT_RUN** — to be produced at the Phase 10 production gate (§42–43). A longer synthesis window or a different transform will cost more than the original 1,039 CPU-s; no number is claimed now.
- Persistence: only files under `/home/user` are saved; snapshots are capped at ≈128 MB / 10,000 files, so per-run `.npz` outputs must stay below that.

## 4. Scientific scope constraints (carried from the handoff, with my corrections)
- Research type: computational scientific study with analytical verification anchors (`PROBLEM_DEFINITION.md` §15).
- Physical validation: the correct §14 label is **APPLICABLE — EVIDENCE_UNAVAILABLE** (handoff wording: "NOT_AVAILABLE"). No transient cavity experiments for β-Ga₂O₃ are known to the handoff. Hence no physically validated predictive claims; τ values are hypothetical; c_p ≈ 560 J/(kg·K) is estimated (band 500–700); α₅ (shear expansion) is unmeasured and set to 0.
- Continuum validity: `ASSUMPTIONS.md` assumes a phonon MFP of 1–2 nm and a continuum flag at a ≥ 5 nm. Literature seen on 2026-10-01 (abstract/snippet level, §10): a gray mean free path of a few nm, but a spectrum reaching ≈0.7–1 µm with a significant heat share near 1 µm (OSTI 1817728; Appl. Phys. Express, doi 10.35848/1882-0786/ad0ba8; arXiv 2507.14763). Fourier / Cattaneo–Vernotte for 5–50 nm cavities is therefore outside demonstrated validity → any paper must frame results as a **continuum-model parametric study**, not as predictions for real nanocavities.
- Claim gates G1–G5 (`PROJECT_STATE_PHASE_00.md` §7) must be resolved before manuscript claims that depend on them (§78, §80).

## 5. Licensing, integrity, privacy (§54)
- No PDFs are in the package; third-party PDFs must not be redistributed. The benchmark PDFs came from the user's public repo and their redistribution rights are not established.
- **Privacy flag:** `RESEARCH_READING/SOURCE_MANIFEST.json` shows the user's repo `vipin-oss/BFS-FEM-MATLAB` (public when retrieved) hosting `FEM_Total.zip` — 8 unpublished manuscripts — and this handoff holds ≈810 kB of text extracted from 7 of them. Prior public availability can affect journal originality/similarity checks. Decision (make private / remove files): the user's.
- Code licence: none stated anywhere in the handoff → UNKNOWN; choose one before any public release (§55).
- Authorship, funding, conflicts: placeholders only (`declarations.md`, `title_page.md`). The AI-use disclosure is a template the authors must review; the current IJHMT AI policy was NOT checked (UNVERIFIED).
- Independent expert review of the formulation, constitutive assumptions, major claims and manuscript is strongly recommended (§84). My review is not peer review.

## 6. Language and output constraints
- Manuscript language: English (my assumption; the user has not stated one). Chat: Hinglish.
- Formats I can produce here: `.docx` (python-docx), `.xlsx` (openpyxl), `.md`, `.html`, figures `.png`/`.svg` (matplotlib). PDF/LaTeX typesetting: not available in this sandbox (`TOOL_AVAILABILITY.md`). Target-journal template and format: UNVERIFIED until Phase 13 (§53).

## 7. Open information requests (§7 items — nothing invented)
Non-blocking for the next phase unless marked. One line each is enough.
1. Main research areas/expertise. `RESEARCH_PROFILE.md` is absent; the corpus suggests three streams (analytical wave/thermoelastic mechanics; variational higher-order FEM with BFS elements; identifiability/model discrimination) — inferred from titles and sections, NOT confirmed.
2. Existing codes to reuse (FEM4 MATLAB package known; others?).
3. Software/licences you can run (MATLAB? Python only?).
4. Your hardware (CPU/RAM/GPU). The sandbox figures are not yours.
5. Target journal/level: handoff has IJHMT primary / MDSM fallback (D017) — reconfirm or change.
6. Constraints: deadline, authors/affiliations, funding, data/code release plan.
7. Project-specific: (a) is "the paper" the β-Ga₂O₃ circular-vs-elliptical cavity study (assumed)? (b) does the D013 blanket authorization still stand? (c) privacy decision for the public repo.
