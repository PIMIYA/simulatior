from yaml import load

try:
    from yaml import SafeLoader as Loader
except ImportError:
    from yaml import Loader
from collections import namedtuple


def convert(obj):
    if isinstance(obj, dict):
        for key, value in obj.items():
            if isinstance(value, dict):
                obj[key] = convert(value)
            elif isinstance(value, list):
                obj[key] = [convert(i) for i in value]
            else:
                obj[key] = value
        return namedtuple('GenericDict', obj.keys())(**obj)
    elif isinstance(obj, list):
        for index, value in enumerate(obj, start=0):
            if isinstance(value, dict):
                obj[index] = convert(value)
            elif isinstance(value, list):
                obj[index] = [convert(i) for i in value]
            else:
                obj[index] = value
        return obj
    else:
        return obj


def yaml2obj(path):
    with open(path, 'r', encoding='utf-8') as stream:
        obj = load(stream, Loader=Loader)
        return convert(obj)
