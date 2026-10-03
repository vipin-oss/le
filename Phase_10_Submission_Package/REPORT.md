# Phase 10 - submission package: self-contained LaTeX artwork and uploadable cover letter

Two things were still only half-done after Phases 8-9. Both are closed here, and no builder or
frozen source was modified, so the code freeze stays `CODE_FREEZE_submission_2026_10_03j.json`.

## 1. The LaTeX figure paths were not portable

`tools/md_to_tex.py` emitted `\includegraphics[width=...]{../11_Figures/figN.png}` - a path
that climbs out of the manuscript folder, so it resolves only when the whole repository layout
travels with the `.tex`, and it pointed at the 200-dpi PNGs while Phase 9 had produced vector
renditions. Now:

* `verification/make_tex_figure_set.py` copies the eight vector PDFs into
  `PAPER_PROJECT/13_Manuscript/figures/` (running the Phase 9 exporter first if they are not on
  disk) and prints the sha256 of each file, then checks that the figure names match the
  manuscript exactly: `RESULT: OK - 8 figures, names match the manuscript exactly`.
* `tools/md_to_tex.py` puts `\graphicspath{{figures/}}` in both preambles and includes figures by
  name only (`{fig1_setup}`), so `FINAL_REVISED_MANUSCRIPT.tex` + `figures/` +
  `FINAL_REVISED_REFERENCES.bib` compile on their own. `grep 11_Figures` on the regenerated
  `.tex` now returns nothing.
* **Fallback verified, not assumed**: with `13_Manuscript/figures/` temporarily moved away, the
  generator reverts to the PNG paths and still produces a valid `.tex`; the folder was restored,
  the `.tex` regenerated, and `tools/audit_tex.py` passes in both states.
* The Markdown and the locally rendered preview PDF keep embedding the frozen 200-dpi PNGs, so
  the provenance of the figures the reported numbers were read from is unchanged - only the
  LaTeX source switched. `tools/audit_tex.py` learned to resolve `\graphicspath` the way LaTeX
  does (it previously declared every extensionless include missing, which was the checker's
  limitation, not the document's).

## 2. The letter and the compile check were not in uploadable form

* `verification/make_cover_letter_package.py` renders `13_Manuscript/cover_letter.md` to
  `cover_letter.docx` and `cover_letter.pdf` (2 pages, 765 words against the 766-word source -
  the difference is the `#` marker). It parses the Markdown at run time, so there is no second
  copy of the prose to drift; bracketed author-input fields are bolded so they cannot be missed.
  The letter still names the 03j freeze, the 28-case suite and the Cattaneo/Vernotte citation
  decision, all confirmed present in the rendered PDF.
* `compile_check.sh` is the author-side half of the one thing this environment cannot do: with
  TeX Live present it compiles both documents (pdflatex, bibtex, pdflatex x2), reports page
  counts, undefined citations, undefined references, overfull hboxes and bibtex warnings into
  `COMPILE_CHECK.txt`, and copies the compiled PDFs back for inspection; without an engine it
  prints the exact commands, the `elsarticle.cls` requirement and the static gates that do run
  headless. `bash -n` clean. It writes nothing into the manuscript sources.

## 3. The deposit object refreshed

`00_Project_Control/make_packages.py final` re-run so the package matches the tree as it now is:
`RESEARCH_PROJECT_FINAL.zip`, 604 files, ~46.6 MB uncompressed, `MANIFEST.json` with a SHA-256
per file, and it verified to contain `13_Manuscript/figures/` (8 vector PDFs), the 03j freeze and
the cover letter. This remains the object to upload for the DOI.

## Gates after the phase

`tools/audit_tex.py` ALL CHECKS PASSED (with `info  8 of 8 figures resolve from
13_Manuscript/figures/ (vector PDF set)`), `tools/check_crossrefs.py` all resolve,
`tools/check_tex_commands.py` ALL DEFINED, `tools/test_md_to_tex.py` ALL 26 CONVERSION TESTS
PASSED, `tools/verify_pdf.py` ALL CHECKS PASSED for the manuscript and (`-c`) the companion,
`Phase_08_Final_Audit/verification/final_consistency.py` 0 failures,
`tools/connection_audit.py` all connection checks passed after the commit.

## 4. Downloadable bundle (this phase's deliverable for the authors)

`verification/make_upload_bundle.py` builds `Phase_10_Submission_Package/IJHMT_submission_bundle.zip`
(2.62 MB, 29 entries): the two `.tex` sources, the `.bib`, the eight vector figures under
`MANUSCRIPT/figures/`, the Markdown sources of truth, the rendered preview PDFs,
`highlights.txt`, the supplementary workbook, the cover letter in .md/.docx/.pdf, the submission
checklist and author-input list, the deposit manifest
(`CODE_FREEZE_submission_2026_10_03j.json`), `PDF_VERIFICATION.txt`, the
reference-ordering artifacts, a `PROVENANCE/README.txt` that says how every file was produced and
what is still bracketed for the authors, and a `MANIFEST.json` with a SHA-256 and byte size for
every file. The bundle is verified after building (`testzip()` clean, 27/27 manifest hashes
match) and it is **deterministic** - rebuilding gives byte-identical output (fixed timestamps,
sorted order, fixed compression), which is what makes the manifest hashes usable as a checksum of
the upload.

It is committed on purpose: the workspace has been rebuilt from git eleven times during this
programme, and `PAPER_PROJECT/packages/` is gitignored by the repository's own convention, so a
large generated zip there does not survive a reset while this one does.

The **full deposit package** (raw per-run `.npz/.json` outputs, convergence families, the whole
code tree, ~43.6 MB, 603 files) is regenerated with
`python3 PAPER_PROJECT/00_Project_Control/make_packages.py final` into
`PAPER_PROJECT/packages/RESEARCH_PROJECT_FINAL.zip`; that is the object to deposit in a public
repository to obtain the DOI quoted in the Data availability statement, and it is deliberately not
kept in git.
