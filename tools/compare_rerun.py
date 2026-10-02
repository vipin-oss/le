#!/usr/bin/env python3
"""compare_rerun.py — compare the results regenerated in THIS session against the
results delivered in le.zip (snapshot in baseline_provided/).

Usage:  python3 tools/compare_rerun.py [--tol 1e-10]

Reports, per item, the delivered value, the recomputed value and the relative
difference, and flags anything above tolerance.  Read-only: writes one report file
`RERUN_COMPARISON.md` in the repo root and prints a summary.
"""
import json, os, sys, math
import numpy as np

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = os.path.join(REPO, 'PAPER_PROJECT')
B = os.path.join(REPO, 'baseline_provided')


def jload(p):
    with open(p) as f:
        return json.load(f)


def rel(a, b):
    """relative difference, robust to zeros"""
    a = float(a); b = float(b)
    d = abs(a - b)
    s = max(abs(a), abs(b))
    return 0.0 if s == 0.0 else d / s


def num(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def fmt(x):
    return f'{x:.6e}' if isinstance(x, float) else str(x)


def compare_numeric(old, new, keys=None, tol=1e-9, label=''):
    """Walk two JSON objects; compare every scalar leaf."""
    rows = []
    if keys is None:
        keys = sorted(set(old) & set(new))
    for k in keys:
        if k not in old or k not in new:
            rows.append((k, 'present-absent', '', '', ''))
            continue
        o, n = old[k], new[k]
        if isinstance(o, dict) and isinstance(n, dict):
            rows += [(f'{k}.{kk}', *r) for kk, *r in compare_numeric(o, n, tol=tol)]
        elif isinstance(o, list) and isinstance(n, list) and o and isinstance(o[0], dict):
            for i, (oo, nn) in enumerate(zip(o, n)):
                rows += [(f'{k}[{i}].{kk}', *r) for kk, *r in compare_numeric(oo, nn, tol=tol)]
        else:
            if isinstance(o, list) and isinstance(n, list):
                if len(o) != len(n):
                    rows.append((k, 'length-diff', len(o), len(n), '')); continue
                worst, wo, wn = 0.0, None, None
                for a, b in zip(o, n):
                    fa, fb = num(a), num(b)
                    if fa is None or fb is None:
                        if a != b:
                            rows.append((k, 'str-diff', a, b, ''))
                        continue
                    d = rel(fa, fb)
                    if d > worst:
                        worst, wo, wn = d, fa, fb
                rows.append((k, 'array', wo, wn, worst))
            else:
                fo, fn = num(o), num(n)
                if fo is None or fn is None:
                    rows.append((k, 'same' if o == n else 'STR-DIFF', o, n, 0.0))
                else:
                    rows.append((k, 'num', fo, fn, rel(fo, fn)))
    return rows


def main():
    tol = 1e-9
    if '--tol' in sys.argv:
        tol = float(sys.argv[sys.argv.index('--tol') + 1])
    out = []
    nbad = 0
    ntot = 0

    # ---------- 1. verification suite ----------
    for name, newp, oldp in [
        ('TEST_RESULTS.json', os.path.join(P, '07_Tests', 'TEST_RESULTS.json'),
         os.path.join(B, 'TEST_RESULTS.json')),
        ('CONVERGENCE_RESULTS.json', os.path.join(P, '10_Processed_Data', 'CONVERGENCE_RESULTS.json'),
         os.path.join(B, '10_Processed_Data', 'CONVERGENCE_RESULTS.json')),
        ('CONVERGENCE_DIRS.json', os.path.join(P, '10_Processed_Data', 'CONVERGENCE_DIRS.json'),
         os.path.join(B, '10_Processed_Data', 'CONVERGENCE_DIRS.json')),
        ('ANALYSIS_V2.json', os.path.join(P, '10_Processed_Data', 'ANALYSIS_V2.json'),
         os.path.join(B, '10_Processed_Data', 'ANALYSIS_V2.json')),
    ]:
        if not (os.path.exists(newp) and os.path.exists(oldp)):
            out.append(f'\n### {name}\n_missing_ (new={os.path.exists(newp)}, delivered={os.path.exists(oldp)})\n')
            continue
        old, new = jload(oldp), jload(newp)
        rows = compare_numeric(old, new, tol=tol)
        bad = [r for r in rows if isinstance(r[4], float) and r[4] > tol]
        nbad += len(bad); ntot += len(rows)
        out.append(f'\n### {name}\ncompared {len(rows)} scalar/array leaves; '
                   f'{len(bad)} exceed tol={tol:g}\n')
        if bad:
            out.append('| key | delivered | recomputed | rel.diff |')
            out.append('|---|---|---|---|')
            for k, _, o, n, d in bad[:60]:
                out.append(f'| `{k}` | {fmt(o)} | {fmt(n)} | {d:.3e} |')
        else:
            out.append('All compared values agree within tolerance.')

    # ---------- 2. production runs ----------
    newd = os.path.join(P, '09_Raw_Data', 'production')
    oldd = os.path.join(B, '09_Raw_Data', 'production')
    tags = sorted(set(f[:-5] for f in os.listdir(newd) if f.endswith('.json')) &
                  set(f[:-5] for f in os.listdir(oldd) if f.endswith('.json')))
    worst = []
    for t in tags:
        o, n = jload(os.path.join(oldd, t + '.json')), jload(os.path.join(newd, t + '.json'))
        for k in ('sig_interp', 'sig_nodal', 't_star', 'th_star_interp_deg',
                  'wall_pulse_err', 'back_max', 'Lambda', 'epsilon'):
            if k in o and k in n:
                d = rel(o[k], n[k])
                worst.append((d, t, k, o[k], n[k]))
    worst.sort(reverse=True)
    big = [w for w in worst if w[0] > 1e-10]
    out.append(f'\n### production runs\n{len(tags)} common tags, {len(worst)} QoI values compared; '
               f'{len(big)} differ by more than 1e-10\n')
    if big:
        out.append('| run | quantity | delivered | recomputed | rel.diff |')
        out.append('|---|---|---|---|---|')
        for d, t, k, o, n in big[:40]:
            out.append(f'| {t} | {k} | {fmt(o)} | {fmt(n)} | {d:.3e} |')
    else:
        out.append(f'max relative difference over all QoIs: {worst[0][0]:.3e} ({worst[0][1]}/{worst[0][2]})'
                   if worst else 'no data')

    # ---------- 3. npz series ----------
    npztags = sorted(set(f[:-4] for f in os.listdir(newd) if f.endswith('.npz')) &
                     set(f[:-4] for f in os.listdir(oldd) if f.endswith('.npz')))
    ser = []
    for t in npztags[:40]:
        a = np.load(os.path.join(oldd, t + '.npz')); b = np.load(os.path.join(newd, t + '.npz'))
        if a['hoop'].shape != b['hoop'].shape:
            ser.append((float('inf'), t, 'shape', a['hoop'].shape, b['hoop'].shape)); continue
        d = float(np.abs(a['hoop'] - b['hoop']).max() / max(np.abs(a['hoop']).max(), 1e-300))
        ser.append((d, t, 'hoop', a['hoop'].shape, b['hoop'].shape))
    ser.sort(reverse=True)
    out.append(f'\n### stored wall-stress series (npz)\n{len(npztags)} common runs; '
               f'worst max-relative difference of the hoop series:\n')
    for d, t, k, so, sn in ser[:10]:
        out.append(f'- {t}: {d:.3e}')

    # ---------- 4. figures / tables ----------
    import hashlib
    def sha(p):
        return hashlib.sha256(open(p, 'rb').read()).hexdigest()[:16]
    lines = []
    for sub in ('11_Figures', '12_Tables', '13_Manuscript'):
        nd, od = os.path.join(P, sub), os.path.join(B, sub)
        for f in sorted(os.listdir(od)):
            if not os.path.isfile(os.path.join(od, f)):
                continue
            np_ = os.path.join(nd, f)
            if os.path.exists(np_):
                same = sha(np_) == sha(os.path.join(od, f))
                lines.append(f'- `{sub}/{f}`: {"identical" if same else "REGENERATED (differs)"}')
            else:
                lines.append(f'- `{sub}/{f}`: missing in recomputed tree')
    out.append('\n### figures / tables / manuscript\n' + '\n'.join(lines))

    rep = ('# RERUN COMPARISON — recomputed (this session) vs delivered (le.zip)\n'
           f'tolerance {tol:g} · production tolerance 1e-10\n' + '\n'.join(out) + '\n')
    with open(os.path.join(REPO, 'RERUN_COMPARISON.md'), 'w') as f:
        f.write(rep)
    print(rep)


if __name__ == '__main__':
    main()
