#!/usr/bin/env python3
"""Phase 6 (part 3) patcher - A4, the AI disclosure.

Elsevier's guidance splits the two uses of AI: writing-process use belongs in the
"Declaration of Generative AI and AI-assisted technologies in the writing process"
above the references, research-process use belongs in the methods. The methods
disclosure already exists (build_manuscript.py, the "Software and AI assistance"
paragraph), so what changes here is the declaration itself:

  * the "[TEMPLATE - to be reviewed, edited and confirmed by the authors; ...]"
    wrapper is dropped - the audit gate and the author fill-in list carry that
    obligation instead of leaving editorial scaffolding in the manuscript text;
  * the platform-internals clause about which models the service runs is removed;
    the tool is named, which is what the Elsevier sentence asks for;
  * the wording follows the Elsevier template ("used X in order to Y", "reviewed
    and edited", "take(s) full responsibility"), states where the research-process
    use is recorded, and keeps the three safeguards (no AI-generated result, no
    AI-selected number, AI not an author and not citable);
  * nothing claims the tool acted independently.

The builders are the source of truth, so the change is applied there and the
documents are regenerated. Because the builders changed, both move from the
2026-10-03f freeze to 2026-10-03g and the companion's supersession list gains 03f.
"""
from pathlib import Path
import ast

ROOT = Path(__file__).resolve().parents[2]
MAN = ROOT / 'PAPER_PROJECT' / '13_Manuscript'

SENT = [
    "Declaration of Generative AI and AI-assisted technologies in the writing process. ",
    "During the preparation of this work the author(s) used a generative-AI assistant "
    "(Arena.ai Agent Mode) in order to draft and revise the text and the figure captions, "
    "and to check the internal consistency of the manuscript, the calculation companion and "
    "the tables. After using this tool the author(s) reviewed and edited the content as "
    "needed and take(s) full responsibility for the content of the publication. The "
    "research-process use of the same class of tool - reviewing and extending the numerical "
    "code and the verification suite, and running the simulations - is recorded with the "
    "numerical-methods section, as the journal policy directs. No AI tool generated a "
    "physical result and no AI tool produced or selected any number reported here; no AI "
    "tool acted without the author(s)' review, and no AI tool is an author or is cited as a "
    "source.",
]

BODY = SENT[1]


def esc(s):
    return s.replace('\\', '\\\\').replace("'", "\\'")


def main():
    p = MAN / 'build_manuscript.py'
    t = p.read_text()
    a = t.index("           ('p', '**Declaration of Generative AI")
    b = t.index("')]\n", a) + 3                      # up to and including the closing "')"
    head = "Declaration of Generative AI and AI-assisted technologies in the writing process."
    lead = "           ('p', '**" + head + "** '\n"
    parts = []
    chunk = BODY
    words = chunk.split(' ')
    line, size = [], 0
    for w in words:
        line.append(w)
        size += len(w) + 1
        if size > 96:
            parts.append(' '.join(line))
            line, size = [], 0
    if line:
        parts.append(' '.join(line))
    body = "".join("                 '" + esc(x) + " '\n" for x in parts[:-1])
    tail = "                 '" + esc(parts[-1]) + "')]\n"
    new = lead + body + tail
    out = t[:a] + new + t[b:]
    assert 'TEMPLATE' not in new and 'underlying models' not in new
    out = out.replace("SUB_FREEZE, PREV_FREEZE = 'submission_2026_10_03f', 'submission_2026_10_03e'",
                      "SUB_FREEZE, PREV_FREEZE = 'submission_2026_10_03g', 'submission_2026_10_03f'")
    assert "submission_2026_10_03g'" in out
    ast.parse(out)
    p.write_text(out)
    print('declaration replaced; manuscript builder at 03g')

    q = MAN / 'build_calculations.py'
    u = q.read_text()
    u = u.replace("SUB_FREEZE, PREV_FREEZE = 'submission_2026_10_03f', 'submission_2026_10_03e'",
                  "SUB_FREEZE, PREV_FREEZE = 'submission_2026_10_03g', 'submission_2026_10_03f'")
    u = u.replace("CODE_FREEZE_submission_2026_10_03e.json, CODE_FREEZE_submission_2026_10_03d.json",
                  "CODE_FREEZE_submission_2026_10_03f.json, CODE_FREEZE_submission_2026_10_03e.json, "
                  "CODE_FREEZE_submission_2026_10_03d.json", 1)
    ast.parse(u)
    q.write_text(u)
    print('companion builder at 03g, supersession list extended to 03f')


if __name__ == '__main__':
    main()
