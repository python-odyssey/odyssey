import pytest
from odyssey.reflect import is_callable, is_method_with_bound_self, is_directory, is_package, list_directories, list_packages, is_module_file, list_module_files, import_path_from_module_path, import_module_file
from os.path import join, realpath, dirname
from collections import Counter

def free_function():
    pass

class EmptyClass():
    pass

class ExampleClass():
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

reflect_tests_directory = dirname(realpath(__file__))
reflect_tests_data = join(reflect_tests_directory, "reflect_test_data")
directory_one_path = join(reflect_tests_data, "directory_one")
directory_two_path = join(reflect_tests_data, "directory_two")
directory_three_path = join(reflect_tests_data, "directory_three")
package_one_path = join(reflect_tests_data, "package_one")
package_two_path = join(reflect_tests_data, "package_two")
package_three_path = join(reflect_tests_data, "package_three")

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

    result = list_directories(reflect_tests_data)

    assert Counter(expected) == Counter(result)

def test_list_packages():
    expected = [package_one_path, package_two_path, package_three_path]

    result = list_packages(reflect_tests_data)

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
