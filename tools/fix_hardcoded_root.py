#!/usr/bin/env python3
"""fix_hardcoded_root.py — one-off repair (2026-10-02).

Thirteen project scripts hard-coded ``ROOT = '/home/user/PAPER_PROJECT'`` (or an absolute
path into that tree).  That breaks as soon as the project is checked out anywhere else —
exactly what happened when the repository was moved to /home/user/le.  Each literal is
replaced by a lookup that walks up from the script's own location for the PAPER_PROJECT
directory, so the scripts work in any checkout.  No numbers or scientific content change.

Run from the repository root:  python3 tools/fix_hardcoded_root.py
"""
import os
import re
import subprocess

HELPER = """def _pp_root(_start):
    \"\"\"walk up from _start to the PAPER_PROJECT directory (path-independent replacement
    for the hard-coded '/home/user/PAPER_PROJECT' that used to be here).\"\"\"
    _p = os.path.abspath(_start)
    while True:
        if os.path.basename(_p) == 'PAPER_PROJECT':
            return _p
        _q = os.path.dirname(_p)
        if _q == _p:
            break
        _p = _q
    return os.environ.get('PAPER_PROJECT_ROOT', '/home/user/PAPER_PROJECT')


"""

ROUND = re.compile(r"^(?P<indent>\s*)ROOT = '/home/user/PAPER_PROJECT'")
SRCONE = re.compile(r"^SRC = '/home/user/PAPER_PROJECT/06_Source_Code/src'")


def patch(path):
    src = open(path, encoding='utf-8').read()
    if '/home/user/PAPER_PROJECT' not in src:
        return False
    lines = src.split('\n')
    out, changed, helper_done = [], False, False
    for ln in lines:
        if not helper_done and ('/home/user/PAPER_PROJECT' in ln):
            m = ROUND.match(ln)
            if m:
                out.append(HELPER.rstrip('\n'))
                out.append('ROOT = _pp_root(os.path.dirname(os.path.abspath(__file__)))' +
                           ln[m.end():])
                changed = helper_done = True
                continue
            m = SRCONE.match(ln)
            if m:
                out.append(HELPER.rstrip('\n'))
                out.append("SRC = os.path.join(_pp_root(os.path.dirname(os.path.abspath(__file__))),"
                           " '06_Source_Code', 'src')" + ln[m.end():])
                changed = helper_done = True
                continue
            raise SystemExit(f'unhandled literal in {path}: {ln!r}')
        out.append(ln)
    if changed:
        open(path, 'w', encoding='utf-8').write('\n'.join(out))
    return changed


def main():
    hits = subprocess.run(['grep', '-rl', '/home/user/PAPER_PROJECT', '--include=*.py', '.'],
                          capture_output=True, text=True, cwd=os.getcwd())
    files = [f for f in hits.stdout.split() if os.path.basename(f) != 'fix_hardcoded_root.py']
    for f in sorted(files):
        print(('patched  ' if patch(f) else 'skipped  ') + f)
    print(len(files), 'files inspected')


if __name__ == '__main__':
    main()
