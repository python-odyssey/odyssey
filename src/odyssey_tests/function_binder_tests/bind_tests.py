from odyssey.function_binder.bind import (
    bind_positional_only,
    bind_positional_or_keyword,
    bind_var_positional,
    bind_keyword_only,
    bind_var_keyword,
    bind_arguments,
)
from odyssey.python_reflector.reflect import (
    reflect_function,
    ReflectedParameter,
    ParameterKind,
)
from odyssey.cli_parser import parse_arguments
from odyssey_tests.function_binder_tests.bind_test_data import (
    positional_only_parameter,
    positional_or_keyword_parameter,
    var_positional_parameter,
    keyword_only_parameter,
    var_keyword_parameter,
    simple_function,
    parameter_type_function,
)
from odyssey.name_resolver.resolve import NameResolver


RESOLVER = NameResolver()


def test_bind_positional_only():
    reflected_parameter = positional_only_parameter
    arguments = ["value"]
    parsed_arguments = parse_arguments(arguments)

    result = bind_positional_only(reflected_parameter, parsed_arguments)

    assert result.value == "value"


def test_bind_positional_or_keyword():
    reflected_parameter = positional_or_keyword_parameter
    arguments = ["--first-parameter=value"]
    parsed_arguments = parse_arguments(arguments)

    result = bind_positional_or_keyword(reflected_parameter, parsed_arguments, RESOLVER)

    assert result.value == "value"


def test_bind_var_positional():
    reflected_parameter = var_positional_parameter
    arguments = ["value1", "value2", "value3"]
    parsed_arguments = parse_arguments(arguments)

    results = bind_var_positional(reflected_parameter, parsed_arguments)

    assert [result.value for result in results] == ["value1", "value2", "value3"]


def test_bind_keyword_only():
    reflected_parameter = keyword_only_parameter
    arguments = ["--keyword-only-parameter=value"]
    parsed_arguments = parse_arguments(arguments)

    result = bind_keyword_only(reflected_parameter, parsed_arguments, RESOLVER)

    assert result.value == "value"


def test_bind_var_keyword():
    reflected_parameter = var_keyword_parameter
    arguments = ["--first-name=value1", "--second-name=value2"]
    parsed_arguments = parse_arguments(arguments)
    results = bind_var_keyword(reflected_parameter, parsed_arguments, RESOLVER)

    assert {
        name: bound_parameter.value for name, bound_parameter in results.items()
    } == {"first_name": "value1", "second_name": "value2"}


def test_bind_arguments_empty():
    expected = None

    reflected_function = reflect_function(simple_function)
    bound_function = bind_arguments(reflected_function, [], RESOLVER)
    result = bound_function.invoke()

    assert expected == result


def test_bind_parameter_type_function():
    arguments = [
        "--var-keyword-one=really",
        "are",
        "--positional-or-keyword=dragons",
        "the",
        "--keyword-only=best",
    ]
    expected = {
        "positional_or_keyword": "dragons",
        "var_positional": ("are", "the"),
        "keyword_only": "best",
        "var_keyword": {"var_keyword_one": "really"},
    }

    reflected_function = reflect_function(parameter_type_function)
    parsed_arguments = parse_arguments(arguments)
    print(parsed_arguments)
    bound_function = bind_arguments(reflected_function, parsed_arguments, RESOLVER)
    result = bound_function.invoke()

    assert expected == result
