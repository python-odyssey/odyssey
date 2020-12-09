#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from inspect import ismodule, isclass, getmembers, signature, Signature, Parameter
from enum import Enum, unique
from os import scandir
from os.path import isdir, isfile, join, splitext, basename, split
from importlib.util import spec_from_file_location, module_from_spec


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
        if is_directory(entry):
            result.append(entry.path)
    return result


def list_packages(path) -> list:
    result = []
    for entry in scandir(path):
        if is_package(entry):
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
        if is_module_file(entry):
            result.append(entry.path)
    return result


def is_module(obj) -> bool:
    return ismodule(obj)


def is_class(obj) -> bool:
    return isclass(obj)


def is_function(obj) -> bool:
    return not isclass(obj) and callable(obj)


def is_value(obj) -> bool:
    return not isclass(obj) and not callable(obj)


def import_path_from_module(module) -> str:
    return module.__name__


def import_path_from_module_path(path) -> str:
    path, ext = splitext(path)
    result = []
    path, module = split(path)
    result.append(module)
    while is_package(path):
        path, package = split(path)
        result.append(package)
    return ".".join(reversed(result))


def import_module_file(path):
    import_path = import_path_from_module_path(path)
    spec = spec_from_file_location(import_path, path)
    loaded_module = module_from_spec(spec)
    spec.loader.exec_module(loaded_module)
    return loaded_module


def has_member(module, member) -> bool:
    return hasattr(module, member)


def get_member(module, member) -> bool:
    return getattr(module, member)


def get_classes(module):
    return getmembers(module, is_class)


def get_functions(module):
    return getmembers(module, is_function)


def get_values(module):
    return getmembers(module, is_value)


@unique
class ReflectType(Enum):
    Directory = 1
    Package = 2
    ModuleFile = 3
    Module = 4
    Class = 5
    Function = 6
    Value = 7


class Reflected:
    def __init__(self, reflect_type, name, value):
        self.reflect_type = reflect_type
        self.name = name
        self.value = value


def reflect_directory(path):
    result = []


def is_private_name(name) -> bool:
    return name.startswith("__") and name.endswith("__")


class Directory:
    def __init__(self, path):
        self.path = path
        self.directory_paths = list_directories(path)
        self.package_paths = list_packages(path)
        self.module_file_paths = list_module_files(path)
        names = []
        private_names = []
        for directory in self.directory_paths:
            path, name = split(directory)
            if not is_private_name(name):
                names.append(name)
            else:
                private_names.append(name)
        for package in self.package_paths:
            path, name = split(package)
            if not is_private_name(name):
                names.append(name)
            else:
                private_names.append(name)
        for module_file in self.module_file_paths:
            path, name = split(module_file)
            name, ext = splitext(name)
            if not is_private_name(name):
                names.append(name)
            else:
                private_names.append(name)
        self.names = sorted(names)


def reflect_directory(path):
    return Directory(path)


class Package:
    def __init__(self, path):
        self.path = path
        self.directory_paths = list_directories(path)
        self.package_paths = list_packages(path)
        self.module_file_paths = list_module_files(path)
        names = []
        private_names = []
        for directory in self.directory_paths:
            path, name = split(directory)
            if not is_private_name(name):
                names.append(name)
            else:
                private_names.append(name)
        for package in self.package_paths:
            path, name = split(package)
            if not is_private_name(name):
                names.append(name)
            else:
                private_names.append(name)
        for module_file in self.module_file_paths:
            path, name = split(module_file)
            name, ext = splitext(name)
            if not is_private_name(name):
                names.append(name)
            else:
                private_names.append(name)
        self.names = sorted(names)


def reflect_package(path):
    return Package(path)


class ModuleFile:
    def __init__(self, path):
        self.path = path

    def load(self):
        return import_module_file(self.path)


def reflect_module_file(path):
    return ModuleFile(path)


class Module:
    def __init__(self, module):
        self.module = module
        self.classes = get_classes(module)
        self.functions = get_functions(module)
        self.values = get_values(module)


def reflect_module(module):
    return Module(module)


class Class:
    def __init__(self, class_object):
        self.class_object = class_object
        self.classes = get_classes(class_object)
        self.functions = get_functions(class_object)
        self.values = get_values(class_object)


def reflect_class(class_object):
    return Class(class_object)


class Value:
    def __init__(self, value):
        self.value = value
        self.classes = get_classes(value)
        self.functions = get_functions(value)
        self.values = get_values(value)


def reflect_value(value):
    return Value(value)


@unique
class ParameterKind(Enum):
    # Value must be supplied as a positional argument. Positional only parameters are those which appear before a / entry (if present) in a Python function definition.
    PositionalOnly = 1
    # Value may be supplied as either a keyword or positional argument (this is the standard binding behaviour for functions implemented in Python.)
    PositionalOrKeyword = 2
    # A tuple of positional arguments that aren’t bound to any other parameter. This corresponds to a *args parameter in a Python function definition.
    VarPositional = 3
    # Value must be supplied as a keyword argument. Keyword only parameters are those which appear after a * or *args entry in a Python function definition.
    KeywordOnly = 4
    # A dict of keyword arguments that aren’t bound to any other parameter. This corresponds to a **kwargs parameter in a Python function definition.
    VarKeyword = 5


def inspect_to_reflect_parameter_kind(kind):
    if kind == Parameter.POSITIONAL_ONLY:
        return ParameterKind.PositionalOnly
    if kind == Parameter.POSITIONAL_OR_KEYWORD:
        return ParameterKind.PositionalOrKeyword
    if kind == Parameter.VAR_POSITIONAL:
        return ParameterKind.VarPositional
    if kind == Parameter.KEYWORD_ONLY:
        return ParameterKind.KeywordOnly
    if kind == Parameter.VAR_KEYWORD:
        return ParameterKind.VarKeyword


class ReflectedParameter:
    def __init__(self, parameter):
        self.parameter = parameter
        self.name = parameter.name
        self.annotation = parameter.annotation
        self.default = parameter.default
        self.kind = inspect_to_reflect_parameter_kind(parameter.kind)

    def has_annotation(self) -> bool:
        return not self.annotation is Signature.empty

    def has_default(self) -> bool:
        return not self.default is Signature.empty


class Function:
    def __init__(self, function):
        self.function = function
        self.signature = signature(function)
        self.return_annotation = self.signature.return_annotation
        self.parameters = [
            ReflectedParameter(parameter)
            for parameter in self.signature.parameters.values()
        ]

    def has_return_annotation(self) -> bool:
        return not self.signature.return_annotation is Signature.empty

    def invoke(self, *args, **kwargs):
        return self.function(*args, **kwargs)


def reflect_function(function):
    return Function(function)
