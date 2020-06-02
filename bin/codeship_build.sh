#!/usr/bin/env bash

BIN_DIRECTORY=$(dirname "$(readlink -f "$0")")
echo BIN_DIRECTORY: $BIN_DIRECTORY

$BIN_DIRECTORY/install_poetry.sh
$BIN_DIRECTORY/install_dependencies.sh
$BIN_DIRECTORY/run_tox.sh
$BIN_DIRECTORY/build.sh