from odyssey.cli_parser.pattern import *


def test_single_letter_flag():
    arguments = ["-a", "-b", "-c"]
    pattern = PatternStyle.SINGLE_DASH_FLAG | PatternStyle.NAME_LOWERCASE_LETTERS
    expected = [
        {"argument": "-a", "name": "a"},
        {"argument": "-b", "name": "b"},
        {"argument": "-c", "name": "c"},
    ]

    result = match(pattern, arguments)

    assert expected == result
