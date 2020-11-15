#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import inspect
from enum import Enum, unique

def is_callable(obj) -> bool:
    return callable(obj)

def is_method_with_bound_self(obj) -> bool:
    return callable(obj) and hasattr(obj, "__self__") and obj.__self__ is not None
