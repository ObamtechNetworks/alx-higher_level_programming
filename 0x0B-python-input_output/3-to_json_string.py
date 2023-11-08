#!/usr/bin/python3
"""This function returns the JSON representation of an object (string)
"""


import json


def to_json_string(obj):
    """returns the JSON repre. of the given object
    """
    return json.dumps(obj)
