#!/usr/bin/python3
"""This module defines a class Square class

Privatize the class instance attribute: size
size is optionally initialized to 0
size is strictly meant to be an integer else a TypeError is raised
Also, value of size must not be < 0, else a ValueError is raised

A property setter and getter is implemented
This is necessary to control the type and value passed to the instances

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

    @property
    def size(self):
        """int: returns the class instance/object size property

        setter sets the value of the size data attribute
        """
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            self.__size = value
        else:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """This method computes the area of a given class instance/object

        Args:
            None

        Returns:
            returns the area of the current square object/instance

        """
        return self.__size * self.__size
