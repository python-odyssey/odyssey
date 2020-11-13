if (!(Test-Path Env:PYTHON_EXECUTABLE)) {
    throw "Env:PYTHON_EXECUTABLE is missing!"
}

poetry env use $Env:PYTHON_EXECUTABLE;
$paths = poetry run python -c 'import site; print(\"--paths=\" + \" --paths=\".join(site.getsitepackages()));'
Invoke-Expression "poetry run pyinstaller $PSScriptRoot\..\src\odyssey\__main__.py --noconfirm --clean --onefile --console $paths --name odyssey"
