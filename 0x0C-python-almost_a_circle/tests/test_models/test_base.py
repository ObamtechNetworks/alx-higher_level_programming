#!/usr/bin/python3
"""Unittest for `base.py`
"""


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """creates tests cases and runs the test cases"""
    def setUp(self):
        """this method is called before each test method"""
        # reset the nb_objects attribute before each test
        Base._Base__nb_objects = 0
        pass

    def tearDown(self):
        """this method is called after each test method"""
        pass

    def test_instance_with_id(self):
        """tests if the __init__ method initializes
        the id attribute correctly
        """
        obj = Base(id=5)
        self.assertEqual(obj.id, 5)

    def test_instance_without_id(self):
        """tests if the __nb_objects attribute increments correctly"""
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

    def test_nb_objects_increment(self):
        """tests if the __nb_objects attr increments correctly"""
        my_obj1 = Base()
        my_obj2 = Base()
        new_obj = Base()
        self.assertEqual(Base._Base__nb_objects, 3)

    def test_None_as_arg(self):
        """tests if None was passed as id"""
        new_obj = Base(None)
        self.assertEqual(Base._Base__nb_objects, 1)

    def test_other_data_types(self):
        """test other invalid types"""
        obj_1 = Base("str")
        self.assertEqual(obj_1.id, 'str')
        obj_2 = Base(4.33)
        self.assertEqual(obj_2.id, 4.33)
        # check the total __nb_objects
        self.assertEqual(Base._Base__nb_objects, 0)

if __name__ == '__main__':
    unittest.main()
