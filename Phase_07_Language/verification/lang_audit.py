#!/usr/bin/env python3
"""Phase 7 language/style audit (read-only).

Scans the two generated documents and prints a machine-readable findings table.
Nothing here edits anything: the point is to enumerate what a language pass should
change, and to keep the pass honest about what it deliberately leaves alone.

Checks
  A  project-internal vocabulary that means nothing to a reader of the journal
     (phase numbers, audit/gate language, finding ids, build scaffolding)
  B  banned hyperbole (the programme forbids "novel/breakthrough/comprehensive/robust")
  C  duplication: repeated sentences inside each document and shared sentences
     between manuscript and companion
  D  style mechanics: British/American -ise/-ize mixing, en-dash vs hyphen in
     numeric ranges, double spaces, "et al." punctuation, Section/Eq. capitalisation
  E  readability: sentences of >= 45 words
  F  abbreviations used before any expansion-style context (heuristic: a bare
     upper-case acronym whose first appearance is not adjacent to a gloss)

Usage: python3 lang_audit.py [manuscript.md] [companion.md]
"""
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MAN = ROOT / 'PAPER_PROJECT' / '13_Manuscript'
MS = Path(sys.argv[1]) if len(sys.argv) > 1 else MAN / 'manuscript_IJHMT.md'
CALC = Path(sys.argv[2]) if len(sys.argv) > 2 else MAN / 'calculations_IJHMT.md'

INTERNAL = [
    'Phase ', 'phase ', ' audit', 'gate', 'GATE', 'finding', 'FINDINGS', 'ledger',
    'CHECKLIST', 'snapshot', 'A1', 'A2', 'A3', 'A4', 'A5', 'B1', 'B2', 'C1', 'C2',
    'builder', 'build_manuscript', 'docbuilder', 'bootstrap', 'sandbox', 'repo state',
    'submission_2026', 'v2_gate', '_gate', 're-check', 'recheck',
]
BANNED = ['novel', 'breakthrough', 'comprehensive', 'robust', 'state-of-the-art',
          'first study', 'unprecedented', 'significantly', 'markedly', 'dramatic',
          'clearly demonstrates', 'undoubtedly', 'cutting-edge', 'well-known']


def prose(md):
    """(kind, line) for text-bearing lines only: no table rules, no equations."""
    out = []
    in_refs = False
    for i, line in enumerate(md.split('\n'), 1):
        s = line.strip()
        if s.startswith('## References'):
            in_refs = True
        if not s or s.startswith('|--') or s.startswith('$$'):
            continue
        if in_refs and re.match(r'^\[\d+\] ', s):
            continue
        if s.startswith('!['):
            continue
        out.append((i, s))
    return out


def sentences(text):
    t = re.sub(r'\s+', ' ', text)
    return [x.strip() for x in re.split(r'(?<=[.!?]) (?=[A-Z(])', t) if len(x.strip()) > 1]


def norm(s):
    s = re.sub(r'[*`_$\\]', '', s)
    s = re.sub(r'\[[0-9,\s-]+\]', '', s)
    return re.sub(r'\s+', ' ', s).strip().lower()


def report(title, items, limit=40):
    print('\n== %s: %d' % (title, len(items)))
    for x in items[:limit]:
        print('   -', x if isinstance(x, str) else json.dumps(x, ensure_ascii=False)[:190])


