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
        __position (tuple): must be a tuple of two positive integers
    """

    def __init__(self, size=0, position=(0, 0)):
        """initializes the class with a private __size attr

        Args:
            size (int): must be integer indicating size of the square
            position (:obj: `tuple`): must be a tuple of two positive integers

        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """:obj: `tuple`: returns a tuple object of two positive integers

        setter sets the value fo the position obj data attribute

        """
        return self.__position

    @position.setter
    def position(self, value):
        if ((not isinstance(value, tuple)) and len(value) != 2) \
                and any(not isinstance(elem, int) for elem in value):
            raise TypeError(
                    "position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """This method computes the area of a given class instance/object

        Args:
            None

        Returns:
            returns the area of the current square object/instance

        """
        return self.__size * self.__size

    def my_print(self):
        """This method prints in stdout the square with the char '#'

        If size is == 0, an empty line is printed

        Args:
            None

        Returns:
            None
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + self.__size * '#')
