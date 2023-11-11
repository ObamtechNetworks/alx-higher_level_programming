#!/usr/bin/python3
"""Unittest for rectangle class"""


import unittest
# import the rectangle class
from models.rectangle import Rectangle
from models.base import Base


# setup the test cases

class TestRectangle(unittest.TestCase):
    """creates different test cases (methods) for the rectangle cls"""
    def setUp(self):
        """this method is called before each test case"""
        # reset the id so as to properly set the __nb_objects of the base
        Base._Base__nb_objects = 0
    
    def test_constructor_with_id(self):
        """tests instances with ids"""
        rectangle = Rectangle(width=5, height=10, id=1)
        self.assertEqual(rectangle.width, 5)
        self.assertEqual(rectangle.height, 10)
        self.assertEqual(rectangle.x, 0)
        self.assertEqual(rectangle.y, 0)

    def test_constructor_without_id(self):
        """tests instances without ids,
        __nb_objects should assign correctly
        """
        rectangle = Rectangle(width=3, height=8)
        self.assertEqual(rectangle.id, 1)  # id is generated automat.
        self.assertEqual(rectangle.width, 3)
        self.assertEqual(rectangle.height, 8)
        self.assertEqual(rectangle.x, 0)
        self.assertEqual(rectangle.y, 0)

    def test_attr_setters_getters(self):
        """tests setters and getters for all attributes"""
        rectangle = Rectangle(width=5, height=10)
        rectangle.width = 15
        rectangle.height = 20
        rectangle.x = 3
        rectangle.y = 4

        self.assertEqual(rectangle.width, 15)
        self.assertEqual(rectangle.height, 20)
        self.assertEqual(rectangle.x, 3)
        self.assertEqual(rectangle.y, 4)

    def test_nb_objects(self):
        """tests how many objects created per instance"""
        rect1 = Rectangle(width=2, height=3)
        rect2 = Rectangle(0, 0)
        rect2.width = 3
        rect2.height = 6
        rect3 = Rectangle(1, 2, 0, 0)

        # test rect1
        self.assertEqual(rect1.width, 2)
        self.assertEqual(rect1.height, 3)
        self.assertEqual(rect1.x, 0)
        self.assertEqual(rect1.y, 0)

        # test rect2
        self.assertEqual(rect2.width, 3)
        self.assertEqual(rect2.height, 6)
        self.assertEqual(rect2.x, 0)
        self.assertEqual(rect2.y, 0)

        # test rect3
        self.assertEqual(rect3.width, 1)
        self.assertEqual(rect3.height, 2)
        self.assertEqual(rect3.x, 0)
        self.assertEqual(rect3.y, 0)

        # test total number of objects
        self.assertEqual(Base._Base__nb_objects, 3)

if __name__ == '__main__':
    unittest.main()
