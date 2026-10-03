"""Phase 2: keep the abstract inside the 250-word limit after the scope labels added for findings A8/A9.

Idempotent anchor-and-replace edits on the abstract template in build_manuscript.py.
"""
import ast, pathlib

REPS = [
    ("The response of a quiescent medium to one pulse is obtained from a ",
     "The single-pulse response is obtained from a "),
    ("and verified against exact \"", "verified against exact \""),
    ("stress of the circle is orientation-invariant to round-off and equals ",
     "stress is orientation-invariant to round-off: "),
    (" MPa/K. The ellipse converts", " MPa/K for the circle. The ellipse converts"),
    ("production grid), numerical uncertainty", "production grid) with numerical uncertainty"),
    ("among the dynamic runs alone); the residual size dependence is a quasi-static collapse in the memory number plus an O(",
     "among dynamic runs); the residual size dependence is a quasi-static collapse plus an O("),
    ("as the primary models and a two-relaxation-time ", "as primary models and a two-relaxation-time "),
    ("kernel as an exploratory variant.", "kernel as exploratory variant."),
]

p = pathlib.Path('PAPER_PROJECT/13_Manuscript/build_manuscript.py')
s = p.read_text()
i0 = s.index('abstract = (f"')
i1 = s.index('n_abs = len(abstract.split())')
body, done = s[i0:i1], []
for a, b in REPS:
    if a in body and b not in body:
        body = body.replace(a, b, 1)
        done.append(a[:34])
s = s[:i0] + body + s[i1:]
ast.parse(s)
p.write_text(s)
print('applied', len(done), 'of', len(REPS), 'trims:', '; '.join(x.strip()[:24] for x in done))
