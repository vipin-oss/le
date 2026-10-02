#!/usr/bin/env python3
"""audit_tex.py — static audit of the generated elsarticle source.

No TeX engine is available in this environment, so the submission source is checked statically:
balanced braces and environments, resolvable \\cite / \\ref / \\includegraphics, consistent table
column counts, portability (ASCII only, matched $), editorial limits (abstract, highlights) and
the presence of the carried numbers and of the labelling that the brief requires.

Exit status 0 means every check passed.

Usage:  python3 tools/audit_tex.py
"""
import argparse
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MS = os.path.join(ROOT, 'PAPER_PROJECT', '13_Manuscript')
TEX = os.path.join(MS, 'FINAL_REVISED_MANUSCRIPT.tex')
BIB = os.path.join(MS, 'FINAL_REVISED_REFERENCES.bib')
MD = os.path.join(MS, 'manuscript_IJHMT.md')

fails, warns, oks = [], [], []


def check(cond, msg):
    (oks if cond else fails).append(msg)
    return cond


def warn(cond, msg):
    if not cond:
        warns.append(msg)


def main():
    global TEX, BIB, MD
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('-t', '--tex', default=TEX)
    ap.add_argument('-b', '--bib', default=BIB)
    ap.add_argument('-m', '--md', default=MD)
    ap.add_argument('-c', '--companion', action='store_true',
                    help='audit a companion document: no abstract, highlights, figures or '
                         'carried-number list are expected')
    a = ap.parse_args()
    TEX, BIB, MD = a.tex, a.bib, a.md
    COMP = a.companion
    if not os.path.exists(TEX):
        print('MISSING', TEX)
        return 1
    src = open(TEX, encoding='utf-8').read()
    bib = open(BIB, encoding='utf-8').read()
    md = open(MD, encoding='utf-8').read()
    lines = src.split('\n')
    body = src

    # ---------------------------------------------------------------- 1. portability
    non_ascii = sorted({c for c in body if ord(c) > 127})
    check(not non_ascii, 'ASCII only (%d non-ASCII: %s)'
          % (len(non_ascii), ''.join(non_ascii)))
    ctrl = sorted({hex(ord(c)) for c in body if ord(c) < 32 and c not in '\n\t'})
    check(not ctrl, 'no control characters (%s)' % ctrl)
    odd = [n for n, l in enumerate(lines, 1) if l.count('$') % 2 and not l.lstrip().startswith('%')]
    check(not odd, 'math delimiters balanced (odd $ on lines %s)' % odd[:5])
    check('$$$' not in body, 'no triple $')
    check('$$' not in body, 'no empty math group ($$)')

    # ---------------------------------------------------------------- 2. braces & environments
    stripped = re.sub(r'\\[{}]', '', body)
    stripped = re.sub(r'^[ \t]*%.*$', '', stripped, flags=re.M)
    check(stripped.count('{') == stripped.count('}'),
          'braces balanced (%d { vs %d })' % (stripped.count('{'), stripped.count('}')))
    for env in ('document', 'frontmatter', 'abstract', 'highlights', 'keyword',
                'equation', 'figure', 'table', 'tabular', 'tabularx', 'itemize'):
        b = len(re.findall(r'\\begin{%s}' % env, body))
        e = len(re.findall(r'\\end{%s}' % env, body))
        check(b == e, 'environment %-12s begin/end %d/%d' % (env, b, e))

    # ---------------------------------------------------------------- 3. citations
    keys = set(re.findall(r'@(?:article|book|incollection|inbook|misc|phdthesis|inproceedings)\s*\{\s*([^,]+),', bib))
    cited = set()
    for c in re.findall(r'\\cite\{([^}]*)\}', body):
        cited |= {k.strip() for k in c.split(',') if k.strip()}
    check(bool(keys), 'bib parsed: %d entries' % len(keys))
    check(cited <= keys, 'every \\cite key exists in the bib (missing: %s)'
          % sorted(cited - keys))
    uncited = sorted(keys - cited)
    if not COMP:
        check(not uncited, 'every bib entry is cited (uncited: %s)' % uncited)
    check(not re.search(r'\\cite\{\s*\}', body), 'no empty \\cite')
    nomath = re.sub(r'\\begin\{equation\*?\}.*?\\end\{equation\*?\}', ' ', body, flags=re.S)
    nomath = re.sub(r'\$\$?[^$]*\$\$?', ' ', nomath)          # $...$ and $$...$$
    nomath = nomath.replace('%', '')
    check(not re.search(r'\[\d+(?:,\s*\d+)*\]', nomath),
          'no leftover numeric citations such as [3] or [1,2]')

    # ---------------------------------------------------------------- 4. cross references
    labels = set(re.findall(r'\\label\{([^}]*)\}', body))
    refs = set(re.findall(r'\\(?:ref|eqref)\{([^}]*)\}', body))
    check(refs <= labels, 'every \\ref resolves (missing labels: %s)' % sorted(refs - labels))
    unused = sorted(l for l in labels - refs
                    if not l.startswith('sec:') and not l.startswith('eq:'))
    if not COMP:
        check(not unused, 'every figure/table is referenced in the text (unused: %s)' % unused)
    warn(True, 'equations not referenced in the text: %s'
         % sorted(l for l in labels - refs if l.startswith('eq:')))
    check(not re.search(r'\\(?:ref|eqref)\{\s*\}', body), 'no empty \\ref')
    check(not re.search(r'Eq\.\s*\(\d+\)', body), 'no hard-coded equation numbers')

    # ---------------------------------------------------------------- 5. graphics
    figs = re.findall(r'\\includegraphics(?:\[[^\]]*\])?\{([^}]*)\}', body)
    missing = [f for f in figs if not os.path.exists(os.path.normpath(os.path.join(MS, f)))]
    if not COMP:
        check(len(figs) == 8, '8 figures included (%d)' % len(figs))
    check(not missing, 'every figure file exists (missing: %s)' % missing)
    n_cap = len(re.findall(r'\\caption\{', body))
    n_floats = len(re.findall(r'\\label\{fig:', body)) + len(re.findall(r'\\label\{tab:', body))
    check(n_cap == n_floats, 'one caption per float (%d captions, %d floats)' % (n_cap, n_floats))
    figlabels = sorted(int(x) for x in re.findall(r'\\label\{fig:(\d+)\}', body))
    if not COMP:
        check(figlabels == list(range(1, 9)), 'figures numbered 1..8 (%s)' % figlabels)
    tablabels = sorted(int(x) for x in re.findall(r'\\label\{tab:(\d+)\}', body))
    check(tablabels == list(range(1, len(tablabels) + 1)),
          'tables numbered 1..%d (%s)' % (len(tablabels), tablabels))

    # ---------------------------------------------------------------- 6. tables
    for m in re.finditer(r'\\begin\{(tabular|tabularx)\}(\{\\textwidth\})?\{([a-zA-Z]+)\}'
                         r'(.*?)\\end\{\1\}', body, flags=re.S):
        spec, block = m.group(3), m.group(4)
        ncol = len(spec)
        rows = [r for r in block.split('\\\\') if r.strip() and 'toprule' not in r
                and 'midrule' not in r and 'bottomrule' not in r]
        bad = [r for r in rows if len(re.findall(r'(?<!\\)&', r)) + 1 != ncol]
        check(not bad, 'table with %d columns: all %d rows agree (%d bad)'
              % (ncol, len(rows), len(bad)))
    check(len(re.findall(r'\\toprule', body)) == len(re.findall(r'\\bottomrule', body)),
          'booktabs rules paired')

    # ---------------------------------------------------------------- 7. editorial limits
    ab = re.search(r'\\begin\{abstract\}\n(.*?)\n\\end\{abstract\}', body, flags=re.S)
    if not COMP:
        check(bool(ab), 'abstract present')
    if ab:
        txt = re.sub(r'\$[^$]*\$', 'x', ab.group(1))
        txt = re.sub(r'\\[a-zA-Z]+', ' ', txt)
        n = len(txt.split())
        check(n <= 250, 'abstract %d words (limit 250)' % n)
    hlb = re.search(r'\\begin\{highlights\}\n(.*?)\\end\{highlights\}', body, flags=re.S)
    hl = re.findall(r'\\item (.*)', hlb.group(1)) if hlb else []
    if not COMP:
        check(3 <= len(hl) <= 5, 'highlights: %d items (3-5)' % len(hl))
        long = [h for h in hl if len(h) > 85]
        check(not long, 'highlights <= 85 characters (%d too long)' % len(long))

    # ---------------------------------------------------------------- 8. required content
    must = {
        'author placeholder': '[AUTHOR INPUT REQUIRED:',
        'primary Fourier + Lord-Shulman': 'Fourier and Lord--Shulman conduction as the primary',
        'exploratory kernel labelled': 'exploratory sensitivity kernel only',
        'MCV3 exploratory in results': 'exploratory',
        'no experimental validation': 'no experimental validation exists',
        'expansion uncertainty >10x': 'more than an order of magnitude',
        'continuum validity': 'continuum validity',
        'AI declaration': 'Declaration of Generative AI',
        'data availability': 'Data availability',
        'reproducibility placeholder': 'PUBLIC REPOSITORY/DOI TO BE INSERTED',
        'elsarticle class': 'documentclass[preprint,12pt]{elsarticle}',
        'numbered bibliography': 'elsarticle-num',
        'bib call': '\\bibliography{FINAL_REVISED_REFERENCES}',
    }
    for k, v in must.items():
        if COMP and k in ('verification label', 'repository placeholder'):
            continue
        check(v in body, 'required content: %s' % k)
    n_eq = body.count('\\begin{equation}')
    md_eq = len(re.findall(r'\$\$.*?\\qquad \(\d+\)\s*\$\$', md, flags=re.S))
    if COMP:
        check(n_eq >= 20, 'at least 20 numbered equations (%d)' % n_eq)
        check(n_eq == md_eq, 'equation count matches the .md (%d vs %d)' % (n_eq, md_eq))
        check(body.count('\\section{') >= 5, 'sections present')
    else:
        check(n_eq >= 80, 'at least 80 numbered equations (%d)' % n_eq)
        check(n_eq == md_eq, 'equation count matches the .md (%d vs %d)' % (n_eq, md_eq))
        check(body.count('\\section{') + body.count('\\section*{') >= 7, 'sections present')

    # ---------------------------------------------------------------- 9. numbers carried over
    numbers = ['0.854', '28.7', '29.9', '0.966', '1.322', '6.4', '1.4', '1.078',
               '2.0213e-03', '5.291e-03', '6.19e-04', '5.39e-03', '3.959', '25.3',
               '7686', '0.0515', '0.040', '0.198', '0.792', '1.16', '0.08', '2.6']
    miss = [x for x in numbers if x not in body]
    if not COMP:
        check(not miss, 'carried numbers present (missing: %s)' % miss)

    # ---------------------------------------------------------------- 10. agreement with the .md
    if COMP:
        check(body.count('\\begin{table}') == md.count('**Table C'),
              'table count matches the .md (%d vs %d)'
              % (body.count('\\begin{table}'), md.count('**Table C')))
    else:
        for tok in ('0.854', '28.7', '29.9', '1.078', '2.0213e-03'):
            check(tok in md, 'number %s also present in the master .md' % tok)
        check(body.count('\\begin{table}') == md.count('**Table '),
              'table count matches the .md (%d vs %d)'
              % (body.count('\\begin{table}'), md.count('**Table ')))

    # ---------------------------------------------------------------- report
    print('AUDIT', os.path.relpath(TEX, ROOT))
    for m in oks:
        print('  ok   ', m)
    for m in warns:
        print('  warn ', m)
    for m in fails:
        print('  FAIL ', m)
    print('RESULT:', 'ALL CHECKS PASSED' if not fails else '%d CHECK(S) FAILED' % len(fails))
    return 1 if fails else 0


if __name__ == '__main__':
    sys.exit(main())
