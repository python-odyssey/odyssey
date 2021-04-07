Push-Location $PSScriptRoot
try {
    .\activate_env.ps1
}
finally {
    Pop-Location
}
poetry run python -m pip install --upgrade pip
poetry install
