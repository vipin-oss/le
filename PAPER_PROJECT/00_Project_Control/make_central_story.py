"""make_central_story.py — CENTRAL_STORY.md (MASTER_PROMPT §47) with numbers from ANALYSIS_V2.json."""
import json, os
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
ROOT = _pp_root(os.path.dirname(os.path.abspath(__file__)))
def J(p):
    p = os.path.join(ROOT, p); return json.load(open(p)) if os.path.exists(p) else {}
AN = J('10_Processed_Data/ANALYSIS_V2.json'); CR = J('10_Processed_Data/CONVERGENCE_RESULTS.json')
T1, T2, T3, T4, circ, E, F = AN.get('T1_H1', {}), AN.get('T2_H3', {}), AN.get('T3_H4', {}), AN.get('T4_H2', {}), AN.get('circle_peak', {}), AN.get('E_ablations', {}), (AN.get('F_locality', {}) or {}).get('rows', [])
def pc(x, nd=1): return f'{100*x:.{nd}f}%' if x is not None else 'n/a'
def mp(x): return f'{abs(x)/1e6:.3f}' if x is not None else 'n/a'
def sci(x): return f'{x:.1e}' if x is not None else 'n/a'
a6 = T4.get('extrapolated_6phi', {}); pq = T2.get('pair_QS') or {}; pd_ = T2.get('pair_dynamic') or {}
dyn = [r for r in T2.get('dynamic', []) if r['model'] == 'CV']; dmax = max([r['D'] for r in dyn + [r for r in T2.get('quasi_static', []) if r['model'] == 'CV']] or [float('nan')])
base = E.get('baseline_6phi', {}).get('amplitude')
abl = {k: (E[k]['amplitude'] / base if base else None) for k in ('E3_K_iso', 'E4_C_iso', 'E2_alpha_iso', 'E1_alpha_cheng298') if k in E}
L = ['# CENTRAL_STORY (MASTER_PROMPT §47) — 2026-10-01', '',
 '1. **Problem.** How do crystal orientation, cavity shape and heat-conduction law (Fourier vs relaxation-time) interact in the transient thermoelastic stress around a cavity in a low-symmetry crystal (monoclinic β-Ga₂O₃, plane strain in the a–c plane)?',
 '2. **Existing limitation.** Cavity studies with finite heat-wave speed treat isotropic or highly symmetric media and circular/spherical geometry; studies of general anisotropy and non-circular holes are steady/quasi-static (bounded search, PROVISIONAL). In addition, the preliminary internal analysis from which this work started contained a rotation-tensor sign error, a periodic-pulse-train synthesis and an under-resolved wall mesh, so none of its numbers could be used.',
 f"3. **Proposed solution.** A verified computational study: frequency-domain mapped-grid solver evaluated at complex frequency; single-pulse response by Bromwich inversion (verified against exact/independent solutions); mesh-direction study and Richardson uncertainty; ablations (isotropic K, C, α; expansion set; quasi-static; feedback off; pulse width).",
 f"4. **Scientific mechanism.** The peak wall stress is, to ≈ 10⁻³ in the far-field term, a local–instantaneous constraint response (isotropic Lamé closed form). The circle peak is orientation-invariant ({sci(T1.get('M_sig_nodal', {}).get('spread_rel'))}); the ellipse breaks locality (iso ellipse ≈ 1.5× iso circle) and its orientation modulation depends only weakly on the heated-layer thickness (pulse-width test) — a non-local interaction of the heated region with the cavity shape; the thin-layer limit is not reached. Thermal memory enters the wall stress only through the weak far-field term; in the quasi-static uncoupled limit D depends on Λ alone (exact scaling).",
 f"5. **Main evidence.** Circle peak {mp(circ.get('radial_interp', {}).get('f_ext'))} MPa/K (extrapolated); ellipse modulation {pc(a6.get('amplitude'))} (six-orientation, extrapolated; grid M 12 φ: {pc(T4.get('amplitude_M_12phi'))}; u_num {pc(T4.get('u_num'), 2)}; T4 {T4.get('status')}); D ≤ {pc(dmax, 2)}; quasi-static equal-Λ residual {pc(pq.get('residual'), 4)} ({T2.get('status_quasi_static')}), dynamic residual {pc(pd_.get('residual'), 1)} ({T2.get('status_dynamic')}); feedback {T3.get('status')}; ablation ratios (amplitude / baseline): {', '.join(f'{k.split(chr(95))[1] if False else k}={round(v, 2)}' for k, v in abl.items() if v)}; pulse-width test A₂ = {[pc(r['A2'], 1) for r in F]} for t_w = {[r['tw'] for r in F]}.",
 f"6. **Main finding.** Crystal orientation matters for the stress around a non-circular cavity (≈ {pc(a6.get('amplitude'), 0)} modulation of the peak wall stress for an axis ratio of 2) but not for a circular one; the heat-conduction law has a bounded, small effect (≤ {pc(dmax, 1)}) on this observable. Absolute stress scale is parameter-uncertain (α) by more than an order of magnitude (factor ≈ 16 between two literature-based expansion sets). Thermal-memory runs were made for the circular cavity only.",
 '7. **Why it matters.** (i) A verification-grade route to single-pulse responses from frequency-domain solvers and a cautionary example of how a periodic synthesis and an unseen rotation-sign error inflate/blur results; (ii) shows that wall stress under a prescribed wall temperature is a poor discriminator of non-Fourier conduction → guides which observables to study; (iii) quantifies when crystal orientation must be considered for cavity-containing β-Ga₂O₃ components (relative, not absolute, statements).',
 '8. **Exact novelty (bounded).** The combination: monoclinic crystal × circular/elliptical cavity × orientation sweep × thermal-memory parameter × transient coupled thermoelasticity × verification chain with uncertainty (not a claim of priority).',
 '9. **Evidence supporting novelty.** `01_Literature/SEARCH_LOG.md` (11 logged searches + handoff searches), `REFERENCES_VERIFIED.md`; closest works: Chao & Gao 2001 (steady, elliptic, anisotropic), Shiah & Liu 2026 (BEM, anisotropic holes), Abbas et al. 2015/2022 (generalized, circular/cylindrical).',
 '10. **What the work does NOT claim.** No physical validation; no validity of Fourier/CV conduction at 5–50 nm; no measured relaxation times; no absolute stress predictions for real devices (α uncertain by more than 10×, c_p assumed); no 3-D, nonlinear, or temperature-dependent effects; no interior-stress or heat-flux conclusions; no priority claim; no expert review yet.']
open(os.path.join(ROOT, '00_Project_Control', 'CENTRAL_STORY.md'), 'w').write('\n\n'.join(L) + '\n')
print('CENTRAL_STORY.md written')
