from odyssey.cli_parser.pattern import *


def test_single_letter_flag():
    arguments = ["-a", "-b", "-c"]
    pattern = PatternStyle.SINGLE_LETTER_FLAG | PatternStyle.NAME_LOWERCASE_LETTERS
    expected = [
        {"name": "a"},
        {"name": "b"},
        {"name": "c"},
    ]

    result = match(pattern, arguments)

    assert expected == result


def test_single_dash_flag():
    arguments = ["-abc"]
    pattern = PatternStyle.SINGLE_DASH_FLAG | PatternStyle.NAME_LOWERCASE_LETTERS
    expected = [
        {"name": "abc"},
    ]

    result = match(pattern, arguments)

    assert expected == result


def test_double_dash_flag():
    arguments = ["--abc"]
    pattern = PatternStyle.DOUBLE_DASH_FLAG | PatternStyle.NAME_LOWERCASE_LETTERS
    expected = [
        {"name": "abc"},
    ]

    result = match(pattern, arguments)

    assert expected == result
