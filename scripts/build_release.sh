#!/usr/bin/env bash
# Build release packages into dists/ (CLAUDE.md §8 M6).
#
#   scripts/build_release.sh [SDK_DIR]
#
# Produces:
#   dists/<name>-<version>-win.zip         Windows
#   dists/<name>-<version>-mac.zip         macOS (.app, unsigned)
#   dists/<name>-<version>-linux.tar.bz2   Linux
#   dists/<name>-<version>-web.zip         HTML5 for itch.io (no Dev tools)
#   dists/SHA256SUMS.txt
#
# Works on macOS and Linux. The SDK needs web support for the web zip
# (scripts/fetch_renpy.sh --web). Release builds never include the playtest
# Dev button: this script refuses to run if game/playtest_enabled.txt exists.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
VERSION_RENPY="$(cat "$ROOT/RENPY_VERSION")"
SDK="${1:-$HOME/renpy-sdk/renpy-$VERSION_RENPY-sdk}"
DEST="$ROOT/dists"

export SDL_VIDEODRIVER="${SDL_VIDEODRIVER:-dummy}"
export SDL_AUDIODRIVER="${SDL_AUDIODRIVER:-dummy}"

if [[ -e "$ROOT/game/playtest_enabled.txt" ]]; then
  echo "error: game/playtest_enabled.txt exists; delete it before a release build." >&2
  exit 1
fi
if grep -Eq '^define PLAYTEST = True' "$ROOT/game/playtest.rpy"; then
  echo "error: PLAYTEST is hard-coded to True in game/playtest.rpy." >&2
  exit 1
fi

GAME_VERSION="$(sed -nE 's/^define config.version = "([^"]+)".*/\1/p' "$ROOT/game/options.rpy")"
BUILD_NAME="$(sed -nE 's/^define build.name = "([^"]+)".*/\1/p' "$ROOT/game/options.rpy")"
BASE="$BUILD_NAME-$GAME_VERSION"
echo "Building $BASE with Ren'Py $VERSION_RENPY"

"$SDK/renpy.sh" "$ROOT" lint --error-code

rm -rf "$DEST"
mkdir -p "$DEST"

distribute() {  # package [format]
  local args=("$SDK/launcher" distribute "$ROOT" --destination "$DEST" --package "$1")
  [[ -n "${2:-}" ]] && args+=(--format "$2")
  "$SDK/renpy.sh" "${args[@]}"
}

distribute win
distribute linux
distribute mac app-zip      # .dmg needs macOS tools; the zip works everywhere

# HTML5 build for itch.io: same as the Pages build but without the Dev flag.
rm -rf "$ROOT/web-build"
"$SDK/renpy.sh" "$SDK/launcher" web_build "$ROOT" --destination "$ROOT/web-build"
test -f "$ROOT/web-build/index.html"
(cd "$ROOT/web-build" && zip -qr "$DEST/$BASE-web.zip" .)

# Ren'Py writes an update/ directory and .sums files we don't ship.
rm -rf "$DEST/update"
find "$DEST" -maxdepth 1 -type f ! -name "$BASE-*" -delete

(cd "$DEST" && { command -v sha256sum >/dev/null && sha256sum "$BASE"-* || shasum -a 256 "$BASE"-*; } > SHA256SUMS.txt)

echo
echo "Release packages in $DEST:"
ls -lh "$DEST"
