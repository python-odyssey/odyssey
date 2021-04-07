Push-Location $PSScriptRoot
try {
    .\activate_env.ps1
}
finally {
    Pop-Location
}

$paths = poetry run python -c 'import site; print(\"--paths=\" + \" --paths=\".join(site.getsitepackages()));'
Invoke-Expression "poetry run pyinstaller $PSScriptRoot\..\src\odyssey\__main__.py --noconfirm --clean --onefile --console $paths --name odyssey"
