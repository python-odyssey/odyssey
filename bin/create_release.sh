#!/usr/bin/env bash

set -e

if [[ -z "${PYTHON_EXECUTABLE}" ]]; then
  PYTHON="python3"
else
  PYTHON="${PYTHON_EXECUTABLE}"
fi

if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    BIN_DIRECTORY=$(dirname "$(readlink -f "$0")")
elif [[ "$OSTYPE" == "darwin"* ]]; then
    BIN_DIRECTORY=$(dirname "$(greadlink -f "$0")")

source $HOME/.poetry/env
poetry env use $PYTHON
poetry run python $BIN_DIRECTORY/create_release.py
