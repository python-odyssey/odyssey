Push-Location (Resolve-Path ($PSScriptRoot))
try {
    Get-ChildItem -Recurse -File -Path *.sh | ForEach-Object { git update-index --chmod=+x "$_"; Write-Output "$_"; }
} finally {
    Pop-Location
}

Push-Location (Resolve-Path (Join-Path $PSScriptRoot '..' 'src'))
try {
    Get-ChildItem -Recurse -File -Path *.py | ForEach-Object { git update-index --chmod=+x "$_"; Write-Output "$_"; }
} finally {
    Pop-Location
}
