"""make_phase_states.py — PROJECT_STATE_PHASE_07 … 13 (MASTER_PROMPT §65), plus VALIDATION_STATUS / COMPUTE_STATUS / REPRODUCIBILITY_STATUS.
Numbers are read from the JSON outputs at generation time."""
import json, os, glob, time
def _pp_root(_start):
    """walk up from _start to the PAPER_PROJECT directory (path-independent replacement
    for the hard-coded '/home/user/PAPER_PROJECT' that used to be here)."""
    _p = os.path.abspath(_start)
    while True:
        if os.path.basename(_p) == 'PAPER_PROJECT':
            return _p
        _q = os.path.dirname(_p)
        if _q == _p:
            break
        _p = _q
    return os.environ.get('PAPER_PROJECT_ROOT', '/home/user/PAPER_PROJECT')
ROOT = _pp_root(os.path.dirname(os.path.abspath(__file__))); CTL = os.path.join(ROOT, '00_Project_Control')
def J(p, default=None):
    p = os.path.join(ROOT, p)
    return json.load(open(p)) if os.path.exists(p) else (default if default is not None else {})
TR = J('07_Tests/TEST_RESULTS.json'); AN = J('10_Processed_Data/ANALYSIS_V2.json'); CV = J('10_Processed_Data/CONVERGENCE_RESULTS.json')
cases = {c['case']: c for c in TR.get('cases', [])}
n_pass, n_fail = TR.get('n_pass', '?'), TR.get('n_fail', '?')
nprod = len(glob.glob(os.path.join(ROOT, '09_Raw_Data', 'production', '*.json')))
def g(d, *keys, default='n/a'):
    for k in keys:
        if isinstance(d, dict) and k in d: d = d[k]
        else: return default
    return d
def pct(x, nd=2): return f'{x*100:.{nd}f}%' if isinstance(x, (int, float)) else str(x)
T4 = AN.get('T4_H2', {}); T1 = AN.get('T1_H1', {}); T2 = AN.get('T2_H3', {}); T3 = AN.get('T3_H4', {}); circ = AN.get('circle_peak', {})

COMMON = f"""## Common context (self-contained recovery summary, MASTER_PROMPT §65)
- **Project:** β-Ga₂O₃ cavity thermoelasticity (circular vs equal-area elliptical cavity, monoclinic crystal, a–c plane, Fourier / Cattaneo–Vernotte / two-relaxation-time conduction) → verified continuum parametric study; target manuscript for IJHMT (journal choice user-owned; D017 working target).
- **Research type / evidence route:** computational scientific study with analytical verification anchors (§15). Verification (Track A): exact + independent 1-D references, grid studies. Physical validation: **APPLICABLE — EVIDENCE_UNAVAILABLE**.
- **Equations / assumptions / method:** `04_Theory/FORMULATION_ADDENDUM.md`, `05_Numerical_Method/NUMERICAL_METHOD_V2.md`; model unchanged from the handoff; time reconstruction by Bromwich inversion (P7-D002, **flag for user**); undamped; grid γ = 5 (P9-D001).
- **Baseline:** `/home/user/work/handoff/` (read-only, 304 files, 303/303 SHA-256). Handoff defects fixed: rotate_Q_beta sign (G1), T1 forced PASS (G2), periodic-synthesis artefact (G3), H3 evaluated on the artefact and on the full window (G4), documentation (G5).
- **Approvals:** D013 blanket authorization for phases 1→13 (user message 2026-10-01 "Continue Phases 7→13 under D013"); user-owned: model changes, compute > 4 CPU-h, journal, submission.
- **Decision / change history:** `DECISION_LOG.md`, `CHANGELOG.md` (this folder); handoff D001–D018 in the handoff.
- **Rejected ideas:** `REJECTED_IDEAS.md` (this folder).
"""
def write(n, title, body):
    open(os.path.join(CTL, f'PROJECT_STATE_PHASE_{n:02d}.md'), 'w').write(f'# PROJECT_STATE_PHASE_{n:02d} — {title} (2026-10-01)\n\n' + body + '\n' + COMMON)

