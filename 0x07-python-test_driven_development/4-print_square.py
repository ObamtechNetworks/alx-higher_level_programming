#!/usr/bin/python3
"""
This module defines a function that prints a square with character '#'

Prototype: def print_square(size):
- size is the size lenghth of the square
- size must be an integer, else a TypeError exception is raised
- if size < 0, ValueError is raised

Returns:
    None

"""


def print_square(size):
    """
    This function prints a square with the character '#'

    Args:
        size (int): must be an integer and must be > 0

    Returns:
        None
    """

    # case 1: check type of size if an integer
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    # case 2: check type of size if float and < 0
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    # case 3: check value of size if int but < 0
    if size < 0:
        raise ValueError("size must be >= 0")

    # CORRECT OUTPUT IMPLEMENTATION
    for i in range(size):
        print('#' * size)
