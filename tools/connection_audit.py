#!/usr/bin/env python3
"""connection_audit.py — read-only audit of the paper <-> git repository connection.

Checks, without modifying or pushing anything:
  A) worktree vs HEAD at content level (git hash-object, not stat heuristics)
  B) .gitignore audit — what is ignored and whether it is regenerable
  C) le.zip (the archive the workspace was built from) vs the committed tree
  D) work/handoff/MANIFEST_SHA256.json self-verification (the 303/303 claim)
  E) paper internal links: figures/tables/inputs referenced but missing
  F) git <-> GitHub connection: remote, upstream, ahead/behind, reachability

Usage:  python3 tools/connection_audit.py
Exit status 0 = every check passed.
"""
import hashlib
import json
import os
import re
import subprocess
import sys
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MS = os.path.join(ROOT, "PAPER_PROJECT", "13_Manuscript")
fails = []
notes = []


def git(*args, check=False):
    p = subprocess.run(["git"] + list(args), cwd=ROOT, capture_output=True, text=True)
    if check and p.returncode != 0:
        fail("git " + " ".join(args) + " -> " + p.stderr.strip())
    return p


def fail(msg):
    fails.append(msg)
    print("  FAIL  " + msg)


def ok(msg):
    print("  ok    " + msg)


def head(t):
    print("\n" + "=" * 72 + "\n" + t + "\n" + "=" * 72)


head("A) worktree vs HEAD (content level)")
tracked = [l for l in git("ls-files").stdout.splitlines() if l]
print("  info  tracked files: %d" % len(tracked))
hashed = git("hash-object", *tracked, check=True).stdout.split()
if len(hashed) != len(tracked):
    fail("hash-object returned %d hashes for %d files" % (len(hashed), len(tracked)))
else:
    ls = git("ls-tree", "-r", "HEAD", check=True).stdout.splitlines()
    committed = {}
    for line in ls:
        meta, path = line.split("\t", 1)
        _mode, _typ, sha = meta.split()
        committed[path] = sha
    missing_in_head = [f for f in tracked if f not in committed]
    differing = [f for f, h in zip(tracked, hashed) if committed.get(f) and committed[f] != h]
    if missing_in_head:
        fail("%d tracked file(s) not in HEAD tree, e.g. %s" % (len(missing_in_head), missing_in_head[:5]))
    elif differing:
        fail("%d file(s) differ from HEAD: %s" % (len(differing), differing[:10]))
    else:
        ok("all %d tracked files hash-identical to HEAD blobs (no uncommitted edits)" % len(tracked))
    untracked = [l for l in git("ls-files", "--others", "--exclude-standard").stdout.splitlines() if l]
    deleted = [l for l in git("ls-files", "--deleted").stdout.splitlines() if l]
    if deleted:
        fail("%d tracked file(s) missing from disk: %s" % (len(deleted), deleted[:10]))
    else:
        ok("no tracked file missing from disk")
    print("  info  untracked (not ignored): %d%s" % (len(untracked), (" -> " + ", ".join(untracked[:5])) if untracked else ""))

head("B) .gitignore audit")
ign = git("check-ignore", "-v", "--no-index", "PAPER_PROJECT/packages/RESEARCH_PROJECT_FINAL.zip",
          "PAPER_PROJECT/13_Manuscript/equations/x.png", "baseline_provided/x",
          "work/handoff.zip", "PAPER_PROJECT/__pycache__/x.pyc")
pat = {}
for line in ign.stdout.splitlines():
    if "\t" in line:
        src, pathname = line.split("\t", 1)
        pat[pathname] = src
for p, rule in sorted(pat.items()):
    print("  info  ignored by %-32s %s" % (rule, p))
for d in ("PAPER_PROJECT/packages", "PAPER_PROJECT/13_Manuscript/equations", "baseline_provided"):
    exists = os.path.isdir(os.path.join(ROOT, d))
    print("  info  %-38s on disk: %s" % (d + "/", "yes" if exists else "no (rebuild with the generator script)"))
    if not exists and d == "PAPER_PROJECT/packages":
        notes.append("README 'Start here' points at packages/*.zip, which are gitignored and absent; "
                     "regenerate with `python PAPER_PROJECT/00_Project_Control/make_packages.py final`")

