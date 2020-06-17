#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Tests for odyssey.__main__.
"""

import sys
import pytest
from click.exceptions import Exit
from click.testing import CliRunner
from odyssey.__main__ import main
from unittest.mock import patch


@pytest.fixture
def runner():
    cli_runner = CliRunner()
    with cli_runner.isolated_filesystem():
        yield cli_runner


def raise_exit(exit_code):
    raise


def test_bare(runner):
    argv = []
    with patch.object(sys, 'argv', argv), patch.object(sys, 'exit', raise_exit), pytest.raises(Exit) as exception_info:
        main()

    assert exception_info.value.exit_code == 0


def test_help(runner):
    argv = ['--help']
    with patch.object(sys, 'argv', argv), patch.object(sys, 'exit', raise_exit), pytest.raises(Exit) as exception_info:
        main()

    assert exception_info.value.exit_code == 0


def test_version(runner):
    argv = ['--version']
    with patch.object(sys, 'argv', argv), patch.object(sys, 'exit', raise_exit), pytest.raises(Exit) as exception_info:
        main()

    assert exception_info.value.exit_code == 0
