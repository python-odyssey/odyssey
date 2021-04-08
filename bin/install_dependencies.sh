#!/usr/bin/env bash

set -e

poetry env use python
poetry run python -m pip install --upgrade pip
poetry install