head("C) le.zip vs the committed tree")
zp = os.path.join(ROOT, "le.zip")
if not os.path.isfile(zp):
    notes.append("le.zip not present in worktree")
else:
    with zipfile.ZipFile(zp) as z:
        names = [i.filename for i in z.infolist() if not i.is_dir()]
    def norm(n):
        while n.startswith("./"):
            n = n[2:]
        return n
    zfiles = {norm(n) for n in names}
    present = {f for f in tracked}
    ignored_only = {f for f in zfiles if f not in present and
                    git("check-ignore", "-q", "--no-index", f).returncode == 0}
    absent = sorted(zfiles - present - ignored_only)
    extra = sorted(present - zfiles)
    ok("le.zip entries: %d files; repo tracks %d" % (len(zfiles), len(present)))
    if absent:
        fail("%d file(s) in le.zip are neither tracked nor ignored (paper content at risk): %s"
             % (len(absent), absent[:15]))
    else:
        ok("every le.zip file is either committed in the repo or explicitly gitignored")
    print("  info  tracked but not in le.zip (session additions): %d; sample: %s"
          % (len(extra), ", ".join(extra[:6]) if extra else "-"))

head("D) handoff manifest SHA-256 self-verification")
man = os.path.join(ROOT, "work", "handoff", "MANIFEST_SHA256.json")
if not os.path.isfile(man):
    notes.append("work/handoff/MANIFEST_SHA256.json not found — skipping")
else:
    data = json.load(open(man))
    raw = data["files"] if isinstance(data, dict) and "files" in data else data
    if isinstance(raw, list):
        entries = {e["path"]: e["sha256"] for e in raw}
    else:
        entries = {k: (v["sha256"] if isinstance(v, dict) else v) for k, v in raw.items()}
    claim = data.get("file_count") if isinstance(data, dict) else None
    if claim is not None and claim != len(entries):
        fail("manifest file_count=%s but %d entries listed" % (claim, len(entries)))
    good = bad = miss = 0
    for rel, want in sorted(entries.items()):
        p = os.path.join(ROOT, "work", "handoff", rel)
        if not os.path.isfile(p):
            p = os.path.join(ROOT, "work", rel)
        if not os.path.isfile(p):
            miss += 1
            continue
        h = hashlib.sha256()
        with open(p, "rb") as fh:
            for blk in iter(lambda: fh.read(1 << 20), b""):
                h.update(blk)
        if h.hexdigest() == want:
            good += 1
        else:
            bad += 1
            notes.append("handoff file hash mismatch: " + rel)
    if bad or miss:
        fail("handoff manifest: %d ok, %d mismatched, %d missing (README claims 303/303)"
             % (good, bad, miss))
    else:
        ok("handoff manifest verified: %d/%d read-only input files intact" % (good, len(entries)))

head("E) manuscript internal references")
tex = os.path.join(MS, "FINAL_REVISED_MANUSCRIPT.tex")
md = os.path.join(MS, "manuscript_IJHMT.md")
for path in (tex, md):
    if not os.path.isfile(path):
        fail("missing manuscript artifact: " + os.path.relpath(path, ROOT))
        continue
    txt = open(path, encoding="utf-8", errors="replace").read()
    if path.endswith(".tex"):
        refs = set(re.findall(r"\\includegraphics(?:\[[^\]]*\])?\{([^}]*)\}", txt))
        refs |= set(re.findall(r"\\input\{([^}]*)\}", txt))
        kinds = "includegraphics/input"
    else:
        refs = set(re.findall(r"!\[[^\]]*\]\(([^)\s]+)", txt))
        kinds = "markdown images"
    base = os.path.dirname(path)
    figdirs = [os.path.join(ROOT, "PAPER_PROJECT", "11_Figures"),
               os.path.join(ROOT, "PAPER_PROJECT", "12_Tables"), base]
    dead = []
    for r in sorted(refs):
        r2 = r if os.path.isabs(r) else os.path.join(base, r)
        cands = [r2, r2 + ".pdf", r2 + ".png", r2 + ".eps", r2 + ".svg"] + \
                [os.path.join(d, os.path.basename(r)) for d in figdirs]
        if not any(os.path.isfile(c) for c in cands):
            dead.append(r)
    if dead:
        fail("%s: %d unresolved %s reference(s): %s" % (os.path.basename(path), len(dead), kinds, dead[:8]))
    else:
        ok("%s: all %d %s reference(s) resolve on disk" % (os.path.basename(path), len(refs), kinds, ))
    sz = os.path.getsize(path)
    ok("%s present (%.1f kB)" % (os.path.basename(path), sz / 1024))
