from odyssey.reflect import (
    ReflectedParameter,
    ParameterKind,
)


positional_only_parameter = ReflectedParameter(
    parameter=None,
    name="first_parameter",
    annotation=ReflectedParameter.empty_annotation,
    default=ReflectedParameter.empty_annotation,
    kind=ParameterKind.PositionalOnly,
)


positional_or_keyword_parameter = ReflectedParameter(
    parameter=None,
    name="first_parameter",
    annotation=ReflectedParameter.empty_annotation,
    default=ReflectedParameter.empty_annotation,
    kind=ParameterKind.PositionalOrKeyword,
)


var_positional_parameter = ReflectedParameter(
    parameter=None,
    name="var_parameter",
    annotation=ReflectedParameter.empty_annotation,
    default=ReflectedParameter.empty_annotation,
    kind=ParameterKind.VarPositional,
)


keyword_only_parameter = ReflectedParameter(
    parameter=None,
    name="keyword_only_parameter",
    annotation=ReflectedParameter.empty_annotation,
    default=ReflectedParameter.empty_annotation,
    kind=ParameterKind.KeywordOnly,
)


var_keyword_parameter = ReflectedParameter(
    parameter=None,
    name="var_keyword_parameter",
    annotation=ReflectedParameter.empty_annotation,
    default=ReflectedParameter.empty_annotation,
    kind=ParameterKind.VarKeyword,
)


def simple_function():
    pass


def parameter_type_function(positional_or_keyword, *var_positional, keyword_only, **var_keyword):
    return {
        "positional_or_keyword": positional_or_keyword,
        "var_positional": var_positional,
        "keyword_only": keyword_only,
        "var_keyword": var_keyword
    }