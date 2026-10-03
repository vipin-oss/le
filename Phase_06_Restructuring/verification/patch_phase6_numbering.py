#!/usr/bin/env python3
"""patch_phase6_numbering.py — Q1 (Elsevier numbered style) conformance for the reference apparatus.

Two changes, both made in the generators so that the documents stay reproducible:

 1. Sequential numbering. IJHMT uses the numbered style, where the list order is the order of first citation.
    The list was thematic (grouped by topic), so Section 1.1 cited [7] before [6] and [48]-[51] before [10].
    Here the citation numbers in the generated text are remapped to order-of-first-appearance and the reference
    list is reprinted in that order; the mapping is written to 13_Manuscript/REF_ORDER.json and the ordered list
    to 13_Manuscript/REFERENCES_ORDERED.json, which the companion builder and tools/md_to_tex.py then use so
    that the Markdown, the companion's "manuscript reference [n]" pointers and the .tex \\cite mapping cannot
    disagree. 01_Literature/REFERENCES_VERIFIED.json is left untouched (it is the verification record, keyed by
    its own order and by the Crossref date of each check).

 2. Back-matter order. Appendix A currently prints after the References; Elsevier's order is text,
    declarations, appendix, references. The block order is changed in build_manuscript.py.

Diagnostical output first (which bracket groups were treated as citations), then the edits. Idempotent.
"""
import ast
import json
import re
import sys
from pathlib import Path

MS = Path('/home/user/le/PAPER_PROJECT/13_Manuscript')
NREFS = 55
GROUP = re.compile(r'\[(\d{1,2}(?:\s*[,;-]\s*\d{1,2})*)\]')


def nums(text):
    out = []
    for part in re.split(r'[,;]', text):
        part = part.strip()
        if '-' in part:
            lo, hi = part.split('-')
            if lo.isdigit() and hi.isdigit():
                out.extend(range(int(lo), int(hi) + 1))
        elif part.isdigit():
            out.append(int(part))
        else:
            return None
    if not out or any(n < 1 or n > NREFS for n in out):
        return None
    return out


refs = json.loads(Path('/home/user/le/PAPER_PROJECT/01_Literature/REFERENCES_VERIFIED.json').read_text())
assert len(refs) == NREFS, len(refs)

# ---------------------------------------------------------------- build the map from the current text
bm = MS / 'build_manuscript.py'
t = bm.read_text()
if 'REF_ORDER.json' in t:
    print('build_manuscript.py already carries the numbering pass - skipping')
    sys.exit(0)

# Render the block texts that contain citations by harvesting the source strings that end up in the document:
# the blocks are built across modules, so the map is computed at build time inside build_manuscript.py. The
# script therefore inserts a pass there rather than computing the map here, but it needs to know what counts as
# a citation, so it reports the groups found in the *current* document for review.
cur = (MS / 'manuscript_IJHMT.md').read_text()
seen, skipped = [], []
for line in cur.split('\n'):
    if line.startswith('|'):
        continue
    for m in GROUP.finditer(line):
        (seen if nums(m.group(1)) else skipped).append(m.group(0))
print('citation groups recognised in prose: %d (distinct %s)' % (len(seen), sorted(set(seen))[:12]))
print('bracket groups left alone: %d, e.g. %s' % (len(skipped), sorted(set(skipped))[:10]))

