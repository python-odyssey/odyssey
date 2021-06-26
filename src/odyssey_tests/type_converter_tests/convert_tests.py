import pytest
from odyssey.type_converter.convert import (
    to_string,
    to_int,
    to_float,
    to_complex,
    to_bool,
    to_tuple,
    to_list,
    to_dict,
)


def test_to_string_string():
    expected = "Hello, World!"
    value = expected

    result = to_string(value)

    assert expected == result


def test_to_string_int():
    expected = "42"
    value = 42

    result = to_string(value)

    assert expected == result


def test_to_int():
    expected = 42
    value = "42"

    result = to_int(value)

    assert expected == result


def test_to_string_float():
    expected = "2.56"
    value = 2.56

    result = to_string(value)

    assert expected == result


def test_to_float():
    expected = 2.56
    value = "2.56"

    result = to_float(value)

    assert expected == result


def test_to_string_complex():
    expected = "(2+4j)"
    value = complex(2, 4)

    result = to_string(value)

    assert expected == result


def test_to_complex():
    expected = complex(2, 4)
    value = "(2+4j)"

    result = to_complex(value)

    assert expected == result


def test_to_string_bool():
    expected = "True"
    value = True

    result = to_string(value)

    assert expected == result


def test_to_bool():
    expected = True
    value = "True"

    result = to_bool(value)

    assert expected == result


def test_to_string_tuple():
    expected = '["Hello, World", 42, 2.56]'
    value = ("Hello, World", 42, 2.56)

    result = to_string(value)

    assert expected == result


def test_to_tuple():
    expected = ("Hello, World", 42, 2.56)
    value = '["Hello, World", 42, 2.56]'

    result = to_tuple(value)

    assert expected == result


def test_to_string_list():
    expected = '["Hello, World", 42, 2.56]'
    value = ["Hello, World", 42, 2.56]

    result = to_string(value)

    assert expected == result


def test_to_list():
    expected = ["Hello, World", 42, 2.56]
    value = '["Hello, World", 42, 2.56]'

    result = to_list(value)

    assert expected == result


def test_to_string_dict():
    expected = '{"value1": "Hello, World", "value2": 42, "value3": 2.56}'
    value = {"value1": "Hello, World", "value2": 42, "value3": 2.56}

    result = to_string(value)

    assert expected == result


def test_to_dict():
    expected = {"value1": "Hello, World", "value2": 42, "value3": 2.56}
    value = '{"value1": "Hello, World", "value2": 42, "value3": 2.56}'

    result = to_dict(value)

    assert expected == result
