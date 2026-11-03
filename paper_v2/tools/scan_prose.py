#!/usr/bin/env python3
"""Scan manuscript prose for AI-writing patterns and long sentences.

Produces a TSV of candidate sentences with the pattern numbers that fired.
Math, citations, labels and figure/table environments are protected and are
never proposed for change; they only act as opaque tokens.
"""
import json
import re
import sys
from pathlib import Path

ENVS = ("equation", "equation*", "align", "align*", "gather", "gather*",
        "multline", "multline*", "eqnarray", "eqnarray*", "split", "cases",
        "array", "tabular", "tabularx", "longtable", "tikzpicture", "figure",
        "figure*", "table", "table*", "verbatim", "lstlisting", "math")

CMDS = ("cite", "citep", "citet", "citealp", "citeauthor", "citeyear",
        "cref", "Cref", "ref", "eqref", "label", "input", "include",
        "includegraphics", "url", "href", "bibliography", "bibliographystyle",
        "begin", "end", "caption", "item", "SI", "si", "num", "unit",
        "newcommand", "renewcommand", "providecommand", "DeclareMathOperator")

PH = "\u0000"

BANNED = {
    "delve": 1, "delves": 1, "delving": 1, "intricate": 1, "intricacies": 1,
    "tapestry": 1, "pivotal": 1, "underscore": 1, "underscores": 1,
    "underscored": 1, "underscoring": 1, "landscape": 1, "foster": 1,
    "fosters": 1, "fostered": 1, "fostering": 1, "testament": 1,
    "enhance": 1, "enhances": 1, "enhanced": 1, "enhancing": 1,
    "enhancement": 1, "crucial": 1, "crucially": 1, "vibrant": 1,
    "garner": 1, "garnered": 1, "garnering": 1, "bolster": 1, "bolsters": 1,
    "bolstered": 1, "interplay": 1, "meticulous": 1, "meticulously": 1,
    "robust": 1, "robustly": 1, "robustness": 1, "leverage": 1,
    "leverages": 1, "leveraging": 1, "paradigm": 1, "paradigms": 1,
    "paradigmatic": 1, "realm": 1, "myriad": 1, "seamless": 1,
    "seamlessly": 1, "holistic": 1, "nuanced": 1, "showcase": 1,
    "showcases": 1, "showcasing": 1, "embark": 1, "unveil": 1, "unveils": 1,
    "illuminate": 1, "illuminates": 1, "cutting-edge": 1, "deep dive": 1,
    "comprehensive": 1, "comprehensively": 1, "multifaceted": 1,
    "ever-evolving": 1, "game-changer": 1, "unprecedented": 11,
}

SIGNIF = [
    r"plays? a (vital|crucial|key|critical|significant|central|major) role",
    r"stands? as a testament", r"is a testament to", r"underscor\w+ its significance",
    r"marks? a turning point", r"sets? the stage", r"paves? the way",
    r"sheds? light on", r"opens? the door", r"speaks to the",
    r"is (of|nothing short of)", r"cannot be overstated", r"should not be underestimated",
]

BOILER = [
    r"^In conclusion", r"^In summary", r"^Overall,", r"^It is important to (note|emphasize|stress)",
    r"^It is worth (mentioning|noting)", r"^It should be noted", r"^This highlights",
    r"^This demonstrates", r"^This underscores", r"^Taken together", r"^In essence",
    r"^To sum up", r"^In short,", r"^Importantly,", r"^Notably,", r"^Indeed,",
    r"^Furthermore,", r"^Moreover,", r"^Additionally,",
]

VAGUE = [
    r"some (researchers|authors|studies|workers)", r"many (researchers|authors|studies|workers)",
    r"studies (show|have shown|suggest)", r"it is (widely|generally) (known|accepted|believed)",
    r"researchers have", r"it has been (shown|observed|reported) (that )?(by many|widely)",
    r"various (authors|studies)", r"several (authors|studies)",
]

HEDGE = [
    r"it could be argued", r"to a certain extent", r"to some (extent|degree)",
    r"arguably", r"in some sense", r"it may (well )?be that",
    r"relatively", r"quite ", r"rather ", r"somewhat",
]

NEGPAR = [r"not just .{2,80}? but", r"not only .{2,80}? but also", r"not merely .{2,80}? but",
          r"rather than merely", r"is not .{2,60}? but rather"]

FORMAT = [r"\\textbf\{", r"\\emph\{"]


