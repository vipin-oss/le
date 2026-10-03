#!/usr/bin/env python3
"""Phase 6 (part 2) patcher: back-matter conformance for the IJHMT/Elsevier style.

1. build_manuscript.py
   * replaces the stale Data-availability sentence (it named the obsolete
     `CODE_FREEZE_v2_gate.json` and had a broken sentence boundary) with text
     that resolves the submitted freeze through `SUB_FREEZE` and cross-references
     Section 9.1 instead of repeating the package inventory;
   * adds an unnumbered Acknowledgements block ahead of the Declarations
     (Elsevier back-matter order: Acknowledgements, Declarations, Appendix,
     References), as an explicit author-input placeholder;
   * repairs the syntax defect introduced by an earlier incomplete patch of the
     same sentence.
2. tools/md_to_tex.py - 'Acknowledgements' becomes an unnumbered \\section* like
   'Declarations', so the LaTeX path does not renumber the back matter.
3. Both builders move to the 2026-10-03f freeze (the code changed, so the
   documents must be re-anchored), and the companion's supersession list gains
   2026-10-03d.

Every write is preceded by ast.parse, and the script is idempotent: already
patched files are reported and skipped.
"""
from pathlib import Path
import ast
import sys

ROOT = Path(__file__).resolve().parents[2]
MAN = ROOT / 'PAPER_PROJECT' / '13_Manuscript'

DA_NEW = """           ('p', '**Data availability:** the Python source code, verification suite, '
                 'per-run raw outputs (npz/json, including the frequency-domain transfer '
                 'values), analysis and figure scripts and the production matrix are provided '
                 'in the project data package, whose contents are fixed by the SHA-256 code '
                 f'freeze `CODE_FREEZE_{SUB_FREEZE}.json` described in Section 9.1; the package '
                 'will be deposited in a public repository under the persistent identifier '
                 'given at submission [REPOSITORY AND DOI: AUTHOR INPUT REQUIRED].'),
"""

ACK_NEW = """blocks += [('h1', 'Acknowledgements'),
           ('p', '[AUTHOR INPUT REQUIRED: acknowledge any funding, technical help or '
                 'computing facilities not already named in the Funding statement; omit this '
                 'section if there is nothing to acknowledge.]'),
           ]

"""


def note(msg):
    print(msg)


def patch_manuscript():
    p = MAN / 'build_manuscript.py'
    t = p.read_text()

    # --- 1. Data availability sentence (or the broken remnant of one) ---
    a = t.find("           ('p', '**Data availability:**")
    b = t.find("           ('p', '**Declaration of Generative AI")
    if t.find('f\'**Data availability:** the Python source code, verification suite, per-run raw outputs "') >= 0:
        a = t.find("           ('p', f'**Data availability:**")
    if a < 0 or b < 0 or b < a:
        note('data availability: block boundary not found - skipping')
        return False
    seg = t[a:b]
    changed = False
    if 'CODE_FREEZE_v2_gate' in seg or '{SUB_FREEZE}' not in seg or seg.count('\n') > 2:
        t = t[:a] + DA_NEW + t[b:]
        changed = True
        note('data availability: rewritten against the submitted freeze')
    else:
        note('data availability: already current')

    # --- 2. Acknowledgements before the Declarations ---
    if "('h1', 'Acknowledgements')" in t:
        note('acknowledgements: already present')
    else:
        anchor = "blocks += [('h1', 'Declarations'),"
        assert t.count(anchor) == 1
        t = t.replace(anchor, ACK_NEW + anchor, 1)
        changed = True
        note('acknowledgements: inserted before the Declarations')

    if changed:
        ast.parse(t)
        p.write_text(t)
    return changed


def patch_tex():
    q = ROOT / 'tools' / 'md_to_tex.py'
    u = q.read_text()
    old = "            if head == 'Declarations':                      # Elsevier: unnumbered, before the bib\n                out.append('\\\\section*{Declarations}')\n"
    new = ("            if head in ('Declarations', 'Acknowledgements'):   # Elsevier: unnumbered\n"
           "                out.append('\\\\section*{%s}' % head)\n")
    if new.split('\n')[0] in u:
        note('md_to_tex: already handles Acknowledgements')
        return False
    assert old in u, 'md_to_tex Declarations handler not recognised'
    u = u.replace(old, new, 1)
    ast.parse(u)
    q.write_text(u)
    note('md_to_tex: Acknowledgements emitted as \\section*')
    return True


def bump_freeze():
    moved = False
    for name in ('build_manuscript.py', 'build_calculations.py'):
        f = MAN / name
        s = f.read_text()
        s2 = s.replace("SUB_FREEZE, PREV_FREEZE = 'submission_2026_10_03e', 'submission_2026_10_03d'",
                       "SUB_FREEZE, PREV_FREEZE = 'submission_2026_10_03f', 'submission_2026_10_03e'")
        if s2 == s:
            if "'submission_2026_10_03f'" not in s2:
                note('%s: freeze line not recognised' % name)
            else:
                note('%s: already at 03f' % name)
            continue
        ast.parse(s2)
        f.write_text(s2)
        note('%s: freeze 03e -> 03f' % name)
        moved = True
    c = MAN / 'build_calculations.py'
    s = c.read_text()
    old = "'submission_2026_10_03c', 'submission_2026_10_03b'"
    if old in s and "'submission_2026_10_03d'" not in s:
        s2 = s.replace(old, "'submission_2026_10_03d', 'submission_2026_10_03c', 'submission_2026_10_03b'", 1)
        ast.parse(s2)
        c.write_text(s2)
        note('companion: supersession list extended to 03d')
    return moved


def main():
    for fn in (patch_manuscript, patch_tex, bump_freeze):
        fn()
    print('done')
    return 0


if __name__ == '__main__':
    sys.exit(main())
