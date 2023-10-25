#!/usr/bin/python3
"""This module defines a class Square class

It also privatize the class instance attribute: size

"""


class Square:
    """Defines a class 'Square'

    Sets a private instance attribute: size
    Instantiation w/t opt. size: def __init__(self, size=0):

    Attributes:
        __size (int): the size of the square (must be an integer)
    """

    def __init__(self, size=0):
        """initializes the class with a private __size attr

        Args:
        size (int): must be integer indicating size of the square

        """
        self.__size = size
        if isinstance(size, int):
            pass
        else:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
