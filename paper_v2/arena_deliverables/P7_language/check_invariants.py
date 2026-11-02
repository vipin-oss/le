#!/usr/bin/env python3
"""Invariant gate for the P7 language pass.

Every rewritten section is compared against its original in paper_v2/overleaf_package.zip (the
abstract against abstract_original.tex, which is the front matter copied verbatim out of main.tex).
Six things must be identical, as multisets unless stated otherwise:

  (a) the content of every equation environment, character for character
  (b) \\label, \\eqref, \\cref, \\Cref, \\ref (and \\autoref, \\pageref) with their arguments
  (c) the keys inside every \\cite* command
  (d) every number token (decimal, integer, scientific)
  (e) the sequence of \\begin/\\end environments, in order
  (f) every \\path{...} and \\texttt{...} argument

A section that fails any of these must not be shipped: the original stays, and the failure is
written to FAILED_INVARIANTS.csv with the reason. Prints PASS and exits 0 only when every
rewritten file passes.

Usage:
  python3 check_invariants.py                 # check every .tex here against the zip
  python3 check_invariants.py --file s01_intro.tex
  python3 check_invariants.py --zip ../overleaf_package.zip --verbose
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
import unicodedata
import zipfile
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
PAPER = HERE.parent.parent
DEFAULT_ZIP = PAPER / "overleaf_package.zip"
FAILED = HERE / "FAILED_INVARIANTS.csv"

EQ_ENVS = r"(?:equation|align|gather|multline|eqnarray|flalign|alignat|displaymath)\*?"


def strip_comments(tex: str) -> str:
    """Drop LaTeX comments so a comment cannot smuggle a number or a label past the gate."""
    out = []
    for line in tex.splitlines():
        m = re.search(r"(?<!\\)%", line)
        out.append(line[: m.start()] if m else line)
    return "\n".join(out)


def equations(tex: str) -> list[str]:
    tex = strip_comments(tex)
    found = re.findall(r"\\begin\{(" + EQ_ENVS + r")\}(.*?)\\end\{\1\}", tex, flags=re.S)
    block = [m.group(0) for m in re.finditer(r"\\\[(.*?)\\\]", tex, flags=re.S)]
    dollar = [m.group(0) for m in re.finditer(r"(?<!\\)\$\$(.*?)(?<!\\)\$\$", tex, flags=re.S)]
    return [" ".join(x[1].split()) for x in found] + [" ".join(b.split()) for b in block + dollar]


REF_RE = re.compile(r"\\(label|eqref|cref|Cref|ref|autoref|pageref|nameref)\*?\{([^}]*)\}")
CITE_RE = re.compile(r"\\cite[a-zA-Z]*\*?(?:\s*\[[^\]]*\]){0,2}\s*\{([^}]*)\}")
NUM_RE = re.compile(r"(?<![\w.])\d+(?:\.\d+)?(?:[eE][+-]?\d+)?")
ENV_RE = re.compile(r"\\(begin|end)\s*\{([^}]*)\}")
PATH_RE = re.compile(r"\\(path|texttt)\s*\{([^}]*)\}")


def facts(tex: str) -> dict:
    clean = strip_comments(tex)
    refs = Counter((m.group(1), m.group(2).strip()) for m in REF_RE.finditer(clean))
    cites = Counter()
    for m in CITE_RE.finditer(clean):
        for key in m.group(1).split(","):
            if key.strip():
                cites[key.strip()] += 1
    nums = Counter(NUM_RE.findall(clean))
    envs = [(m.group(1), m.group(2).strip()) for m in ENV_RE.finditer(clean)]
    paths = Counter((m.group(1), m.group(2)) for m in PATH_RE.finditer(clean))
    return {"equations": equations(tex), "refs": refs, "cites": cites, "numbers": nums,
            "environments": envs, "paths": paths}


def describe(name: str, a, b) -> str:
    """Say what differs between two multisets/lists, in a form a human can act on."""
    if isinstance(a, list):
        if len(a) != len(b):
            return f"{name}: {len(a)} in the original, {len(b)} in the rewrite"
        for i, (x, y) in enumerate(zip(a, b)):
            if x != y:
                return f"{name}: block {i + 1} differs ({x[:60]!r} vs {y[:60]!r})"
        return f"{name}: differs"
    missing, extra = a - b, b - a
    bits = []
    if missing:
        bits.append("missing " + ", ".join(f"{k}x{v}" if isinstance(k, tuple) and v > 1 else str(k)
                                           for k, v in list(missing.items())[:6]))
    if extra:
        bits.append("extra " + ", ".join(f"{k}x{v}" if isinstance(k, tuple) and v > 1 else str(k)
                                         for k, v in list(extra.items())[:6]))
    return f"{name}: " + "; ".join(bits)


def compare(original: str, rewrite: str) -> list[str]:
    fo, fr = facts(original), facts(rewrite)
    problems = []
    if len(fo["equations"]) != len(fr["equations"]):
        problems.append(describe("equation environments", fo["equations"], fr["equations"]))
    else:
        for i, (x, y) in enumerate(zip(fo["equations"], fr["equations"])):
            if x != y:
                problems.append(f"equation block {i + 1} content changed: "
                                f"{x[:70]!r} -> {y[:70]!r}")
    for key, label in (("refs", "refs/labels"), ("cites", "cite keys"), ("numbers", "numbers"),
                       ("paths", r"\path/\texttt"), ("environments", "environment sequence")):
        if fo[key] != fr[key]:
            problems.append(describe(label, fo[key], fr[key]))
    return problems


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--zip", default=str(DEFAULT_ZIP))
    ap.add_argument("--file", action="append", help="only this rewritten file (may repeat)")
    ap.add_argument("--verbose", action="store_true")
    a = ap.parse_args()

    zpath = Path(a.zip).resolve()
    if not zpath.exists():
        print(f"FAIL original package not found: {zpath}")
        return 1
    originals = {}
    with zipfile.ZipFile(zpath) as z:
        for n in z.namelist():
            if n.startswith("sections/") and n.endswith(".tex"):
                originals[n.split("/")[-1]] = z.read(n).decode("utf-8", "ignore")

    base = HERE / "abstract_original.tex"
    if base.exists():
        originals["abstract.tex"] = base.read_text(encoding="utf-8")

    rewritten = sorted(p for p in HERE.glob("*.tex") if p.name != "abstract_original.tex")
    if a.file:
        wanted = set(a.file)
        rewritten = [p for p in rewritten if p.name in wanted]

    rows, ok, bad = [], 0, 0
    for p in rewritten:
        name = p.name
        if name not in originals:
            rows.append({"file": name, "verdict": "FAIL", "reason": "no original in the package"})
            print(f"FAIL {name}: no original in the package")
            bad += 1
            continue
        problems = compare(originals[name], p.read_text(encoding="utf-8"))
        if problems:
            bad += 1
            rows.append({"file": name, "verdict": "FAIL", "reason": " | ".join(problems)})
            print(f"FAIL {name}: {' | '.join(problems)[:300]}")
        else:
            ok += 1
            rows.append({"file": name, "verdict": "PASS", "reason": ""})
            if a.verbose:
                f = facts(originals[name])
                print(f"PASS {name}: equations {len(f['equations'])}, refs {sum(f['refs'].values())}, "
                      f"cite keys {sum(f['cites'].values())}, numbers {sum(f['numbers'].values())}, "
                      f"environments {len(f['environments'])}, paths {sum(f['paths'].values())}")

    with FAILED.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["file", "verdict", "reason"])
        w.writeheader()
        w.writerows(rows)

    if not rewritten:
        print("FAIL nothing to check")
        return 1
    print(f"checked {len(rewritten)} rewritten file(s): {ok} PASS, {bad} FAIL")
    if bad:
        print("FAIL")
        return 1
    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
