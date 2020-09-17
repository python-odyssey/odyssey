if (!(Test-Path $Env:PYTHON_EXECUTABLE)) {
    throw "Env:PYTHON_EXECUTABLE is missing!"
}

Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing -OutFile get-poetry.py; & $Env:PYTHON_EXECUTABLE get-poetry.py --yes --version 1.0.10; Remove-Item get-poetry.py;
