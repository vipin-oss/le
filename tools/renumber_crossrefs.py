#!/usr/bin/env python3
"""renumber_crossrefs.py — guard for the 2026-10-02 structural edit (now a check).

The manuscript was restructured from 7 sections / 21 subsections to 9 sections / 41 subsections
to match the required format, and extra tables were added.  Hard-coded cross-references in the
section builders therefore had to move; those edits have been applied and this script now only
*verifies* them, so that re-running it is safe and a later drift is caught:

  * the post-restructure string must be present the expected number of times;
  * the pre-restructure string must be gone.

Nothing scientific is touched here: no number, result, parameter or limitation is changed.
The live cross-reference check is tools/check_crossrefs.py, which validates every "Section x.y",
"Table n", "Fig. n" and "Eq. (n)" against the built manuscript.

Run from the repository root:  python3 tools/renumber_crossrefs.py
"""
import os
import sys

MS = os.path.join('PAPER_PROJECT', '13_Manuscript')

# (file, old, new, expected count)
EDITS = [
    # ---------------- ms_static.py
    ('ms_static.py',
     'two-relaxation-time kernel is carried along as an exploratory sensitivity variant only (Section 2.1)',
     'two-relaxation-time kernel is carried along as an exploratory sensitivity variant only (Section 2.5)', 1),
    ('ms_static.py',
     'Section 2 states the model, Section 3 the method, Section 4 the verification, Section 5 the results, and Section 6 '
     'the discussion, the limitations and the scope of what can be claimed from them.',
     'Section 2 states the governing equations and the constitutive framework, Section 3 the analytical results, '
     'Section 4 the numerical method, Section 5 the verification, Section 6 the results, and Section 7 the discussion, '
     'the limitations and the scope of what can be claimed from them. Section 8 concludes and Section 9 gives the code, '
     'the data package and the reproduction procedure.', 1),
    ('ms_static.py',
     'cross-checked against an independent three-dimensional rank-four implementation (Section 4.1)',
     'cross-checked against an independent three-dimensional rank-four implementation (Section 5.1)', 1),
    ('ms_static.py',
     'The quantities of interest are defined in Section 2.4.',
     'The quantities of interest are defined in Section 2.9 and their discrete forms in Section 4.7.', 1),
    ('ms_static.py',
     'are collected in Table 1.',
     'are collected in @@tab:params@@.', 1),
    ('ms_static.py',
     'continuum validity not established (Section 6)',
     'continuum validity not established (Section 7)', 1),
    ('ms_static.py',
     'The radial clustering parameter was chosen from a mesh-direction study (Section 4.2).',
     'The radial clustering parameter was chosen from a mesh-direction study (Section 5.2).', 1),
    # ---------------- ms_results.py
    ('build_manuscript.py',
     '(Section 4 lists the tests',
     '(Section 5 lists the tests', 1),
    ('ms_results.py',
     'The suite is summarised in Table 2,',
     'Summary of the verification suite (full table: supplementary material).', 1),
    ('ms_results.py',
     '(Table 6, Fig. 7)',
     'one tensor at a time made isotropic', 1),
    # ---------------- build_manuscript.py
    ('build_manuscript.py',
     'The symbols used in this paper are listed in Table 8.',
     'The symbols used in this paper are listed in @@tab:nom@@.', 1),
    ('build_manuscript.py',
     'radial integral of θ in Eq. (2)',
     'radial integrals of θ (a to R, a to r) in Eq. (@@eq:local@@)', 1),
]


def main():
    bad = 0
    for fname, old, new, want in EDITS:
        path = os.path.join(MS, fname)
        src = open(path, encoding='utf-8').read()
        n_new, n_old = src.count(new), src.count(old)
        if n_new != want or (n_old and old != new):
            print('  FAIL %s: post-restructure %r found %d (want %d); pre-restructure %r found %d'
                  % (fname, new[:52], n_new, want, old[:52], n_old))
            bad += 1
            continue
        print('  ok   %s: %r' % (fname, new[:58]))
    print('\n%s — %d edit(s) verified' % ('ALL EDITS IN PLACE' if not bad
                                          else 'DRIFT DETECTED', len(EDITS) - bad))
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main())
