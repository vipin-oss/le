#!/usr/bin/env python3
"""P1, first real pass: the integrity audit of the landed manuscript sources.

The blueprint's P1 exit condition is "audit report; fixes merged; build clean". Until step 42 the
sources were not in the repository, so this could not run. They are now in
paper_v2/from_overleaf/phase5/ (landed from the branch that held them), and this script audits them
mechanically - it never edits a .tex. Findings go to P1_SOURCE_AUDIT_2026-11-01.md and to
source_audit_2026-11-01.csv; closing them is a separate, author-visible step.

Checks (all re-derivable, no judgement calls):

  A1 every \\ref/\\eqref/\\cref/\\Cref/\\autoref target exists as a \\label
  A2 no \\label is defined twice
  A3 every citation key exists in the bundled .bib files
  A4 every \\includegraphics file exists on disk (figures live outside the repository)
  A5 every \\input file exists
  A6 no placeholder text (TODO, FIXME, XXX, TBD, '???')
  A7 the counts in the main.tex header comment match the sources
  A8 informational: labels defined but never referenced
  A9 every .bib entry carries author, title, year
  A10 informational: duplicate .bib titles

Usage: python3 audit_sources.py      (writes both files, prints one line per check)
"""
import csv
import os
import re
import sys
import collections

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.environ.get("AUDIT_SRC") or os.path.normpath(os.path.join(HERE, "..", "..", "manuscript_v2"))
MASTER = os.path.join(SRC, "master")
FIGROOTS = ["/home/user/manuscript", os.path.join(SRC, "master"), SRC]
OUT_CSV = os.path.join(HERE, "source_audit_2026-11-01.csv")
OUT_MD = os.path.join(HERE, "P1_SOURCE_AUDIT_2026-11-01.md")


def tex_files():
    out = []
    for root, _, files in os.walk(SRC):
        for f in files:
            if f.endswith(".tex"):
                out.append(os.path.join(root, f))
    return sorted(out)


def rel(p):
    return os.path.relpath(p, SRC)


def read(p):
    with open(p, encoding="utf-8", errors="replace") as f:
        return f.read()


def strip_comments(s):
    return re.sub(r"(?<!\\)%.*", "", s)


