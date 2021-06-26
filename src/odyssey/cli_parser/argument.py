import re
from enum import Enum, unique, auto


@unique
class ArgumentKind(Enum):
    Positional = auto()
    Flag = auto()
    Assignment = auto()


def monotonic_id() -> int:
    monotonic_id.counter += 1
    return monotonic_id.counter


monotonic_id.counter = 0


class Argument:
    def __init__(self, name, position, kind, value):
        self.name = name
        self.position = position
        self.kind = kind
        self.value = value
        self.id = monotonic_id()

    def __repr__(self):
        return f"Argument(name={self.name},position={self.position},kind={self.kind},value={self.value},id={self.id})"


def make_argument_list(matched_arguments):
    result = list()
    for position in range(len(matched_arguments)):
        argument = matched_arguments[position]

        if "name" in argument and "value" in argument:
            result.append(
                Argument(
                    argument["name"],
                    position,
                    ArgumentKind.Assignment,
                    argument["value"],
                )
            )
        if "name" in argument and "value" not in argument:
            result.append(Argument(argument["name"], position, ArgumentKind.Flag, None))
        if "name" not in argument and "value" in argument:
            result.append(
                Argument(None, position, ArgumentKind.Positional, argument["value"])
            )

    return result