for name in ("manuscript_IJHMT.pdf", "manuscript_IJHMT.docx", "FINAL_REVISED_MANUSCRIPT.pdf",
             "FINAL_REVISED_REFERENCES.bib", "highlights.txt", "cover_letter.md"):
    p = os.path.join(MS, name)
    if os.path.isfile(p) and os.path.getsize(p) > 0:
        ok("%-32s %8d bytes" % (name, os.path.getsize(p)))
    else:
        fail("%s missing or empty" % name)
# PDF magic bytes / page count without external deps
for name in ("manuscript_IJHMT.pdf", "FINAL_REVISED_MANUSCRIPT.pdf", "calculations_IJHMT.pdf"):
    p = os.path.join(MS, name)
    if not os.path.isfile(p):
        continue
    raw = open(p, "rb").read()
    magic = raw[:5] == b"%PDF-"
    pages = len(re.findall(rb"/Type\s*/Page[^s]", raw))
    trailer = b"%%EOF" in raw[-1024:]
    if magic and trailer:
        ok("%-30s valid PDF header+EOF, ~%d page objects" % (name, pages))
    else:
        fail("%s: header=%s trailer=%s -> truncated/corrupt PDF" % (name, magic, trailer))

head("E2) code-freeze manifests vs the committed code")
SC = os.path.join(ROOT, "PAPER_PROJECT", "06_Source_Code")
deposited = "submission_2026_10_03"  # floor: the oldest submission manifest; the loop below takes the newest
_subs = sorted(fn for fn in os.listdir(SC)
              if fn.startswith("CODE_FREEZE_submission_") and fn.endswith(".json"))
if _subs:
    deposited = _subs[-1][len("CODE_FREEZE_"):-len(".json")]
for fn in sorted(os.listdir(SC)):
    if not (fn.startswith("CODE_FREEZE") and fn.endswith(".json")):
        continue
    d = json.load(open(os.path.join(SC, fn)))
    files = d.get("files", {})
    same = diff = gone = 0
    bad = []
    for rel, want in files.items():
        fp = os.path.join(ROOT, "PAPER_PROJECT", rel)
        if not os.path.isfile(fp):
            gone += 1; bad.append(rel + " (absent)"); continue
        got = hashlib.sha256(open(fp, "rb").read()).hexdigest()
        if got == want:
            same += 1
        else:
            diff += 1; bad.append(rel)
    label = fn.replace("CODE_FREEZE_", "").replace(".json", "")
    if label == deposited:
        if diff or gone:
            fail("deposited manifest %s is stale for %d entries: %s" % (fn, diff + gone, bad[:6]))
        else:
            ok("%-36s %2d/%2d entries byte-identical  <- the manifest to deposit" % (fn, same, len(files)))
    else:
        print("  info  %-36s %2d/%2d identical%s%s (historical, kept as delivered)"
              % (fn, same, len(files), (", %d stale" % diff) if diff else "",
                 (", %d absent" % gone) if gone else ""))
        if "v2_gate" in fn:
            # the manuscript does not claim this manifest is current — it states a number. Check that
            # the number in the paper is the number the code actually gives.
            msmd = os.path.join(MS, "manuscript_IJHMT.md")
            compmd = os.path.join(MS, "calculations_IJHMT.md")
            for label, path, rx in (("manuscript \u00a79.1", msmd,
                                     r"(\d+) of the (\d+) entries of `CODE_FREEZE_v2_gate\.json`"),
                                    ("companion \u00a711", compmd,
                                     r"(\d+) of the (\d+) entries of the (?:gate freeze|archived manifest)")):
                if not os.path.isfile(path):
                    continue
                m = re.search(rx, open(path, encoding="utf-8").read())
                if not m:
                    fail("%s: the archived-manifest statement could not be found to verify" % label)
                elif (int(m.group(1)), int(m.group(2))) == (same, len(files)):
                    ok("%s states %s of %s byte-identical — recomputed and confirmed"
                       % (label, m.group(1), m.group(2)))
                else:
                    fail("%s states %s of %s byte-identical but the code gives %d of %d"
                         % (label, m.group(1), m.group(2), same, len(files)))

