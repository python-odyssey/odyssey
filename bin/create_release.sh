#!/usr/bin/env bash

if [[ -z "${PYTHON_EXECUTABLE}" ]]; then
  PYTHON="python3"
else
  PYTHON="${PYTHON_EXECUTABLE}"
fi

BIN_DIRECTORY=$(dirname "$(readlink -f "$0")")

source $HOME/.poetry/env
poetry env use $PYTHON
poetry run python $BIN_DIRECTORY/create_release.py
