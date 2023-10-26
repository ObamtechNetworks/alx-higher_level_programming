#!/usr/bin/python3
"""This module defines a class that calculates the radius of a cirle

"""


class MagicClass:
    """This creates a class with attributes of a radius

    Attributes:
        __radius (int): must be an integer

    """
    def __init__(self, radius=0):
        """initializes the class with a private attr(variable) 'raidus'

        Args:
            radius (int): must be an integer
        """
        self.__radius = radius
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        else:
            self.__radius = radius

    def area(self):
        """This method calculates the area of a circle

        Args:
            None

        Returns:
            returns the result for area of a circle

        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """This method calculates the value circumference of a circle

        Args:
            None

        Returns:
            returns the value of the circumference

        """
        return 2 * math.pi * self.__radius
