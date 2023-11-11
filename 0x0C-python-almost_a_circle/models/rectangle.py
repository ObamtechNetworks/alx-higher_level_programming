#!/usr/bin/python3
"""This module defines a class `Rectangle` that inherits from `Base`"""


# import the base class
from models.base import Base


class Rectangle(Base):
    """This class inherits from the base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initializes the class attributes"""
        # call the base class constructor to set the id attribute
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    # define getters and setters for the attributes
    @property
    def width(self):
        """returns the value for the width attribute
        the width value is defined by the width.setter method
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not type(value) is int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """returns the value for the height attribute
        the height value is defined by the height.setter method
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not type(value) is int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """returns the value for the 'x' attribute
        this value is defined by the x.setter method
        """
        return self.__x

    @x.setter
    def x(self, value):
        if not type(value) is int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """returns the value for the 'y' attribute
        this value is defined by the y.setter method
        """
        return self.__y

    @y.setter
    def y(self, value):
        if not type(value) is int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """computes the area of the rectangle class"""
        return self.__width * self.__height

    def display(self):
        """prints to the stdout the Rectangle instance with char #"""
        for _ in range(self.y):
            print('')
        for _ in range(self.height):
            print(' ' * self.x, end='')
            for _ in range(self.width):
                print('#', end='')
            print()

    def __str__(self):
        """prints a nicely formatted string representation"""
        return "[{}] ({}) {}/{} - {}/{}".\
               format(type(self).__name__, self.id,
                      self.x, self.y, self.width,
                      self.height)

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute
        1st argument is set to be the id attribute
        2nd arg is set to be the width attribute
        3rd arg is set to be the height attribute
        4th arg is set to be the x attribute
        5th arg is set to be teh y attribute
        """
        attributes = ['id', 'width', 'height', 'x', 'y']

        # set the attributes using the setattr function
        if len(args) >= 1:
            for index, value in enumerate(args):
                setattr(self, attributes[index], value)
        else:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)
