# Escape bare '_' and '^' in TEXT MODE (outside $...$ and outside LaTeX command
# arguments) ONLY within the verified register region of sec12_comparative.tex.
# Pre-existing table \label{...} underscores outside this region are left intact.
import re

SEC = "/home/user/le/phase5/master/sections/sec12_comparative.tex"
s = open(SEC, encoding="utf-8").read()
start_marker = "\\subsection{Verified equation register: assumptions and limits}"
end_marker = "\\subsection{Status by family: established, disputed or model-dependent, open}"
si = s.find(start_marker)
ei = s.find(end_marker)
assert si >= 0 and ei > si, "markers not found"
region = s[si:ei]

CMD = re.compile(
    r'\\(subsection|subsubsection|paragraph|label|ref|eqref|cite|textbf|emph|item|'
    r'begin\{itemize\}|end\{itemize\}|url|path|texttt|textrm|dotfill)\{([^}]*)\}'
)

def protect_cmds(text):
    tokens = []
    def repl(m):
        tokens.append(m.group(0))
        return "\x00CMD%d\x00" % (len(tokens) - 1)
    protected = CMD.sub(repl, text)
    return protected, tokens

def restore_cmds(text, tokens):
    for i, tok in enumerate(tokens):
        text = text.replace("\x00CMD%d\x00" % i, tok)
    return text

def fix_region(text):
    out_lines = []
    for line in text.split("\n"):
        parts = re.split(r'(\$[^$]*\$)', line)
        new_parts = []
        for k, part in enumerate(parts):
            if k % 2 == 1:
                new_parts.append(part)  # inline math: keep
            else:
                protected, tokens = protect_cmds(part)
                protected = re.sub(r'(?<!\\)_', r'\\_', protected)
                protected = re.sub(r'(?<!\\)\^', r'\\^', protected)
                part = restore_cmds(protected, tokens)
                new_parts.append(part)
        out_lines.append("".join(new_parts))
    return "\n".join(out_lines)

new_region = fix_region(region)
added_ = new_region.count("\\_") - region.count("\\_")
added_caret = new_region.count("\\^") - region.count("\\^")
print("escaped underscores added:", added_)
print("escaped carets added:", added_caret)
assert added_ > 0, "expected some underscores to escape"

s2 = s[:si] + new_region + s[ei:]
open(SEC, "w", encoding="utf-8").write(s2)
print("updated sec12 verified register region; escaped", added_, "underscores")
