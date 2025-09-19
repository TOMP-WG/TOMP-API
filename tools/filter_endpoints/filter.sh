#!/usr/bin/env bash
set -euo pipefail
# Usage: ./filter.sh filter_file.txt [input.yaml] [output.yaml]

if [[ $# -lt 1 ]]; then
  echo "Usage: $0 <filters-file> [input.yaml] [output.yaml]"
  exit 1
fi

FILTERFILE="$1"
INPUT="${2:-.\..\..\TOMP-API.yaml.yaml}"
OUTPUT="${3:-TOMP-API-filtered.yaml}"

PY="${PYTHON:-python3}"
SCRIPT="filter_openapi.py"

if [[ ! -f "$FILTERFILE" ]]; then
  echo "Filters file not found: $FILTERFILE"
  exit 1
fi

# Read non-empty, non-comment lines into an array
mapfile -t RAW_LINES < "$FILTERFILE"
FILTERS=()
for line in "${RAW_LINES[@]}"; do
  # trim leading/trailing whitespace
  line="${line#"${line%%[![:space:]]*}"}"
  line="${line%"${line##*[![:space:]]}"}"
  [[ -z "$line" ]] && continue
  [[ "${line:0:1}" == "#" ]] && continue
  FILTERS+=("$line")
done

echo "Running: $PY $SCRIPT -i $INPUT -o $OUTPUT --preselect ${FILTERS[*]}"
"$PY" "$SCRIPT" -i "$INPUT" -o "$OUTPUT" --preselect "${FILTERS[@]}"

echo "Done. Output: $OUTPUT"