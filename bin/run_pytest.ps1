Push-Location $PSScriptRoot
try {
    .\activate_env.ps1
}
finally {
    Pop-Location
}

poetry run pytest
