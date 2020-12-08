from sys import version_info


def simplest_function():
    pass


def string_function() -> str:
    return "string"


def identity_function(value):
    return value


if version_info.major >= 3 and version_info.minor >= 7:

    def parameter_kind_function(
        positional_only,
        /,
        positional_or_keyword,
        *var_positional,
        keyword_only,
        **var_keyword,
    ):
        return (
            positional_only,
            positional_or_keyword,
            *var_positional,
            keyword_only,
            var_keyword,
        )


else:

    def parameter_kind_function(
        positional_or_keyword, *var_positional, keyword_only, **var_keyword,
    ):
        return (
            positional_or_keyword,
            *var_positional,
            keyword_only,
            var_keyword,
        )
