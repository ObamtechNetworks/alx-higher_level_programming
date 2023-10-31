#!/usr/bin/python3
"""This module defines a function that adds 2 integers

>>> add_integer(2, 5)
    7
"""


def add_integer(a, b=98):
    """Return the sum of two integers a, b

    Args:
        a (int): an integer or float
        b (int): must be an integer or float

    Returns:
        result: sum of a + b

    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    result = a + b

    return result
