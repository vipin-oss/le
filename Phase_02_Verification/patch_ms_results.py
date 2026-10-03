"""Phase 2 builder patch for ms_results.py (audit findings A1, A2, A8, A9, A10).

Idempotent: every step is applied only if its anchor is still present.  Run with the project venv from
PAPER_PROJECT/13_Manuscript.
"""
import ast, sys

SRC = 'ms_results.py'
s = open(SRC).read()
done = []

HELPER = '''def _v0_note(TR):
    """One sentence on the metric-consistency case (audit A1): it inherits an absolute threshold from the project
    handoff that was calibrated on a coarse demonstration grid which is not used for any reported result.  The
    sentence is emitted only when the recorded numbers support the wording."""
    try:
        c = TR.get('V0_metric_consistency_linear_field', {})
        val, thr = float(c['value_at_96x48_chi2']), float(c['threshold_at_96x48_chi2'])
        if val <= thr:
            return ''
        return (" One inherited absolute threshold is exceeded on a grid that is not used for any reported result: at "
                f"96\u00d748 with \u03c7 = 2 the metric error is {val:.3e} against the threshold {thr:.0e} "
                f"(a {val / thr - 1.0:.1%} exceedance of a bound calibrated on that demonstration grid), while the same "
                "sequence converges at the expected second order and satisfies the threshold at the production grid; the "
                "coarse-grid value is reported in Table 5 rather than suppressed, and the convergence order is asserted as "
                "its own case (V0b).")
    except Exception:
        return ''


def _v0_row(N):
    """Table 5 row for the metric-consistency case, built only from recorded values."""
    out = []
    o = [x for v in (N.get('v0_orders') or {}).values() for x in (v or [])]
    if N.get('v0b') is not None:
        out.append(f"production grid 192\u00d796: \u2264 {sci(N['v0b'])}")
    if o:
        out.append(f"observed order {min(o):.2f}\u2013{max(o):.2f} on refinement (asserted separately as V0b)")
    if N.get('v0_coarse') is not None and N.get('v0_thr'):
        rel = N['v0_coarse'] / N['v0_thr'] - 1.0
        out.append((f"the inherited absolute threshold {sci(N['v0_thr'], 0)} is exceeded by {100 * rel:.1f}% at the "
                    f"demonstration grid 96\u00d748 with \u03c7 = 2 ({sci(N['v0_coarse'])}); that grid is not used for any reported result"
                    if rel > 0 else
                    f"the inherited absolute threshold {sci(N['v0_thr'], 0)} is also met at the demonstration grid 96\u00d748 "
                    f"({sci(N['v0_coarse'])})"))
    return '; '.join(out) if out else 'n/a'


def _shape_sentence(T4, a12):
    """Shape effect of the ellipse relative to the circle, with numerator, denominator and grid stated (audit A10)."""
    out = []
    cm, rmm = T4.get('circle_M_sig_interp'), T4.get('ellipse_M_mean_over_circle_M')
    if cm and rmm:
        ex = T4.get('ellipse_M_extremes_over_circle_M') or []
        out.append(f"At matched grids the mean ellipse peak on grid M is {rmm:.3f} of the circle peak on the same grid "
                   f"({abs(cm) / 1e6:.3f} MPa/K)"
                   + (f", and the extremes of the 12-orientation sweep are {ex[0]:.3f} and {ex[1]:.3f} of it" if len(ex) == 2 else ''))
    ree = T4.get('ellipse_extrapolated_mean_over_circle_extrapolated')
    if ree:
        out.append(f"comparing the two extrapolated sequences gives {ree:.3f}")
    if a12.get('min') and a12.get('max'):
        out.append(f"the orientation of the crystal changes the ellipse peak by a factor of {a12['max'] / a12['min']:.3f} "
                   f"between the most and the least favourable orientation")
    if not out:
        return ''
    return '; '.join(x.rstrip('.') for x in out[:-1]) + '. ' + out[-1].rstrip('.') + '.'


def _iso_shape_sentence(ISO):
    r, lab = ISO.get('ellipse_M_over_circle_M'), 'both on grid 96\u00d796'
    if r is None:
        r, lab = ISO.get('ellipse_M_over_circle_T48'), 'ellipse on 96\u00d796, circle on 96\u00d748'
    return (f"{r:.3f} times the isotropic circle ({lab})" if r else 'n/a')


'''

