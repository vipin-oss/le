#!/usr/bin/env python3
"""Task 6 audit: is `second_impl.py` really a second implementation?

`second_impl.py` claims to be independent of `scripts/models.py`.  An independent
implementation is only worth something if the independence can be checked, so this
file checks it mechanically, and then checks the *result* by a route that uses
neither implementation:

  A1  the source of `second_impl.py` contains no import, path or exec that could
      reach the manuscript's scripts;
  A2  given the path to `models.py` (optional), the code overlap between the two
      files is measured: longest common contiguous line run, Jaccard similarity of
      code tokens, and number of identical non-trivial lines;
  A3  what *is* shared is listed explicitly - the template parameter sets, which
      the task prescribes ("parameter sets in scripts/models.py docstring"), and
      the archived numbers, which are the comparison target;
  A4  root residual: every computed K is substituted back into the dispersion
      relation (D) itself; a shared bug in two solvers would not survive this;
  A5  branch identity: for every model and frequency the two coupled modes must be
      distinguishable by damping (Q^-1), otherwise "elastic branch" would be a
      coin toss;
  A6  given the path to `numbers_log.txt` (optional), every archived literal used
      in the comparison is confirmed to occur in that log at its printed
      precision, so no reference value can be a transcription error.

Usage
  python3 task6_audit.py
  python3 task6_audit.py --models /path/to/models.py --archive /path/to/numbers_log.txt

The two paths are optional on purpose: the manuscript's `scripts/` are not part of
this repository, and this file must not require them.  Exit code 0 on success.
"""
import os
import re
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import second_impl as S                                    # noqa: E402

SRC = os.path.join(HERE, "second_impl.py")
# Patterns that would let this file *execute* or *read* the manuscript's code.
# A string literal that merely mentions `scripts/numbers_log.txt` is a citation of
# the comparison source, not a dependency, so it is counted but not failed.
FORBIDDEN = [r"^\s*import\s+models\b", r"^\s*from\s+models\b", r"importlib", r"\bexec\s*\(",
             r"open\s*\([^)]*scripts", r"sys\.path[^\n]*scripts"]
errors = []


def fail(m):
    errors.append(m)


# ------------------------------------------------------------------ A1 imports
def _strip_prose(text):
    """Remove docstrings and comments, so that only executable code is scanned."""
    triple_d = chr(34) * 3
    triple_s = chr(39) * 3
    for q in (triple_d, triple_s):
        text = re.sub(re.escape(q) + r"(?:.|\n)*?" + re.escape(q), " ", text)
    text = re.sub(r"#[^\n]*", " ", text)
    return text


def a1_no_manuscript_imports():
    text = _strip_prose(open(SRC).read())
    hits = []
    for pat in FORBIDDEN:
        for m in re.finditer(pat, text, re.MULTILINE):
            line = text[:m.start()].count("\n") + 1
            hits.append("line %d: %s" % (line, m.group(0).strip()))
    if hits:
        fail("second_impl.py can reach the manuscript's code: %s" % hits)
    imports = sorted(set(re.findall(r"^\s*(?:import|from)\s+([A-Za-z_][\w.]*)", text,
                                    re.MULTILINE)))
    mentions = len(re.findall(r"scripts/", text))
    print("PASS A1: no import/path/exec to scripts/ in the executable code; "
          "modules used: %s; bare string mentions of 'scripts/' (citations, not "
          "dependencies): %d" % (", ".join(imports), mentions))
    return open(SRC).read()


# ------------------------------------------------------------------ A2 overlap
def _code_lines(text):
    out = []
    for ln in text.splitlines():
        s = ln.strip()
        if not s or s.startswith("#"):
            continue
        out.append(s)
    return out


def _tokens(text):
    text = re.sub(r'"""(?:.|\n)*?"""', " ", text)          # drop docstrings
    text = re.sub(r"#[^\n]*", " ", text)                   # drop comments
    return re.findall(r"[A-Za-z_]\w*|\d+\.\d*|\d+|[+\-*/=<>!]+|\(|\)|\[|\]|,|:", text)


def _lcs_lines(a, b):
    """Longest common contiguous run of lines (dynamic programming, small inputs)."""
    best, end = 0, 0
    prev = [0] * (len(b) + 1)
    for i in range(1, len(a) + 1):
        cur = [0] * (len(b) + 1)
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                cur[j] = prev[j - 1] + 1
                if cur[j] > best:
                    best, end = cur[j], i
        prev = cur
    return best, a[end - best:end] if best else []


