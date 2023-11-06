#!/usr/bin/python3
"""this module defines a func that checks if an obj is a subclass
of a given class (directly or indirect inheritance)

Returns:
    True if a subclass else False
"""


def inherits_from(obj, a_class):
    """this func checks if an obj is a subclass or instance
    of a given class

    Returns:
        True if true, else False if false
    """

    if isinstance(obj, a_class) and not type(obj) is a_class:
        return True
    else:
        return False
