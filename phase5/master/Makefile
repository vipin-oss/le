# Reproducible phase5 build target; runs static checks, figure conversion, TeX/BibTeX and gates.
.PHONY: pdf clean check

pdf:
	bash ../scripts/build_master.sh

check: pdf

clean:
	latexmk -C -outdir=build main.tex
