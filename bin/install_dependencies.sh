#!/usr/bin/env bash

set -e

if [[ -z "${PYTHON_EXECUTABLE}" ]]; then
  PYTHON="python3"
else
  PYTHON="${PYTHON_EXECUTABLE}"
fi

source $HOME/.poetry/env

if [[ -z "${VIRTUAL_ENVIRONMENT}" ]]; then
  poetry env use $PYTHON
fi

poetry install
