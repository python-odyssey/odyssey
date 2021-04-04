Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing -OutFile get-poetry.py;
& python get-poetry.py --yes --version 1.0.9;
Remove-Item get-poetry.py;
