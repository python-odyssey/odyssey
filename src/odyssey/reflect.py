#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from inspect import ismodule, isclass
from enum import Enum, unique
from os import scandir
from os.path import isdir, isfile, join, splitext, basename, split

def is_callable(obj) -> bool:
    return callable(obj)

def is_method_with_bound_self(obj) -> bool:
    return callable(obj) and hasattr(obj, "__self__") and obj.__self__ is not None

def has_init_py(path) -> bool:
    return isfile(join(path, "__init__.py"))

def is_directory(path) -> bool:
    return isdir(path) and not has_init_py(path)

def is_package(path) -> bool:
    return isdir(path) and has_init_py(path)

def list_directories(path) -> list:
    result = []
    for entry in scandir(path):
        if(is_directory(entry)):
            result.append(entry.path)
    return result

def list_packages(path) -> list:
    result = []
    for entry in scandir(path):
        if(is_package(entry)):
            result.append(entry.path)
    return result

def has_py_extension(path) -> bool:
    return splitext(path)[1] == ".py"

def has_private_name(path) -> bool:
    return basename(path).startswith("__")

def is_module_file(path) -> bool:
    return isfile(path) and has_py_extension(path) and not has_private_name(path)

def list_module_files(path) -> list:
    result = []
    for entry in scandir(path):
        if(is_module_file(entry)):
            result.append(entry.path)
    return result

def is_module(obj) -> bool:
    return ismodule(obj)

def is_class(obj) -> bool:
    return isclass(obj)

def import_path_from_module_path(path) -> str:
    path, ext = splitext(path)
    result = []
    path, module = split(path)
    result.append(module)
    while is_package(path):
        path, package = split(path)
        result.append(package)
    return ".".join(reversed(result))
