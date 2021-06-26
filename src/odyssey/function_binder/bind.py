"""Functionality for binding a list of strings to a set of function parameters."""

import odyssey.type_converter.convert as convert
from odyssey.python_reflector.reflect import (
    Function,
    ParameterKind,
)
from odyssey.cli_parser.argument import ArgumentKind

# The rules herein determine how function parameters are parsed.
# We support positional only parameters. They must come before all positional var parameters. They can support annotated implicit conversion.
# We support positional + keyword parameters in either usage. They can appear in keyword form in any position. They can support annotated implicit conversion.
# We support positional var parameters. They must appear after all positional only parameters. They cannot support annotated implicit conversion.
# We support keyword only parameters. They can appear in any position. They can support annotated implicit conversion.
# We support keyword var parameters. They can appear in any position. They cannot support annotated implicit conversion.


class BoundParameter:
    def __init__(self, parsed_arguments, reflected_parameter, name=None, value=None):
        self.parsed_arguments = parsed_arguments
        self.reflected_parameter = reflected_parameter
        self.name = name
        self.value = value


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


def bind_positional_only(parameter, parsed_arguments: list):
    for argument in parsed_arguments:
        if argument.kind == ArgumentKind.Positional:
            return BoundParameter(
                parsed_arguments=[argument],
                reflected_parameter=parameter,
                value=argument.value,
            )

    raise Exception(
        f"No positional arguments available to bind to parameter {parameter.name}"
    )


def bind_positional_or_keyword(parameter, parsed_arguments: list, name_resolver):
    # First look for assignments
    for argument in parsed_arguments:
        if argument.kind == ArgumentKind.Assignment and name_resolver.resolve(
            argument.name, parameter.name
        ):
            return BoundParameter(
                parsed_arguments=[argument],
                reflected_parameter=parameter,
                value=argument.value,
            )

    # Next look for flags with positional values
    for index in range(len(parsed_arguments)):
        pass

    # Next look for positional values

    raise Exception(
        f"No positional arguments available to bind to parameter {parameter.name}"
    )


def bind_var_positional(parameter, parsed_arguments: list):
    result = list()
    for i in range(len(parsed_arguments)):
        argument = parsed_arguments[i]
        if argument.kind != ArgumentKind.Positional:
            continue
        result.append(
            BoundParameter(
                parsed_arguments=[argument],
                reflected_parameter=parameter,
                value=argument.value,
            )
        )

    return result


def bind_keyword_only(parameter, parsed_arguments: list, name_resolver):
    for i in range(len(parsed_arguments)):
        argument = parsed_arguments[i]
        if argument.kind == ArgumentKind.Assignment and name_resolver.resolve(
            argument.name, parameter.name
        ):
            return BoundParameter(
                parsed_arguments=[argument],
                reflected_parameter=parameter,
                name=parameter.name,
                value=argument.value,
            )

    raise Exception(f"No arguments available to bind to parameter {parameter.name}")


def bind_var_keyword(parameter, parsed_arguments: list, name_resolver):
    result = dict()
    for i in range(len(parsed_arguments)):
        argument = parsed_arguments[i]
        if argument.kind == ArgumentKind.Assignment:
            converted_name = name_resolver.convert(argument.name)
            result[converted_name] = BoundParameter(
                parsed_arguments=[argument],
                reflected_parameter=parameter,
                name=converted_name,
                value=argument.value,
            )

    return result


def bind_arguments(reflected_function: Function, parsed_arguments: list, name_resolver):
    arguments = parsed_arguments.copy()
    bound_args = []
    bound_kwargs = {}
    for parameter in reflected_function.parameters:
        if parameter.kind == ParameterKind.PositionalOnly:
            bound_parameter = bind_positional_only(parameter, arguments)
            bound_args.append(bound_parameter.value)

            for parsed_argument in bound_parameter.parsed_arguments:
                for index in [
                    i
                    for i in range(len(arguments))
                    if parsed_argument.id == arguments[i].id
                ]:
                    del arguments[index]
        if parameter.kind == ParameterKind.PositionalOrKeyword:
            bound_parameter = bind_positional_or_keyword(
                parameter, arguments, name_resolver
            )
            bound_args.append(bound_parameter.value)

            for parsed_argument in bound_parameter.parsed_arguments:
                for index in [
                    i
                    for i in range(len(arguments))
                    if parsed_argument.id == arguments[i].id
                ]:
                    del arguments[index]
        if parameter.kind == ParameterKind.VarPositional:
            bound_parameters = bind_var_positional(parameter, arguments)
            for bound_parameter in bound_parameters:
                bound_args.append(bound_parameter.value)

                for parsed_argument in bound_parameter.parsed_arguments:
                    for index in [
                        i
                        for i in range(len(arguments))
                        if parsed_argument.id == arguments[i].id
                    ]:
                        del arguments[index]
        if parameter.kind == ParameterKind.KeywordOnly:
            bound_parameter = bind_keyword_only(parameter, arguments, name_resolver)
            bound_kwargs[bound_parameter.name] = bound_parameter.value

            for parsed_argument in bound_parameter.parsed_arguments:
                for index in [
                    i
                    for i in range(len(arguments))
                    if parsed_argument.id == arguments[i].id
                ]:
                    del arguments[index]
        if parameter.kind == ParameterKind.VarKeyword:
            bound_var_keyword = bind_var_keyword(parameter, arguments, name_resolver)
            for name, bound in bound_var_keyword.items():
                bound_kwargs[name] = bound.value

                for parsed_argument in bound.parsed_arguments:
                    for index in [
                        i
                        for i in range(len(arguments))
                        if parsed_argument.id == arguments[i].id
                    ]:
                        del arguments[index]
    return BoundFunction(reflected_function, parsed_arguments, bound_args, bound_kwargs)
