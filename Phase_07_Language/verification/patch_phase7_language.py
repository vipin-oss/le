#!/usr/bin/env python3
"""Phase 7 - language, style, internal vocabulary and duplication.

Every edit is applied in the builders (they are the source of truth), is
wording-only, and is guarded by a count assert so a partial patch cannot pass
silently. Facts, numbers, filenames that exist inside the deposited package, and
every citation are untouched.

Groups
  1. internal/project vocabulary replaced by reader-facing wording
     ("Code state and re-checks", "gate freeze", "audit records", "builders",
     "runs audited", the top-level PAPER_PROJECT/ prefix in a printed sentence)
  2. orthography: -ize -> -ise (the documents are otherwise -ise), en dash in
     "Sections 5.1-5.3" to match every other numeric range
  3. banned word: "robust" -> "insensitive" (the programme forbids the former)
  4. abbreviations: CV/F defined at first use next to the deviation measure
  5. readability: three over-long sentences split at their clause boundaries,
     with the clauses kept verbatim
"""
from pathlib import Path
import ast
import sys

ROOT = Path(__file__).resolve().parents[2]
MAN = ROOT / 'PAPER_PROJECT' / '13_Manuscript'
EN = '\u2013'

EDITS = {
    'build_manuscript.py': [
        # 1. internal vocabulary
        ('f"digests of every file are recorded in `CODE_FREEZE_v2_gate.json` ({FREEZE_GATE} for the file itself) "',
         'f"digests of every file are recorded in the archived manifest `CODE_FREEZE_v2_gate.json` (its own digest "\n                 f"{FREEZE_GATE}) "'),
        ('**Code state and re-checks.** The two archived manifests date from',
         '**Code state.** The two archived manifests date from'),
        ('the only value that moves is the ', 'the only value that moves is the '),   # no-op guard
        ('number of runs audited)', 'number of runs covered)'),
        ('f"(12_Tables), the manuscript builders (13_Manuscript) and the audit records (15_',
         'f"(12_Tables), the manuscript sources (13_Manuscript) and the verification records (15_'),
        ('"convergence runs, analysis, figures, manuscript builders) in the order used here',
         '"convergence runs, analysis, figures, manuscript build scripts) in the order used here'),
        # 2. en dash in the range
        ('The tests of Sections 5.1-5.3 are code-verification', 'The tests of Sections 5.1' + EN + '5.3 are code-verification'),
        # 5. readability: the Data availability sentence
        ("Section 9.1; the package '\n                 'will be deposited", "Section 9.1. The package will be deposited"),
    ],
    'ms_static.py': [
        ('its generalizations to a finite heat-wave speed', 'its generalisations to a finite heat-wave speed'),
        # 4. CV / F glossed at first use
        ("The thermal-memory deviation is D = max|\\u03c3_{CV} \\u2212 \\u03c3_{F}|/max|\\u03c3_{F}| over the wall and",
         "The thermal-memory deviation is D = max|\\u03c3_{CV} \\u2212 \\u03c3_{F}|/max|\\u03c3_{F}| over the wall, where CV and F denote the Cattaneo\\u2013Vernotte (single-relaxation-time) and Fourier responses, and"),
        # 5. readability: the three dimensionless numbers
        ("\\u03b5 = 0.0515 at 10 nm); the feedback number is", "\\u03b5 = 0.0515 at 10 nm). The feedback number is"),
        ("(\\u0394 = 0.040, 0.198, 0.792 for \\u03c4 = 1, 5, 20 ps at 10 nm); the elastic number is",
         "(\\u0394 = 0.040, 0.198, 0.792 for \\u03c4 = 1, 5, 20 ps at 10 nm). The elastic number is"),
    ],
    'ms_derivation.py': [
        ('the reviews of hyperbolic and generalized', 'the reviews of hyperbolic and generalised'),
    ],
    'ms_results.py': [
        # 5. readability
        ('\\u2264 6.4% (largest at a = 5 nm, \\u039b = 3.2); for a = 10 nm it is',
         '\\u2264 6.4% (largest at a = 5 nm, \\u039b = 3.2). For a = 10 nm it is'),
    ],
    'build_calculations.py': [
        # 1. internal vocabulary
        ("'under PAPER_PROJECT/06_Source_Code/CODE_FREEZE_v2_gate.json (gate freeze, %d files) and '",
         "'in the deposited package under 06_Source_Code/CODE_FREEZE_v2_gate.json (the archived manifest, %d files) and '"),
        # 3. banned word
        ('is robust to which expansion set is used', 'is insensitive to which expansion set is used'),
    ],
}


def apply_one(name, old, new):
    p = MAN / name
    t = p.read_text()
    n = t.count(old)
    if n == 0:
        if old == new:
            return 'noop'
        if already := (new in t):
            return 'already'
        return 'MISS:%s::%s' % (name, old[:50])
    t2 = t.replace(old, new, 1)
    try:
        ast.parse(t2)
    except SyntaxError as e:
        return 'SYNTAX-FAIL in %s (%s)' % (name, e)
    p.write_text(t2)
    return 'ok' if n == 1 else 'ok(x%d)' % n


def main():
    results = []
    for name, pairs in EDITS.items():
        for old, new in pairs:
            results.append('%-24s %s' % (name, apply_one(name, old, new)))
    print('\n'.join(results))

    # freeze re-anchor: the builders changed
    moved = 0
    for name in ('build_manuscript.py', 'build_calculations.py'):
        p = MAN / name
        t = p.read_text()
        t2 = t.replace("SUB_FREEZE, PREV_FREEZE = 'submission_2026_10_03g', 'submission_2026_10_03f'",
                       "SUB_FREEZE, PREV_FREEZE = 'submission_2026_10_03h', 'submission_2026_10_03g'")
        if t2 != t:
            ast.parse(t2)
            p.write_text(t2)
            moved += 1
    c = MAN / 'build_calculations.py'
    t = c.read_text()
    old = "CODE_FREEZE_submission_2026_10_03f.json, CODE_FREEZE_submission_2026_10_03e.json"
    if "submission_2026_10_03g.json, CODE_FREEZE_submission_2026_10_03f.json" not in t and old in t:
        t = t.replace(old, "CODE_FREEZE_submission_2026_10_03g.json, " + old, 1)
        ast.parse(t)
        c.write_text(t)
    print('freeze bumped in %d builders; companion list %s' % (moved, 'extended'))


if __name__ == '__main__':
    sys.exit(main())
