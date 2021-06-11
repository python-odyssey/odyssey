from odyssey.cli_parser.pattern import PatternStyle, match
from odyssey.cli_parser.argument import make_argument_list

def parse_arguments(arguments, style=PatternStyle.DEFAULT):
    return make_argument_list(match(style, arguments))
