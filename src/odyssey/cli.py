#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""main click group click group and no application logic.
"""

import odyssey
import odyssey.core
import logging
import click
import click_log
import platform


@click.group()
@click.version_option(odyssey.__version__, message="%(version)s")
@click_log.simple_verbosity_option(odyssey.logger)
def main():
    pass


@main.resultcallback()
def main_result_callback(result):
    if result is None:
        return

    string = odyssey.core.convert_to_cli_string(result)
    
    if string:
        click.echo(string)

    return result


@main.group()
@click.version_option(platform.python_version(), message="%(version)s")
def python():
    pass


@python.command()
def importable_modules():
    return odyssey.core.importable_modules()


@python.command()
def imported_modules():
    return odyssey.core.imported_modules()
