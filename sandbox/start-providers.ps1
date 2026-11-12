<#
.SYNOPSIS
  Starts several sandbox instances at once, each simulating a different shared-mobility operator.

.DESCRIPTION
  Each instance gets its own port, SANDBOX_PROVIDER and SANDBOX_DATA_FILE (so they don't overwrite
  each other's persisted state), and opens in its own PowerShell window so you can watch its
  request log. Close a window (or Ctrl+C inside it) to stop that one instance - the window itself
  closes too, it's not left behind as an empty shell.
  If something is already listening on an instance's port (e.g. left over from a previous run of
  this script), it's stopped first (window and all) so the replacement instance can bind that port.
  See src/data/providers.js and "Simulating different providers" in README.md for the full list
  of providers, modes and cities.

.PARAMETER Providers
  Which provider keys to start, one instance each, or a single number N to start the first N
  providers from the default list below. Defaults to just 'gosharing'.

.EXAMPLE
  .\start-providers.ps1
.EXAMPLE
  .\start-providers.ps1 4
.EXAMPLE
  .\start-providers.ps1 gosharing uber
#>
param(
    [string[]]$Providers = @('gosharing')
)

# The pool a bare count (e.g. "4") picks from: a mix of bike-share and taxi, multi-city and
# single-city, so the different coverage areas are easy to compare.
$defaultProviderPool = @('gosharing', 'uber', 'check', 'viavan')

if ($Providers.Count -eq 1 -and $Providers[0] -match '^\d+$') {
    $count = [int]$Providers[0]
    if ($count -lt 1 -or $count -gt $defaultProviderPool.Count) {
        Write-Error "Count must be between 1 and $($defaultProviderPool.Count) (got $count)."
        exit 1
    }
    $Providers = $defaultProviderPool[0..($count - 1)]
}

$basePort = 4010
$sandboxRoot = $PSScriptRoot

# node.exe is the one actually bound to the port, but it's a grandchild of the PowerShell window
# this script started (powershell -> npm -> node). Walks up to that window's own PID, if found, so
# killing "the instance on this port" closes the window too, instead of leaving it behind as an
# empty, process-less shell.
function Get-SandboxWindowProcessId {
    param([int]$LeafProcessId)

    $current = $LeafProcessId
    for ($hop = 0; $hop -lt 6; $hop++) {
        $info = Get-CimInstance Win32_Process -Filter "ProcessId = $current" -ErrorAction SilentlyContinue
        if (-not $info -or -not $info.ParentProcessId) {
            return $LeafProcessId
        }
        $parent = Get-Process -Id $info.ParentProcessId -ErrorAction SilentlyContinue
        if (-not $parent) {
            return $LeafProcessId
        }
        if ($parent.ProcessName -eq 'powershell') {
            return $info.ParentProcessId
        }
        $current = $info.ParentProcessId
    }
    return $LeafProcessId
}

# Stops whatever is currently listening on $Port (e.g. a sandbox instance left running from a
# previous invocation of this script), so the replacement instance can bind that same port.
function Stop-SandboxOnPort {
    param([int]$Port)

    $conns = Get-NetTCPConnection -LocalPort $Port -State Listen -ErrorAction SilentlyContinue
    if (-not $conns) {
        return
    }

    foreach ($procId in ($conns.OwningProcess | Sort-Object -Unique)) {
        $targetId = Get-SandboxWindowProcessId -LeafProcessId $procId
        $proc = Get-Process -Id $targetId -ErrorAction SilentlyContinue
        $name = if ($proc) { $proc.ProcessName } else { 'unknown' }
        Write-Host "  Port $Port already in use (PID $targetId, $name) - stopping it first"
        # /T kills the whole process tree (window, npm, node), not just the single PID
        & taskkill /PID $targetId /T /F 2>$null | Out-Null
    }

    # give the OS a moment to release the socket before the replacement instance binds it
    for ($i = 0; $i -lt 10; $i++) {
        if (-not (Get-NetTCPConnection -LocalPort $Port -State Listen -ErrorAction SilentlyContinue)) {
            break
        }
        Start-Sleep -Milliseconds 300
    }
}

for ($i = 0; $i -lt $Providers.Count; $i++) {
    $provider = $Providers[$i]
    $port = $basePort + $i
    $dataFile = ".data/$provider.json"

    Stop-SandboxOnPort -Port $port

    Write-Host "Starting $provider on port $port (data: $dataFile)"

    # No -NoExit: the window should close as soon as npm start does (Ctrl+C, a crash, or being
    # stopped by Stop-SandboxOnPort above), not linger as an empty prompt.
    $command = "`$env:PORT='$port'; `$env:SANDBOX_PROVIDER='$provider'; `$env:SANDBOX_DATA_FILE='$dataFile'; " +
        "`$host.UI.RawUI.WindowTitle='sandbox: $provider (:$port)'; npm start"
    Start-Process powershell -ArgumentList '-Command', $command -WorkingDirectory $sandboxRoot | Out-Null
}

Write-Host ""
Write-Host "Started $($Providers.Count) sandbox instance(s):"
for ($i = 0; $i -lt $Providers.Count; $i++) {
    Write-Host ("  {0,-10} http://localhost:{1}  (GET /health to confirm)" -f $Providers[$i], ($basePort + $i))
}
