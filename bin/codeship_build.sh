#!/usr/bin/env bash

set -e

if [[ "$OSTYPE" == "linux-gnu"* ]] || [[ "$OSTYPE" == "linux-musl"* ]]; then
    BIN_DIRECTORY=$(dirname "$(readlink -f "$0")")
elif [[ "$OSTYPE" == "darwin"* ]]; then
    BIN_DIRECTORY=$(dirname "$(greadlink -f "$0")")
fi
echo BIN_DIRECTORY: $BIN_DIRECTORY

$BIN_DIRECTORY/install_poetry.sh
$BIN_DIRECTORY/install_dependencies.sh
$BIN_DIRECTORY/run_pytest.sh
$BIN_DIRECTORY/build.sh
$BIN_DIRECTORY/build_executable.sh
