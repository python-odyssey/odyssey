Set-Location $PSScriptRoot
try {
    .\activate_env.ps1
}
finally {
    Pop-Location
}

poetry run black --line-length 88 .
