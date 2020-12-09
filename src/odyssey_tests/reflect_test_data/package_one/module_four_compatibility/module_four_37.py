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
