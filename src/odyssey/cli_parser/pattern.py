"""This file contains all the regex patterns for the cli parser.

Recall the three different categories of cli parameters:
Assignments contain both name and value in a single term.
Flags contain and name, and it is implementation defined
whether a value follows a given flag or not. There is no
way to tell from within the parser.
Positional terms are everything else.

Additionally, we want to support different styles:
-s Single letter Flag
-sdc Multiple Letter Flags
-long Single Dash Flag
--long Double Dash Flag
/slash Single Slash Flag
--long=assignment Double Dash Equals Assignment
--long:assignment Double Dash Colon Assignment
/slash=assignment Single Slash Equals Assignment
/slash:assignment Single Slash Colon Assignment

"""

import re
from enum import IntFlag, auto


class PatternStyle(IntFlag):
    """Use members of this enum to define which pattern styles
    will be accepted during parsing.
    """

    # Flag
    SINGLE_LETTER_FLAG = auto()
    SINGLE_DASH_FLAG = auto()
    DOUBLE_DASH_FLAG = auto()
    SINGLE_SLASH_FLAG = auto()
    # Assignment
    EQUALS_ASSIGNMENT = auto()
    COLON_ASSIGNMENT = auto()
    # Name
    NAME_LOWERCASE_LETTERS = auto()
    NAME_UPPERCASE_LETTERS = auto()
    NAME_NUMBERS = auto()
    NAME_DASHES = auto()
    NAME_UNDERSCORES = auto()


# Combinations
PatternStyle.NAME_LETTERS = (
    PatternStyle.NAME_LOWERCASE_LETTERS | PatternStyle.NAME_UPPERCASE_LETTERS
)
PatternStyle.DEFAULT_SYNTAX = (
    PatternStyle.DOUBLE_DASH_FLAG | PatternStyle.EQUALS_ASSIGNMENT
)
PatternStyle.DEFAULT_NAME = (
    PatternStyle.NAME_LOWERCASE_LETTERS | PatternStyle.NAME_DASHES
)
PatternStyle.DEFAULT = PatternStyle.DEFAULT_SYNTAX | PatternStyle.DEFAULT_NAME


def get_regex_string(pattern_style):
    lowercase = "a-z"
    uppercase = "A-Z"
    numbers = "0-9"
    dashes = "-"
    underscores = "_"

    name_patterns = ""
    if pattern_style & PatternStyle.NAME_LOWERCASE_LETTERS:
        name_patterns += lowercase
    if pattern_style & PatternStyle.NAME_UPPERCASE_LETTERS:
        name_patterns += uppercase
    if pattern_style & PatternStyle.NAME_NUMBERS:
        name_patterns += numbers
    if pattern_style & PatternStyle.NAME_DASHES:
        name_patterns += dashes
    if pattern_style & PatternStyle.NAME_UNDERSCORES:
        name_patterns += underscores

    if name_patterns:
        name_pattern = f"[{name_patterns}]"
    else:
        name_pattern = ""

    single_dash = "-"
    double_dash = "--"
    single_slash = "/"
    flag_patterns = list()
    if (
        pattern_style & PatternStyle.SINGLE_LETTER_FLAG
        or pattern_style & PatternStyle.SINGLE_DASH_FLAG
    ):
        flag_patterns.append(single_dash)
    if pattern_style & PatternStyle.DOUBLE_DASH_FLAG:
        flag_patterns.append(double_dash)
    if pattern_style & PatternStyle.SINGLE_SLASH_FLAG:
        flag_patterns.append(single_slash)

    name_count = ""
    if pattern_style & PatternStyle.SINGLE_LETTER_FLAG and (
        pattern_style & PatternStyle.SINGLE_DASH_FLAG
        or pattern_style & PatternStyle.DOUBLE_DASH_FLAG
        or pattern_style & PatternStyle.SINGLE_SLASH_FLAG
    ):
        name_count = r"{1,}"
    elif pattern_style & PatternStyle.SINGLE_LETTER_FLAG and not (
        pattern_style & PatternStyle.SINGLE_DASH_FLAG
        or pattern_style & PatternStyle.DOUBLE_DASH_FLAG
        or pattern_style & PatternStyle.SINGLE_SLASH_FLAG
    ):
        name_count = r"{1}"
    elif not pattern_style & PatternStyle.SINGLE_LETTER_FLAG and (
        pattern_style & PatternStyle.SINGLE_DASH_FLAG
        or pattern_style & PatternStyle.DOUBLE_DASH_FLAG
        or pattern_style & PatternStyle.SINGLE_SLASH_FLAG
    ):
        name_count = r"{2,}"

    if flag_patterns:
        flag_pattern = "(?:" + "|".join(flag_patterns) + ")"
    else:
        flag_pattern = ""

    equals = "="
    colon = ":"
    assignment_patterns = list()
    if pattern_style & PatternStyle.EQUALS_ASSIGNMENT:
        assignment_patterns.append(equals)
    if pattern_style & PatternStyle.COLON_ASSIGNMENT:
        assignment_patterns.append(colon)

    if assignment_patterns:
        assignment_pattern = "(?:[" + "|".join(assignment_patterns) + "](?P<value>.*))?"
    else:
        assignment_pattern = ""

    if flag_pattern and name_pattern:
        return f"{flag_pattern}(?P<name>{name_pattern}{name_count}){assignment_pattern}"

    raise ValueError(
        "flag_pattern should include at least one flag style and at least one name style"
    )


def get_compiled_regex(pattern_style):
    return re.compile(get_regex_string(pattern_style))


def match_argument(compiled_regex, argument_string):
    match = compiled_regex.match(argument_string)
    if match:
        groupdict = match.groupdict()
        if "value" in groupdict and groupdict["value"] is None:
            del groupdict["value"]
        return [groupdict]
    return [{"value": argument_string}]


def match(pattern_style, argument_list):
    compiled_regex = get_compiled_regex(pattern_style)
    result = list()
    for argument_string in argument_list:
        result.extend(match_argument(compiled_regex, argument_string))
    return result
