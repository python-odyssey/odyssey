#!/usr/bin/env bash

set -e

if [[ "$OSTYPE" == "linux-gnu"* ]] || [[ "$OSTYPE" == "linux-musl"* ]]; then
    BIN=$(dirname "$(readlink -f "$0")")
elif [[ "$OSTYPE" == "darwin"* ]]; then
    BIN=$(dirname "$(greadlink -f "$0")")
fi
echo BIN: $BIN

. $BIN/install_poetry.sh
$BIN/install_dependencies.sh
$BIN/run_pytest.sh
$BIN/build.sh
$BIN/build_executable.sh