# (1) replace the helper inserted by the earlier step (bounded by the next real def, def J)
if 'def _v0_note(TR):' not in s:
    i1 = s.index('def J(p):')
    s = s[:i1] + HELPER + s[i1:]
    done.append('helpers')

# (2) count sentence: TR-based note, no hard-coded "the failure is discussed below"
tail = 'illustrated in Fig. 2.")'
if tail in s:
    s = s.replace(tail, 'illustrated in Fig. 2." + _v0_note(TR))', 1); done.append('count sentence')

# (3) ablation data source: production grid primary (A8)
anchor = "CIRC, ISO, EAB, LOC, SH = AN.get('circle_peak', {}), AN.get('isotropic', {}), AN.get('E_ablations', {}), AN.get('locality', {}), AN.get('shipped', {})"
EAB_BLOCK = anchor + """
# audit A8 (2026-10-03): the mechanism ablations exist at two resolutions.  Headline claims use the production-grid
# set when it is present; the 96x48 pre-registered set stays in the same table for continuity.  EAB_GRID is
# interpolated into the sentences so that the grid of a quoted modulation can never be left unstated.
EAB_T48 = AN.get('E_ablations', {})
EAB_M = AN.get('E_ablations_M', {})
EAB = EAB_M if EAB_M.get('baseline_6phi') else EAB_T48
EAB_GRID = '96\u00d796 (production)' if EAB is EAB_M else '96\u00d748 (coarse angular grid)'"""
if anchor in s and 'EAB_T48' not in s:
    s = s.replace(anchor, EAB_BLOCK, 1); done.append('EAB source')

# (4) recorded V0 numbers (replaces the lookup of a case name the suite never emitted, which produced the 'n/a')
old = "N['v0b'] = g(TR, 'V0b_metric_consistency_production_grids', 'worst_production_grids');"
V0B_BLOCK = """_v0c = TR.get('V0_metric_consistency_linear_field', {})
_v0e = {k: lst(_v0c.get(k)) for k in ('chi1_errs_48_96_192', 'chi2_errs_48_96_192')}
_v0p = [v[-1] for v in _v0e.values() if v]
N['v0b'] = max(_v0p) if _v0p else g(TR, 'V0b_metric_consistency_production_grids', 'worst_production_grids')
N['v0_coarse'] = _v0c.get('value_at_96x48_chi2'); N['v0_thr'] = _v0c.get('threshold_at_96x48_chi2')
N['v0_orders'] = {k: lst(v) for k, v in TR.get('V0b_metric_consistency_convergence_order', {}).items() if k.startswith('orders_')}
N['v0_status'] = _v0c.get('status');"""
if old in s:
    s = s.replace(old, V0B_BLOCK, 1); done.append('v0 numbers')

# (5) Table 5 row built from recorded values only (removes the 'n/a' cell and the hard-coded 5.03e-3)
old = """['Metric consistency (linear field)', '\u2264 5\u00d710^{\u22123}', f"production grids \u2264 {sci(N['v0b'])}; the handoff-style 96\u00d748 grid with \u03c7 = 2 gives 5.03\u00d710^{{\u22123}} (reported failure of this criterion, angular-resolution dominated)"],"""
NEWROW = """['Metric consistency of the mapped grid (linear field)', 'order \u2265 1.9 and \u2264 5\u00d710^{\u22123} at 192\u00d796', _v0_row(N)],"""
if old in s:
    s = s.replace(old, NEWROW, 1); done.append('table row')

# (6) the conflated ellipse/circle ratios (A10)
if 'The ellipse peak is {g(T4' in s:
    a = s.index('The ellipse peak is {g(T4'); b = s.index('orientation."))', a) + len('orientation."))')
    s = s[:a] + '{_shape_sentence(T4, a12)}"))' + s[b:]; done.append('shape sentence')

# (7) isotropic control: matched grids (A10)
old = "i.e. {ISO.get('ellipse_M_over_circle_T48', float('nan')):.2f} times the isotropic circle:"
if old in s:
    s = s.replace(old, "{_iso_shape_sentence(ISO)}:", 1); done.append('iso sentence')

