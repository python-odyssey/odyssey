Set-Location $PSScriptRoot
try {
    .\activate_env.ps1
}
finally {
    Pop-Location
}
poetry run python $PSScriptRoot\create_release.py
