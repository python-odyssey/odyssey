#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""main click group click group and no application logic.
"""

import odyssey
import odyssey.core
import odyssey.perforce_ftp
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


@main.group()
def perforce_ftp():
    """Interacts with perforce installer dist server."""
    pass


@perforce_ftp.command()
def find_version():
    return odyssey.perforce_ftp.find_version()


@perforce_ftp.command()
@click.option("-v", "--version", "version")
def find_platform(version):
    return odyssey.perforce_ftp.find_platform(version)


@perforce_ftp.command()
@click.option("-v", "--version", "version")
@click.option("-p", "--platform", "platform")
def find_file(version, platform):
    return odyssey.perforce_ftp.find_file(version, platform)


@perforce_ftp.command()
@click.option("-v", "--version", "version")
@click.option("-p", "--platform", "platform")
@click.option("-f", "--file", "file_name")
@click.option("-o", "--output", "output_path")
def download_file(version, platform, file_name, output_path):
    return odyssey.perforce_ftp.download_file(version, platform, file_name, output_path)
