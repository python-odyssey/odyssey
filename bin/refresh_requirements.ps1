Set-Location $PSScriptRoot
try {
    .\activate_env.ps1
}
finally {
    Pop-Location
}

poetry export --dev --without-hashes --format requirements.txt --output requirements.txt
