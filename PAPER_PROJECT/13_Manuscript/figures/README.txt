Figure set for the LaTeX source (FINAL_REVISED_MANUSCRIPT.tex).
Vector renditions of the eight manuscript figures, exported by
Phase_09_Closeout/verification/export_submission_figures.py from the frozen
08_Experiments/make_figures.py, and copied here by
Phase_10_Submission_Package/verification/make_tex_figure_set.py.

tools/md_to_tex.py points \graphicspath at this folder and includes the figures by
name only, so the .tex file plus this folder compile on their own. The Markdown and
the locally rendered preview PDF still use the frozen 200-dpi PNGs in 11_Figures/, so
the provenance of the figures the reported numbers were read from is unchanged.
If this folder is absent, md_to_tex.py falls back to the PNG paths automatically.
