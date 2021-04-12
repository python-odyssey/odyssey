#!/usr/bin/env bash

set -e

curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -o get-poetry.py && chmod u+x ./get-poetry.py && python ./get-poetry.py --yes --version 1.0.9 && rm -f ./get-poetry.py

echo "" >> ~/.bashrc
echo "# Automatically setup poetry" >> ~/.bashrc
echo ". ~/.poetry/env" >> ~/.bashrc

. ~/.poetry/env
