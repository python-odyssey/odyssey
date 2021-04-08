#!/usr/bin/env bash

set -e

poetry env use python
poetry run pytest
