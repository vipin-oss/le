# Makefile for Multiphysics Wave Mechanics Review Manuscript
# Version B — Extended Authoritative Review
#
# Usage: make pdf        # Compile PDF (requires TeX engine)
#        make clean      # Remove auxiliary files
#        make check      # Check for compilation issues
#
# Requires: pdflatex, bibtex (or a complete TeX Live distribution)

TEX      = pdflatex
BIBTEX   = bibtex
LATEXMK  = latexmk
MAIN     = main.tex
TARGET   = main.pdf

.PHONY: pdf clean check bib

pdf: $(TARGET)

$(TARGET): $(MAIN) frontmatter/*.tex sections/*.tex appendices/*.tex references/library.bib
	$(LATEXMK) -pdf -interaction=nonstopmode $(MAIN) 2>&1 || \
	( $(TEX) -interaction=nonstopmode $(MAIN) && \
	  $(BIBTEX) main && \
	  $(TEX) -interaction=nonstopmode $(MAIN) && \
	  $(TEX) -interaction=nonstopmode $(MAIN) )

bib:
	$(BIBTEX) main

check: $(TARGET)
	@echo "=== Checking for undefined references ==="
	@grep -c "Undefined reference" main.log 2>/dev/null || echo "0 undefined references"
	@echo "=== Checking for undefined control sequences ==="
	@grep -c "Undefined control sequence" main.log 2>/dev/null || echo "0 undefined control sequences"
	@echo "=== Checking for missing bibliography entries ==="
	@grep -c "undefined" main.blg 2>/dev/null || echo "0 missing bibliography entries"
	@echo "=== Checking for overfull boxes ==="
	@grep -c "Overfull" main.log 2>/dev/null || echo "0 overfull boxes"

clean:
	rm -f *.aux *.log *.blg *.bbl *.out *.toc *.lof *.lot \
	      *.synctex.gz *.fdb_latexmk *.fls *.pdf

view: $(TARGET)
	@xdg-open $(TARGET) 2>/dev/null || echo "PDF viewer not available"
