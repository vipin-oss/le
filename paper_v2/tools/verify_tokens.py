#!/usr/bin/env python3
"""Token-exactness check: compare the working tree against a baseline copy of
main.tex + sections/*.tex.

For every file it compares multisets of
  * math fragments  ($...$, $$...$$, \[...\], \(...\), and math environments)
  * citation arguments (\cite, \citep, \citet, ...)
  * \\ref/\\cref/\\eqref/\\label arguments
  * numeric literals
and reports any file where a multiset differs.
"""
import re
import sys
from collections import Counter
from pathlib import Path

MATH_ENV = ("equation", "equation*", "align", "align*", "gather", "gather*",
            "multline", "multline*", "eqnarray", "eqnarray*", "split",
            "cases", "array")


def fragments(text):
    math = []
    for env in MATH_ENV:
        for m in re.finditer(r"\\begin\{" + re.escape(env) + r"\}(.*?)\\end\{"
                             + re.escape(env) + r"\}", text, re.S):
            math.append(re.sub(r"\s+", " ", m.group(1)).strip())
    t = re.sub(r"\\begin\{(equation|align|gather|multline|eqnarray)\*?\}.*?"
               r"\\end\{\1\*?\}", " ", text, flags=re.S)
    for pat in (r"\$\$(.*?)\$\$", r"\\\[(.*?)\\\]", r"(?<!\\)\$(.+?)(?<!\\)\$",
                r"\\\((.*?)\\\)"):
        for m in re.finditer(pat, t, re.S):
            math.append(re.sub(r"\s+", " ", m.group(1)).strip())
    cites, refs, nums = [], [], []
    for m in re.finditer(r"\\cite[a-zA-Z]*\*?(?:\[[^\]]*\])*\{([^{}]*)\}", text):
        cites.extend(k.strip() for k in m.group(1).split(","))
    for m in re.finditer(r"\\(?:cref|Cref|ref|eqref|label|autoref)\{([^{}]*)\}", text):
        refs.append(m.group(1).strip())
    body = re.sub(r"\\begin\{verbatim\}.*?\\end\{verbatim\}", " ", text, flags=re.S)
    for m in re.finditer(r"(?<![a-zA-Z\\{])\d+(?:\.\d+)?(?![a-zA-Z])", body):
        nums.append(m.group(0))
    return {"math": Counter(math), "cite": Counter(cites),
            "ref": Counter(refs), "num": Counter(nums)}


def main():
    base = Path(sys.argv[1])
    work = Path(sys.argv[2])
    files = ["main.tex"] + sorted(str(p.relative_to(work / "sections"))
                                  for p in (work / "sections").glob("*.tex"))
    bad = 0
    for rel in files:
        sub = "" if rel == "main.tex" else "sections/"
        wf = work / sub / rel
        bf = base / sub / rel
        if not bf.exists():
            print(f"MISSING BASELINE {rel}")
            bad += 1
            continue
        a = fragments(bf.read_text(encoding="utf-8", errors="replace"))
        b = fragments(wf.read_text(encoding="utf-8", errors="replace"))
        diffs = []
        for key in a:
            if a[key] != b[key]:
                missing = a[key] - b[key]
                extra = b[key] - a[key]
                diffs.append((key, missing, extra))
        if diffs:
            bad += 1
            print(f"\n=== {rel} ===")
            for key, missing, extra in diffs:
                if missing:
                    print(f"  {key} MISSING: {dict(list(missing.items())[:6])}")
                if extra:
                    print(f"  {key} EXTRA  : {dict(list(extra.items())[:6])}")
    print(f"\nfiles with differences: {bad} / {len(files)}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
