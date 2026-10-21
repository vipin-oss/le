#!/usr/bin/env bash
# ---------------------------------------------------------------------------
# build_deliverable_zip.sh
#
# Packages the complete review manuscript work into a single distributable
# ZIP archive.
#
# Contents:
#   01_manuscript_latex/   - full LaTeX source (main.tex, 17 sections,
#                            frontmatter, appendices, tables, figure sources)
#   02_bibliography/       - verified BibTeX library + DOI verification
#   03_figures/            - original vector figure sources (SVG) + rendered
#   04_tables/             - standalone table sources
#   05_compiled_pdf/       - compiled manuscript PDF (from CI build)
#   06_literature_database/- expanded literature database + text extractions
#   07_research_history/   - phases 1-3 planning/research records
#   08_build_guides/       - build instructions, CI workflow, scripts
#   DELIVERABLES.md        - manifest and scientific-readiness assessment
#   ZIP_MANIFEST.txt       - full file inventory with SHA-256 checksums
#
# NOTE: copyrighted source PDFs are NEVER included. Only text extractions
#       and synthesized content are packaged, per the repository's
#       copyright guidance.
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

# --- helper: copy a tracked file if it exists -------------------------------
copy_if() {
  local rel="$1"
  if [ -e "${REPO_ROOT}/${rel}" ]; then
    mkdir -p "$STAGE/$(dirname "$rel")"
    cp -r "${REPO_ROOT}/${rel}" "$STAGE/$rel"
  fi
}

copy_all() {
  local dest="$1"; shift
  mkdir -p "$STAGE/${dest}"
  for rel in "$@"; do
    if [ -e "${REPO_ROOT}/${rel}" ]; then
      mkdir -p "$STAGE/$(dirname "${rel}")"
      cp -r "${REPO_ROOT}/${rel}" "$STAGE/$rel"
    fi
  done
}

# --- 01 manuscript LaTeX source --------------------------------------------
copy_all "01_manuscript_latex/manuscript" \
  phase4/manuscript/main.tex \
  phase4/manuscript/Makefile \
  phase4/manuscript/BUILD.md \
  phase4/manuscript/sections \
  phase4/manuscript/frontmatter \
  phase4/manuscript/appendices \
  phase4/manuscript/tables \
  phase4/manuscript/figures

# --- 02 bibliography --------------------------------------------------------
copy_all "02_bibliography" \
  phase4/references/library.bib \
  phase4/references/doi_verification.csv \
  phase4/references/source_provenance.csv \
  phase4/manuscript/references_local.bib

# --- 03 figures -------------------------------------------------------------
copy_all "03_figures" \
  phase4/manuscript/figures/source \
  phase4/manuscript/figures/rendered \
  phase4/figures/source \
  phase4/figures/rendered

# --- 04 tables --------------------------------------------------------------
copy_all "04_tables" \
  phase4/tables/source

# --- 05 compiled PDF --------------------------------------------------------
mkdir -p "$STAGE/05_compiled_pdf"
if [ -f "${REPO_ROOT}/phase4/manuscript/main.pdf" ]; then
  cp "${REPO_ROOT}/phase4/manuscript/main.pdf" "$STAGE/05_compiled_pdf/main.pdf"
  echo "    + compiled PDF included"
else
  echo "    ! compiled PDF not present in working tree (CI publishes it to the branch)"
fi
for lg in main.log main.blg; do
  [ -f "${REPO_ROOT}/phase4/manuscript/${lg}" ] && cp "${REPO_ROOT}/phase4/manuscript/${lg}" "$STAGE/05_compiled_pdf/" || true
done

# --- 06 literature database -------------------------------------------------
mkdir -p "$STAGE/06_literature_database"
for rel in phase4/literature/expanded_literature_database.csv \
           phase4/literature/master_inventory.csv \
           phase4/literature/deep_extraction_summary.md \
           phase4/literature/COPYRIGHT_GUIDANCE.md \
           phase4/literature/search_results_nonlocal_piezoelectric.md \
           phase4/literature/search_results_thermoelasticity_families.md \
           phase4/literature/reports \
           phase4/literature/metadata \
           phase4/literature/extraction; do
  copy_if "$rel"
done

# --- 07 research history (phases 1-3) --------------------------------------
mkdir -p "$STAGE/07_research_history"
for d in phase1 phase2 phase3; do
  if [ -d "${REPO_ROOT}/${d}" ]; then
    mkdir -p "$STAGE/07_research_history/${d}"
    cp -r "${REPO_ROOT}/${d}/." "$STAGE/07_research_history/${d}/"
  fi
done
for f in README.md research_profile.md domain_taxonomy.md \
         recommended_research_direction.md existing_review_analysis.md \
         five_candidate_topics.md source_verification_log.csv \
         topic_comparison_matrix.csv; do
  copy_if "$f"
done
if [ -d "${REPO_ROOT}/phase4/reports" ]; then
  cp -r "${REPO_ROOT}/phase4/reports" "$STAGE/07_research_history/phase4_reports"
fi
if [ -d "${REPO_ROOT}/phase4/equations" ]; then
  cp -r "${REPO_ROOT}/phase4/equations" "$STAGE/07_research_history/phase4_equations"
fi

# --- 08 build guides -------------------------------------------------------
mkdir -p "$STAGE/08_build_guides"
cp -r "${REPO_ROOT}/scripts" "$STAGE/08_build_guides/scripts" 2>/dev/null || true
cp -r "${REPO_ROOT}/.github" "$STAGE/08_build_guides/.github" 2>/dev/null || true
copy_if "Makefile"

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
