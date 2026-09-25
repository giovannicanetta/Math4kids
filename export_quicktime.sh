#!/usr/bin/env bash
# Render the full narrated story and wrap it in a QuickTime-friendly .mov
# (H.264 + AAC, faststart), ready to share and play.
#
#   ./export_quicktime.sh [output.mov] [quality flag, default -qh]
set -euo pipefail

out="${1:-PowersAndLogs.mov}"
quality="${2:--qh}"
manim="${MANIM:-.venv/bin/manim}"

"$manim" "$quality" scenes/full_video.py PowersAndLogs

src=$(ls -t media/videos/full_video/*/PowersAndLogs.mp4 | head -1)
ffmpeg -i "$src" \
  -c:v libx264 -preset medium -crf 22 -pix_fmt yuv420p \
  -c:a aac -b:a 160k -movflags +faststart "$out" -y

echo "wrote $out from $src"
