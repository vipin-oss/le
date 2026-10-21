#!/usr/bin/env bash
# ---------------------------------------------------------------------------
# build_deliverable_zip.sh
#
# Packages the complete review manuscript work into a single distributable
# ZIP archive.
#
# Contents:
#   01_manuscript_latex/   - full LaTeX source (main.tex, 17 sections,
#                            frontmatter, appendices, table sources,
#                            figure sources, build files)
#   02_bibliography/       - verified BibTeX library, DOI verification
#                            ledger, source provenance, manuscript-local copy
#   03_figures/            - original vector figure sources (SVG) + rendered
#   04_tables/             - standalone table sources (T1-T8)
#   05_compiled_pdf/       - compiled manuscript PDF + LaTeX build logs
#   06_literature_database/- expanded literature database, PDF inventory,
#                            text extractions, metadata, ingestion report
#   07_research_history/   - phases 1-3 planning/research records, equation
#                            derivations, verification logs, domain taxonomy
#   08_build_guides/       - build + validation scripts, CI workflow
#   DELIVERABLES.md        - manifest and scientific-readiness assessment
#   ZIP_MANIFEST.txt       - SHA-256 checksum for every packaged file
#
# NOTE: copyrighted source PDFs are NEVER included. Only text extractions
#       and synthesized content are packaged, per the repository's
#       copyright guidance. The single PDF shipped here is the compiled
#       output of this repository's own LaTeX source.
# ---------------------------------------------------------------------------
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VERSION="${1:-v1.0}"
PKG_NAME="le-review-manuscript-${VERSION}"
STAGE="${TMPDIR:-/tmp}/${PKG_NAME}"
OUT_ZIP="${2:-${REPO_ROOT}/../${PKG_NAME}.zip}"

echo "==> Building ${PKG_NAME}"
rm -rf "$STAGE"
mkdir -p "$STAGE"

# --- place <destdir> <srcpath-relative-to-repo> [destname] -----------------
place() {
  local destdir="$1" src="$2" name="${3:-}"
  [ -e "${REPO_ROOT}/${src}" ] || { echo "    ! missing: ${src}"; return 0; }
  local base; base="$(basename "$src")"
  [ -n "$name" ] && base="$name"
  mkdir -p "${STAGE}/${destdir}"
  cp -r "${REPO_ROOT}/${src}" "${STAGE}/${destdir}/${base}"
}

# --- place_dir <destdir> <srcdir-relative-to-repo> <subdir-name> -----------
# <subdir-name> may contain slashes; its parent directories are created.
place_dir() {
  local destdir="$1" src="$2" sub="$3"
  [ -d "${REPO_ROOT}/${src}" ] || { echo "    ! missing: ${src}"; return 0; }
  mkdir -p "${STAGE}/${destdir}/$(dirname "${sub}")"
  cp -r "${REPO_ROOT}/${src}" "${STAGE}/${destdir}/${sub}"
}

# --- 01 manuscript LaTeX source --------------------------------------------
echo "    01_manuscript_latex"
place "01_manuscript_latex/manuscript" phase4/manuscript/main.tex
place "01_manuscript_latex/manuscript" phase4/manuscript/Makefile
place "01_manuscript_latex/manuscript" phase4/manuscript/BUILD.md
place_dir "01_manuscript_latex/manuscript" phase4/manuscript/sections sections
place_dir "01_manuscript_latex/manuscript" phase4/manuscript/frontmatter frontmatter
place_dir "01_manuscript_latex/manuscript" phase4/manuscript/appendices appendices
place_dir "01_manuscript_latex/manuscript" phase4/manuscript/tables tables
place_dir "01_manuscript_latex/manuscript" phase4/manuscript/figures figures
# The manuscript \input{} paths resolve relative to the MAIN file's directory,
# so the compiled table set must sit one level above the manuscript folder
# and the manuscript-local bibliography must sit beside main.tex.
place_dir "01_manuscript_latex" phase4/tables/source tables/source
place "01_manuscript_latex/manuscript" phase4/manuscript/references_local.bib references_local.bib

