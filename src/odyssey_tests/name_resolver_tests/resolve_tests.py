import pytest
from odyssey.name_resolver.resolve import (
    ResolveRule,
    resolve_name,
    convert_name,
)


def test_resolve_name_different_length():
    source = "positional"
    target = "positional_or_keyword"

    result = resolve_name(source, target)

    assert not result


def test_resolve_name_equal():
    source = "positional_or_keyword"
    target = "positional_or_keyword"

    result = resolve_name(source, target)

    assert result


def test_resolve_name_dashes():
    source = "positional-or-keyword"
    target = "positional_or_keyword"

    result = resolve_name(source, target)

    assert result


def test_resolve_name_uppercase():
    source = "Positional_Or_Keyword"
    target = "positional_or_keyword"

    result = resolve_name(source, target)

    assert result


def test_resolve_name_dashes_and_uppercase():
    source = "Positional-Or-Keyword"
    target = "positional_or_keyword"

    result = resolve_name(source, target)

    assert result


def test_convert_name_dashes_and_uppercase():
    source = "Positional-Or-Keyword"
    expected = "positional_or_keyword"

    result = convert_name(source)

    assert result == expected
