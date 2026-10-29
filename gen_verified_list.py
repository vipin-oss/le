import csv

BS = chr(92)  # backslash, avoids Python escape interpretation

rows = list(csv.DictReader(open('phase5/reports/EQUATION_AUDIT.csv', newline='', encoding='utf-8')))
verified = [r for r in rows if r['status'].startswith('VERIFIED')]

def secnum(r):
    s = r['section']
    if s == 'B':
        return (99, 'B')
    return (int(s), s)

verified.sort(key=lambda r: (secnum(r)[0], r['audit_id']))

lines = []
lines.append(BS + "subsection{Verified equation register: assumptions and limits}")
lines.append(BS + "label{sec:12.verified_register}")
lines.append("")
lines.append("The displays below were verified either symbolically (VERIFIED-SYMBOLIC) or against the")
lines.append("primary source (VERIFIED-SOURCE) in this revision. For each display, the assumptions")
lines.append("under which it holds and the limits beyond which it does not apply are stated. Conformance")
lines.append("statements are restricted to the displayed equations and the cited sources; they are not")
lines.append("convergence, stability, or source-transcription results beyond the stated scope.")
lines.append("")
lines.append(BS + "begin{itemize}[label=" + BS + "bullet]")
for r in verified:
    label = r['label']
    status = r['status']
    section = r['section']
    assumptions = r['scope_and_assumptions'].strip()
    limits = r['negative_test'].strip()
    basis = r['source_anchor_or_script'].strip()
    lines.append("")
    lines.append(BS + "item " + BS + "textbf{" + label + "} (Section~" + section + ", " + status + ").")
    lines.append("    Assumptions: " + assumptions + " ")
    lines.append("    Limits: " + limits + " ")
    lines.append("    Verified by: " + basis + ".")
lines.append(BS + "end{itemize}")
lines.append("")

open('/home/user/le/verified_list.tex', 'w', encoding='utf-8').write(chr(10).join(lines))
print("wrote", len(verified), "items")
