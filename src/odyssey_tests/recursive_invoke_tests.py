from os.path import join, realpath, dirname
from odyssey.recursive_invoke import recurse


tests_directory = dirname(realpath(__file__))
test_data_directory = join(tests_directory, "test_data")
directory_one_path = join(test_data_directory, "directory_one")
package_one_path = join(test_data_directory, "package_one")
module_one_path = join(directory_one_path, "module_one.py")
module_four_path = join(package_one_path, "module_four.py")


def test_recurse_test_data_directory():
    arguments = []
    result = recurse(test_data_directory, arguments)
