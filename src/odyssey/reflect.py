#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import inspect
from enum import Enum, unique

def is_callable(obj) -> bool:
    return callable(obj)

class CallableType(Enum):
    Unknown = 0
    FreeFunction = 1

def callable_type():
    pass
