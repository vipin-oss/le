#!/usr/bin/env python3
"""Sanitize the W3.1 verified register in sec12_comparative.tex so its body text
contains no internal paths (phase5/...) and no OCL process-tag ids, which the
CI forbidden-tag scan flags in the rendered PDF. The ledger keeps traceability;
the register keeps only a generic verification note keyed to each item's status.
"""
import re

SEC = "/home/user/le/phase5/master/sections/sec12_comparative.tex"
s = open(SEC, encoding="utf-8").read()
start = s.find("\\subsection{Verified equation register: assumptions and limits}")
end = s.find("\\subsection{Status by family: established, disputed or model-dependent, open}")
assert start >= 0 and end > start, "register markers not found"
region = s[start:end]
lines = region.split("\n")

status = "SYMBOLIC"  # default fallback
out = []
changed = 0
for line in lines:
    mstatus = re.search(r'VERIFIED-(\w+)', line)
    if mstatus:
        status = mstatus.group(1)
    if re.match(r'\s*Verified by:', line):
        replacement = ("    Verified by: symbolic verification script."
                       if status == "SYMBOLIC"
                       else "    Verified by: primary-source page check.")
        if line.strip() != replacement:
            changed += 1
        out.append(replacement)
        continue
    # Strip OCL process-tag ids from any other line (e.g. Limits: ... see OCL-489)
    newline = re.sub(r'OCL-\d+[.\w]*', '', line)
    newline = re.sub(r'\s+see\s+', ' ', newline)  # tidy dangling 'see'
    newline = re.sub(r';\s*\.', '.', newline)
    newline = re.sub(r'\.\s*\.', '.', newline)
    newline = re.sub(r',\s*,', ',', newline)
    newline = re.sub(r'\s+\)', ')', newline)
    if newline != line:
        changed += 1
    out.append(newline)

new_region = "\n".join(out)
s2 = s[:start] + new_region + s[end:]
open(SEC, "w", encoding="utf-8").write(s2)
print("register lines changed:", changed)
