#!/usr/bin/python3
"""This module defines an empty class: "BaseGeometry
This would serve as the base class for next coming classes
added area instance method
"""


class BaseGeometry:
    """The base class for geometry objects
    """
    def area(self):
        """method for implementing area!"""
        raise Exception(f"{self.area.__name__}() is not implemented")

    def integer_validator(self, name, value):
        """method for integer validation"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """This class inherits from the BaseGeometry class
    """
    def __init__(self, width, height):
        """initalizes the instance attributes"""
        self.__width = width
        self.__height = height

        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)
