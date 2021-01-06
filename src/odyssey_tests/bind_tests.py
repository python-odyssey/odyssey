from odyssey.bind import (
    bind_positional_only,
    bind_positional_or_keyword,
    bind_var_positional,
    bind_keyword_only,
    bind_var_keyword,
    bind_arguments,
)
from odyssey.reflect import (
    reflect_function,
    ReflectedParameter,
    ParameterKind,
)
from odyssey.parse import parse_arguments
from odyssey_tests.bind_test_data import (
    positional_only_parameter,
    positional_or_keyword_parameter,
    var_positional_parameter,
    keyword_only_parameter,
    var_keyword_parameter,
    simple_function,
)


def test_bind_positional_only():
    reflected_parameter = positional_only_parameter
    arguments = ["value"]
    parsed_arguments = parse_arguments(arguments)
    consume_list = [False]

    result = bind_positional_only(reflected_parameter, parsed_arguments, consume_list)

    assert result == "value"
    assert consume_list == [True]


def test_bind_positional_or_keyword():
    reflected_parameter = positional_or_keyword_parameter
    arguments = ["--first-parameter=value"]
    parsed_arguments = parse_arguments(arguments)
    consume_list = [False]

    result = bind_positional_or_keyword(
        reflected_parameter, parsed_arguments, consume_list
    )

    assert result == "value"
    assert consume_list == [True]


def test_bind_var_positional():
    reflected_parameter = var_positional_parameter
    arguments = ["value1", "value2", "value3"]
    parsed_arguments = parse_arguments(arguments)
    consume_list = [False, False, False]

    result = bind_var_positional(reflected_parameter, parsed_arguments, consume_list)

    assert result == ["value1", "value2", "value3"]
    assert consume_list == [True, True, True]


def test_bind_keyword_only():
    reflected_parameter = keyword_only_parameter
    arguments = ["--name=value"]
    parsed_arguments = parse_arguments(arguments)
    consume_list = [False]

    result = bind_keyword_only(reflected_parameter, parsed_arguments, consume_list)

    assert result == ("name", "value")
    assert consume_list == [True]


def test_bind_var_keyword():
    reflected_parameter = var_keyword_parameter
    arguments = ["--name1=value1", "--name2=value2"]
    parsed_arguments = parse_arguments(arguments)
    consume_list = [False, False]

    result = bind_var_keyword(reflected_parameter, parsed_arguments, consume_list)

    assert result == {"name1": "value1", "name2": "value2"}
    assert consume_list == [True, True]


def test_bind_arguments_empty():
    expected = None

    reflected_function = reflect_function(simple_function)
    bound_function = bind_arguments(reflected_function, [])
    result = bound_function.invoke()

    assert expected == result
