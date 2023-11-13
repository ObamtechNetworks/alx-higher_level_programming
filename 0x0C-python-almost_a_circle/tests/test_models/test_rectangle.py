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

class TestRectangle_order_of_init_values(unittest.TestCase):
    """test order of attributes initalization"""

    def test_invalid_width_before_x(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid width value", 4, "invalid x")


    def test_invalid_width_before_y(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid width value", 2, 4, "invalid y")


    def test_invalid_height_before_x(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, "invalid height value", "invalid x")


    def test_invalid_height_before_y(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "invalid height value", 2, "invalid y")


    def test_invlaid_x_before_y(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "invalid x value", "invalid y value")

    def test_invlaid_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, "invalid y value")

class TestRectangle_area(unittest.TestCase):
    """test area method of the Rectangle class"""

    def test_area_small(self):
        rect = Rectangle(3, 6, 3, 2, 3)
        self.assertEqual(18, rect.area())

    def test_area_large(self):
        rect = Rectangle(999999999999999, 999999999999999999, 0, 0, 12)
        self.assertEqual(999999999999998999000000000000001, rect.area())

    def test_area_changed_height_width(self):
        rect = Rectangle(3, 2, 0, 0, 33)
        rect.width = 8
        rect.height = 6
        self.assertEqual(48, rect.area())

    def test_area_with_arg(self):
        rect = Rectangle(8, 6, 2, 3, 90)
        with self.assertRaises(TypeError):
            rect.area(1)

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

class TestRectangle_str_and_display(unittest.TestCase):
    """Unittests for str method and display method"""

    @staticmethod
    def output(rect, method):
        """captures and return text output from a Rectangle's display method

        Args:
            rect (Rectangle): The Rectangle to capture output from
            method (str): The method to use for displaying
            ('print' or 'display')

        Returns:
            str: a string - The captured text output.
        """
        # create a stringIO object
        output = io.StringIO()
        
        # Redirect stdout to the StringIO buffer
        sys.stdout = output

        # Choose the appropriate display method based on the input
        if method == "print":
            # use the 'print' method to display the Rectangle.
            print(rect)
        else:
            # Use the 'display' method to show the Rectangle.
            rect.display()

        # Restore the original stdout.
        sys.stdout = sys.__stdout__
        # Return the captured text output.
        return output

    # Tests the str method
    def test_str_print_width_and_height(self):
        r = Rectangle(8, 3)
        output = type(self).output(r, "print")  # use print method
        expected = "[Rectangle] ({}) 0/0 - 8/3\n".format(r.id)
        self.assertEqual(expected, output.getvalue())

    def test_str_method_width_height_x(self):
        r = Rectangle(7, 5, 2)
        expected = "[Rectangle] ({}) 2/0 - 7/5".format(r.id)
        self.assertEqual(expected, r.__str__())

    def test_str_method_width_height_x_y(self):
        r = Rectangle(3, 5, 4, 0)
        expected = "[Rectangle] ({}) 4/0 - 3/5".format(r.id)
        self.assertEqual(expected, str(r))

    def test_str_method_width_height_x_y_id(self):
        rect = Rectangle(10, 22, 1, 3, 88)
        self.assertEqual("[Rectangle] (88) 1/3 - 10/22", str(rect))

    def test_str_method_setter_attributes(self):
        r = Rectangle(7, 7, 0, 0, [4])
        r.width = 15
        r.height = 1
        r.x = 8
        r.y = 10
        self.assertEqual("[Rectangle] ([4]) 8/10 - 15/1", str(r))

    def test_str_method_one_arg(self):
        rect = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            rect.__str__(1)

    # Test the display method of the rectangle
    def test_display_width_height(self):
        rect = Rectangle(2, 3, 0, 0, 0)
        output= type(self).output(rect, "display")
        self.assertEqual("##\n##\n##\n", output.getvalue())

    def test_display_width_height_x(self):
        rect = Rectangle(3, 2, 1, 0, 1)
        output= type(self).output(rect, "display")
        self.assertEqual(" ###\n ###\n", output.getvalue())


    def test_display_width_height_y(self):
        rect= Rectangle(4, 5, 0, 1, 0)
        output= type(self).output(rect, "display")
        display = "\n####\n####\n####\n####\n####\n"
        self.assertEqual(display, output.getvalue())

    def test_display_width_height_x_y(self):
        rect = Rectangle(2, 4, 3, 2, 0)
        output= type(self).output(rect, "display")
        display = "\n\n   ##\n   ##\n   ##\n   ##\n"
        self.assertEqual(display, output.getvalue())


    def test_display_one_arg(self):
        rect = Rectangle(5, 1, 2, 4, 7)
        with self.assertRaises(TypeError):
            rect.display(1)

class TestRectangle_update_args(unittest.TestCase):
    """unit testings for updating the args attribute
    of the Rectangle class"""

    def test_update_with_zero_args(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update()
        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(r))

    def test_update_with_one_arg(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89)
        self.assertEqual("[Rectangle] (89) 10/10 - 10/10", str(r))

    def test_update_with_two_args(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/10", str(r))

    def test_update_with_three_args(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(r))

    def test_update_with_four_args(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4)
        self.assertEqual("[Rectangle] (89) 4/10 - 2/3", str(r))

    def test_update_with_five_args(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual("[Rectangle] (89) 4/5 - 2/3", str(r))

    def test_update_with_more_than_five_args(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5, 6)
        self.assertEqual("[Rectangle] (89) 4/5 - 2/3", str(r))

    def test_update_args_None_id(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(None)
        correct = "[Rectangle] ({}) 10/10 - 10/10".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_args_None_id_and_more(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(None, 4, 5, 2)
        correct = "[Rectangle] ({}) 2/10 - 4/5".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_args_values_twice(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5, 6)
        r.update(5, 8, 2, 0, 0, 22)  # extra args beyond index
        self.assertEqual("[Rectangle] (5) 0/0 - 8/2", str(r))

    def test_update_args_with_invalid_width_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(22, "invalid")

    def test_update_args_width_zero(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(18, 0)

    def test_update_args_width_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(20, -5)

    def test_update_args_invalid_height_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(30, 12, "invalid")

    def test_update_args_height_zero(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(22, 11, 0)

    def test_update_args_height_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(101, 11, -15)

    def test_update_args_invalid_x_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(800, 12, 23, "invalid")

    def test_update_args_x_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(890, 21, 22, -6)

    def test_update_args_invalid_y(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(750, 6, 8, 3, "invalid")

    def test_update_args_y_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(75, 8, 12, 23, -6)

    def test_update_args_invalid_width_before_height(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(750, "invalid", "invalid")

    def test_update_args_invalid_width_before_x(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(35, "invalid", 12, "invalid")

    def test_update_args_invalid_width_before_y(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(74, "invalid", 10, 12, "invalid")

    def test_update_args_invalid_height_before_x(self):
        r = Rectangle(100, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(330, 5, "invalid", "invalid")

    def test_update_args_invalid_height_before_y(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(20, 11, "invalid", 1, "invalid")

    def test_update_args_invalid_x_before_y(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(33, 9, 5, "invalid", "invalid")


class TestRectangle_updating_kwargs(unittest.TestCase):
    """unit tests for update kwargs method of the Rectangle class"""

    def test_update_kwargs_with_one_arg(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=30)
        self.assertEqual("[Rectangle] (30) 10/10 - 10/10", str(r))

    def test_update_kwargs_with_two_args(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(width=2, id=22)
        self.assertEqual("[Rectangle] (22) 10/10 - 2/10", str(r))

    def test_update_kwargs_with_three_args(self):
        r = Rectangle(10, 22, 3, 2, 1)
        r.update(width=2, height=3, id=88)
        self.assertEqual("[Rectangle] (88) 3/2 - 2/3", str(r))

    def test_update_kwargs_with_four(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=89, x=1, height=2, y=3, width=4)
        self.assertEqual("[Rectangle] (89) 1/3 - 4/2", str(r))

    def test_update_kwargs_with_five(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(y=5, x=8, id=99, width=1, height=2)
        self.assertEqual("[Rectangle] (99) 8/5 - 1/2", str(r))

    def test_update_kwargs_with_None_as_id(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=None)
        correct = "[Rectangle] ({}) 10/10 - 10/10".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_kwargs_None_id_and_more(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=None, height=7, y=9)
        correct = "[Rectangle] ({}) 10/9 - 10/7".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_kwargs_twice(self):
        r = Rectangle(7, 3, 3, 3, 232)
        r.update(id=400, x=1, height=2)
        r.update(y=3, height=15, width=2)
        self.assertEqual("[Rectangle] (400) 1/3 - 2/15", str(r))

    def test_update_kwargs_with_invalid_width_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(width="string")

    def test_update_kwargs_width_with_zero(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(width=0)

    def test_update_kwargs_width_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(width=-5)

    def test_update_kwargs_invalid_height_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(height="invalid")

    def test_update_kwargs_height_zero(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(height=0)

    def test_update_kwargs_height_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(height=-5)

    def test_update_kwargs_inavlid_x_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(x="invalid")

    def test_update_kwargs_x_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(x=-5)

    def test_update_kwargs_invalid_y_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(y="invalid")

    def test_update_kwargs_y_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(y=-5)

    def test_update_args_and_kwargs(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, height=4, y=6)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/10", str(r))

    def test_update_kwargs_wrong_keys(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(a=5, b=10)
        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(r))

    def test_update_kwargs_some_wrong_keys(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(height=5, id=89, a=1, b=54, x=19, y=7)
        self.assertEqual("[Rectangle] (89) 19/7 - 10/5", str(r))


class TestRectangle_to_dict(unittest.TestCase):
    """Unittests for testing to_dictionary method of the Rectangle class."""

    def test_to_dictionary_output(self):
        r = Rectangle(10, 2, 1, 9, 5)
        expected = {'x': 1, 'y': 9, 'id': 5, 'height': 2, 'width': 10}
        self.assertDictEqual(expected, r.to_dictionary())

    def test_to_dictionary_two_instances(self):
        r1 = Rectangle(10, 2, 1, 9, 5)
        r2 = Rectangle(5, 9, 1, 2, 10)
        r2.update(**r1.to_dictionary())
        self.assertNotEqual(r1, r2)

    def test_to_dictionary_with_arg(self):
        r = Rectangle(10, 2, 4, 1, 2)
        with self.assertRaises(TypeError):
            r.to_dictionary(1)

if __name__ == '__main__':
    unittest.main()
