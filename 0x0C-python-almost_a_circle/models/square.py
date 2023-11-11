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

    def __str__(self):
        """prints str representation of Square"""
        return "[{}] ({}) {}/{} - {}".\
               format(type(self).__name__,
                      self.id, self.x,
                      self.y, self.size)
