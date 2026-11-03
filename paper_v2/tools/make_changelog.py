#!/usr/bin/env python3
"""Build paper_v2/language_changelog.csv by diffing the working tree against the
baseline package at sentence level.

Reason codes (the pattern numbers used in the task brief):
 1 AI vocabulary, 2 empty significance phrase, 3 rule of three, 4 negative
 parallelism, 5 dash overuse, 6 boilerplate transition, 7 vague attribution,
 8 formatting overkill, 9 over-hedging, 10 uniform rhythm, 11 unsupported
 adjective, 12 long sentence split.  0 = wording only.
"""
import csv
import difflib
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from scan_prose import BANNED, SIGNIF, NEGPAR, BOILER, VAGUE, HEDGE, protect, restore, words


def sentences_raw(masked, store):
    out = []
    for para in re.split(r"\n\s*\n", masked):
        body = para.strip()
        if not body:
            continue
        parts = re.split(r"(?<=[.!?])[\"')\]]*\s+(?=[A-Z(\[\\\u0000])", body)
        for p in parts:
            p = p.strip()
            if p:
                out.append(restore(p, store))
    return out


def detect(sent):
    flags = set()
    low = re.sub(r"\s+", " ", sent).lower()
    for w, p in BANNED.items():
        if re.search(r"\b" + re.escape(w) + r"\b", low):
            flags.add(p)
    for p, pats in ((2, SIGNIF), (4, NEGPAR), (6, BOILER), (7, VAGUE), (9, HEDGE)):
        for pat in pats:
            if re.search(pat, sent, flags=re.I):
                flags.add(p)
                break
    if "---" in sent or re.search(r"(?<=\s)--(?=\s)", sent):
        flags.add(5)
    if len(words(protect(sent)[0])) > 35:
        flags.add(12)
    return sorted(flags)


def main():
    base, work = Path(sys.argv[1]), Path(sys.argv[2])
    files = ["main.tex"] + sorted(str(p.relative_to(work / "sections"))
                                  for p in (work / "sections").glob("*.tex"))
    rows = []
    for rel in files:
        sub = "" if rel == "main.tex" else "sections/"
        bf, wf = base / sub / rel, work / sub / rel
        if not bf.exists():
            continue
        old_t = bf.read_text(encoding="utf-8", errors="replace")
        new_t = wf.read_text(encoding="utf-8", errors="replace")
        if old_t == new_t:
            continue
        om, os_ = protect(old_t)
        nm, ns_ = protect(new_t)
        old_s = sentences_raw(om, os_)
        new_s = sentences_raw(nm, ns_)
        sm = difflib.SequenceMatcher(None, [re.sub(r"\s+", " ", s) for s in old_s],
                                     [re.sub(r"\s+", " ", s) for s in new_s],
                                     autojunk=False)
        new_lines = new_t.split("\n")
        for tag, i1, i2, j1, j2 in sm.get_opcodes():
            if tag == "equal":
                continue
            pairs = min(i2 - i1, j2 - j1)
            for k in range(pairs):
                o, n = old_s[i1 + k], new_s[j1 + k]
                line = next((i + 1 for i, l in enumerate(new_lines)
                             if n.split(".")[0][:40] in l), 0)
                rows.append([rel, line, o, n, ",".join(str(x) for x in detect(o)) or "10"])
            for k in range(pairs, i2 - i1):
                o = old_s[i1 + k]
                rows.append([rel, 0, o, "", ",".join(str(x) for x in detect(o)) or "10"])
            for k in range(pairs, j2 - j1):
                n = new_s[j1 + k]
                rows.append([rel, 0, "", n, "10"])
    out = work / "paper_v2" / "language_changelog.csv"
    with open(out, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL)
        w.writerow(["file", "line", "old_sentence", "new_sentence", "reason"])
        w.writerows(rows)
    print(f"{len(rows)} changed sentences -> {out}")
    per = {}
    for r in rows:
        for p in r[4].split(","):
            per[p] = per.get(p, 0) + 1
    print("by pattern:", dict(sorted(per.items(), key=lambda kv: int(kv[0]))))


if __name__ == "__main__":
    main()
