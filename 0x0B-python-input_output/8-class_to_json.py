#!/usr/bin/python3
"""
This module defines a function that returns the
dictioinary description of a class object
"""


def class_to_json(obj):
    """This function returns the dictionary description of a class obj
    it considers only the follwing data structures
    ``list, dictionary, string, integer and boolean``
    ... for a JSON serialization of an object

    Returns:
        the dictionary description of the class
    """
    # check if obj is an instance of a class
    if not isinstance(obj, object):
        return None

    # initialize an empty dict for obj attributes
    obj_attr = {}

    # loop thru the dict obj and retrieve only stated data structure above
    for key, value in obj.__dict__.items():
        # verify if attribute is serializable
        if isinstance(value, (list, dict, str, int, bool)):
            obj_attr[key] = value
        elif hasattr(value, '__dict__'):  # chk if value is a class inst
            obj_attr[key] = class_to_json(value)  # Recursively serialzie
        else:
            raise TypeError(f"Type {type(value)} is not serializable")

    # return a dict of the collected obj attribute
    return obj_attr
