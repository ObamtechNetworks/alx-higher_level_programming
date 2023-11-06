#!/usr/bin/python3
"""This module defines a function that checks if an obj is an instance
-- of a specified class
"""


def is_kind_of_class(obj, a_class):
    """this func check if an obj is an instance of
    a class or subclass (inherits from)

    Returns:
        True if true else False if false
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
