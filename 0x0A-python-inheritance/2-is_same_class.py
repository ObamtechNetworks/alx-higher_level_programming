#!/usr/bin/python3
"""This module defines a function that checks if an obj is an instance
-- of a specified class, returns the exact type of obj.
to use the type() func:
    Behavior: It returns the specific class type of the object,
    without considering subclasses.
"""


def is_same_class(obj, a_class):
    """checks an obj is an instance of a_class

    Returns:
        True if true else False if false
    """
    if not obj or not a_class:
        return False

    if type(obj) is a_class:
        return True
    else:
        return False