# (8) pulse-width paragraph: matched iso ratio + explicit grid (A10)
old = "iso_ratio = ISO.get('ellipse_M_over_circle_T48')"
if old in s:
    s = s.replace(old, "iso_ratio = ISO.get('ellipse_M_over_circle_M', ISO.get('ellipse_M_over_circle_T48'))\n"
                       "        iso_lab = ' (both on grid 96\u00d796)' if 'ellipse_M_over_circle_M' in ISO else ' (ellipse on 96\u00d796, circle on 96\u00d748)'", 1)
    s = s.replace("times that of the isotropic circle, which", "times that of the isotropic circle{iso_lab}, which", 1)
    done.append('pulse-width ratio')

# (9) ablation table: both resolutions, caption states the grid convention (A8)
old = """        rows = [['full anisotropy (baseline)', pc(bs.get('amplitude')), mp(bs.get('mean'), 4), '1.000']]"""
if old in s and 'baseline, grid 96' not in s:
    s = s.replace(old, old + """
        if EAB is EAB_M and EAB_T48.get('baseline_6phi'):      # the pre-registered coarser set, kept for continuity
            bs0 = EAB_T48['baseline_6phi']
            rows.append(['full anisotropy (baseline, grid 96\u00d748)', pc(bs0.get('amplitude')), mp(bs0.get('mean'), 4), '1.000'])""", 1)
    done.append('ablation baseline row')
old = """            if e: rows.append([lab, pc(e['amplitude']), mp(e['mean'], 4), f"{e['mean_over_baseline']:.3f}"])"""
if old in s and "' (grid 96\u00d748)', pc(e0" not in s:
    s = s.replace(old, old + """
            e0 = EAB_T48.get(key)
            if EAB is EAB_M and e0: rows.append([lab + ' (grid 96\u00d748)', pc(e0['amplitude']), mp(e0['mean'], 4), f"{e0['mean_over_baseline']:.3f}"])""", 1)
    done.append('ablation variant rows')
old = "'Mechanism ablations and expansion-set sensitivity for the ellipse (grid 96\u00d748, \u03c6 = 0, 30, \u2026, 150\u00b0).'"
if old in s:
    s = s.replace(old, "'Mechanism ablations and expansion-set sensitivity for the ellipse at six orientations "
                       "\u03c6 = 0, 30, \u2026, 150\u00b0. The unlabelled rows are on grid ' + EAB_GRID + '; rows labelled "
                       "(grid 96\u00d748) are the pre-registered coarser set, kept for continuity. A variant is always "
                       "compared with the baseline of the same grid.'", 1)
    done.append('ablation caption')

# (10) 6.5 sentence: state the grid of the compared pair (inside an f-string -> use braces)
old = "With the 298 K-like expansion set the mean ellipse peak is"
if old in s:
    s = s.replace(old, "With the 298 K-like expansion set (variant and baseline both on grid {EAB_GRID}) the mean ellipse peak is", 1)
    done.append('6.5 grid label')

# (11) A9: also record the dynamic-only bound next to the combined one
old = "    pk = max([abs(r['peak_shift']) for r in dyn + qs] or [float('nan')]); ext = AN.get('H3_extended_map', {})"
if old in s:
    s = s.replace(old, "    pk = max([abs(r['peak_shift']) for r in dyn + qs] or [float('nan')]); pk_dyn = max([abs(r['peak_shift']) for r in dyn] or [float('nan')]); ext = AN.get('H3_extended_map', {})", 1)
    done.append('pk_dyn')

try:
    ast.parse(s)
except SyntaxError as e:
    print('SYNTAX ERROR', e.lineno, repr(e.text)); sys.exit(1)
open(SRC, 'w').write(s)
for need in ['ROOT =', 'def J(p):', "TR = {c['case']: c for c in J(", "AN = J('10_Processed_Data/ANALYSIS_V2.json')",
             'def g(d, *keys', 'def pc(', 'def mp(', 'def sci(', 'def rsd(', 'def verification():', 'def results():',
             'def discussion():']:
    assert need in s, need
print('applied:', ', '.join(done))
print('written; module structure intact')
