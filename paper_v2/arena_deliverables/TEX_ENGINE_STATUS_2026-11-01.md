# Can a PDF be built inside this sandbox? No — and here is the evidence

The author asked for the TeX engine to be installed so that the PDF can be built here instead of on Overleaf.
Everything below was actually tried on 2026-11-01, in this workspace, in this order.

| route | what was tried | result |
|---|---|---|
| system TeX | `which pdflatex xelatex lualatex latexmk tectonic` | none present |
| Debian/Ubuntu packages | `curl https://deb.debian.org/debian/` | **000** — host not reachable |
| CTAN | `curl https://mirror.ctan.org` | **000** — not reachable |
| GitHub raw / release assets | `curl https://raw.githubusercontent.com`, `https://objects.githubusercontent.com` | **000** — the two hosts every prebuilt binary download redirects to |
| tectonic binary (npm `node-tectonic-linux-x64`, 56 MB) | extracted, `--version` | `error while loading shared libraries: libgraphite2.so.3` — the binary does **not** import a single graphite2 symbol (`nm -D \| grep -c graphite` = **0**), so a stub library would satisfy the loader; but |
| tectonic's TeX bundle | `curl https://relay.fullyjustified.net/default_bundle.tar`, `https://archive.org` | **000** — tectonic cannot typeset a single character without its bundle, and every host that serves it is blocked |
| tectonic binary (`@node-latex-compiler/bin-linux-x64`) | extracted, `ldd` | needs `GLIBC_2.38`/`GLIBC_2.39`; this image has older glibc |
| npm `texlive` (88 MB) | installed, `binary.zip` inspected | contains **pdfTeX 1.40.11 source** (368 `.h`, 291 `.c`, 196 `.o`), not a build — and no `texmf` tree |
| npm `texlive.js` wasm route | `texlyre-busytex`, `SwiftLaTeX/busytex`, `TeXlyre/texlyre-busytex-build` (154 MB) | these are API wrappers and emcc build scripts: **no prebuilt `.wasm`, no TeX Live data** in the repository trees; Emscripten itself would also have to be downloaded |
| PyPI | `tectonic`, `texlive`, `texlive-bundle`, `pdflatex`, `latexmk`, `swiftlatex`, `busytex` | 404 everywhere; `latex`/`pdflatex`/`latexmk` are thin wrappers that call a `pdflatex` that does not exist |
| any TeX files already on disk | `find / -name "*.sty" -o -name "article.cls" -o -name "*.fmt"` | **nothing** — there is not one `.sty` on this machine to feed an engine even if one loaded |

**Conclusion.** The engine is not a matter of trying harder; the distribution is unreachable and absent. A LaTeX
PDF cannot be produced in this sandbox today.

## What unblocks it, in order of preference

1. **Overleaf** (the author's normal workflow): upload `le_review_v1.2_2026-11-01.zip` as a new project, main
   document `main.tex`, and it builds with `pdflatex + bibtex + pdflatex×2`. This is what the package is built for.
2. **Give the sandbox a TeX distribution offline.** Any of these, dropped into Drive, would be installed here and
   the PDF would then be built and iterated *in this session*:
   - the `.deb` files of `texlive-latex-base`, `texlive-latex-recommended`, `texlive-latex-extra`,
     `texlive-fonts-recommended`, `texlive-science`, `texlive-publishers` (+ `dvi2pdf`); `dpkg -i` needs no network;
   - or a `texlive` `.tar.xz` tree (TeX Live full or the `install-tl` "scheme-medium" archive).
   With either, `pdflatex main && bibtex main && pdflatex main && pdflatex main` runs here, and every subsequent
   revision can be rebuilt and page-checked in this session.

## What is verified instead, and is not a substitute for compiling

`P1_audit/audit_sources.py` (12 checks, 0 failures) verifies every `\ref`, `\label`, `\cite`, `\input` and
`\includegraphics`, duplicate labels, placeholder text, header counts and bibliography completeness against the
sources. `make_submission_zip.py` repeats that verification on the **staged** tree and refuses to write a zip that
fails it. What neither can catch, and only a compile can: overfull boxes, page count, float placement, whether
`cleveref` and `subcaption` agree with `hyperref`, and the page-level appearance of the 166 equations.