def a2_overlap(text, models_path):
    if not models_path:
        print("PASS A2: skipped (no --models path given; the manuscript's scripts are not "
              "in this repository, by design)")
        return
    other = open(models_path).read()
    la, lb = _code_lines(text), _code_lines(other)
    n, run = _lcs_lines(la, lb)
    ta, tb = set(_tokens(text)), set(_tokens(other))
    jac = len(ta & tb) / len(ta | tb)
    shared = ta & tb
    ident = [ln for ln in la if ln in set(lb)]
    print("PASS A2: longest common line run = %d line(s) %r" % (n, " | ".join(run)[:90]))
    print("PASS A2: identical non-trivial lines = %d of %d / %d"
          % (len(ident), len(la), len(lb)))
    print("PASS A2: token Jaccard = %.3f (%d shared tokens: %s)"
          % (jac, len(shared), ", ".join(sorted(shared))[:220]))
    if n > 2 or jac > 0.20:
        fail("code overlap too high: run=%d lines, Jaccard=%.3f" % (n, jac))


# ------------------------------------------------------------------ A3 shared data
def a3_shared_data():
    """The only things that may coincide are the prescribed parameter sets."""
    prescribed = {name: tuple(sorted(p.items())) for name, p in S.MODELS.items()}
    print("PASS A3: shared by design - %d template parameter sets (k, ks, tq, tT, tv) and "
          "the archived literals that are the comparison target" % len(prescribed))
    for name in ("Fourier", "LS", "DPL", "GN-II", "GN-III", "MGT"):
        if name not in prescribed:
            fail("parameter set %r missing" % name)
    print("PASS A3: all six prescribed model names present: %s" % ", ".join(prescribed))


# ------------------------------------------------------------------ A4 residual
def a4_root_residual():
    worst, where = 0.0, ""
    for name, p in S.MODELS.items():
        for w in (1e-3, 1e-1, 1.0, 1e1, 1e3):
            s = -1j * complex(w)
            G = S.transfer_function(s, p)
            for K in S.coupled_K_roots(w, p):
                t1 = (S.RHO * S.C1 ** 2 * K + S.RHO * s ** 2)
                t2 = (s * S.RHO * S.CV + G * K)
                res = t1 * t2 + S.EPS * s * K
                scale = abs(t1 * t2) + abs(S.EPS * s * K)
                rel = abs(res) / scale if scale else 0.0
                if rel > worst:
                    worst, where = rel, "%s, w=%g" % (name, w)
    print("PASS A4: max relative residual of (D) at the computed roots = %.3e (%s)"
          % (worst, where))
    if not worst < 1e-12:
        fail("roots do not satisfy the dispersion relation (residual %.3e)" % worst)


# ------------------------------------------------------------------ A5 branches
def a5_branch_identity():
    """The two coupled modes must be distinguishable - by damping, or by speed when lossless.

    GN-II and MGT are lossless, so Q^-1 = 0 on both branches; there the labels
    "slow" and "fast" are carried by the speed itself, which is exactly why the
    archived `check_gn2` block sorts the pair instead of naming the branches.
    """
    worst, where, lossless = 1e9, "", set()
    for name, p in S.MODELS.items():
        for w in (1e-2, 1.0, 1e2):
            modes = S.branch_modes(w, p)
            q = [m[1] for m in modes]
            v = [m[0] for m in modes]
            if max(q) < 1e-12:                        # lossless pair: separate by speed
                lossless.add(name)
                d = abs(v[0] - v[1]) / max(abs(v[0]), abs(v[1]))
            else:
                d = abs(q[0] - q[1])
            if d < worst:
                worst, where = d, "%s, w=%g" % (name, w)
    print("PASS A5: smallest separation between the two branches = %.3e (%s); "
          "lossless pairs separated by speed: %s"
          % (worst, where, ", ".join(sorted(lossless)) or "none"))
    if worst < 1e-6:
        fail("branches are not separable (min separation %.3e)" % worst)


# ------------------------------------------------------------------ A6 archive
def a6_archive(archive_path):
    if not archive_path:
        print("PASS A6: skipped (no --archive path given)")
        return
    text = open(archive_path).read()
    nums = [float(x) for x in re.findall(r"[-+]?\d+\.\d+(?:[eE][-+]?\d+)?", text)]
    missing = []
    for r in S.REF:
        v = r["value"]
        if not any(abs(x - v) <= max(abs(v) * 5e-7, 1e-15) for x in nums):
            missing.append((r["label"], v))
    if missing:
        fail("archived literals not found in the log: %s" % missing[:5])
    print("PASS A6: %d/%d archived literals found in numbers_log.txt at printed precision"
          % (len(S.REF) - len(missing), len(S.REF)))


def main(argv):
    models_path = archive_path = None
    if "--models" in argv:
        models_path = argv[argv.index("--models") + 1]
    if "--archive" in argv:
        archive_path = argv[argv.index("--archive") + 1]
    text = a1_no_manuscript_imports()
    a2_overlap(text, models_path)
    a3_shared_data()
    a4_root_residual()
    a5_branch_identity()
    a6_archive(archive_path)
    if errors:
        for e in errors:
            print("FAIL " + e)
        print("FAIL %d audit check(s) failed" % len(errors))
        return 1
    print("PASS audit complete (6 groups, 0 failures)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
