Set-Location $PSScriptRoot
try {
    .\activate_env.ps1
}
finally {
    Pop-Location
}
poetry build