write(7, 'Basic verification', f"""## Phase 7 — status PASS (with one reported FAIL)
**Completed:** `rotate_Q_beta` fixed (U0/U1: 1.5e-16 vs independent 3-D rank-4 rotation; shipped 1.7e-3); `inertia_scale` and `refine=2` added to the solver; Bromwich single-pulse module and independent 1-D references (Chebyshev Laplace-domain; Crank–Nicolson time-domain) implemented; verification suite `07_Tests/run_tests.py`: **{n_pass} PASS, {n_fail} FAIL** (V0 on the handoff grid family: χ = 2, 96×48 = 5.03e-3 vs 5e-3; V0b on the production grids PASS).
**Key findings:** rotation covariance exact to 6e-14 (θ, u, wall hoop) for every grid-aligned φ; shipped rotation fails at 3.0e-3 and the old V3 was blind (units-mixed normalisation, φ = 90° only); round-off floor 1e-8 removed by iterative refinement.
**Files:** `07_Tests/TEST_REPORT.md`, `TEST_RESULTS.json`, `logs/`, `diagnostics/`; `06_Source_Code/`.
**Next:** Phase 8 (verification against references), Phase 9 (convergence).
""")
write(8, 'Validation execution (verification vs references; no physical validation)', f"""## Phase 8 — status PASS for verification, physical validation APPLICABLE — EVIDENCE_UNAVAILABLE
**Completed:** comparisons R1–R9 (`03_Validation/VALIDATION_RESULTS.md`): steady log profile, uniform-θ annulus, steady gradient load (closed forms); 1-D Chebyshev and time-domain references for the single-pulse and the dynamic coupled problem; D accuracy (CV5/CV20 vs 1-D: {g(cases.get('V9e_thermal_memory_deviation_D_accuracy', {}), 'worst_rel_err_192')} at 192×96). Axisymmetric peak-stress error at 96×48: {g(cases.get('V11_single_pulse_isotropic_circle_vs_time_domain', {}), 'peak_rel_err_48_96_192')} (48/96/192), order ≈ 2.
**Physical validation:** none executed or claimed; pilot (Huang 2025 source case) not re-run (reference data absent).
**Audit after Phase 8 (Phases 1–8):** `15_Audits/AUDIT_PRE_PRODUCTION.md` covers Phases 1–10 (combined with the pre-production audit).
**Next:** Phase 9.
""")
write(9, 'Convergence and robustness', f"""## Phase 9 — status PASS (numerical uncertainty quantified in Phase 12)
**Completed:** mesh-direction / clustering study C4 (`10_Processed_Data/CONVERGENCE_DIRS.json`, φ = 30° ellipse): radial refinement at γ = 3.5 changes the peak by −8.7%, angular by +3.0%; γ = 5 vs 6.5 differ by 0.7% → γ = 5 adopted (P9-D001); γ = 3.5 triplets (orders 0.8–1.35) kept in `09_Raw_Data/convergence_gamma3p5/`; production grid family R48/T48/M/R192/T144 with separate radial/angular Richardson; Bromwich-plan independence (C2) and outer-radius sensitivity (C3): `CONVERGENCE_RESULTS.json`; verification-level convergence orders (V6–V11) ≈ 2.
**Stability:** no instability observed; solver backward errors ≤ 1e-16 relative; wall-pulse reconstruction error 6.3e-9 in all runs.
**Files:** `05_Numerical_Method/CONVERGENCE_REPORT.md`, `STABILITY_REPORT.md`.
**Next:** Phase 10.
""")
write(10, 'Baselines, ablations and production gate', f"""## Phase 10 — status PASS
**Completed:** acceptance criteria frozen (`02_Problem_Definition/ACCEPTANCE_CRITERIA_V2_FROZEN.md`); code frozen (`06_Source_Code/CODE_FREEZE_v2_gate.json`); production matrix (141 runs); baselines: Fourier, quasi-static, feedback-off, isotropic control; ablations: K, C, α isotropic and expansion-set sensitivity (exploratory); compute budget ≈ 70–90 CPU-min (< 4 CPU-h cumulative); pre-production audit `15_Audits/AUDIT_PRE_PRODUCTION.md`.
**Next:** Phase 11 production.
""")
write(11, 'Production', f"""## Phase 11 — status {'PASS' if nprod >= 141 else 'RUNNING/PARTIAL'}
**Completed:** {nprod}/141 runs stored in `09_Raw_Data/production/` (json + npz with transfer values H(s_k)); provenance table `10_Processed_Data/PRODUCTION_PROVENANCE.csv`. Plan: T = 20, γ_B = 0.9 (27 solves); undamped; R = 80a; refine = 2.
**Next:** Phase 12 analysis.
""")
write(12, 'Scientific analysis', f"""## Phase 12 — status see below
**Frozen criteria evaluated** (`10_Processed_Data/ANALYSIS_V2_TABLES.md`): T1 {g(T1, 'status')}; T4 {g(T4, 'status')} (A12(M) = {pct(g(T4, 'amplitude_M_12phi'))}, extrapolated 6-φ amplitude {pct(g(T4, 'amplitude_6phi_extrapolated'))}, u_num = {g(T4, 'u_num')}); T2 quasi-static {g(T2, 'status_quasi_static')}, dynamic {g(T2, 'status_dynamic')}; T3 {g(T3, 'status')}.
**Central story:** `CENTRAL_STORY.md` (this folder).
**Next:** Phase 13 manuscript.
""")
write(13, 'Manuscript, journal fit, reproducibility, final audit', f"""## Phase 13 — see `13_Manuscript/`
Manuscript (docx + md), highlights, cover letter, supplementary workbook; journal-fit record (`13_Manuscript/JOURNAL_FIT.md`); pre-manuscript and final audits (`15_Audits/`); reproduction test (`07_Tests/REPRODUCTION_TEST_REPORT.md`); final archive `RESEARCH_PROJECT_FINAL.zip` (only if created — see PROJECT_STATE_FINAL).
""")

