#!/usr/bin/env bash
# Starts several sandbox instances at once, each simulating a different shared-mobility operator.
#
# Each instance gets its own port, SANDBOX_PROVIDER and SANDBOX_DATA_FILE (so they don't overwrite
# each other's persisted state), and logs to logs/<provider>.log. Press Ctrl+C to stop all of them.
# If something is already listening on an instance's port (e.g. left over from a previous run of
# this script), it's stopped first so the replacement instance can bind that port.
# See src/data/providers.js and "Simulating different providers" in README.md for the full list
# of providers, modes and cities.
#
# Usage:
#   ./start-providers.sh                 # just gosharing
#   ./start-providers.sh 4               # first 4 providers from the default pool below
#   ./start-providers.sh gosharing uber  # only these providers (port/data file still assigned)

set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")"

# The pool a bare count (e.g. "4") picks from: a mix of bike-share and taxi, multi-city and
# single-city, so the different coverage areas are easy to compare.
default_provider_pool=(gosharing uber check viavan)

providers=("$@")
if [ ${#providers[@]} -eq 0 ]; then
  providers=(gosharing)
elif [ ${#providers[@]} -eq 1 ] && [[ "${providers[0]}" =~ ^[0-9]+$ ]]; then
  count="${providers[0]}"
  if [ "$count" -lt 1 ] || [ "$count" -gt "${#default_provider_pool[@]}" ]; then
    echo "Count must be between 1 and ${#default_provider_pool[@]} (got $count)." >&2
    exit 1
  fi
  providers=("${default_provider_pool[@]:0:$count}")
fi

base_port=4010
mkdir -p logs .data
pids=()

# Whether something is currently listening on TCP $1, using whatever tool this platform has.
port_is_listening() {
  local port="$1"
  if command -v lsof >/dev/null 2>&1; then
    lsof -ti "tcp:${port}" >/dev/null 2>&1
  elif command -v netstat >/dev/null 2>&1; then
    netstat -ano 2>/dev/null | grep -qE "[.:]${port}[[:space:]].*LISTEN"
  else
    return 1
  fi
}

# Stops whatever is currently listening on TCP $1 (e.g. a sandbox instance left running from a
# previous invocation of this script). A backgrounded `npm start`'s own $! isn't a reliable handle
# for this: on Git Bash/Windows in particular, it's often an intermediate launcher that exits on
# its own well before the node.exe it spawned does, so bookkeeping our own pid wouldn't actually
# tell us whether the port is still held. Asking the OS who owns the port does.
stop_port() {
  local port="$1"

  if command -v lsof >/dev/null 2>&1; then
    local owner_pids
    owner_pids=$(lsof -ti "tcp:${port}" 2>/dev/null || true)
    [ -n "$owner_pids" ] || return 0
    echo "  Port $port already in use (PID(s) ${owner_pids//$'\n'/, }) - stopping it first"
    # shellcheck disable=SC2086
    kill $owner_pids 2>/dev/null || true
  elif command -v netstat >/dev/null 2>&1 && command -v taskkill >/dev/null 2>&1; then
    local win_pid
    for win_pid in $(netstat -ano 2>/dev/null | grep -E "[.:]${port}[[:space:]].*LISTEN" | awk '{print $NF}' | sort -u); do
      echo "  Port $port already in use (PID $win_pid) - stopping it first"
      taskkill //F //PID "$win_pid" >/dev/null 2>&1 || true
    done
  else
    return 0
  fi

  for _ in 1 2 3 4 5 6 7 8 9 10; do
    port_is_listening "$port" || break
    sleep 0.3
  done
}

cleanup() {
  echo
  echo "Stopping sandbox instances..."
  kill "${pids[@]}" 2>/dev/null || true
}
trap cleanup EXIT INT TERM

for i in "${!providers[@]}"; do
  provider="${providers[$i]}"
  port=$((base_port + i))
  data_file=".data/${provider}.json"
  log_file="logs/${provider}.log"

  stop_port "$port"

  echo "Starting $provider on port $port (data: $data_file, log: $log_file)"
  PORT=$port SANDBOX_PROVIDER=$provider SANDBOX_DATA_FILE=$data_file npm start > "$log_file" 2>&1 &
  pids+=($!)
done

echo
echo "Started ${#providers[@]} sandbox instance(s):"
for i in "${!providers[@]}"; do
  printf "  %-10s http://localhost:%s  (GET /health to confirm, tail -f logs/%s.log)\n" \
    "${providers[$i]}" "$((base_port + i))" "${providers[$i]}"
done

wait
