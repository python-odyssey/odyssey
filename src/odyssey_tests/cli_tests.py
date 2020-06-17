#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Tests for odyssey.cli.
"""

import pytest
from click.testing import CliRunner
from odyssey.cli import main


@pytest.fixture
def runner():
    cli_runner = CliRunner()
    with cli_runner.isolated_filesystem():
        yield cli_runner


def test_bare(runner):
    result = runner.invoke(main, [])

    assert result.exit_code == 0


def test_help(runner):
    result = runner.invoke(main, ['--help'])
    
    assert result.exit_code == 0


def test_version(runner):
    result = runner.invoke(main, ['--version'])

    assert result.exit_code == 0