# --- 02 bibliography --------------------------------------------------------
echo "    02_bibliography"
place "02_bibliography" phase4/references/library.bib
place "02_bibliography" phase4/references/doi_verification.csv
place "02_bibliography" phase4/references/source_provenance.csv
place "02_bibliography" phase4/manuscript/references_local.bib references_local.bib

# --- 03 figures -------------------------------------------------------------
echo "    03_figures"
place_dir "03_figures/manuscript" phase4/manuscript/figures/source source
place_dir "03_figures/manuscript" phase4/manuscript/figures/rendered rendered
place_dir "03_figures/legacy" phase4/figures/source source
place_dir "03_figures/legacy" phase4/figures/rendered rendered

# --- 04 tables --------------------------------------------------------------
echo "    04_tables"
place_dir "04_tables" phase4/tables/source source

# --- 05 compiled PDF --------------------------------------------------------
echo "    05_compiled_pdf"
mkdir -p "$STAGE/05_compiled_pdf"
if [ -f "${REPO_ROOT}/phase4/manuscript/main.pdf" ]; then
  cp "${REPO_ROOT}/phase4/manuscript/main.pdf" "$STAGE/05_compiled_pdf/main.pdf"
  echo "    + compiled PDF included"
else
  echo "    ! compiled PDF not present in working tree"
fi
for lg in main.log main.blg build_diagnostics.txt; do
  [ -f "${REPO_ROOT}/phase4/manuscript/${lg}" ] && cp "${REPO_ROOT}/phase4/manuscript/${lg}" "$STAGE/05_compiled_pdf/" || true
done

# --- 06 literature database -------------------------------------------------
echo "    06_literature_database"
for rel in expanded_literature_database.csv master_inventory.csv \
           deep_extraction_summary.md COPYRIGHT_GUIDANCE.md \
           search_results_nonlocal_piezoelectric.md \
           search_results_thermoelasticity_families.md; do
  place "06_literature_database" "phase4/literature/${rel}"
done
place_dir "06_literature_database" phase4/literature/extraction extraction
place_dir "06_literature_database" phase4/literature/metadata metadata
place_dir "06_literature_database" phase4/literature/reports reports

# --- 07 research history (phases 1-3) --------------------------------------
echo "    07_research_history"
for d in phase1 phase2 phase3; do
  place_dir "07_research_history" "$d" "$d"
done
for f in README.md research_profile.md domain_taxonomy.md \
         recommended_research_direction.md existing_review_analysis.md \
         five_candidate_topics.md source_verification_log.csv \
         topic_comparison_matrix.csv; do
  place "07_research_history" "$f"
done
place_dir "07_research_history" phase4/reports phase4_reports
place_dir "07_research_history" phase4/equations phase4_equations

# --- 08 build guides -------------------------------------------------------
echo "    08_build_guides"
place_dir "08_build_guides" scripts scripts
place_dir "08_build_guides" .github .github
place "08_build_guides" Makefile top-level-Makefile

# --- manifest ---------------------------------------------------------------
if [ -f "${REPO_ROOT}/DELIVERABLES.md" ]; then
  cp "${REPO_ROOT}/DELIVERABLES.md" "$STAGE/DELIVERABLES.md"
fi

echo "==> Generating file manifest with checksums"
( cd "$STAGE" && find . -type f ! -name "ZIP_MANIFEST.txt" -print0 \
    | sort -z \
    | xargs -0 sha256sum > ZIP_MANIFEST.txt )

# --- zip --------------------------------------------------------------------
rm -f "$OUT_ZIP"
( cd "$(dirname "$STAGE")" && zip -r -q "$OUT_ZIP" "$PKG_NAME" )

SIZE=$(du -h "$OUT_ZIP" | cut -f1)
COUNT=$(find "$STAGE" -type f | wc -l)
echo "==> ${PKG_NAME}.zip  (${COUNT} files, ${SIZE})"
echo "    ${OUT_ZIP}"