PASS_SRC = '''
# ------------------------------------------------------------------ Elsevier numbered style: sequential citations
_CITE = re.compile(r'\\[(\\d{1,2}(?:\\s*[,;-]\\s*\\d{1,2})*)\\]')


def _cite_nums(text):
    out = []
    for part in re.split(r'[,;]', text):
        part = part.strip()
        if '-' in part:
            lo, hi = part.split('-')
            if lo.isdigit() and hi.isdigit():
                out.extend(range(int(lo), int(hi) + 1))
        elif part.isdigit():
            out.append(int(part))
        else:
            return None
    if not out or any(n < 1 or n > len(refs) for n in out):
        return None
    return out


def _sequentialise(blocks):
    """Renumber [n] citations to order of first appearance and reorder the printed list to match.

    Only prose/table blocks are scanned for first appearances (the reference list itself is not a citation); a
    bracket group counts only when every number is a valid reference index, so grid sizes and percentages in
    square brackets are left alone. The mapping is written for tools/md_to_tex.py and for the companion
    builder, which point at the same numbers.
    """
    order, body = [], []
    for kind, txt in blocks:
        if kind == 'refs':
            continue
        if isinstance(txt, str):
            for m in _CITE.finditer(txt):
                for n in (_cite_nums(m.group(1)) or []):
                    if n not in order:
                        order.append(n)
    for n in range(1, len(refs) + 1):
        if n not in order:
            order.append(n)                      # uncited entries keep their relative order at the end
    new_of = {old: i + 1 for i, old in enumerate(order)}

    def remap(txt):
        def sub(m):
            ns = _cite_nums(m.group(1))
            if not ns:
                return m.group(0)
            return '[' + ','.join(str(new_of[n]) for n in ns) + ']'
        return _CITE.sub(sub, txt)

    out = [(k, remap(x) if isinstance(x, str) else x) for k, x in blocks]
    ordered = [dict(refs[old - 1], n=i + 1) for i, old in enumerate(order)]
    out = [(k, [x['text'] for x in ordered]) if k == 'refs' else (k, v) for k, v in out]
    json.dump({'old_to_new': {str(k): v for k, v in new_of.items()},
               'order': order, 'n_refs': len(refs)},
              open(os.path.join(MS, 'REF_ORDER.json'), 'w'), indent=1)
    json.dump(ordered, open(os.path.join(MS, 'REFERENCES_ORDERED.json'), 'w'), indent=1)
    return out, sum(1 for old, new in new_of.items() if old != new)


_blocks_pre = blocks
blocks, n_moved = _sequentialise(blocks)
print('sequential citation numbering: %d of %d entries changed number' % (n_moved, len(refs)))

# ------------------------------------------------------------------ back matter order (Elsevier)
_i_app = next(i for i, b in enumerate(blocks) if b[0] == 'h1' and b[1].startswith('Appendix A'))
_i_ref = next(i for i, b in enumerate(blocks) if b[0] == 'h1' and b[1] == 'References')
if _i_app > _i_ref:                               # text, declarations, appendix, references
    _i_end = _i_app + 1
    while _i_end < len(blocks) and not (blocks[_i_end][0] == 'h1'):
        _i_end += 1
    blk = blocks[_i_app:_i_end]
    blocks = blocks[:_i_app] + blocks[_i_end:]
    _i_ref = next(i for i, b in enumerate(blocks) if b[0] == 'h1' and b[1] == 'References')
    blocks = blocks[:_i_ref] + blk + blocks[_i_ref:]
    print('back matter: Appendix A moved before the References (Elsevier order)')
'''

anchor = "\n# The placeholder guard must see the text being generated"
assert anchor in t, 'guard anchor not found - inspect build_manuscript.py before editing'
i = t.index(anchor)
t = t[:i] + "\n" + PASS_SRC + t[i:]
ast.parse(t)
bm.write_text(t)
print('build_manuscript.py: numbering pass + back-matter order inserted')

# ---------------------------------------------------------------- md_to_tex: use the ordered list
mt = Path('/home/user/le/tools/md_to_tex.py')
t = mt.read_text()
old = "REFS = os.path.join(ROOT, 'PAPER_PROJECT', '01_Literature', 'REFERENCES_VERIFIED.json')"
if 'REFERENCES_ORDERED' in t:
    print('md_to_tex.py: already prefers the ordered list')
else:
    new = (old + "\n_ORDERED = os.path.join(ROOT, 'PAPER_PROJECT', '13_Manuscript', 'REFERENCES_ORDERED.json')\n"
           "if os.path.exists(_ORDERED):      # the manuscript prints its list in order of first citation; the .tex\n"
           "    REFS = _ORDERED               # \\cite mapping must use the same numbering or the two disagree\n")
    t = t.replace(old, new, 1)
    ast.parse(t)
    mt.write_text(t)
    print('md_to_tex.py: number -> key mapping now follows the printed order')

# ---------------------------------------------------------------- companion: same numbers
bc = MS / 'build_calculations.py'
t = bc.read_text()
if 'REF_ORDER.json' in t:
    print('build_calculations.py: already remaps its manuscript pointers')
else:
    helper = '''

# The manuscript numbers its references by order of first citation (Elsevier numbered style); a pointer written
# here as [55] must follow the same mapping, so it is read from the file the manuscript builder wrote.
try:
    _RO = json.load(open(os.path.join(HERE, 'REF_ORDER.json')))['old_to_new']
except (OSError, ValueError, KeyError):
    _RO = {}   # fall back to the numbers as written


def _msref(n):
    return _RO.get(str(n), n)
'''
    i = t.index('\ndef para')
    assert 'HERE = ' in t or 'os.path.dirname' in t, 'no HERE/dirname in build_calculations'
    t = t[:i] + helper + t[i:]
    first = "para('Both non-Fourier kernels are positive-real (passive) for real"
    old = "manuscript reference [55]); '"
    assert first in t and t.count(old) == 1
    t = t.replace(first, "para(f'Both non-Fourier kernels are positive-real (passive) for real", 1)
    t = t.replace(old, "manuscript reference {_msref(55)}); '", 1)
    ast.parse(t)
    bc.write_text(t)
    print('build_calculations.py: pointers now remapped through REF_ORDER.json')
print('done')
