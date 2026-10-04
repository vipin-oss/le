# KNOWN_LIMITATIONS

Everything here is stated in the manuscript too; this file exists so a
reader of the archive does not mistake a limit for a defect waiting to be fixed.

## Scientific limits (from `08_FINAL_OUTPUTS/manuscript/AUTHOR_INPUT_REQUIRED.md` section C)

- No physical validation exists: no transient cavity measurements for beta-Ga2O3 are available, so
- every comparison is against an exact solution or an independent implementation of the same model.
- The relaxation times (1, 5, 20 ps) are hypothetical order-of-magnitude values; the memory results
- are sensitivities, not predictions.
- Continuum validity at 5-50 nm is not established (grey MFP about 3 nm, long-MFP phonons to about
- 0.7-1 um), which is stated where the size effect is discussed.
- Thermal-expansion data differ by more than an order of magnitude between the two cited sources;
- the ablation E-series is the honest account of what that does to the absolute stress scale.
- `cp = 560 J/(kg K)` is an estimate (Debye) against reported 485-537; `alpha_5 = 0` is assumed.
- Coverage is partial by design: memory and feedback runs are circular-cavity only, the ellipse was
- run with Fourier conduction.
- An 80a outer boundary with a clamped cold rim makes elastic echoes a model feature above about
- 20 nm; the quantity-of-interest window is echo-free only up to about 10 nm.
- A 192x192 grid could not be run in the memory available; the grid uncertainty is from the
- extrapolated sweep instead.
- One verification test fails (V0, hand-off grid family, chi = 2, 5.03e-3 against a 5e-3 threshold,
- dominated by angular resolution). It is reported, not hidden. One further test is exploratory.

## Authorship and submission items still open

These are not limitations of the science; they are the fields only the authors can supply. The
five blocking ones are set out as blanks in `08_FINAL_OUTPUTS/manuscript/AUTHOR_INPUT_FORM.md`:
authors/affiliations/ORCID, CRediT, competing interest, funding, and the data DOI. The placeholder
tokens `[AUTHOR INPUT REQUIRED]` and `[PUBLIC REPOSITORY/DOI TO BE INSERTED]` appear in the
manuscript sources, and the QA gate refuses to pass while the *wrong* kind of placeholder exists,
so their presence is deliberate and tracked, not an oversight.

## Environment limits of this archive

- **The manuscript was never compiled here.** No TeX engine exists in the packaging environment, so
  `02_OVERLEAF/README_OVERLEAF.md` reports a static verification (paths, figures, citations,
  commands, references) and the compile itself stays an author-side step. Nothing in the archive
  claims a successful compile.
- **The 600-dpi raster and TIFF renditions are derived, gitignored files.** They are included when
  the working copy has them and omitted otherwise, always regenerable with the command in
  `FIGURE_PROVENANCE.md` (about a minute); the count actually packed is in
  `archive_build.json` -> `derived_files`. The tracked 200-dpi PNGs and the vector PDFs are in the
  archive in both cases, so nothing needed for reproduction depends on the derived set.
- **`reportlab`/`python-docx` versions used for the .docx/.pdf previews are not pinned anywhere in
  the repository**, so a different version can render slightly different page breaks in the preview
  PDFs. The `.md` and `.tex` sources are the authoritative text; the PDFs are previews.
- Reproduction status recorded by this build: PASS (5 steps reported)