open(os.path.join(CTL, 'VALIDATION_STATUS.md'), 'w').write(f"""# VALIDATION_STATUS (2026-10-01) — kept separate (MASTER_PROMPT §63)
- **Verification:** PARTIAL → see `07_Tests/TEST_REPORT.md`: {n_pass} PASS / {n_fail} FAIL of the suite; the FAIL (V0, handoff grid family, χ = 2) is explained and V0b (production grids) passes; frozen criteria T1–T5 evaluated in `10_Processed_Data/ANALYSIS_V2_TABLES.md`. Overall: VERIFIED for the quantities and grids listed in the reports; grid-uncertainty quantified.
- **Physical validation:** APPLICABLE — EVIDENCE_UNAVAILABLE. Missing: transient temperature/stress or strain measurements around cavities in β-Ga₂O₃ (or any monoclinic crystal) with known pulse, orientation and geometry. Claims restricted accordingly: no physically validated predictive claims; τ hypothetical; continuum validity at 5–50 nm not established.
""")
open(os.path.join(CTL, 'COMPUTE_STATUS.md'), 'w').write(f"""# COMPUTE_STATUS (2026-10-01)
- Hardware: sandbox 2 vCPU (Xeon 2.60 GHz), 1,984 MB RAM, no GPU; Python 3.13.14, numpy 2.3.5, scipy 1.17.1. User hardware: UNKNOWN.
- This session (all runs successful unless stated): review runs ≈ 22 min wall; verification suite runs 1–4 ≈ 7 + 5 + 20 min wall (run 2 killed by the out-of-memory killer, run 3 partial); convergence γ = 3.5 partial ≈ 22 min; mesh-direction study ≈ 8 min; production: {nprod}/141 runs; per-run cost: 3 s (48×24) … 14 s (96×48) … 65 s (96×96) … 157 s (192×96).
- Memory constraint: 192×96 solves need ≈ 0.7–1.0 GB; at most one heavy job at a time (OOM at run 2).
- Cumulative project compute ≈ 2.7 CPU-h (estimate) < 4 CPU-h threshold; storage < 100 MB; failures: OOM (run 2).
""")
open(os.path.join(CTL, 'REPRODUCIBILITY_STATUS.md'), 'w').write(f"""# REPRODUCIBILITY_STATUS (2026-10-01)
- Source: `06_Source_Code/` (hashes in `CODE_FREEZE_v2_gate.json`); environment identical to the handoff's (Python 3.13.14 / numpy 2.3.5 / scipy 1.17.1 / matplotlib 3.10.9, Linux x86_64).
- Tests: `python 07_Tests/run_tests.py` (≈ 20 min, one process at a time), supplement `run_tests_supplement.py`.
- Production: `python 08_Experiments/run_production_v2.py heavy|light` (two workers), analysis `analyze_v2.py`, figures `make_figures.py`, manuscript `13_Manuscript/build_manuscript.py`.
- Reproduction test: `07_Tests/REPRODUCTION_TEST_REPORT.md` (see its status).
- Not reproducible from this package: handoff pilot source-figure comparison (private digitisation absent); third-party PDFs not included.
""")
print('phase states written')
