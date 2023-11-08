#!/usr/bin/python3
"""
This module defines a function that:

Returns an object (python data structure) represented by a JSON str
"""

import json


def from_json_string(my_str):
    """returns an obj (python data structure)
    reprensented by a JSON string
    """
    # load the obj to a python object using the `load` json method
    python_obj = json.loads(my_str)

    # return the object representation
    return python_obj
