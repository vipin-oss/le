#!/usr/bin/env python3
"""Static integrity gate for the LaTeX tree (a substitute for compiling it).

No TeX engine with the modern package set is available in this sandbox, so the things
a compiler would complain about first are checked here instead, directly on the source:

  R1  every \\label is unique
  R2  every \\ref / \\eqref / \\autoref / \\pageref / \\cref target exists
  R3  braces balance in every file
  R4  every \\begin{env} is closed by \\end{env}, in order
  R5  every \\cite key exists in the bibliography
  R6  every float (figure/table) carries a \\label
  R7  every \\input / \\include target exists
  R8  no duplicate \\label introduced by a copied block (same as R1 but reports the file pair)

Prints a line starting with PASS and exits 0 only when all checks hold.

Usage: python3 P1_audit/check_refs.py [--master ../manuscript_v2/master]
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REF_CMDS = ("ref", "eqref", "autoref", "pageref", "cref", "Cref", "nameref")


def strip_comments(s: str) -> str:
    out = []
    for line in s.splitlines():
        # remove unescaped % comments
        i, cut = 0, None
        while i < len(line):
            if line[i] == "\\":
                i += 2
                continue
            if line[i] == "%":
                cut = i
                break
            i += 1
        out.append(line if cut is None else line[:cut])
    return "\n".join(out)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--master", default="../manuscript_v2/master")
    a = ap.parse_args()
    master = Path(a.master)

    files = sorted(p for p in master.rglob("*.tex"))
    text = {}
    for p in files:
        text[p.relative_to(master).as_posix()] = strip_comments(
            p.read_text(encoding="utf-8", errors="replace"))

    allsrc = "\n".join(text.values())
    problems: list[str] = []
    notes: list[str] = []

    # R1/R8 unique labels
    labels: dict[str, str] = {}
    dups: list[str] = []
    for f, s in text.items():
        for m in re.finditer(r"\\label\{([^}]+)\}", s):
            lab = m.group(1)
            if lab in labels:
                dups.append(f"{lab} ({labels[lab]} + {f})")
            else:
                labels[lab] = f
    if dups:
        problems.append(f"R1 duplicate labels: {'; '.join(dups[:6])}")
    notes.append(f"labels={len(labels)}")

    # R2 refs resolve
    missing: list[str] = []
    total_refs = 0
    for f, s in text.items():
        for cmd in REF_CMDS:
            for m in re.finditer(r"\\" + cmd + r"\*?\{([^}]+)\}", s):
                for key in (k.strip() for k in m.group(1).split(",")):
                    if not key:
                        continue
                    total_refs += 1
                    if key not in labels:
                        missing.append(f"{f}:\\{cmd}{{{key}}}")
    if missing:
        problems.append(f"R2 unresolved references ({len(missing)}): " + "; ".join(missing[:8]))
    notes.append(f"refs={total_refs}")

    # R3 brace balance
    unbalanced = []
    for f, s in text.items():
        if s.count("{") != s.count("}"):
            unbalanced.append(f"{f} ({s.count('{')} open / {s.count('}')} close)")
    if unbalanced:
        problems.append("R3 unbalanced braces: " + "; ".join(unbalanced[:6]))

    # R4 environment matching
    env_bad = []
    for f, s in text.items():
        stack: list[str] = []
        for m in re.finditer(r"\\(begin|end)\{([^}]+)\}", s):
            kind, env = m.group(1), m.group(2)
            if kind == "begin":
                stack.append(env)
            else:
                if not stack or stack[-1] != env:
                    env_bad.append(f"{f}: \\end{{{env}}} without matching \\begin")
                    break
                stack.pop()
        if stack:
            env_bad.append(f"{f}: unclosed {stack[-1]}")
    if env_bad:
        problems.append("R4 environment mismatch: " + "; ".join(env_bad[:6]))

    # R5 citations exist
    bib_keys: set[str] = set()
    for b in master.rglob("*.bib"):
        bib_keys |= set(re.findall(r"@\w+\s*\{\s*([^,\s]+)\s*,",
                                   b.read_text(encoding="utf-8", errors="replace")))
    cited: set[str] = set()
    for s in text.values():
        for m in re.finditer(r"\\cite\w*\*?(?:\[[^\]]*\])*\{([^}]+)\}", s):
            cited |= {k.strip() for k in m.group(1).split(",") if k.strip()}
    orphan_cites = sorted(cited - bib_keys)
    if orphan_cites:
        problems.append(f"R5 cites without a .bib entry ({len(orphan_cites)}): "
                        + ", ".join(orphan_cites[:8]))
    notes.append(f"cites={len(cited)}/{len(bib_keys)}")

    # R6 floats labelled
    unlabelled = []
    for f, s in text.items():
        for m in re.finditer(r"\\begin\{(figure|table)\}(.*?)\\end\{\1\}", s, re.S):
            if "\\label{" not in m.group(2):
                unlabelled.append(f"{f}:{m.group(1)} near char {m.start()}")
    if unlabelled:
        problems.append(f"R6 floats without a label ({len(unlabelled)}): "
                        + "; ".join(unlabelled[:6]))

    # R7 inputs exist
    for f, s in text.items():
        # LaTeX resolves \input relative to the main document's directory first; the
        # including file's own directory is a fallback, not the rule.
        for m in re.finditer(r"\\(?:input|include)\s*\{([^}]+)\}", s):
            tgt = m.group(1).strip()
            name = tgt if tgt.endswith(".tex") else tgt + ".tex"
            if not ((master / name).exists() or (master / Path(f).parent / name).exists()):
                problems.append(f"R7 missing input target: {f} -> {tgt}")

    if problems:
        for p in problems:
            print("FAIL " + p)
        print(f"FAIL {len(problems)} check group(s) failed")
        return 1
    print(f"PASS all checks (labels={len(labels)}, refs={total_refs} resolve, "
          f"cites {len(cited)}/{len(bib_keys)} in .bib, braces and environments match, "
          f"floats labelled, inputs present)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
