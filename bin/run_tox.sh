#!/usr/bin/env bash

source $HOME/.poetry/env
poetry env use python3
poetry run pip --disable-pip-version-check install poetry
poetry run tox
