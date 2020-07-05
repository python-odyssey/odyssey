#!/usr/bin/env bash

set -e

if [[ -z "${PYTHON_EXECUTABLE}" ]]; then
  PYTHON_EXECUTABLE="python3"
else
  PYTHON_EXECUTABLE="${PYTHON_EXECUTABLE}"
fi

source $HOME/.poetry/env

if [[ -z "${VIRTUAL_ENVIRONMENT}" ]]; then
  poetry env use $PYTHON_EXECUTABLE
fi

poetry run pip --disable-pip-version-check install poetry
poetry run tox
