#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""The main odyssey application.
"""

__version__ = "1.0.2"

# Setup which must run before child modules are imported
import logging
import click_log

logger = logging.getLogger("odyssey")
click_log.basic_config(logger)
