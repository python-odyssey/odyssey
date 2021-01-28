"""Functionality for binding a list of strings to a set of function parameters."""

import odyssey.convert as convert
from odyssey.reflect import (
    Function,
    ParameterKind,
)
from odyssey.parse import ArgumentKind

# The rules herein determine how function parameters are parsed.
# We support positional only parameters. They must come before all positional var parameters. They can support annotated implicit conversion.
# We support positional + keyword parameters in either usage. They can appear in keyword form in any position. They can support annotated implicit conversion.
# We support positional var parameters. They must appear after all positional only parameters. They cannot support annotated implicit conversion.
# We support keyword only parameters. They can appear in any position. They can support annotated implicit conversion.
# We support keyword var parameters. They can appear in any position. They cannot support annotated implicit conversion.


class BoundFunction:
    def __init__(
        self, function: Function, args: list, bound_args: list, bound_kwargs: dict
    ):
        self.function = function
        self.args = args
        self.bound_args = bound_args
        self.bound_kwargs = bound_kwargs

    def invoke(self):
        return self.function.invoke(*self.bound_args, **self.bound_kwargs)


def bind_positional_only(parameter, parsed_arguments: list, consume_list: list):
    assert len(parsed_arguments) == len(consume_list)
    for i in range(len(parsed_arguments)):
        if consume_list[i]:
            continue
        argument = parsed_arguments[i]
        if argument.kind == ArgumentKind.Positional:
            consume_list[i] = True
            return argument.value

    raise None


def bind_positional_or_keyword(parameter, parsed_arguments: list, consume_list: list):
    result = None
    assert len(parsed_arguments) == len(consume_list)
    for i in range(len(parsed_arguments)):
        if consume_list[i]:
            continue
        argument = parsed_arguments[i]
        if argument.kind == ArgumentKind.Assignment and argument.name == parameter.name:
            consume_list[i] = True
            return argument.value

    raise None


def bind_var_positional(parameter, parsed_arguments: list, consume_list: list):
    result = []
    assert len(parsed_arguments) == len(consume_list)
    for i in range(len(parsed_arguments)):
        if consume_list[i]:
            continue
        argument = parsed_arguments[i]
        if argument.kind != ArgumentKind.Positional:
            continue
        consume_list[i] = True
        result.append(argument.value)

    return result


def bind_keyword_only(parameter, parsed_arguments: list, consume_list: list):
    assert len(parsed_arguments) == len(consume_list)
    for i in range(len(parsed_arguments)):
        if consume_list[i]:
            continue
        argument = parsed_arguments[i]
        if argument.kind == ArgumentKind.Assignment:
            consume_list[i] = True
            return (argument.name, argument.value)

    raise None


def bind_var_keyword(parameter, parsed_arguments: list, consume_list: list):
    result = dict()
    assert len(parsed_arguments) == len(consume_list)
    for i in range(len(parsed_arguments)):
        if consume_list[i]:
            continue
        argument = parsed_arguments[i]
        if argument.kind == ArgumentKind.Assignment:
            consume_list[i] = True
            result[argument.name] = argument.value

    return result


def bind_arguments(reflected_function: Function, parsed_arguments: list):
    bound_args = []
    bound_kwargs = {}
    consume_list = [False] * len(parsed_arguments)
    for parameter in reflected_function.parameters:
        if parameter.kind == ParameterKind.PositionalOnly:
            bound_args.append(
                bind_positional_only(parameter, parsed_arguments, consume_list)
            )
        if parameter.kind == ParameterKind.PositionalOrKeyword:
            bound_args.append(
                bind_positional_or_keyword(parameter, parsed_arguments, consume_list)
            )
        if parameter.kind == ParameterKind.VarPositional:
            bound_args.extend(
                bind_var_positional(parameter, parsed_arguments, consume_list)
            )
        if parameter.kind == ParameterKind.KeywordOnly:
            key, value = bind_keyword_only(parameter, parsed_arguments, consume_list)
            bound_kwargs[key] = value
        if parameter.kind == ParameterKind.VarKeyword:
            bound_kwargs.update(
                bind_var_keyword(parameter, parsed_arguments, consume_list)
            )
    return BoundFunction(reflected_function, parsed_arguments, bound_args, bound_kwargs)
