#!/usr/bin/python3
"""This module defines an empty class: "BaseGeometry
This would serve as the base class for next coming classes
added area instance method
added integer_validator
added a subclass Rectangle
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This class inherits from the BaseGeometry class
    """
    def __init__(self, width, height):
        """initalizes the instance attributes"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """overrides base class' area and implements area calc"""
        return self.__width * self.__height

    def __str__(self):
        """returns a nicely formatted string"""
        return f"[{type(self).__name__}] {self.__width}/{self.__height}"
