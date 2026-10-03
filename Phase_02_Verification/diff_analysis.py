"""diff_analysis.py — compare two ANALYSIS_V2.json files key by key (Phase 2 reproducibility gate).

Usage:  python3 Phase_02_Verification/diff_analysis.py OLD.json NEW.json

Reports, in markdown: keys present only in the new file (additive work), keys that disappeared (must be empty),
and every scalar whose value moved, with the relative difference.  Ends with a verdict line stating the largest
relative change among pre-existing quantities.
"""
import json, math, sys


def walk(a, b, path=''):
    """yield (path, kind, old, new)"""
    if isinstance(a, dict) and isinstance(b, dict):
        for k in b:
            if k not in a:
                yield (f'{path}.{k}', 'added', None, b[k])
            else:
                yield from walk(a[k], b[k], f'{path}.{k}')
        for k in a:
            if k not in b:
                yield (f'{path}.{k}', 'removed', a[k], None)
    elif isinstance(a, list) and isinstance(b, list):
        if len(a) != len(b):
            yield (path, 'list-length', len(a), len(b))
        for i, (x, y) in enumerate(zip(a, b)):
            yield from walk(x, y, f'{path}[{i}]')
    else:
        na, nb = _num(a), _num(b)
        if na is None and nb is None:
            if str(a) != str(b):
                yield (path, 'text', a, b)
        elif na is None or nb is None or na != nb:
            yield (path, 'value', a, b)


def _num(x):
    if isinstance(x, bool):
        return None
    if isinstance(x, (int, float)):
        return float(x)
    if isinstance(x, str):
        try:
            return float(x)
        except ValueError:
            return None
    return None


def reldiff(a, b):
    na, nb = _num(a), _num(b)
    if na is None or nb is None:
        return None
    if na == nb:
        return 0.0
    if na == 0:
        return math.inf
    return abs(nb - na) / abs(na)


def main(old, new):
    A, B = json.load(open(old)), json.load(open(new))
    rows = list(walk(A, B))
    added = [r for r in rows if r[1] == 'added']
    removed = [r for r in rows if r[1] == 'removed']
    changed = [r for r in rows if r[1] in ('value', 'list-length')]
    text = [r for r in rows if r[1] in ('text',)]
    mx = max([reldiff(r[2], r[3]) or 0.0 for r in changed] or [0.0])
    print('# ANALYSIS_V2.json — diff before/after the Phase 2 re-analysis')
    print()
    print(f'* keys added: **{len(added)}**  ·  keys removed: **{len(removed)}**  · '
          f'scalar values changed: **{len(changed)}**  ·  strings changed: **{len(text)}**')
    print(f'* largest relative change among pre-existing quantities: **{mx:.3e}**')
    print()
    if removed:
        print('## Keys that disappeared (must be explained)')
        for p, k, o, n in removed:
            print(f'* `{p}` was `{str(o)[:60]}`')
        print()
    if changed:
        print('## Changed values')
        print()
        print('| key | before | after | rel. diff |')
        print('|---|---|---|---|')
        for p, k, o, n in sorted(changed, key=lambda r: -(reldiff(r[2], r[3]) or 0))[:40]:
            rd = reldiff(o, n)
            print(f'| `{p}` | `{str(o)[:28]}` | `{str(n)[:28]}` | {rd:.2e} |' if rd is not None else
                  f'| `{p}` | `{str(o)[:28]}` | `{str(n)[:28]}` | — |')
        print()
    if text:
        print('## Changed strings (provenance labels, notes)')
        for p, k, o, n in text[:12]:
            print(f'* `{p}`: `{str(o)[:70]}` → `{str(n)[:70]}`')
        print()
    print('## Keys added by this phase')
    top = {}
    for p, k, o, n in added:
        head = p.lstrip('.').split('.')[0].split('[')[0]
        top[head] = top.get(head, 0) + 1
    for h, c in sorted(top.items(), key=lambda x: -x[1]):
        print(f'* `{h}`: {c} new scalar(s)')
    print()
    print(f'VERDICT: {"additive only" if not removed and mx == 0 else ("values moved — inspect" if mx > 1e-12 else "no pre-existing value changed beyond round-off")}')


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
