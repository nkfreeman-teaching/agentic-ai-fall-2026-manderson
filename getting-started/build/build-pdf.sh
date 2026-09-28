#!/usr/bin/env bash
# Rebuild the PDF versions of the getting-started guides from their markdown.
# Run from any directory after editing mac.md or windows.md. Pixi supplies
# pandoc and the Tectonic LaTeX engine, so no system LaTeX install is needed.
set -euo pipefail

cd "$(dirname "$0")/.."
for guide in mac windows; do
  pixi exec --spec pandoc --spec tectonic -- pandoc "${guide}.md" \
    --from=gfm \
    --shift-heading-level-by=-1 \
    --lua-filter=build/pdf-filter.lua \
    --include-in-header=build/header.tex \
    --pdf-engine=tectonic \
    --variable=geometry:margin=1in \
    --variable=papersize=letter \
    --variable=fontsize=11pt \
    --variable=colorlinks=true \
    --variable=linkcolor=linkblue \
    --variable=urlcolor=linkblue \
    --output="${guide}.pdf"
  echo "Wrote getting-started/${guide}.pdf"
done
