#!/usr/bin/env bash
set -euo pipefail

# Config
WORK_DIR="./work"
CORE="TOMP-API-1-CORE.yaml"
OFFERS="TOMP-API-2-OFFERS.yaml"
PURCHASE="TOMP-API-4-PURCHASE.yaml"
BOM_OUT="./TOMP-API-BOM.yaml"
FINAL_OUT="./TOMP-API.yaml"
DRAFT_DIR="./draft modules"

# Functions
ask() {
  # ask "Prompt [Y/n]" default(Y/N)
  local prompt="$1"
  local default="${2:-}"
  local reply
  read -r -p "$prompt " reply || true
  if [[ -z "${reply// }" ]]; then
    reply="$default"
  fi
  [[ "$reply" == "y" || "$reply" == "Y" ]]
}

# Ensure work dir exists
mkdir -p "$WORK_DIR"

# Determine files and drafts
ASK="y"
FILES=()
DRAFTS=()

if (( $# > 0 )); then
  if [[ "$1" == "all" ]]; then
    echo "fetch files"
    # shellcheck disable=SC2207
    FILES=($(ls -1 TOMP-API-*.yaml 2>/dev/null || true))
    # shellcheck disable=SC2207
    DRAFTS=($(ls -1 "$DRAFT_DIR"/TOMP-API-*.yaml 2>/dev/null || true))
    ASK="n"
  else
    # Treat args as explicit file list
    FILES=("$@")
    DRAFTS=()
    ASK="n"
  fi
else
    echo "fetch files"
    # shellcheck disable=SC2207
    FILES=($(ls -1 TOMP-API-*.yaml 2>/dev/null || true))
    # shellcheck disable=SC2207
    DRAFTS=($(ls -1 "$DRAFT_DIR"/TOMP-API-*.yaml 2>/dev/null || true))
fi

# Debug print
printf "%s\n" "${FILES[@]:-}"

# Build selection and replacement
JOIN_ARGS=()

for arg in "${FILES[@]:-}"; do
  # Skip CORE itself from prompting/processing like in PS (it never gets added here)
  if [[ "$arg" == "$CORE" ]]; then
    continue
  fi

  # Determine default based on OFFERS / PURCHASE names
  DEFAULT="N"
  DISPLAY="Add $arg [y/N]"
  if [[ "$arg" == "$OFFERS" || "$arg" == "$PURCHASE" ]]; then
    DEFAULT="Y"
    DISPLAY="Add $arg [Y/n]"
  fi

  CONFIRM="n"
  if [[ "$ASK" == "y" ]]; then
    if ask "$DISPLAY" "$DEFAULT"; then
      CONFIRM="y"
    else
      CONFIRM="n"
    fi
  else
    CONFIRM="y"
  fi

  if [[ "$CONFIRM" == "y" || "$CONFIRM" == "Y" ]]; then
    # Destination mirrors PS behavior; also remove "draft modules/" in path if present
    dest="$WORK_DIR/$arg"
    dest="${dest//draft modules\//}"

    echo "$dest"
    mkdir -p "$(dirname "$dest")"

    # Emuleer drievoudige vervanging zoals in PS:
    # 1) replace 'TOMP-API-1-CORE.yaml' -> '' and write to dest
    # 2) then replace 'TOMP-API-2-OFFERS.yaml' -> '' in the just-written dest
    # 3) then replace 'TOMP-API-4-PURCHASE.yaml' -> '' in the just-written dest
    # Gebruik sed (GNU). -e voor meerdere passes. Schrijf in drie stappen om PS-gedrag te spiegelen.
    # Stap 1: from source file
    sed "s|$CORE||g" "./$arg" > "$dest"
    # Stap 2: in-place op dest
    sed -i "s|$OFFERS||g" "$dest"
    # Stap 3: in-place op dest
    sed -i "s|$PURCHASE||g" "$dest"

    JOIN_ARGS+=("$dest")
  fi
done

# Process drafts: interactive always [y/N], and replace ../TOMP-API-1-CORE.yaml with ''
for d in "${drafts[@]:-}"; do :; done # prevent unused var in case directory missing
for draft in "${DRAFTS[@]:-}"; do
  name_only="$(basename "$draft")"
  if ask "Add $draft [y/N]" "N"; then
    mkdir -p "$WORK_DIR"
    sed "s|\.\./$CORE||g" "$draft" > "$WORK_DIR/$name_only"
    JOIN_ARGS+=("$WORK_DIR/$name_only")
  fi
done

# Compose yaml-merge command
# PowerShell built: yaml