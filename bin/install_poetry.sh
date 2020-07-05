#!/usr/bin/env bash

set -e

if [[ -z "${PYTHON_EXECUTABLE}" ]]; then
  PYTHON="python3"
else
  PYTHON="${PYTHON_EXECUTABLE}"
fi

curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -o get-poetry.py && chmod u+x ./get-poetry.py && $PYTHON_EXECUTABLE ./get-poetry.py --yes && rm -f ./get-poetry.py
