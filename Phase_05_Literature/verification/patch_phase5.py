#!/usr/bin/env python3
"""patch_phase5.py — Phase 5 (literature audit, introduction repositioning): the two additions the audit found
justified, applied where the prose is generated.

A13 asked for the classical Cattaneo (1948) and Vernotte (1958) papers to be cited. They are NOT added: no
DOI-bearing record for either original could be verified from here (the search evidence is in ../SEARCH_NOTES.md),
and the project rule is that a reference is added only when it can be verified. What the audit did find addable,
and what this script does, is to anchor the statements that were carried by nothing at all:

  * the passivity (positive-real) sentence of Section 2.2 -> Gurtin & Pipkin, Arch. Ration. Mech. Anal. 31(2),
    113-126 (1968), doi 10.1007/BF00281373, verified via the Crossref REST API on 2026-10-03;
  * the framework sentence of the introduction gains the same reference, so the finite-wave-speed generalisation
    is attributed to a primary theory paper and not only to the reviews and to Lord-Shulman [11].

The Richardson extrapolation already carries its methodological citation ([52], Richardson and Gaunt), so B19's
first half needed no change. Idempotent; anchors asserted; files parsed before writing.
"""
import ast
import json
from pathlib import Path

ROOT = Path('/home/user/le/PAPER_PROJECT')
MS = ROOT / '13_Manuscript'
LIT = ROOT / '01_Literature'

NEW = {
    "n": 55,
    "key": "gurtin1968",
    "text": ("Gurtin, M.E., Pipkin, A.C. A general theory of heat conduction with finite wave speeds. "
             "Archive for Rational Mechanics and Analysis, 31(2), 113-126 (1968). "
             "https://doi.org/10.1007/BF00281373"),
    "doi": "10.1007/BF00281373",
    "level": "METADATA VERIFIED (Crossref 2026-10-03, Phase 5 audit; query 'Gurtin Pipkin general theory heat "
             "conduction memory', fields title/authors/journal/volume/pages/year as returned by Crossref; full "
             "text not read)",
}
log = []

# ---------------------------------------------------------------- reference database
p = LIT / 'REFERENCES_VERIFIED.json'
J = json.loads(p.read_text())
if any(r.get('key') == NEW['key'] for r in J):
    log.append('REFERENCES_VERIFIED.json: already contains gurtin1968 (%d entries)' % len(J))
else:
    assert len(J) == 54, 'expected 54 entries, found %d' % len(J)
    J.append(NEW)
    p.write_text(json.dumps(J, indent=1) + '\n')
    log.append('REFERENCES_VERIFIED.json: entry 55 appended (54 -> 55)')

# ---------------------------------------------------------------- bib file (the .tex path reads this)
b = MS / 'FINAL_REVISED_REFERENCES.bib'
t = b.read_text()
if 'gurtin1968' in t:
    log.append('FINAL_REVISED_REFERENCES.bib: already contains gurtin1968')
else:
    b.write_text(t.rstrip() + """

@article{gurtin1968,
  author    = {Gurtin, Morton E. and Pipkin, A. C.},
  title     = {A general theory of heat conduction with finite wave speeds},
  journal   = {Archive for Rational Mechanics and Analysis},
  volume    = {31},
  number    = {2},
  pages     = {113-126},
  year      = {1968},
  doi       = {10.1007/BF00281373},
}
""")
    log.append('FINAL_REVISED_REFERENCES.bib: @article{gurtin1968} appended')

# ---------------------------------------------------------------- Section 2.2 passivity sentence
d = MS / 'ms_derivation.py'
t = d.read_text()
OLD = "'kernel; the two-relaxation-time kernel of Section 2.5 is positive-real for the same reason but is not derived '"
NEW_S = ("'kernel [55], a restriction stated there for a memory kernel rather than for a single relaxation time; the '\n"
         "              'two-relaxation-time kernel of Section 2.5 is positive-real for the same reason but is not derived '")
if 'kernel [55], a restriction stated there' in t:
    log.append('ms_derivation.py: passivity sentence already cites [55]')
else:
    assert t.count(OLD) == 1, 'passivity sentence not found in ms_derivation.py'
    t = t.replace(OLD, NEW_S, 1)
    ast.parse(t)
    d.write_text(t)
    log.append('ms_derivation.py: the passivity statement now carries [55]')

# ---------------------------------------------------------------- Introduction 1.2 framework sentence
s = MS / 'ms_static.py'
t = s.read_text()
NEEDLE = "its extension to anisotropic media with a uniqueness theorem [12]"
ADD = ("its extension to anisotropic media with a uniqueness theorem [12]; the general theory of heat conduction "
       "with a memory kernel and finite wave speeds is due to Gurtin and Pipkin [55]")
if 'Gurtin and Pipkin [55]' in t:
    log.append('ms_static.py: introduction framework sentence already extended')
else:
    assert t.count(NEEDLE) == 1, 'framework sentence not found in ms_static.py (count=%d)' % t.count(NEEDLE)
    t = t.replace(NEEDLE, ADD, 1)
    ast.parse(t)
    s.write_text(t)
    log.append('ms_static.py: introduction 1.2 now names the primary theory reference')

print('\n'.join('  ' + x for x in log))
