#!/usr/bin/python3
"""Unittest for rectangle class"""


import unittest
import sys
import io
import csv

# import the rectangle class
from models.rectangle import Rectangle
from models.base import Base


# setup the test cases

class TestRectangle_instantiation(unittest.TestCase):
    """tests rectangle instance and instantiation of Base class"""
    def test_rect_is_base_instance(self):
        """test if it's an instance of base"""
        self.assertIsInstance(Rectangle(1, 2), Base)

    def test_no_arguments(self):
        """test rectangle with no argument"""
        with self.assertRaises(TypeError):
            Rectangle()

    def test_rect_with_one_arg(self):
        """test rectangle with one argument"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(1)

    def test_rect_with_two_args_width(self):
        """test rectangle with two arguments"""
        r1 = Rectangle(1, 2)
        self.assertEqual(r1.width, 1)

    def test_rect_with_two_args_height(self):
        """test rectangle with two arguments"""
        r1 = Rectangle(1, 2)
        self.assertEqual(r1.height, 2)

    def test_rect_with_three_args_x(self):
        """test rectangle with two arguments"""
        r1 = Rectangle(1, 2, 3)
        self.assertEqual(r1.x, 3)
    
    def test_rect_with_four_args_y(self):
        """test rectangle with two arguments"""
        r1 = Rectangle(1, 2, 3, 4)
        self.assertEqual(r1.y, 4)

    def test_rect_with_five_args_id(self):
        """test rectangle with two arguments"""
        r1 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r1.id, 5)

    def test_rect_too_many_args(self):
        """test rectangle with two arguments"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 2, 3, 4, 5, 6)

class TestRectangle_private_attribute(unittest.TestCase):
    """test AttributeError exceptions with private attributes"""
    def test_private_attr_width(self):
        """test accessing of private attribute - width"""
        with self.assertRaises(AttributeError):
            r1 = Rectangle(1, 2, 3, 4, 5)
            print(r1.__width)
    
    def test_private_attr_height(self):
        """test accessing of private attribute - height"""
        with self.assertRaises(AttributeError):
            r1 = Rectangle(1, 2, 3, 4, 5)
            print(r1.__height)

    def test_private_attr_x(self):
        """test accessing of private attribute - x"""
        with self.assertRaises(AttributeError):
            r1 = Rectangle(1, 2, 3, 4, 5)
            print(r1.__x)

    def test_private_attr_y(self):
        """test accessing of private attribute - y"""
        with self.assertRaises(AttributeError):
            r1 = Rectangle(1, 2, 3, 4, 5)
            print(r1.__y)

class TestRectangle_setters_getters(unittest.TestCase):
    """test if setters and getters are working rightly"""
    
    def test_attr_setters_width(self):
        """tests setters width"""
        r = Rectangle(width=5, height=10)
        r.width = 15
        self.assertEqual(r.width, 15)
    
    def test_attr_setters_height(self):
        """tests setters height"""
        r = Rectangle(width=5, height=10)
        r.height = 20
        self.assertEqual(r.height, 20)
    
    def test_attr_setters_x(self):
        """tests setters x"""
        r = Rectangle(width=5, height=10)
        r.x = 3
        self.assertEqual(r.x, 3)
    
    def test_attr_setters_y(self):
        """tests setters y"""
        r = Rectangle(width=5, height=10)
        r.y = 4
        self.assertEqual(r.y, 4)

    def test_attr_getter_width(self):
        """tests getters width"""
        r = Rectangle(5, 10)
        self.assertEqual(r.width, 5)
    
    def test_attr_getter_height(self):
        """tests getters height"""
        r = Rectangle(5, 10)
        self.assertEqual(r.height, 10)
    
    def test_attr_getters_x(self):
        """tests getters x"""
        r = Rectangle(5, 10, 3)
        self.assertEqual(r.x, 3)
    
    def test_attr_getters_y(self):
        """tests getters y"""
        r = Rectangle(5, 10, 3, 4)
        self.assertEqual(r.y, 4)

