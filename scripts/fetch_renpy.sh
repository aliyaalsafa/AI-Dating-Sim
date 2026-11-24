#!/usr/bin/env bash
# Download and verify the Ren'Py SDK pinned in RENPY_VERSION.
#
# Usage: scripts/fetch_renpy.sh [--web] [DEST_DIR]
#   --web     also install RenPyWeb (needed for web builds)
#   DEST_DIR  where to unpack (default: ~/renpy-sdk)
#
# Prints the SDK directory path on the last line of output.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
VERSION="$(tr -d '[:space:]' < "$ROOT/RENPY_VERSION")"

WEB=0
if [[ "${1:-}" == "--web" ]]; then WEB=1; shift; fi
DEST="${1:-$HOME/renpy-sdk}"
SDK_DIR="$DEST/renpy-$VERSION-sdk"
BASE="https://www.renpy.org/dl/$VERSION"

case "$(uname -s)" in
  Linux) SDK_FILE="renpy-$VERSION-sdk.tar.bz2" ;;
  *)     SDK_FILE="renpy-$VERSION-sdk.zip" ;;
esac
WEB_FILE="renpy-$VERSION-web.zip"

mkdir -p "$DEST"
cd "$DEST"

if [[ ! -f checksums-$VERSION.txt ]]; then
  curl -fsSL "$BASE/checksums.txt" -o "checksums-$VERSION.txt"
fi

verify() {
  local file="$1" expected actual
  expected="$(grep -E "^[0-9a-f]{64} $file\$" "checksums-$VERSION.txt" | cut -d' ' -f1)"
  if [[ -z "$expected" ]]; then echo "No sha256 listed for $file" >&2; exit 1; fi
  if command -v sha256sum >/dev/null; then
    actual="$(sha256sum "$file" | cut -d' ' -f1)"
  else
    actual="$(shasum -a 256 "$file" | cut -d' ' -f1)"
  fi
  if [[ "$expected" != "$actual" ]]; then echo "Checksum mismatch for $file" >&2; exit 1; fi
}

fetch() {
  local file="$1"
  [[ -f "$file" ]] || curl -fsSL "$BASE/$file" -o "$file"
  verify "$file"
}

if [[ ! -x "$SDK_DIR/renpy.sh" ]]; then
  fetch "$SDK_FILE"
  case "$SDK_FILE" in
    *.tar.bz2) tar -xjf "$SDK_FILE" ;;
    *.zip)     unzip -q "$SDK_FILE" ;;
  esac
fi

if [[ "$WEB" == 1 && ! -f "$SDK_DIR/web/renpy.wasm" ]]; then
  fetch "$WEB_FILE"
  (cd "$SDK_DIR" && unzip -qo "../$WEB_FILE")
fi

echo "$SDK_DIR"
