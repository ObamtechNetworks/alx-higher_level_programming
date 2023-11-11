#!/usr/bin/python3
"""This module defines a class that demonstrate the representation
of a square

the square inherits from the rectangle class
"""


from models.rectangle import Rectangle
from models.base import Base


class Square(Rectangle):
    """a representation of a Square object"""

    def __init__(self, size, x=0, y=0, id=None):
        """initializes the class attributes"""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """returns the value of size"""
        return self.__size

    @size.setter
    def size(self, value):
        if not type(value) is int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        # set width and height with the same value
        self.width = value
        self.heigth = value
        self.__size = value

    def __str__(self):
        """prints str representation of Square"""
        return "[{}] ({}) {}/{} - {}".\
               format(type(self).__name__,
                      self.id, self.x,
                      self.y, self.size)