def main():
    ms = MS.read_text(encoding='utf-8')
    calc = CALC.read_text(encoding='utf-8')
    ms_p, calc_p = prose(ms), prose(calc)

    # ---- A internal vocabulary ----
    hits = []
    for line, (i, s) in enumerate(ms_p):
        for w in INTERNAL:
            for m in re.finditer(re.escape(w), s):
                a = max(0, m.start() - 55)
                hits.append({'doc': 'ms', 'line': i, 'word': w,
                             'context': s[a:m.end() + 55]})
    kinds = Counter(h['word'] for h in hits)
    print('\n== A internal-vocabulary hits: %d  by token: %s' % (len(hits), dict(kinds)))
    # show the two families that a journal reader cannot interpret
    report('A audit/gate/phase vocabulary', [
        'ms:%d [%s] …%s…' % (h['line'], h['word'], h['context']) for h in hits
        if h['word'] in ('Phase ', 'phase ', ' audit', 'gate', 'GATE', 'finding',
                         'ledger', 're-check', 'recheck', 'A1', 'A2', 'A3', 'A4', 'A5',
                         'B1', 'B2', 'C1', 'C2', 'v2_gate', '_gate', 'builder',
                         'docbuilder', 'bootstrap', 'sandbox', 'snapshot')])

    # ---- B banned hyperbole ----
    bad = []
    for tag, p in (('ms', ms_p), ('calc', calc_p)):
        for i, s in p:
            for w in BANNED:
                if re.search(re.escape(w), s, re.I):
                    bad.append('%s:%d "%s": …%s…' % (tag, i, w, s[max(0, s.lower().find(w.lower()) - 60):][:170]))
    report('B banned words', bad)

    # ---- C duplication ----
    seen, dups = {}, []
    for tag, p in (('ms', ms_p), ('calc', calc_p)):
        for i, s in p:
            for sen in sentences(s):
                n = norm(sen)
                if len(n) < 60:
                    continue
                if n in seen:
                    dups.append('%s == %s:%d / %s:%d :: %s' % (seen[n], tag, i, tag, i, n[:130]))
                else:
                    seen[n] = '%s:%d' % (tag, i)
    shared = []
    ms_set = {norm(x) for _, s in ms_p for x in sentences(s) if len(norm(x)) > 60}
    calc_set = {norm(x) for _, s in calc_p for x in sentences(s) if len(norm(x)) > 60}
    for n in sorted(ms_set & calc_set):
        shared.append(n[:150])
    report('C duplicate sentences (same doc)', dups)
    report('C sentences shared with the companion', shared)

    # ---- D style mechanics ----
    brit = len(re.findall(r'\b\w+is(?:e|ed|ing|ation)\b', ms))
    amer = len(re.findall(r'\b\w+iz(?:e|ed|ing|ation)\b', ms))
    hy_ranges = re.findall(r'\b\d+(?:\.\d+)?-\d+(?:\.\d+)?\s?(?:ps|ns|fs|K|GPa|%|MPa)\b', ms)
    en_ranges = re.findall(r'\b\d+(?:\.\d+)?\u2013\d+(?:\.\d+)?', ms)
    dbl = len(re.findall(r'[A-z]  +[A-z]', ms))
    al = re.findall(r'et al[^.,;\s]', ms)
    sec = Counter(re.findall(r'\b(Section|Sections|Eq\.|Eq|Eqs|Figure|Figures|Fig\.|Table|Tables)\b', ms))
    print('\n== D mechanics: -ise %d / -ize %d | hyphen ranges %d / en-dash ranges %d | '
          'double spaces %d | "et al" unmarked %d' % (brit, amer, len(hy_ranges), len(en_ranges), dbl, len(al)))
    print('   reference-word counts:', dict(sec))
    print('   hyphen range examples:', hy_ranges[:8])
    print('   "et al" contexts:', [ms[max(0, m.start() - 40):m.start() + 25].replace('\n', ' ') for m in list(re.finditer(r'et al[^.,;\s]', ms))][:5])

    # ---- E readability ----
    longs = []
    for i, s in ms_p:
        if s.startswith('#'):
            continue
        for sen in sentences(s):
            w = len(re.findall(r"[A-Za-z\u00c0-\u024f'`-]+", re.sub(r'\$[^$]*\$', ' X ', sen)))
            if w >= 45:
                longs.append({'line': i, 'words': w, 'text': sen[:120]})
    longs.sort(key=lambda d: -d['words'])
    report('E sentences >= 45 words', ['ms:%d (%d w) %s…' % (d['line'], d['words'], d['text']) for d in longs])

    # ---- F acronyms ----
    alnum = Counter(re.findall(r'\b[A-Z]{2,6}\b', re.sub(r'\$[^$]*\$', ' ', ms)))
    gloss = set(re.findall(r'\(([A-Z]{2,6})\)', ms))
    bare = sorted(a for a in alnum if alnum[a] >= 2 and a not in gloss)
    print('\n== F acronyms with no "(X)" gloss anywhere:', [f'{a} x{alnum[a]}' for a in bare][:30])

    print('\nSUMMARY: A=%d B=%d C(dup)=%d C(shared)=%d E=%d F=%d' %
          (len([h for h in hits if h['word'] in ('Phase ', ' audit', 'gate', 'GATE', 'finding', 'ledger', 'A1', 'A2', 'A3', 're-check')]),
           len(bad), len(dups), len(shared), len(longs), len(bare)))
    out = {'internal': hits, 'banned': bad, 'dup_within': dups, 'dup_shared': shared,
           'long_sentences': longs, 'acronyms_unsupported': bare,
           'mechanics': {'ise': brit, 'ize': amer, 'hyphen_ranges': len(hy_ranges),
                         'en_ranges': len(en_ranges), 'double_spaces': dbl,
                         'et_al_unmarked': len(al), 'ref_words': dict(sec),
                         'acronyms': dict(alnum), 'glossed': sorted(gloss)}}
    (Path(__file__).resolve().parent / 'lang_audit.json').write_text(json.dumps(out, indent=1))
    print('wrote lang_audit.json')


if __name__ == '__main__':
    main()
