#!/usr/bin/env bash

if [[ -z "${PYTHON_EXECUTABLE}" ]]; then
  PYTHON="python3"
else
  PYTHON="${PYTHON_EXECUTABLE}"
fi

source $HOME/.poetry/env
poetry env use $PYTHON
poetry run pip --disable-pip-version-check install poetry
poetry run tox