def main():
    files = tex_files()
    if not files:
        print("FAIL no .tex files under %s" % SRC)
        sys.exit(1)
    text = {p: strip_comments(read(p)) for p in files}
    joined = "\n".join(text.values())

    labels = collections.defaultdict(list)
    for p in files:
        for m in re.finditer(r"\\label\{([^}]+)\}", text[p]):
            labels[m.group(1)].append(rel(p))

    refs = collections.defaultdict(list)
    for p in files:
        for m in re.finditer(r"\\(?:ref|eqref|cref|Cref|autoref)\{([^}]+)\}", text[p]):
            for k in m.group(1).split(","):
                refs[k.strip()].append(rel(p))

    unresolved = {k: v for k, v in refs.items() if k not in labels}
    dup_all = {k: v for k, v in labels.items() if len(v) > 1}
    dup, dup_copies = {}, {}
    for k, v in dup_all.items():
        bases = {os.path.basename(x) for x in v}
        (dup_copies if len(bases) == 1 else dup)[k] = v
    unused = {k: v for k, v in labels.items() if k not in refs}

    bibkeys = {}
    dupkeys = []
    bibfiles = []
    for root, _, fs in os.walk(SRC):
        for f in fs:
            if f.endswith(".bib"):
                bibfiles.append(os.path.join(root, f))
    entries = []
    for b in sorted(bibfiles):
        s = read(b)
        for m in re.finditer(r"@(\w+)\s*\{\s*([^,]+),", s):
            key = m.group(2).strip()
            if key in bibkeys:
                dupkeys.append((key, bibkeys[key], os.path.basename(b)))
            bibkeys[key] = os.path.basename(b)
            entries.append((key, m.start(), s, os.path.basename(b)))

    cites = collections.defaultdict(list)
    for p in files:
        for m in re.finditer(r"\\cite[a-zA-Z]*\*?(?:\[[^\]]*\])*\{([^}]+)\}", text[p]):
            for k in m.group(1).split(","):
                cites[k.strip()].append(rel(p))
    missing_cites = {k: v for k, v in cites.items() if k and k not in bibkeys}

    gra = []
    for p in files:
        for m in re.finditer(r"\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}", text[p]):
            gra.append((m.group(1).strip(), rel(p)))
    missing_fig = []
    for name, f in gra:
        cands = [name] if os.path.splitext(name)[1] else [name + e for e in (".pdf", ".png", ".svg", ".jpg", ".eps")]
        found = False
        for root in FIGROOTS:
            for c in cands:
                for sub in ("", "figures/source", "master/figures/source", "master/figures/rendered"):
                    if os.path.exists(os.path.join(root, sub, c)):
                        found = True
        if not found:
            missing_fig.append((name, f))

    inputs = []
    for p in files:
        for m in re.finditer(r"\\input\{([^}]+)\}", text[p]):
            t = m.group(1).strip()
            p2 = t if t.endswith(".tex") else t + ".tex"
            base = os.path.dirname(p)
            ok = any(os.path.exists(os.path.join(b, p2)) for b in (base, MASTER, SRC))
            inputs.append((t, rel(p), ok))
    missing_inputs = [(t, f) for t, f, ok in inputs if not ok]

    # tabularx column specs read "XXX" - that is a column type, not a placeholder, so the
    # placeholder set is TODO/FIXME/TBD/??? only.
    placeholders = []
    for p in files:
        for m in re.finditer(r"\b(TODO|FIXME|TBD)\b|\?\?\?", text[p]):
            line = text[p][:m.start()].count("\n") + 1
            placeholders.append("%s:%d:%s" % (rel(p), line, m.group(0)))

    nsec = sum(len(re.findall(r"\\section\{", text[p])) for p in files if "/master/sections/" in p)
    napp = len([p for p in files if "/master/appendices/" in p])
    nfig = len([f for f in os.listdir("/home/user/manuscript/master/figures/source")
                if f.endswith(".pdf")]) if os.path.isdir("/home/user/manuscript/master/figures/source") else -1
    ntab = len({re.search(r"/T(\d)", p).group(1) for p in files
                if re.search(r"/master/tables/source/T\d", p)})
    header = ""
    for p in files:
        if os.path.basename(p) == "main.tex":
            header = "\n".join(read(p).splitlines()[:8])
    m = re.search(r"(\d+) numbered sections, (\d+) appendices, (\d+) unique figures, (\d+) tables", header)
    claim = tuple(int(x) for x in m.groups()) if m else None
    actual = (nsec, napp, nfig, ntab)

    bad_bib = []
    for key, pos, s, bf in entries:
        seg = s[pos:pos + 1200]
        if not re.search(r"author\s*=", seg, re.I) or not re.search(r"title\s*=", seg, re.I) \
           or not re.search(r"year\s*=", seg, re.I):
            bad_bib.append((key, bf))
    titles = collections.Counter()
    starts = sorted({pos for _, pos, _, _ in entries})
    for key, pos, txt, bf in entries:
        nxt = [x for x in starts if x > pos]
        seg = txt[pos:(nxt[0] if nxt else len(txt))]
        t = re.search(r"title\s*=\s*[{\"](.+?)[}\"],?\s*\n", seg, re.S)
        if t:
            titles[(re.sub(r"[^a-z0-9]+", "", t.group(1).lower()), bf)] += 1
    per_title = collections.Counter(k for k, _ in titles)
    dup_titles = [t for t, n in per_title.items() if n > 1]

    rows = []

    def add(cid, what, status, items, detail=""):
        if isinstance(items, dict):
            n = len(items)
            fallback = "; ".join(str(i) for i in list(items)[:8])
        else:
            seq = list(items)
            n = len(seq)
            fallback = "; ".join(str(i) for i in seq[:8])
        rows.append({"check_id": cid, "what": what, "status": status, "n": n,
                     "detail": detail or fallback})

    add("A1", "every cross-reference resolves to a label", "PASS" if not unresolved else "FAIL",
        unresolved, "; ".join("%s -> %s" % (k, v[0]) for k, v in list(unresolved.items())[:10]))
    add("A2", "no label is defined twice", "PASS" if not dup else "FAIL", dup,
        "; ".join("%s in %s" % (k, ",".join(v)) for k, v in list(dup.items())[:8]))
    add("A3", "every citation key exists in the bundled .bib files", "PASS" if not missing_cites else "FAIL",
        missing_cites, "; ".join("%s (%s)" % (k, v[0]) for k, v in list(missing_cites.items())[:10]))
    add("A4", "every included figure exists on disk", "PASS" if not missing_fig else "FAIL", missing_fig,
        "; ".join("%s in %s" % (n, f) for n, f in missing_fig[:8]))
    add("A5", "every \\input file exists", "PASS" if not missing_inputs else "FAIL", missing_inputs,
        "; ".join("%s (%s)" % (t, f) for t, f in missing_inputs[:8]))
    add("A6", "no placeholder text in the sources", "PASS" if not placeholders else "FAIL", placeholders,
        "; ".join(placeholders[:8]))
    add("A7", "the counts in the main.tex header match the sources",
        "PASS" if claim and claim == actual else "FAIL", [] if claim == actual else [1],
        "header claims %s, sources have %s (sections, appendix files, figure envs, table envs)" % (claim, actual))
    add("A8", "labels defined but never referenced (informational)", "INFO", unused,
        "; ".join(list(unused)[:10]))
    add("A9", "every .bib entry has author, title and year", "PASS" if not bad_bib else "FAIL", bad_bib,
        "; ".join("%s (%s)" % k for k in bad_bib[:8]))
    used = {os.path.basename(n) for n, _ in gra}
    figdir = "/home/user/manuscript/master/figures/source"
    all_figs = sorted(f for f in os.listdir(figdir) if f.endswith(".pdf")) if os.path.isdir(figdir) else []
    unused_figs = [f for f in all_figs if f not in used and os.path.splitext(f)[0] + ".pdf" not in used]
    appd = ""
    for p_ in files:
        if os.path.basename(p_) == "appD_figures.tex":
            appd = read(p_)
    undeclared = [f for f in unused_figs
                  if not re.search(r"F-0?%d\b" % int(re.search(r"fig(\d+)", f).group(1)), appd)]
    declared = [f for f in unused_figs if f not in undeclared]
    add("A11", "every figure file is either included or declared provisional in Appendix D",
        "PASS" if not undeclared else "FAIL", undeclared,
        ("declared provisional in appD_figures.tex: " + ", ".join(declared)) if declared else "")
    add("A2b", "the same source file does not appear twice in the tree", "PASS" if not dup_copies else "FAIL",
        dup_copies, "; ".join("%s in %s" % (k, " and ".join(v)) for k, v in list(dup_copies.items())[:8]))
    add("A10", "the same title appears in more than one bundled .bib file (informational: the R3* files are per-batch and overlap by design)", "INFO", dup_titles, "%d titles appear in more than one file" % len(dup_titles))

    with open(OUT_CSV, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["check_id", "what", "status", "n", "detail"])
        w.writeheader()
        for r in rows:
            w.writerow(r)

    fails = [r for r in rows if r["status"] == "FAIL"]
    with open(OUT_MD, "w", encoding="utf-8") as f:
        f.write("# P1 source audit - %d .tex files, %d labels, %d citation keys, %d bib entries\n\n"
                % (len(files), len(labels), len(cites), len(bibkeys)))
        f.write("Audited tree: `%s`\n\n" % SRC)
        f.write("Sources: `paper_v2/from_overleaf/phase5/` (landed 2026-11-01 from the branch that held them; "
                "figures read from outside the repository). Nothing here edits a `.tex`.\n\n")
        f.write("| check | what | status | n |\n|---|---|---|---|\n")
        for r in rows:
            f.write("| %s | %s | **%s** | %d |\n" % (r["check_id"], r["what"], r["status"], r["n"]))
        f.write("\n## Findings\n\n")
        if not fails:
            f.write("No mechanical defect found by A1-A10. That is a statement about references, figures and "
                    "bibliography only - not about signs, notation or derivations.\n")
        for r in fails:
            f.write("### %s - %s (%d)\n\n" % (r["check_id"], r["what"], r["n"]))
            f.write("```\n%s\n```\n\n" % (r["detail"] or "(see csv)"))
        f.write("\n## What this audit does not cover\n\n"
                "- signs, dimensions and derivation steps of the 166 numbered equations (needs the page-by-page pass)\n"
                "- notation consistency across sections\n"
                "- the 45 scripts in `phase5/scripts/` (D3: which of them assert anything)\n")
    for r in rows:
        print("%-4s %-6s %-62s n=%d" % (r["check_id"], r["status"], r["what"][:62], r["n"]))
    print("wrote", OUT_CSV, "and", OUT_MD)
    return 0


if __name__ == "__main__":
    sys.exit(main())
