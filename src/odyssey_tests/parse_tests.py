from odyssey.parse import (
    flag_regex,
    assignment_regex,
    parse_arguments,
    ArgumentKind,
)


def test_flag_regex():
    value = "--thIs_is-a_Flag"
    expected = "thIs_is-a_Flag"

    matches = flag_regex.match(value)

    assert matches
    assert matches.groups(1)[0] == expected


def test_assignment_regex():
    value = "--thIs_is-an_Assignment=something"
    expected_name = "thIs_is-an_Assignment"
    expected_value = "something"

    matches = assignment_regex.match(value)

    assert matches
    assert matches.groups(1)[0] == expected_name
    assert matches.groups(2)[0] == expected_name


def test_parse():
    arguments = ["dragons", "and", "things", "--first-flag", "--Second-Flag", "value", "--first-assignment=first", "--Second-Assignment=second"]

    parsed_arguments = parse_arguments(arguments)


    assert parsed_arguments[0].kind == ArgumentKind.Positional
    assert parsed_arguments[0].value == "dragons"
    assert parsed_arguments[1].kind == ArgumentKind.Positional
    assert parsed_arguments[1].value == "and"
    assert parsed_arguments[2].kind == ArgumentKind.Positional
    assert parsed_arguments[2].value == "things"
    assert parsed_arguments[3].kind == ArgumentKind.Flag
    assert parsed_arguments[3].name == "first_flag"
    assert parsed_arguments[4].kind == ArgumentKind.Flag
    assert parsed_arguments[4].name == "second_flag"
    assert parsed_arguments[5].kind == ArgumentKind.Positional
    assert parsed_arguments[5].value == "value"
    assert parsed_arguments[6].kind == ArgumentKind.Assignment
    assert parsed_arguments[6].name == "first_assignment"
    assert parsed_arguments[6].value == "first"
    assert parsed_arguments[7].kind == ArgumentKind.Assignment
    assert parsed_arguments[7].name == "second_assignment"
    assert parsed_arguments[7].value == "second"
