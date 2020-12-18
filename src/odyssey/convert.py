import json


def to_string(value):
    if isinstance(value, (int, float, complex)):
        return str(value)
    if isinstance(value, (tuple, list, dict, bool)):
        return json.dumps(value)
    return value


def to_int(string):
    return int(string)


def to_float(string):
    return float(string)


def to_complex(string):
    return complex(string)


def to_bool(string):
    return string.lower() in ("true", "1", "yes")


def to_tuple(string):
    return tuple(json.loads(string))


def to_list(string):
    return json.loads(string)


def to_dict(string):
    return json.loads(string)


def from_string_to(typeinfo, string):
    if typeinfo is str:
        return string
    if typeinfo is int:
        return to_int(string)
    if typeinfo is float:
        return to_float(string)
    if typeinfo is complex:
        return to_complex(string)
    if typeinfo is bool:
        return to_bool(string)
    if typeinfo is tuple:
        return to_tuple(string)
    if typeinfo is list:
        return to_list(string)
    if typeinfo is dict:
        return to_dict
