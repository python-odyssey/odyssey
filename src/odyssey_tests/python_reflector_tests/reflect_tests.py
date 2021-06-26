import pytest
from odyssey.python_reflector.reflect import (
    is_callable,
    is_method_with_bound_self,
    is_directory,
    is_package,
    is_module,
    list_directories,
    list_packages,
    is_module_file,
    list_module_files,
    import_path_from_module,
    import_path_from_module_path,
    import_module_file,
    has_member,
    get_member,
    get_classes,
    get_functions,
    get_values,
    ReflectType,
    reflect_type,
    reflect_directory,
    reflect_package,
    reflect_module_file,
    reflect_module,
    reflect_class,
    reflect_value,
    reflect_function,
    reflect_parameter,
    ParameterKind,
)
from os.path import join, realpath, dirname
from collections import Counter
from sys import version_info


def free_function():
    pass


class EmptyClass:
    pass


class ExampleClass:
    def __init__(self):
        pass

    def __call__(self):
        pass

    def member_function(self):
        pass


example_object = ExampleClass()

example_lambda = lambda param: param


def test_is_callable():
    assert is_callable(int)
    assert is_callable(str)
    assert is_callable(list)
    assert not is_callable(1)
    assert not is_callable("dragons")
    assert not is_callable(["hello", "world"])
    assert is_callable(free_function)
    assert not is_callable(free_function())
    assert is_callable(EmptyClass)
    assert is_callable(ExampleClass)
    assert is_callable(ExampleClass())
    assert is_callable(ExampleClass.member_function)
    assert is_callable(ExampleClass().member_function)
    assert is_callable(example_object)
    assert is_callable(example_lambda)


def test_is_method_with_bound_self():
    assert not is_method_with_bound_self(int)
    assert not is_method_with_bound_self(str)
    assert not is_method_with_bound_self(list)
    assert not is_method_with_bound_self(free_function)
    assert not is_method_with_bound_self(EmptyClass)
    assert not is_method_with_bound_self(ExampleClass)
    assert not is_method_with_bound_self(ExampleClass())
    assert not is_method_with_bound_self(ExampleClass.member_function)
    assert is_method_with_bound_self(ExampleClass().member_function)
    assert not is_method_with_bound_self(example_object)
    assert is_method_with_bound_self(example_object.member_function)
    assert not is_method_with_bound_self(example_lambda)


tests_directory = realpath(join(dirname(realpath(__file__)), ".."))
test_data_directory = join(tests_directory, "test_data")
directory_one_path = join(test_data_directory, "directory_one")
directory_two_path = join(test_data_directory, "directory_two")
directory_three_path = join(test_data_directory, "directory_three")
package_one_path = join(test_data_directory, "package_one")
package_two_path = join(test_data_directory, "package_two")
package_three_path = join(test_data_directory, "package_three")

module_one_path = join(directory_one_path, "module_one.py")
module_two_path = join(directory_one_path, "module_two.py")
module_three_path = join(package_one_path, "module_three.py")
module_four_path = join(package_one_path, "module_four.py")


def test_is_directory():
    assert is_directory(directory_one_path)
    assert is_directory(directory_two_path)
    assert is_directory(directory_three_path)
    assert not is_directory(package_one_path)
    assert not is_directory(package_two_path)
    assert not is_directory(package_three_path)


def test_is_package():
    assert not is_package(directory_one_path)
    assert not is_package(directory_two_path)
    assert not is_package(directory_three_path)
    assert is_package(package_one_path)
    assert is_package(package_two_path)
    assert is_package(package_three_path)


def test_list_directories():
    expected = [directory_one_path, directory_two_path, directory_three_path]

    result = list_directories(test_data_directory)

    assert Counter(expected) == Counter(result)


def test_list_packages():
    expected = [package_one_path, package_two_path, package_three_path]

    result = list_packages(test_data_directory)

    assert Counter(expected) == Counter(result)


def test_is_module_file():
    assert is_module_file(module_one_path)
    assert is_module_file(module_two_path)
    assert is_module_file(module_three_path)
    assert is_module_file(module_four_path)


def test_list_module_files_in_directory():
    expected = [module_one_path, module_two_path]

    result = list_module_files(directory_one_path)

    assert Counter(expected) == Counter(result)


def test_list_module_files_in_package():
    expected = [module_three_path, module_four_path]

    result = list_module_files(package_one_path)

    assert Counter(expected) == Counter(result)


def test_import_path_from_module_path_directory():
    expected = "module_one"

    result = import_path_from_module_path(module_one_path)

    assert expected == result


def test_import_path_from_module_path_package():
    expected = "package_one.module_three"

    result = import_path_from_module_path(module_three_path)

    assert expected == result


def test_is_module():
    assert import_module_file(module_one_path)
    assert import_module_file(module_three_path)


def test_is_callable_after_import():
    assert is_callable(import_module_file(module_one_path).function_one)
    assert is_callable(import_module_file(module_three_path).function_three)


def test_import_module_file_directory():
    expected = "result_one"

    module_one = import_module_file(module_one_path)
    result = module_one.function_one()

    assert expected == result


def test_import_module_file_package():
    expected = "result_three"

    module_three = import_module_file(module_three_path)
    result = module_three.function_three()

    assert expected == result


def test_has_member():
    module_three = import_module_file(module_three_path)

    assert has_member(module_three, "function_three")
    assert has_member(module_three, "ClassOne")
    assert has_member(module_three, "value_one")


def test_get_member():
    module_three = import_module_file(module_three_path)

    assert get_member(module_three, "function_three") is module_three.function_three
    assert get_member(module_three, "ClassOne") is module_three.ClassOne
    assert get_member(module_three, "value_one") is module_three.value_one


