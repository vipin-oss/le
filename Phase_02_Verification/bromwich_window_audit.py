"""bromwich_window_audit.py — Phase 2 evidence for audit finding A5 (Bromwich validity window).

Recomputes, from the stored production series in 09_Raw_Data/production/*.npz (no re-solve), the error between the
synthesised wall-temperature history and the prescribed Gaussian pulse, in two time windows:
  * the reported quantity-of-interest window 0 <= t <= 6 t_th
  * the full stored window 0 <= t <= 12 t_th
The point of the script is that the inversion plan (T = 20, gamma = 0.9, alias e^{-gamma T} = 1.5e-8) bounds the
n = 0 truncation error over the QoI window, whereas for the deliberately wide test pulse (t_w = 2.4) the
neighbouring periodic image at t - T enters inside 0 <= t <= 12.  The manuscript statement of 2026-10-01
("valid for 0 <= t <= 14.5") is unconditional and therefore needs qualifying; this file supplies the numbers for the
qualified sentence.  Output: Phase_02_Verification/verification/BROMWICH_WINDOW.csv (+ .json, + console summary).
"""
import os, json, glob
import numpy as np

PROD = '/home/user/le/PAPER_PROJECT/09_Raw_Data/production'
OUT = '/home/user/le/Phase_02_Verification/verification/BROMWICH_WINDOW.csv'
TQO, TFUL = 6.0, 12.0

rows = []
for jp in sorted(glob.glob(os.path.join(PROD, '*.json'))):
    tag = os.path.basename(jp)[:-5]
    npzp = os.path.join(PROD, tag + '.npz')
    if not os.path.exists(npzp):
        continue
    j = json.load(open(jp))
    d = np.load(npzp)
    t, wall = d['t'], d['wall']
    plan = j.get('plan') or {}
    t0, tw = float(plan.get('t0', 2.5)), float(plan.get('tw', 1.2))
    p = np.exp(-((t - t0) / tw) ** 2)
    err = np.abs(wall - p[None, :]).max(axis=0)
    q, f = (t <= TQO + 1e-9), (t <= TFUL + 1e-9)
    if not q.any() or not f.any():
        continue
    rows.append(dict(tag=tag, block=j.get('block', ''), grid=j.get('grid', ''), model=j.get('model', ''),
                     chi=j.get('chi', ''), tw=tw,
                     err_qoi_0_6=float(err[q].max()), err_full_0_12=float(err[f].max()),
                     t_of_max_full=float(t[f][int(np.argmax(err[f]))])))
if not rows:
    raise SystemExit('no production data found in ' + PROD)

hdr = ['tag', 'block', 'grid', 'model', 'chi', 'tw', 'err_qoi_0_6', 'err_full_0_12', 't_of_max_full']
with open(OUT, 'w') as fh:
    fh.write(','.join(hdr) + '\n')
    for r in rows:
        fh.write(','.join(f"{r[k]:.6g}" if isinstance(r[k], float) else str(r[k]) for k in hdr) + '\n')

worst_q = max(rows, key=lambda r: r['err_qoi_0_6'])
worst_f = max(rows, key=lambda r: r['err_full_0_12'])
above_q = [r for r in rows if r['err_qoi_0_6'] > 1e-6]
above_f = [r for r in rows if r['err_full_0_12'] > 1e-3]
by_tw = {}
for r in rows:
    by_tw.setdefault(r['tw'], []).append(r)
print(f"{len(rows)} stored runs audited")
print(f"  worst error in the reported window t<=6 : {worst_q['err_qoi_0_6']:.3e}  ({worst_q['tag']}, t_w={worst_q['tw']}, grid {worst_q['grid']})")
print(f"  worst error over the full window t<=12  : {worst_f['err_full_0_12']:.3e}  ({worst_f['tag']}, t_w={worst_f['tw']}, grid {worst_f['grid']}, at t={worst_f['t_of_max_full']:.2f})")
print(f"  runs with error > 1e-6 in t<=6          : {len(above_q)}")
print(f"  runs with error > 1e-3 in t<=12         : {len(above_f)}  -> blocks {sorted(set(r['block'] for r in above_f))}, t_w {sorted(set(r['tw'] for r in above_f))}")
print("  by pulse width t_w (max over runs, QoI window / full window):")
for tw in sorted(by_tw):
    g = by_tw[tw]
    print(f"    t_w = {tw:4.1f} (n={len(g):3d}): {max(r['err_qoi_0_6'] for r in g):.2e} / {max(r['err_full_0_12'] for r in g):.2e}")
json.dump(dict(n_runs=len(rows), worst_qoi=worst_q, worst_full=worst_f, n_above_1e6_in_qoi=len(above_q),
               n_above_1e3_in_full=len(above_f),
               by_tw={str(k): dict(n=len(v), qoi=max(r['err_qoi_0_6'] for r in v), full=max(r['err_full_0_12'] for r in v))
                      for k, v in by_tw.items()}), open(OUT.replace('.csv', '.json'), 'w'), indent=1, default=str)
print('wrote', OUT)