head("F) git <-> GitHub connection")
url = git("remote", "get-url", "origin").stdout.strip()
ok("origin = " + url)
branch = git("rev-parse", "--abbrev-ref", "HEAD").stdout.strip()
ok("current branch = " + branch)
sha = git("rev-parse", "HEAD").stdout.strip()
gh_sha = git("rev-parse", "origin/main").stdout.strip()
ok("local HEAD = %s" % sha[:12])
ok("origin/main = %s" % gh_sha[:12])
ahead, behind = git("rev-list", "--left-right", "--count", "HEAD...origin/main").stdout.split()
print("  info  ahead %s / behind %s vs origin/main" % (ahead, behind))
if int(behind) > 0:
    fail("local branch is behind origin/main by %s commit(s) — pull/rebase before any rebuild" % behind)
elif int(ahead) > 0:
    ok("local is a fast-forward of origin/main (no divergence)")
    on_remote = git("rev-parse", "--verify", "--quiet", "origin/%s" % branch).returncode == 0
    if on_remote:
        rsha = git("rev-parse", "origin/%s" % branch).stdout.strip()
        if rsha == sha:
            print("  info  branch is on GitHub at %s, %s commit(s) ahead of main — open a PR when ready"
                  % (rsha[:12], ahead))
        else:
            notes.append("local branch differs from origin/%s (%s vs %s) — push the local commit"
                         % (branch, sha[:12], rsha[:12]))
    else:
        notes.append("%s commit(s) ahead of origin/main and unpushed: `git push -u origin %s`"
                     % (ahead, branch))
if sha != gh_sha and int(ahead) == 0:
    fail("local HEAD differs from origin/main")
elif sha == gh_sha:
    ok("local HEAD == origin/main (paper is on GitHub)")
up = git("rev-parse", "--abbrev-ref", "%s@{upstream}" % branch)
if up.returncode == 0:
    ok("upstream configured: " + up.stdout.strip())
else:
    notes.append("branch '%s' has no upstream (it was never pushed) — `git push -u origin %s`"
                 % (branch, branch))
c = git("config", "--get", "user.name")
e = git("config", "--get", "user.email")
print("  info  commit identity: %s <%s>" % (c.stdout.strip() or "-", e.stdout.strip() or "-"))
if not c.stdout.strip() or not e.stdout.strip():
    notes.append("user.name/user.email not configured in this checkout — local commits may fail")
lsr = git("ls-remote", "--exit-code", "origin", "refs/heads/main")
if lsr.returncode == 0 and lsr.stdout.strip().startswith(gh_sha):
    ok("GitHub reachable over the network; refs/heads/main = %s as fetched" % gh_sha[:12])
else:
    fail("ls-remote did not confirm refs/heads/main at origin/main: " + (lsr.stderr.strip() or lsr.stdout.strip() or "empty"))

print("\n" + "=" * 72)
if notes:
    print("NOTES (%d):" % len(notes))
    for n in notes:
        print("  - " + n)
if fails:
    print("\nRESULT: %d check(s) FAILED" % len(fails))
    sys.exit(1)
print("\nRESULT: all connection checks passed")