class TestRectangle_width_values(unittest.TestCase):
    """test width instantiation with different data types"""

    def test_None_as_width_value(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 10)


    def test_str_as_width_value(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("my string", 15)


    def test_float_as_width(self):
         with self.assertRaisesRegex(TypeError, "width must be an integer"):
             Rectangle(3.335, 18)


    def test_complex_as_width_value(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(complex(2, 3), 10)


    def test_dict_as_width_value(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"id1":7, "id2":6}, 35)


    def test_set_as_width_value(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({2, 4, 6}, 8)


    def test_list_as_width_value(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([3, 5, 7], 9)


    def test_range_as_width_value(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(range(4), 8)


    def test_tuple_as_width_value(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((6, 8, 10), 12)


    def test_frozen_set_as_width_value(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(frozenset({1, 5, 4, 8}), 4)


    def test_bytes_as_width_value(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(b'unittesting', 9)


    def test_bytearray_as_width_value(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(bytearray(b'bytes'), 8)


    def test_memoryview_as_width_value(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(memoryview(b'unittests'), 13)


    def test_positive_inf_width_as_value(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('inf'), 4)

    def test_neg_inf_width_as_value(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('-inf'), 6)


    def test_nan_as_width_value(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('nan'), 6)


    def test_neg_width_value(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-5, 2)


    def test_zero_as_width_value(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 9)

class TestRectangle_height_values(unittest.TestCase):
    """tests height instantiation with different data types"""

    def test_None_as_height_value(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, None)


    def test_str_as_height_value(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(15, "my string")


    def test_float_as_width(self):
         with self.assertRaisesRegex(TypeError, "height must be an integer"):
             Rectangle(5, 3.335)


    def test_complex_as_height_value(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, complex(2, 3))


    def test_dict_as_height_value(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, {"id1":7, "id2":6})


    def test_set_as_height_value(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(8, {2, 4, 6})


    def test_list_as_height_value(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, [3, 5, 7])


    def test_range_as_height_value(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(8, range(4))


    def test_tuple_as_height_value(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(12, (6, 8, 10))


    def test_frozen_set_as_height_value(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, frozenset({1, 5, 4, 8}))


    def test_bytes_as_height_value(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, b'unittesting')


    def test_bytearray_as_height_value(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, bytearray(b'bytes'))


    def test_memoryview_as_height_value(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, memoryview(b'unittests'))


    def test_positive_inf_height_as_value(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, float('inf'))

    def test_neg_inf_height_as_value(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(6, float('-inf'))


    def test_nan_as_height_value(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(6, float('nan'))


    def test_neg_height_value(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(2, -5)

class TestRectangle_x_values(unittest.TestCase):
    """tests x instantiation with different data types"""

    def test_None_as_x_value(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 10, None)


    def test_str_as_x_value(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 15, "my string")


    def test_x_as_width(self):
         with self.assertRaisesRegex(TypeError, "x must be an integer"):
             Rectangle(3, 5, 3.335)


    def test_x_as_height_value(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 10, complex(2, 3))


    def test_dict_as_x_value(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 3, {"id1":7, "id2":6})


    def test_set_as_x_value(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 8, {2, 4, 6})


    def test_list_as_x_value(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 3, [3, 5, 7])


    def test_range_as_x_value(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 8, range(4))


    def test_tuple_as_x_value(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 12, (6, 8, 10))


    def test_frozen_set_as_x_value(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 3, frozenset({1, 5, 4, 8}))


    def test_bytes_as_x_value(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 3, b'unittesting')


    def test_bytearray_as_x_value(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(5, 3, bytearray(b'bytes'))


    def test_memoryview_as_x_value(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(6, 2, memoryview(b'unittests'))


    def test_positive_inf_as_x_value(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 4, float('inf'))

    def test_neg_inf_height_as_x_value(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(5, 6, float('-inf'))


    def test_nan_as_x_value(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(5, 6, float('nan'))


    def test_neg_x_value(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(3, 2, -5)


    def test_zero_as_x_value(self):
        self.assertEqual(Rectangle(9, 3, 0).x, 0)

class TestRectangle_y_values(unittest.TestCase):
    """tests y instantiation with different data types"""

    def test_None_as_y_value(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 10, 2, None)


    def test_str_as_y_value(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 15, 3, "my string")


    def test_y_as_width(self):
         with self.assertRaisesRegex(TypeError, "y must be an integer"):
             Rectangle(3, 5, 4, 3.335)


    def test_y_as_height_value(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 10, 3, complex(2, 3))


    def test_dict_as_y_value(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 3, 4, {"id1":7, "id2":6})


    def test_set_as_y_value(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 8, 3, {2, 4, 6})


    def test_list_as_y_value(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 3, 3, [3, 5, 7])


    def test_range_as_y_value(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 8, 3, range(4))


    def test_tuple_as_y_value(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 12, 3, (6, 8, 10))


    def test_frozen_set_as_y_value(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 3, 2, frozenset({1, 5, 4, 8}))


    def test_bytes_as_y_value(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 3, 3, b'unittesting')


    def test_bytearray_as_y_value(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 3, 3, bytearray(b'bytes'))


    def test_memoryview_as_y_value(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(6, 2, 3, memoryview(b'unittests'))


    def test_positive_inf_as_y_value(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 4, 3, float('inf'))

    def test_neg_inf_height_as_y_value(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 6, 3, float('-inf'))


    def test_nan_as_y_value(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 6, 3, float('nan'))


    def test_neg_y_value(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(3, 2, 2, -5)


    def test_zero_as_y_value(self):
        self.assertEqual(Rectangle(9, 3, 0, 0).y, 0)

class TestRectangle_id(unittest.TestCase):
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

    def test_nb_objects(self):
        """tests how many objects created per instance"""
        rect1 = Rectangle(width=2, height=3)
        rect2 = Rectangle(2, 1)
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

    def test_str_as_id(self):
        """tests str as id"""
        r1 = Rectangle(1, 2, 0, 0, 'str')
        self.assertEqual(r1.id, 'str')

if __name__ == '__main__':
    unittest.main()
