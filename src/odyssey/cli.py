#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""main click group click group and no application logic.
"""

import odyssey
import logging
import click
import click_log


@click.group()
@click.version_option(odyssey.__version__, message="%(version)s")
@click_log.simple_verbosity_option(odyssey.logger)
def main():
    pass
