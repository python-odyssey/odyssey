import re
from enum import (
    Enum,
    unique
)


@unique
class ArgumentKind(Enum):
    # Normal Arguments which can used directly or consumed by flags
    Positional = 0
    # Specified by -- at the beginning without an equals sign
    Flag = 1
    # Specified by -- at the beginning with an equals sign after a term
    Assignment = 2


flag_regex = re.compile(r"--([a-zA-Z0-9-_]+)$")
assignment_regex = re.compile(r"--([a-zA-Z0-9-_]+)=(.*)")


class Argument:
    def __init__(self, name, position, kind, value):
        self.name = name
        self.position = position
        self.kind = kind
        self.value = value

    def __repr__(self):
        return f"Argument(name={self.name},position={self.position},kind={self.kind},value={self.value})"


def parse_arguments(arguments):
    parsed_arguments = []
    for i in range(len(arguments)):
        argument = arguments[i]
        # Flags
        matches = flag_regex.match(argument)
        if matches:
            name = matches.groups(1)[0].replace("-","_").lower()
            parsed_arguments.append(Argument(name, i, ArgumentKind.Flag, None))
            continue
        # Assignments
        matches = assignment_regex.match(argument)
        if matches:
            name = matches.groups(1)[0].replace("-","_").lower()
            value = matches.groups(1)[1]
            parsed_arguments.append(Argument(name, i, ArgumentKind.Assignment, value))
            continue
        parsed_arguments.append(Argument(None, i, ArgumentKind.Positional, argument))
    return parsed_arguments