def protect(text):
    """Replace protected regions with placeholders; return (masked, store)."""
    store = []

    def keep(s):
        store.append(s)
        return f"{PH}{len(store) - 1}{PH}"

    # environments first (they may contain $ signs)
    def env_repl(m):
        return keep(m.group(0))

    env_alt = "|".join(re.escape(e) for e in ENVS)
    text = re.sub(r"\\begin\{(" + env_alt + r")\}.*?\\end\{\1\}", env_repl, text, flags=re.S)

    # display math
    text = re.sub(r"\\\[.*?\\\]", env_repl, text, flags=re.S)
    text = re.sub(r"\$\$.*?\$\$", env_repl, text, flags=re.S)
    # inline math
    text = re.sub(r"(?<!\\)\$[^$]*\$", env_repl, text)
    text = re.sub(r"\\\(.*?\\\)", env_repl, text, flags=re.S)

    # citation / ref / label commands with optional args
    cmd_alt = "|".join(CMDS)
    text = re.sub(r"\\(" + cmd_alt + r")\*?(\[[^\]]*\])?(\{[^{}]*\})?", env_repl, text)
    # other simple commands, keep name only
    text = re.sub(r"\\[a-zA-Z@]+\*?(\[[^\]]*\])?", lambda m: keep(m.group(0)), text)
    return text, store


def restore(text, store):
    return re.sub(PH + r"(\d+)" + PH, lambda m: store[int(m.group(1))], text)


def words(s):
    s = re.sub(PH + r"\d+" + PH, " ", s)
    s = re.sub(r"[\\{}~]", " ", s)
    return [w for w in s.split() if re.search(r"[A-Za-z0-9]", w)]


def sentences(masked):
    """Split masked paragraph text into sentences with approximate char offsets."""
    out = []
    for para in re.split(r"\n\s*\n", masked):
        body = para.strip()
        if not body or body.startswith(PH):
            continue
        parts = re.split(r"(?<=[.!?])[\"')\]]*\s+(?=[A-Z(\[\\]|" + PH + ")", body)
        out.extend(p.strip() for p in parts if p.strip())
    return out


def scan(path, text):
    masked, store = protect(text)
    hits = []
    for sent in sentences(masked):
        raw = restore(sent, store)
        clean = sent
        flags = set()
        low = re.sub(r"\s+", " ", clean).lower()
        for w, p in BANNED.items():
            if re.search(r"\b" + re.escape(w) + r"\b", low):
                flags.add(p)
        for p, pats in ((2, SIGNIF), (4, NEGPAR), (6, BOILER), (7, VAGUE),
                        (9, HEDGE)):
            for pat in pats:
                if re.search(pat, clean, flags=re.I | (re.M if p == 6 else 0)):
                    flags.add(p)
                    break
        for pat in FORMAT:
            if re.search(pat, clean):
                flags.add(8)
        plain = re.sub(PH + r"\d+" + PH, " ", clean)
        if "---" in plain or re.search(r"(?<=\s)--(?=\s)", plain):
            flags.add(5)
        n = len(words(clean))
        if n > 35:
            flags.add(12)
        if flags:
            hits.append({"patterns": sorted(flags), "nwords": n, "sentence": raw})
    return hits


def main():
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
    files = sorted([root / "main.tex"] + list((root / "sections").glob("*.tex")))
    rows = []
    summary = []
    for f in files:
        text = f.read_text(encoding="utf-8", errors="replace")
        hits = scan(f, text)
        for h in hits:
            rows.append({"file": str(f.relative_to(root)), **h})
        counts = {}
        for h in hits:
            for p in h["patterns"]:
                counts[p] = counts.get(p, 0) + 1
        summary.append((str(f.relative_to(root)), len(words(protect(text)[0])), len(hits), counts))
    summary.sort(key=lambda r: -r[1])
    print(f"{'file':32s} {'words':>6s} {'hits':>5s}  patterns")
    tot = 0
    allc = {}
    for name, nw, nh, c in summary:
        tot += nh
        for k, v in c.items():
            allc[k] = allc.get(k, 0) + v
        print(f"{name:32s} {nw:6d} {nh:5d}  {dict(sorted(c.items()))}")
    print(f"\nTOTAL candidate sentences: {tot}")
    print("per-pattern totals:", dict(sorted(allc.items())))
    out = Path("paper_v2") / "prose_scan.json"
    out.write_text(json.dumps(rows, indent=1))
    print("wrote", out)


if __name__ == "__main__":
    main()
