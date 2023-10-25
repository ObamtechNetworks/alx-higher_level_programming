#!/usr/bin/python3
"""This module defines a class Square based on a previous class

It also privatize the class instance attribute: size

"""


class Square:
    """Defines a class Square based

    Sets a private instance attribute: size
    Instantiation with size (no type/value verification)

    Attributes:
        __size (int): the size of the square
    """

    def __init__(self, size):
        """initializes the class with a private size attr

        The init method is for initializing the size attr of the class

        Args:
        size (int): an integer indicating size of the square

        """
        self.__size = size
