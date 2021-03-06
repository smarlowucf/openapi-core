"""OpenAPI core schemas util module"""
from distutils.util import strtobool
from json import dumps
from six import string_types


def forcebool(val):
    if isinstance(val, string_types):
        val = strtobool(val)

    return bool(val)


def dicthash(d):
    return hash(dumps(d, sort_keys=True))
