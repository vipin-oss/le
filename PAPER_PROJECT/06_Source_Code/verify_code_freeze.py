#!/usr/bin/env python3
"""verify_code_freeze.py — read-only check that the code on disk matches a deposited freeze manifest.

Why this exists next to `make_code_freeze.py`: the manifest writer is the only project tool that
recomputes the hashes, and it writes a new file. `tools/connection_audit.py` also verifies the freeze, but
it inspects git state, so it cannot run in a working copy that is not a repository - which is exactly what
a tree restored from the reproducibility archive is. This script needs neither git nor a write: it
re-hashes every entry of a chosen manifest and reports.

Usage
    python3 PAPER_PROJECT/06_Source_Code/verify_code_freeze.py                # newest submission freeze
    python3 PAPER_PROJECT/06_Source_Code/verify_code_freeze.py v2_gate        # a labelled one
    python3 PAPER_PROJECT/06_Source_Code/verify_code_freeze.py --json         # machine-readable

Exit status
    0   every listed file is present and byte-identical
    1   at least one file differs or is missing  (printed with its path and both hashes)
    2   the manifest itself could not be read

Nothing is written. Run it before trusting any rebuild, and after editing code to see that the freeze you
are standing on is the one the manifest describes; to adopt changed code as a new freeze, run
`make_code_freeze.py <label>` deliberately, as the project's convention requires.
"""
import argparse
import glob
import hashlib
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PP = os.path.dirname(HERE)


def sha256(path):
    h = hashlib.sha256()
    with open(path, 'rb') as fh:
        for c in iter(lambda: fh.read(1 << 20), b''):
            h.update(c)
    return h.hexdigest()


def pick(label):
    if label:
        for cand in (os.path.join(HERE, f'CODE_FREEZE_{label}.json'),
                     os.path.join(HERE, label), label):
            if os.path.isfile(cand):
                return cand
        sys.exit(f'no freeze manifest for label {label!r}; available: '
                 + ', '.join(sorted(os.path.basename(p)[12:-5]
                                    for p in glob.glob(os.path.join(HERE, 'CODE_FREEZE_*.json')))))
    subs = sorted(glob.glob(os.path.join(HERE, 'CODE_FREEZE_submission_*.json')))
    if not subs:
        sys.exit('no CODE_FREEZE_submission_*.json in ' + HERE)
    return subs[-1]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('label', nargs='?', default='', help='freeze label, e.g. submission_2026_10_03j')
    ap.add_argument('--json', action='store_true')
    a = ap.parse_args()
    man = pick(a.label)
    d = json.load(open(man, encoding='utf-8'))
    files = d.get('files', d) if isinstance(d, dict) else d
    if isinstance(files, dict):
        items = list(files.items())                       # {path: sha256}
    else:
        items = [(e.get('path') or e.get('name'), e.get('sha256')) for e in files]
    same = diff = miss = 0
    detail = []
    for path, want in items:
        if not path or not want:
            continue
        p = path if os.path.isabs(path) else os.path.join(PP, path)
        if not os.path.isfile(p):
            for cand in (os.path.join(ROOT_PLACEHOLDER, path), os.path.join(os.path.dirname(PP), path)):
                if os.path.isfile(cand):
                    p = cand
                    break
            else:
                miss += 1
                detail.append({'path': path, 'status': 'missing'})
                continue
        got = sha256(p)
        if got == want:
            same += 1
            detail.append({'path': path, 'status': 'identical', 'sha256': got[:16]})
        else:
            diff += 1
            detail.append({'path': path, 'status': 'DIFFERS', 'manifest': want[:16], 'on_disk': got[:16]})
    total = same + diff + miss
    if a.json:
        print(json.dumps({'manifest': os.path.relpath(man, PP), 'label': d.get('label', ''),
                          'date_in_manifest': d.get('date', ''), 'entries': total, 'identical': same,
                          'differing': diff, 'missing': miss, 'detail': detail,
                          'verdict': 'PASS' if total and not diff and not miss else 'FAIL'}, indent=1))
    else:
        print(f'manifest : {os.path.relpath(man, PP)}  (label {d.get("label", "?")}, dated '
              f'{d.get("date", "?")})')
        print(f'entries  : {total}   identical: {same}   differing: {diff}   missing: {miss}')
        for e in detail:
            if e['status'] != 'identical':
                print('  ' + json.dumps(e))
        print('RESULT: ' + ('FROZEN CODE CONFIRMED - every listed file is byte-identical'
                            if total and not diff and not miss else 'FREEZE MISMATCH'))
    return 0 if (total and not diff and not miss) else 1


ROOT_PLACEHOLDER = os.path.dirname(PP)      # the repository root, for paths given relative to it

if __name__ == '__main__':
    sys.exit(main())
