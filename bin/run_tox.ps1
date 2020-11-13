if (!(Test-Path Env:PYTHON_EXECUTABLE)) {
    throw "Env:PYTHON_EXECUTABLE is missing!"
}

poetry env use $Env:PYTHON_EXECUTABLE;
poetry run pip --disable-pip-version-check install poetry
poetry run tox
