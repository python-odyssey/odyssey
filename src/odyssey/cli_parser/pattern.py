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

    # Syntax
    SINGLE_LETTER_FLAG = auto()
    MULTIPLE_LETTER_FLAG = auto()
    SINGLE_DASH_FLAG = auto()
    DOUBLE_DASH_FLAG = auto()
    SINGLE_SLASH_FLAG = auto()
    DOUBLE_DASH_EQUALS_ASSIGNMENT = auto()
    DOUBLE_DASH_COLON_ASSIGNMENT = auto()
    SINGLE_SLASH_EQUALS_ASSIGNMENT = auto()
    SINGLE_SLASH_COLON_ASSIGNMENT = auto()
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
    PatternStyle.DOUBLE_DASH_FLAG | PatternStyle.DOUBLE_DASH_EQUALS_ASSIGNMENT
)
PatternStyle.DEFAULT_NAME = (
    PatternStyle.NAME_LOWERCASE_LETTERS | PatternStyle.NAME_DASHES
)
PatternStyle.DEFAULT = PatternStyle.DEFAULT_SYNTAX | PatternStyle.DEFAULT_NAME


def get_regex_string(pattern_style):
    if (
        pattern_style & PatternStyle.MULTIPLE_LETTER_FLAG
        and pattern_style & SINGLE_DASH_FLAG
    ):
        raise ValueError(
            "Parsing of both multiple letter flags and single dash flags is not supported."
        )

    return "-(?P<name>[a-z])"


def get_compiled_regex(pattern_style):
    return re.compile(get_regex_string(pattern_style))


def match_argument(compiled_regex, argument_string):
    match = compiled_regex.match(argument_string)
    groupdict = match.groupdict()
    groupdict["argument"] = argument_string
    return groupdict


def match(pattern_style, argument_list):
    compiled_regex = get_compiled_regex(pattern_style)
    return [
        match_argument(compiled_regex, argument_string)
        for argument_string in argument_list
    ]


# flag_regex = re.compile(r"--([a-zA-Z0-9-_]+)$")
# assignment_regex = re.compile(r"--([a-zA-Z0-9-_]+)=(.*)")
