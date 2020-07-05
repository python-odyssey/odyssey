#!/usr/bin/env bash

set -e

if [[ -z "${PYTHON_EXECUTABLE}" ]]; then
  PYTHON_EXECUTABLE="python3"
else
  PYTHON_EXECUTABLE="${PYTHON_EXECUTABLE}"
fi

if [[ "$OSTYPE" == "linux-gnu"* ]] || [[ "$OSTYPE" == "linux-musl"* ]]; then
    BIN_DIRECTORY=$(dirname "$(readlink -f "$0")")
elif [[ "$OSTYPE" == "darwin"* ]]; then
    BIN_DIRECTORY=$(dirname "$(greadlink -f "$0")")
fi

source $HOME/.poetry/env

if [[ -z "${VIRTUAL_ENVIRONMENT}" ]]; then
  poetry env use $PYTHON_EXECUTABLE
fi

poetry run python $BIN_DIRECTORY/create_release.py
