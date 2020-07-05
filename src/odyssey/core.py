#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""All application logic.
"""

import sys
import json
import pkgutil


def convert_to_cli_string(obj) -> list:
    if isinstance(obj, (list, tuple, set)):
        return '\n'.join([convert_to_cli_string(item) for item in obj])
    if isinstance(obj, (dict)):
        return json.dumps(obj, sort_key=True, indent=4)
    return str(obj)


def importable_modules() -> list:
    result = []
    for module in pkgutil.iter_modules():
        result.append(module.name)
    return result


def imported_modules():
    result = []
    for module_name in sys.modules.keys():
        result.append(module_name)
    return result
