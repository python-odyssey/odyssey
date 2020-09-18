#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import git


def create(path, **kwargs):
    return git.Repo.init(path, mkdir=True, **kwargs)