def test_get_classes():
    module_three = import_module_file(module_three_path)
    expected = [("ClassOne", module_three.ClassOne)]

    result = get_classes(module_three)

    assert expected == result


def test_get_functions():
    module_three = import_module_file(module_three_path)
    expected = [("function_three", module_three.function_three)]

    result = get_functions(module_three)

    assert expected == result


def test_get_values():
    module_three = import_module_file(module_three_path)
    expected = ("value_one", module_three.value_one)

    result = get_values(module_three)

    assert expected in result


def test_reflect_type_directory():
    expected = ReflectType.Directory

    result = reflect_type(directory_one_path)

    assert expected == result


def test_reflect_type_package():
    expected = ReflectType.Package

    result = reflect_type(package_one_path)

    assert expected == result


def test_reflect_directory():
    directory = reflect_directory(test_data_directory)

    print(directory.names)

    assert False


def test_reflect_directory():
    expected = [
        "directory_one",
        "directory_three",
        "directory_two",
        "package_one",
        "package_three",
        "package_two",
    ]
    directory = reflect_directory(test_data_directory)

    result = directory.names

    assert expected == result


def test_reflect_directory_one():
    expected = ["module_one", "module_two"]
    directory = reflect_directory(directory_one_path)

    result = directory.names

    assert expected == result


def test_reflect_package_one():
    expected = ["module_four", "module_four_compatibility", "module_three"]
    package = reflect_package(package_one_path)

    result = package.names

    assert expected == result


def test_reflect_module_file_one():
    import_path = "module_one"
    module_file = reflect_module_file(module_one_path)

    module = module_file.load()

    assert is_module(module)
    assert import_path == import_path_from_module(module)


def test_reflect_module_file_three():
    import_path = "package_one.module_three"
    module_file = reflect_module_file(module_three_path)

    module = module_file.load()

    assert is_module(module)
    assert import_path == import_path_from_module(module)


def test_reflect_module_one():
    module_file = reflect_module_file(module_one_path)
    loaded_module = module_file.load()
    module = reflect_module(loaded_module)

    assert ("function_one", loaded_module.function_one) in module.functions


def test_reflect_module_three():
    module_file = reflect_module_file(module_three_path)
    loaded_module = module_file.load()
    module = reflect_module(loaded_module)

    assert ("function_three", loaded_module.function_three) in module.functions
    assert ("ClassOne", loaded_module.ClassOne) in module.classes
    assert ("value_one", loaded_module.value_one) in module.values


def test_reflect_class_one():
    module_file = reflect_module_file(module_three_path)
    loaded_module = module_file.load()
    module = reflect_module(loaded_module)
    reflected_class = reflect_class(loaded_module.ClassOne)

    assert (
        "member_function_one",
        loaded_module.ClassOne.member_function_one,
    ) in reflected_class.functions


def test_reflect_value_one():
    module_file = reflect_module_file(module_three_path)
    loaded_module = module_file.load()
    module = reflect_module(loaded_module)
    value = reflect_value(loaded_module.value_one)

    assert (
        "member_function_one",
        loaded_module.value_one.member_function_one,
    ) in value.functions


def test_reflect_simplest_function():
    module_file = reflect_module_file(module_four_path)
    loaded_module = module_file.load()
    function = reflect_function(loaded_module.simplest_function)

    assert not function.has_return_annotation()
    assert function.invoke() is None


def test_reflect_string_function():
    module_file = reflect_module_file(module_four_path)
    loaded_module = module_file.load()
    function = reflect_function(loaded_module.string_function)

    assert function.has_return_annotation()
    assert function.return_annotation is str
    assert function.invoke() == "string"


def test_reflect_identity_function():
    module_file = reflect_module_file(module_four_path)
    loaded_module = module_file.load()
    function = reflect_function(loaded_module.identity_function)

    assert not function.has_return_annotation()
    assert function.invoke("value") == "value"
    for parameter in function.parameters:
        assert not parameter.has_default()
        assert not parameter.has_annotation()
        assert parameter.kind == ParameterKind.PositionalOrKeyword


def test_reflect_parameter_kind_function():
    module_file = reflect_module_file(module_four_path)
    loaded_module = module_file.load()
    function = reflect_function(loaded_module.parameter_kind_function)

    assert not function.has_return_annotation()
    parameters = function.parameters
    if version_info.major >= 3 and version_info.minor >= 8:
        assert parameters[0].kind == ParameterKind.PositionalOnly
        assert parameters[1].kind == ParameterKind.PositionalOrKeyword
        assert parameters[2].kind == ParameterKind.VarPositional
        assert parameters[3].kind == ParameterKind.KeywordOnly
        assert parameters[4].kind == ParameterKind.VarKeyword
    else:
        assert parameters[0].kind == ParameterKind.PositionalOrKeyword
        assert parameters[1].kind == ParameterKind.VarPositional
        assert parameters[2].kind == ParameterKind.KeywordOnly
        assert parameters[3].kind == ParameterKind.VarKeyword

    # In current versions of python you can only specify positional_or_keyword
    # parameters using their positional variant in this complex scenario.
    assert function.invoke(
        "value1",
        "value2",
        "value3",
        "value4",
        keyword_only="value5",
        var_keyword1="value6",
        var_keyword2="value7",
    ) == (
        "value1",
        "value2",
        "value3",
        "value4",
        "value5",
        {"var_keyword1": "value6", "var_keyword2": "value7"},
    )
    for parameter in parameters:
        assert not parameter.has_default()
        assert not parameter.has_annotation()
