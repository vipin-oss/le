#!/usr/bin/env python3
"""check_crossrefs.py — static check of the manuscript's internal cross-references.

After the restructuring to 9 sections the hard-coded "Section x.y", "Table n", "Fig. n" and
"Eq. (n)" strings in the builder modules are the most likely thing to go stale, and a stale
cross-reference is invisible in the rendered text.  This checks every one of them against the
headings, floats and equations actually present in manuscript_IJHMT.md.

Usage:  python3 tools/check_crossrefs.py [-i PAPER_PROJECT/13_Manuscript/manuscript_IJHMT.md]
Exit status 1 if anything is out of range.
"""
import argparse
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DEFAULT = os.path.join(ROOT, 'PAPER_PROJECT', '13_Manuscript', 'manuscript_IJHMT.md')


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('-i', '--input', default=DEFAULT)
    a = ap.parse_args()
    md = open(a.input, encoding='utf-8').read()
    lines = md.split('\n')

    secs = [re.match(r'#{2,3}\s+(\d+(?:\.\d+)?)', l).group(1)
            for l in lines if re.match(r'#{2,3}\s+\d', l)]
    n_eq = len(re.findall(r'\$\$.*?\\qquad \(\d+\)\s*\$\$', md, flags=re.S))
    eq_nums = [int(m) for m in re.findall(r'\\qquad \((\d+)\)\s*\$\$', md)]
    tabs = [int(m) for m in re.findall(r'\*\*Table (\d+)\.\*\*', md)]
    figs = [int(m) for m in re.findall(r'\*\*Fig\. (\d+)\.\*\*', md)]

    bad = []
    if eq_nums != list(range(1, len(eq_nums) + 1)):
        bad.append('equation numbers are not 1..N in order: %s' % eq_nums[:12])
    for m in re.finditer(r'Section[s]?\s*(\d+(?:\.\d+)?)', md):
        if m.group(1) not in secs:
            bad.append('reference to non-existent Section %s' % m.group(1))
    for m in re.finditer(r'Eq\.\s*\((\d+)\)', md):
        if not (1 <= int(m.group(1)) <= n_eq):
            bad.append('reference to non-existent Eq. (%s)' % m.group(1))
    for m in re.finditer(r'Tables?\s*(\d+)', md):
        if int(m.group(1)) not in tabs:
            bad.append('reference to non-existent Table %s' % m.group(1))
    for m in re.finditer(r'Figs?\.\s*(\d+)([a-z]?)', md):
        if int(m.group(1)) not in figs:
            bad.append('reference to non-existent Fig. %s' % m.group(1))

    print('sections   :', ' '.join(secs))
    print('equations  :', n_eq, '| tables:', sorted(set(tabs)), '| figures:', sorted(set(figs)))
    if bad:
        print('\nPROBLEMS:')
        for b in bad:
            print('  -', b)
        return 1
    print('all cross-references resolve')
    return 0


if __name__ == '__main__':
    sys.exit(main())
