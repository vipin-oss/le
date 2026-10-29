import csv
import re

BS = chr(92)  # backslash, avoids Python escape interpretation

rows = list(csv.DictReader(open('phase5/reports/EQUATION_AUDIT.csv', newline='', encoding='utf-8')))
verified = [r for r in rows if r['status'].startswith('VERIFIED')]


def secnum(r):
    s = r['section']
    if s == 'B':
        return (99, 'B')
    return (int(s), s)


verified.sort(key=lambda r: (secnum(r)[0], r['audit_id']))


def clean(text):
    """Remove process/internal language from assumption/limit text."""
    # Remove "the script"/"The script" and script+verb constructions
    text = re.sub(r'\b[Tt]he script\b', '', text)
    text = re.sub(r'\b[Ss]cript (checks|verifies|confirms|tests|retains)\b', '', text, flags=re.I)
    # Remove standalone process verbs when they refer to the checking process
    text = re.sub(r'\bverifies?\b', '', text, flags=re.I)
    text = re.sub(r'\bconfirms?\b', '', text, flags=re.I)
    text = re.sub(r'\bchecks?\b', '', text, flags=re.I)
    text = re.sub(r'\bretains?\b', '', text, flags=re.I)
    text = re.sub(r'\bthe verifier\b', '', text, flags=re.I)
    # Remove standalone "script" references (internal tooling)
    text = re.sub(r'\bscript\b', '', text, flags=re.I)
    # Replace "Eq. (N.N)" and "Eq. N.N" style references
    text = re.sub(r'Eq\. \(([^)]+)\)', r'\1', text)
    text = re.sub(r'Eq\. ([0-9]+\.[0-9]+)', r'\1', text)
    # Remove internal OCL references
    text = re.sub(r'\s*OCL-\d+', '', text)
    text = re.sub(r'\s*see\s+OCL-\d+', '', text)
    # Collapse whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    # Capitalize first letter
    if text:
        text = text[0].upper() + text[1:]
    # Clean up double periods and trailing punctuation
    text = re.sub(r'\.\s*\.', '.', text)
    text = text.rstrip('. ')
    return text


lines = []
lines.append(BS + "subsection{Verified equation register: assumptions and limits}")
lines.append(BS + "label{sec:12.verified_register}")
lines.append("")
lines.append("The displayed equations were checked within the stated scope; each entry gives the")
lines.append("assumptions under which the check holds and the limits beyond which it does not apply.")
lines.append("Conformance statements are restricted to the displayed equations and the cited sources;")
lines.append("they are not convergence, stability, or source-transcription results beyond the stated scope.")
lines.append("")
lines.append(BS + "begin{description}")
for r in verified:
    label = r['label']
    section = r['section']
    assumptions = clean(r['scope_and_assumptions'].strip())
    limits = clean(r['negative_test'].strip())
    lines.append("")
    lines.append(f"  {BS}item[{BS}eqref{{{label}}} (Section~{section})] {assumptions}. {limits}.")
lines.append(BS + "end{description}")
lines.append("")

open('/home/user/le/verified_list.tex', 'w', encoding='utf-8').write(chr(10).join(lines))
print("wrote", len(verified), "items")
