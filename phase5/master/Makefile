# Versioned v1.1 build target; requires latexmk, pdflatex, bibtex, and PDF figures.
LATEXMK ?= latexmk
MAIN := main.tex

.PHONY: pdf clean check
pdf:
	$(LATEXMK) -pdf -interaction=nonstopmode -halt-on-error $(MAIN)

check: pdf
	@if grep -E 'Undefined (reference|control sequence)|Citation .* undefined|There were undefined references' main.log; then exit 1; fi
	@if grep -E 'I couldn.t open database file|Warning--I didn.t find a database entry' main.blg; then exit 1; fi

clean:
	$(LATEXMK) -C $(MAIN)
