#!/usr/bin/python3
"""This module defines a func that rtns the list of all avail.
attr and methods of an object

Returns:
    all available attr and method of object
"""


def lookup(obj):
    """this func rtrns list of all avail attr and methods of an obj

    Args:
        obj (:obj:): an object

    Returns:
        all available attr and methods of the given obj parameter
    """

    if obj is None:
        return None
    if not isinstance(obj, type):
        raise TypeError("argument must be an object")

    return [el for el in dir(obj)]
