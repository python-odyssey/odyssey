from enum import (
    IntFlag,
    unique,
    auto
)

@unique
class ResolveRule(IntFlag):
    DASHES_TO_UNDERSCORES = auto()
    UPPERCASE_TO_LOWERCASE = auto()

ResolveRule.DEFAULT = ResolveRule.DASHES_TO_UNDERSCORES | ResolveRule.UPPERCASE_TO_LOWERCASE
