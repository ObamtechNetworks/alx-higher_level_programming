#!/usr/bin/python3
"""This module defines a class represenation of a rectangle

It also have methods for calculating its area and perimeter
"""


class Rectangle:
    """This class respresents a rectangle

    Attributes:
        width (int): must be an integer
        height (int): must be an integer
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """width must be an integer, returns the width value

        setter is used to set the value
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height must be an integer, returns the width value

        setter is used to set the value
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ returns the area of a rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """
        This defines a nice string represenation of the class instances
        """
        str_s = ""
        for i in range(self.__height):
            for j in range(self.__width):
                str_s += '#'
            str_s += '\n'
        # remove last newline
        str_s = str_s[:-1]
        return str_s
