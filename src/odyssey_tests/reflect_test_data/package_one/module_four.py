from sys import version_info, path
from os.path import dirname, realpath, join

def simplest_function():
    pass


def string_function() -> str:
    return "string"


def identity_function(value):
    return value


path.append(realpath(join(dirname(realpath(__file__)), "..")))

if version_info.major >= 3 and version_info.minor >= 7:
    from package_one.module_four_compatibility.module_four_37 import parameter_kind_function
elif version_info.major >= 3 and version_info.minor >= 6:
    from package_one.module_four_compatibility.module_four_36 import parameter_kind_function
else:
    raise SyntaxError()
