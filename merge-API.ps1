$path = ".\work\"
If(!(test-path -PathType container $path))
{
      New-Item -ItemType Directory -Path $path
}

$join = "yaml-merge";
If ($args.count -ne 0) {
    Write-Host $args
    $files = $args
}
Else {
    Write-Host "fetch files"
    $files = Get-ChildItem -Path . -Filter "TOMP-API-*.yaml"
}

Write-Host $files

ForEach ($arg in $files){
    $confirmation = Read-Host "Add $($arg) [y/N]"

    if ($confirmation -eq 'y') {
        (gc .\$arg) -replace 'TOMP-API.yaml', '' | Out-File -encoding ASCII .\work\$arg
        $join = -join($join, " .\work\", $arg );
    }
}

$join = -join($join, " ", ".\TOMP-API.yaml > .\TOMP-Merged.yaml" );
Write-Host $join
Invoke-Expression $join

Remove-Item -LiteralPath $path