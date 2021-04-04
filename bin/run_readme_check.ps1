Set-Location $PSScriptRoot
try {
    .\activate_env.ps1
}
finally {
    Pop-Location
}

Get-ChildItem dist/*.whl | ForEach-Object { poetry run twine check "$_" }
