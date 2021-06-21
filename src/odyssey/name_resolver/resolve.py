from enum import IntFlag, unique, auto


@unique
class ResolveRule(IntFlag):
    DASHES_TO_UNDERSCORES = auto()
    UPPERCASE_TO_LOWERCASE = auto()


ResolveRule.DEFAULT = (
    ResolveRule.DASHES_TO_UNDERSCORES | ResolveRule.UPPERCASE_TO_LOWERCASE
)


def resolve_name(source, target, rule=ResolveRule.DEFAULT) -> bool:
    source_len = len(source)
    target_len = len(target)

    if source_len != target_len:
        return False

    if source == target:
        return True

    for source_character, target_character in zip(source, target):
        if source_character != target_character:
            if (
                rule & ResolveRule.DASHES_TO_UNDERSCORES
                and source_character == "-"
                and target_character == "_"
            ):
                continue

            if (
                rule & ResolveRule.UPPERCASE_TO_LOWERCASE
                and source_character.lower() == target_character
            ):
                continue

            return False

    return True


def convert_name(source, rule=ResolveRule.DEFAULT) -> bool:
    return "".join(
        [
            "_"
            if rule & ResolveRule.DASHES_TO_UNDERSCORES and source_character == "-"
            else source_character.lower()
            if rule & ResolveRule.UPPERCASE_TO_LOWERCASE and source_character.isupper()
            else source_character
            for source_character in source
        ]
    )


class NameResolver:
    def __init__(self, rule=ResolveRule.DEFAULT):
        self.rule = rule

    def resolve(self, source, target) -> bool:
        return resolve_name(source, target, self.rule)

    def convert(self, source) -> str:
        return convert_name(source, self.rule)
