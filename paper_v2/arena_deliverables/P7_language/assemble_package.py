#!/usr/bin/env python3
"""Assemble a drop-in replacement for overleaf_package.zip with the rewritten prose.

    python3 assemble_package.py [--out ../../rewritten_package.zip] [--check]

Every file comes from paper_v2/overleaf_package.zip unchanged, except:
  * each sections/<name>.tex that has a rewritten twin in this folder is replaced by that twin;
  * main.tex has its Highlights + graphical abstract + abstract + keywords block
    (from the HIGHLIGHTS marker to \\end{abstract}) replaced by the text of abstract.tex.

The originals are never modified: this script only reads the zip and writes a new one.
`--check` verifies the result without writing.
"""
import argparse
import os
import sys
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
PAPER = os.path.dirname(os.path.dirname(HERE))
SRC = os.path.join(PAPER, "overleaf_package.zip")
DEFAULT_OUT = os.path.join(PAPER, "rewritten_package.zip")

START = "%================== HIGHLIGHTS =================="
END = "\\end{abstract}"


def rewritten_sections():
    out = {}
    for f in os.listdir(HERE):
        if f.endswith(".tex") and f != "abstract_original.tex":
            out[f] = open(os.path.join(HERE, f), encoding="utf8").read()
    return out


def new_main(main, abstract):
    i = main.find(START)
    j = main.find(END)
    if i < 0 or j < 0 or j < i:
        raise SystemExit("main.tex: could not locate the abstract block")
    head, tail = main[:i], main[j + len(END):]
    body = abstract.rstrip()
    if not body.endswith(END):
        raise SystemExit("abstract.tex: does not end with \\end{abstract}")
    return head + body + tail


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=DEFAULT_OUT)
    ap.add_argument("--check", action="store_true", help="report what would change and exit")
    a = ap.parse_args()

    secs = rewritten_sections()
    with zipfile.ZipFile(SRC) as z:
        names = z.namelist()
        data = {n: z.read(n) for n in names}

    replaced, untouched = [], []
    for n in names:
        base = n.split("/")[-1]
        if n.startswith("sections/") and base in secs:
            data[n] = secs[base].encode("utf8")
            replaced.append(base)
        elif n == "main.tex":
            abstract = secs.get("abstract.tex")
            if abstract is None:
                raise SystemExit("abstract.tex missing")
            data[n] = new_main(data[n].decode("utf8"), abstract).encode("utf8")
        else:
            untouched.append(n)

    missing = sorted(set(secs) - set(replaced) - {"abstract.tex"})
    print(f"sections replaced: {len(replaced)}")
    print(f"main.tex rewritten with abstract.tex")
    print(f"other entries untouched: {len(untouched)}")
    if missing:
        print(f"NOT in the package (kept out): {missing}")
        if "abstract.tex" not in missing:
            return 1
    if a.check:
        print("CHECK ONLY: no file written")
        return 0

    tmp = a.out + ".tmp"
    with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as z:
        for n in names:
            z.writestr(n, data[n])
    os.replace(tmp, a.out)
    size = os.path.getsize(a.out)
    print(f"wrote {a.out} ({size/1e6:.2f} MB, {len(names)} entries)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
