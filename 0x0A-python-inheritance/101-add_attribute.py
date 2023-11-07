#!/usr/bin/python3
"""This module defiens a function that adds a new attribute
to an object if it's possible
"""


def add_attribute(obj, attr, value):
    """A function that adds attr to an object
    calss the setatrr func
    """
    if hasattr(obj, '__dict__'):  # chk if obj is an instance of a class
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")
