#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import click
from odyssey.git.repository.cli import _repository

@click.group()
def git():
    pass

git.add_command(_repository)