# Insert verified_list.tex block into sec12_comparative.tex between the
# "Scope." paragraph of 12.3b and the "Status by family" subsection.
sec_path = 'phase5/master/sections/sec12_comparative.tex'
frag = open('verified_list.tex', encoding='utf-8').read()
text = open(sec_path, encoding='utf-8').read()

anchor_end = "\\subsection{Status by family: established, disputed or model-dependent, open}"
idx = text.find(anchor_end)
if idx < 0:
    raise SystemExit("anchor not found")

# Insert before the anchor, separated by a blank line.
insertion = "\n\n" + frag.rstrip() + "\n\n"
new_text = text[:idx] + insertion + text[idx:]

open(sec_path, 'w', encoding='utf-8').write(new_text)
print("inserted verified register at char", idx)
