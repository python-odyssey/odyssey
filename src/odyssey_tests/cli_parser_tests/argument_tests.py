import odyssey.cli_parser.pattern as pattern
import odyssey.cli_parser.argument as argument


def test_parse():
    arguments = [
        "dragons",
        "and",
        "things",
        "--first-flag",
        "--second-flag",
        "value",
        "--first-assignment=first",
        "--second-assignment=second",
    ]

    style = pattern.PatternStyle.DEFAULT
    matched_arguments = pattern.match(style, arguments)
    parsed_arguments = argument.make_argument_list(matched_arguments)

    assert parsed_arguments[0].kind == argument.ArgumentKind.Positional
    assert parsed_arguments[0].value == "dragons"
    assert parsed_arguments[1].kind == argument.ArgumentKind.Positional
    assert parsed_arguments[1].value == "and"
    assert parsed_arguments[2].kind == argument.ArgumentKind.Positional
    assert parsed_arguments[2].value == "things"
    assert parsed_arguments[3].kind == argument.ArgumentKind.Flag
    assert parsed_arguments[3].name == "first-flag"
    assert parsed_arguments[4].kind == argument.ArgumentKind.Flag
    assert parsed_arguments[4].name == "second-flag"
    assert parsed_arguments[5].kind == argument.ArgumentKind.Positional
    assert parsed_arguments[5].value == "value"
    assert parsed_arguments[6].kind == argument.ArgumentKind.Assignment
    assert parsed_arguments[6].name == "first-assignment"
    assert parsed_arguments[6].value == "first"
    assert parsed_arguments[7].kind == argument.ArgumentKind.Assignment
    assert parsed_arguments[7].name == "second-assignment"
    assert parsed_arguments[7].value == "second"


def test_parse_with_slashes():
    arguments = [
        "dragons",
        "and",
        "things",
        "/first-flag",
        "/second-flag",
        "value",
        "/first-assignment:first",
        "/second-assignment:second",
    ]

    style = (
        pattern.PatternStyle.NAME_LOWERCASE_LETTERS
        | pattern.PatternStyle.NAME_DASHES
        | pattern.PatternStyle.SINGLE_SLASH_FLAG
        | pattern.PatternStyle.COLON_ASSIGNMENT
    )
    matched_arguments = pattern.match(style, arguments)
    parsed_arguments = argument.make_argument_list(matched_arguments)

    assert parsed_arguments[0].kind == argument.ArgumentKind.Positional
    assert parsed_arguments[0].value == "dragons"
    assert parsed_arguments[1].kind == argument.ArgumentKind.Positional
    assert parsed_arguments[1].value == "and"
    assert parsed_arguments[2].kind == argument.ArgumentKind.Positional
    assert parsed_arguments[2].value == "things"
    assert parsed_arguments[3].kind == argument.ArgumentKind.Flag
    assert parsed_arguments[3].name == "first-flag"
    assert parsed_arguments[4].kind == argument.ArgumentKind.Flag
    assert parsed_arguments[4].name == "second-flag"
    assert parsed_arguments[5].kind == argument.ArgumentKind.Positional
    assert parsed_arguments[5].value == "value"
    assert parsed_arguments[6].kind == argument.ArgumentKind.Assignment
    assert parsed_arguments[6].name == "first-assignment"
    assert parsed_arguments[6].value == "first"
    assert parsed_arguments[7].kind == argument.ArgumentKind.Assignment
    assert parsed_arguments[7].name == "second-assignment"
    assert parsed_arguments[7].value == "second"
