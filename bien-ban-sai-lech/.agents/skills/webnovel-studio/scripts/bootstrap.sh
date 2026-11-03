#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(CDPATH= cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)"
SKILL_DIR="$(CDPATH= cd -- "$SCRIPT_DIR/.." && pwd -P)"
TEMPLATE_DIR="$SKILL_DIR/assets/project_template"
DEST="${1:-$(pwd)/bien-ban-sai-lech}"

usage() {
  echo "Usage: bash webnovel-studio/scripts/bootstrap.sh [NEW_project_directory]"
  echo "Creates an ORIGINAL local novel repository, vendors the skill and makes an initial local Git commit."
}

if [[ "${1:-}" == "--help" || "${1:-}" == "-h" ]]; then
  usage
  exit 0
fi
if [[ ! -d "$TEMPLATE_DIR" ]]; then
  echo "ERROR: project template missing: $TEMPLATE_DIR" >&2
  exit 2
fi
if ! command -v git >/dev/null 2>&1; then
  echo "ERROR: Git is required but not found." >&2
  exit 2
fi
if ! command -v python3 >/dev/null 2>&1; then
  echo "ERROR: Python 3 is required for local QA (no pip dependencies)." >&2
  exit 2
fi
if [[ -e "$DEST" || -L "$DEST" ]]; then
  echo "ERROR: refusing to overwrite existing destination: $DEST" >&2
  exit 3
fi

# Create only a NEW folder. Never reset, clean, or modify any existing Git repository.
mkdir -p "$DEST"
cp -R "$TEMPLATE_DIR/." "$DEST/"
mkdir -p "$DEST/.agents/skills"
cp -R "$SKILL_DIR" "$DEST/.agents/skills/webnovel-studio"

# Sanity-check before creating a Git commit.
python3 "$SKILL_DIR/scripts/check_project.py" "$DEST"

if git -C "$DEST" init -q -b main 2>/dev/null; then
  :
else
  git -C "$DEST" init -q
  git -C "$DEST" branch -m main
fi
if ! git -C "$DEST" config user.name >/dev/null; then
  git -C "$DEST" config --local user.name "Novel Studio Agent"
fi
if ! git -C "$DEST" config user.email >/dev/null; then
  git -C "$DEST" config --local user.email "novel-studio@localhost"
fi
git -C "$DEST" add .
git -C "$DEST" commit -q -m "chore: initialize original webnovel, local skill, first chapter and arc bible"

printf '\nCreated original novel project: %s\n' "$DEST"
printf 'Local Git HEAD: %s\n' "$(git -C "$DEST" rev-parse --short HEAD)"
echo "Read $DEST/AGENTS.md and $DEST/chapters/001.md"
echo "Gate: chapter 001 REVIEW ONLY. Do not write chapter 002 until human approval."
