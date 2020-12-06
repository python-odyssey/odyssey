#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import click

import odyssey.git.repository.core as repository


@click.group(name="repository")
def _repository():
    pass


@_repository.command()
@click.option("-p", "--path", type=click.Path(exists=False, resolve_path=True))
def create(path):
    return repository.create(path)
