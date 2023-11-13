#!/usr/bin/python3
"""Unittest for `base.py`
"""


import unittest
import json
import csv
import turtle
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase_id_instances(unittest.TestCase):
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
        """test other types"""
        # string
        obj_1 = Base("str")
        self.assertEqual(obj_1.id, 'str')

        # float
        obj_2 = Base(4.33)
        self.assertEqual(obj_2.id, 4.33)
        # check the total __nb_objects
        self.assertEqual(Base._Base__nb_objects, 0)

        # list
        r1 = Base([])
        self.assertEqual(r1.id, [])

        # tuples
        r1 = Base((1, 2, 3))
        self.assertEqual(r1.id, (1, 2, 3))

        # sets
        r1 = Base({1, 2,})
        self.assertEqual(r1.id, {1, 2})

        # frozensets
        r1 = Base(frozenset({1, 2, 3}))
        self.assertEqual(frozenset({1, 2, 3}), r1.id)

        # bool
        r1 = Base(True)
        self.assertEqual(r1.id, True)

        # dict
        r1 = Base({'name': 'John', 'age': 24})
        self.assertEqual(r1.id, {'name': 'John', 'age': 24})

        # complex
        r1 = Base(complex(2, 3))
        self.assertEqual(r1.id, complex(2, 3))

        # bytearray
        r1 = Base(b'hello')
        self.assertEqual(r1.id, b'hello')

        # memoryview object
        r1 = Base(memoryview(b'hello'))
        self.assertEqual(r1.id, memoryview(b'hello'))

        # infinity, positive and negatives, nan
        r1 = Base(float('inf'))
        self.assertEqual(r1.id, float('inf'))

        r1 = Base(float('-inf'))
        self.assertEqual(r1.id, float('-inf'))

        r1 = Base(float('nan'))
        self.assertNotEqual(r1.id, float('nan'))

        # range(3)
        r1 = Base(range(3))
        self.assertEqual(r1.id, range(3))

        # test negative ids
        r1 = Base(-1)
        self.assertEqual(r1.id, -1)

    def test_too_many_args(self):
        """test too many arguments as ids"""
        with self.assertRaises(TypeError):
            r1 = Base(1, 2, 3)

    def test_instance_id_zero(self):
        """test initializing an instance with id=0"""
        r1 = Base(0)
        self.assertEqual(r1.id, 0)

class TestBase_to_json_string(unittest.TestCase):
    """tests units for the to_json_string method"""
    # Rectangle
    def test_to_json_string_rectangle(self):
        """test the to_json_string with rectangles"""
        # test to_dictionary and to_json_string
        r1 = Rectangle(10, 7, 2, 8)
        my_dict = r1.to_dictionary()
        json_dictionary = Base.to_json_string([my_dict])
        self.assertEqual(json_dictionary, Base.to_json_string([my_dict]))
    def test_type_to_json_string_rectangle(self):
        """test the type of data after call on to_json_string"""
        r1 = Rectangle(1, 2, 3, 4)
        my_dict_list = [r1.to_dictionary()]
        self.assertEqual(str, type(Base.to_json_string([my_dict_list])))

    def test_len_to_json_string_rectangle_one_dict(self):
        """test length of json string"""
        r1 = Rectangle(10, 7, 2, 8, 6)
        my_dict_list = [r1.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(my_dict_list)) == 53)
    def test_to_json_string_rectangle_two_dicts(self):
        """tests len of two rectangle json_dicts """
        r1 = Rectangle(2, 3, 5, 19, 2)
        r2 = Rectangle(4, 2, 4, 1, 12)
        list_dicts = [r1.to_dictionary(), r2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 106)
    # Square
    def test_to_json_string_square(self):
        """test correct output json string square"""
        s1 = Square(10, 2, 3, 4)
        s_dict = [s1.to_dictionary()]
        s_json_str = Base.to_json_string(s_dict)
        self.assertEqual(Base.to_json_string(s_dict), s_json_str)

    def test_type_to_json_string_square(self):
        """tests type of data for square instance 
        after after call to_json_string
        """
        s1 = Square(10, 2, 3, 4)
        lists_dict = [s1.to_dictionary()]
        self.assertEqual(str, type(Base.to_json_string(lists_dict)))
    def test_len_to_json_string_square_one_dict(self):
        """test length of one square dict"""
        s1 = Square(10, 2, 3, 4)
        s_json_dict = Base.to_json_string([s1.to_dictionary()])
        self.assertTrue(len(s_json_dict) == 39)

    def test_to_json_string_square_two_dicts(self):
        """tests len of two square json_dicts """
        s1 = Square(1, 4, 3, 3)
        s2 = Square(10, 2, 3, 4)
        list_dicts = [s1.to_dictionary(), s2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 77)

    def test_to_json_string_with_empty_list(self):
        """test square to_json sring with empty list"""
        self.assertEqual("[]", Base.to_json_string([]))

    def test_to_json_string_with_none_arg(self):
        """test with None as arg"""
        self.assertEqual("[]", Base.to_json_string(None))

    def test_to_json_string_no_arguments(self):
        """test with no arguments"""
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_too_many_args(self):
        """test Base.to_json_string() with too many args"""
        with self.assertRaises(TypeError):
            Base.to_json_string(["{id: 1, x:2}"], 2, 3)


if __name__ == '__main__':
    unittest.main()
