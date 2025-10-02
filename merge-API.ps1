$path = ".\work\"
If(!(test-path -PathType container $path))
{
      New-Item -ItemType Directory -Path $path
}

$ask = 'y'
$join = "";

If ($args.count -ne 0) {
    $files = $args
    $drafts = @()
    $ask = 'n'
}
Else {
    Write-Host "fetch files"
    $files = Get-ChildItem -Path . -Filter "TOMP-API-*.yaml"
    $drafts = Get-ChildItem -Path "./draft modules/" -Filter "TOMP-API-*.yaml"
}

If ($args[0] -eq 'all') {
    Write-Host "fetch files"
    $files = Get-ChildItem -Path . -Filter "TOMP-API-*.yaml"
    $drafts = Get-ChildItem -Path "./draft modules/" -Filter "TOMP-API-*.yaml"
    $ask = 'n'
}

If ($args[0] -eq 'mp') {
    Write-Host "merge mp files"
    $files = @()
    $drafts = Get-ChildItem -Path "./MP modules/" -Filter "TOMP-API-*.yaml"
    $ask = 'n'
}

Write-Host $files

ForEach ($arg in $files){
    if ('TOMP-API-1-CORE.yaml' -cne $arg) {
        if (('TOMP-API-2-OFFERS.yaml' -cne $arg) -and ('TOMP-API-4-PURCHASE.yaml' -cne $arg)) {
            $defaultValue = 'N'
            $display = "Add $($arg) [y/N]"
        }
        else {
            $defaultValue = 'Y'
            $display = "Add $($arg) [Y/n]"
        }

        if ('y' -eq $ask) {
            $confirmation = Read-Host $display
        }
        else {
            $confirmation = 'y'
        }

        if ([string]::IsNullOrWhiteSpace($confirmation)) {
            $confirmation = $defaultValue
        }

        if ($confirmation -eq 'y' -or $confirmation -eq 'Y') {
            $dest = ".\work\$($arg)"
            $dest = $dest -replace "\\draft modules\\", "\\"
            $dest = $dest -replace "\\MP modules\\", "\\"
            Write-Host $dest
            
            (gc .\$arg) -replace 'TOMP-API-1-CORE.yaml', '' | Out-File -encoding ASCII $dest
            (gc .\work\$arg) -replace 'TOMP-API-2-OFFERS.yaml', '' | Out-File -encoding ASCII $dest
            (gc .\work\$arg) -replace 'TOMP-API-4-PURCHASE.yaml', '' | Out-File -encoding ASCII $dest
            $join = -join($join, " ", $dest);
        }
    }
}

ForEach ($arg in $drafts){
    If ($args[0] -eq 'mp') {
        $confirmation = 'y'
    }
    else {
        $confirmation = Read-Host "Add $($arg) [y/N]"
    }

    if ($confirmation -eq 'y') {
        If ($args[0] -eq 'mp') {
            (gc ".\MP modules\$arg") -replace '../TOMP-API-1-CORE.yaml', '' | Out-File -encoding ASCII .\work\$arg
        }
        else {
            (gc ".\draft modules\$arg") -replace '../TOMP-API-1-CORE.yaml', '' | Out-File -encoding ASCII .\work\$arg
        }
        $join = -join($join, " .\work\", $arg );
    }
}

$join = -join("yaml-merge ", $join, " .\TOMP-API-1-CORE.yaml > .\TOMP-API-BOM.yaml");
Write-Host $join
Invoke-Expression $join

#$content = Get-Content -Path .\TOMP-API-BOM.yaml -Raw
#Set-Content -Path .\TOMP-API.yaml -Value $content -Encoding utf8

$in  = '.\TOMP-API-BOM.yaml'
$out = '.\TOMP-API.yaml'

If ($args[0] -eq 'mp') {
    $out = '.\TOMP-API-MP.yaml'
}

$text = Get-Content $in -Raw
$utf8NoBom = New-Object System.Text.UTF8Encoding($false)
$sw = New-Object System.IO.StreamWriter($out, $false, $utf8NoBom)
$sw.Write($text)
$sw.Close()

Remove-Item .\TOMP-API-BOM.yaml

Remove-Item -LiteralPath $path -Recurse -Force -Confirm:$false