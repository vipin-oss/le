# Export readiness and archive inventory

The manuscript has not been compiled from phase5 v1.1. Consequently, the required **complete master source + final v1.1 PDF ZIP has not been created**; including the preserved v1.0 PDF under a v1.1 label would be misleading. The individual figure PDFs are assets, not a compiled manuscript PDF.

Source-only handoff archives were created and passed `unzip -t`:

- `phase5-v1.1-master-source-only.zip` — master LaTeX, portable tables, SVG/PDF figure assets, bibliography, build scripts, and audit records; no compiled manuscript PDF or baseline PDF.
- `phase5-v1.1-journal-source-supplement-only.zip` — generic journal and supplement wrappers plus shared source/assets and records; not compiled and not journal-specific.
- `phase5-v1.1-source-audit.zip` — audit workspace snapshot, including the preserved v1.0 baseline PDF and thumbnail survey for provenance; no v1.1 PDF.

Do not rename these as final submission packages. The complete master source+PDF archive can be produced only after a successful clean build, inspection of the exact PDF, and a new packaging pass. `scripts/package_sources.py` reproduces the source-only archives and intentionally refuses to label the v1.0 baseline as a v1.1 build.
