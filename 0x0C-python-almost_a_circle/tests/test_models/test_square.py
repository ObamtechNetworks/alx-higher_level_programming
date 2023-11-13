#!/usr/bin/python3
"""unit tests for the Square class"""


# import relevant modules
import unittest
import sys
import io
import csv

# import the base, square and square class
from models.square import Square
from models.base import Base
from models.square import Square



class TestSquare_instantiation(unittest.TestCase):
    """test square instance and instantiation from Base class"""
    def test_square_is_rectangle_instance(self):
        """test if it's an instance of Square"""
        self.assertIsInstance(Square(1, 2), Square)

    def test_no_arguments(self):
        """test square with no argument"""
        with self.assertRaises(TypeError):
            Square()

    def test_square_with_one_arg(self):
        """test square with one argument"""
        r1 = Square(5)
        self.assertEqual(5, r1.size)

    def test_square_with_two_args_size_x(self):
        """test square with two arguments"""
        r1 = Square(5, 2)
        self.assertEqual(r1.size, 5)
        self.assertEqual(r1.x, 2)

    def test_square_with_three_args_size_x_y(self):
        """test square with two arguments"""
        r1 = Square(5, 2, 3)
        self.assertEqual(r1.size, 5)
        self.assertEqual(r1.x, 2)
        self.assertEqual(r1.y, 3)
    
    def test_square_with_four_args_size_x_y_id(self):
        """test square with two arguments"""
        r1 = Square(5, 2, 3, 4)
        self.assertEqual(r1.size, 5)
        self.assertEqual(r1.x, 2)
        self.assertEqual(r1.y, 3)
        self.assertEqual(r1.id, 4)

    def test_square_with_args_id(self):
        """test square with two arguments"""
        r1 = Square(1, 2, 3, 40)
        self.assertEqual(r1.id, 40)

    def test_square_too_many_args(self):
        """test square with too many arguments"""
        with self.assertRaises(TypeError):
            r1 = Square(1, 2, 3, 4, 5)

class TestSquare_private_attribute(unittest.TestCase):
    """test AttributeError exceptions with private attributes"""
    def test_private_attr_size(self):
        """test accessing of private attribute - size"""
        with self.assertRaises(AttributeError):
            r1 = Square(5, 2, 3, 4)
            print(r1.__size)
    
    def test_private_attr_x(self):
        """test accessing of private attribute - x"""
        with self.assertRaises(AttributeError):
            r1 = Square(5, 2, 3, 4)
            print(r1.__x)

    def test_private_attr_y(self):
        """test accessing of private attribute - y"""
        with self.assertRaises(AttributeError):
            r1 = Square(5, 2, 3, 4)
            print(r1.__y)

class TestSquare_setters_getters(unittest.TestCase):
    """test if setters and getters are working rightly"""
    
    def test_attr_setters_size(self):
        """tests setters size"""
        r = Square(size=5)
        r.size = 15
        self.assertEqual(r.size, 15)
    
    def test_attr_setters_x(self):
        """tests setters x"""
        r = Square(size=5)
        r.x = 3
        self.assertEqual(r.x, 3)
    
    def test_attr_setters_y(self):
        """tests setters y"""
        r = Square(size=5)
        r.y = 4
        self.assertEqual(r.y, 4)

    def test_attr_getter_size(self):
        """tests getters size"""
        r = Square(5, 3)
        self.assertEqual(r.size, 5)
    
class TestSquare_size_values(unittest.TestCase):
    """test size instantiation with different data types"""

    def test_None_as_size_value(self):
        with self.assertRaisesRegex(TypeError, "size must be an integer"):
            Square(None, 10)


    def test_str_as_size_value(self):
        with self.assertRaisesRegex(TypeError, "size must be an integer"):
            Square("my string", 15)


    def test_float_as_size(self):
         with self.assertRaisesRegex(TypeError, "size must be an integer"):
             Square(3.335, 18)


    def test_complex_as_size_value(self):
        with self.assertRaisesRegex(TypeError, "size must be an integer"):
            Square(complex(2, 3), 10)


    def test_dict_as_size_value(self):
        with self.assertRaisesRegex(TypeError, "size must be an integer"):
            Square({"id1":7, "id2":6}, 35)


    def test_set_as_size_value(self):
        with self.assertRaisesRegex(TypeError, "size must be an integer"):
            Square({2, 4, 6}, 8)


    def test_list_as_size_value(self):
        with self.assertRaisesRegex(TypeError, "size must be an integer"):
            Square([3, 5, 7], 9)


    def test_range_as_size_value(self):
        with self.assertRaisesRegex(TypeError, "size must be an integer"):
            Square(range(4), 8)


    def test_tuple_as_size_value(self):
        with self.assertRaisesRegex(TypeError, "size must be an integer"):
            Square((6, 8, 10), 12)


    def test_frozen_set_as_size_value(self):
        with self.assertRaisesRegex(TypeError, "size must be an integer"):
            Square(frozenset({1, 5, 4, 8}), 4)


    def test_bytes_as_size_value(self):
        with self.assertRaisesRegex(TypeError, "size must be an integer"):
            Square(b'unittesting', 9)


    def test_bytearray_as_size_value(self):
        with self.assertRaisesRegex(TypeError, "size must be an integer"):
            Square(bytearray(b'bytes'), 8)


    def test_memoryview_as_size_value(self):
        with self.assertRaisesRegex(TypeError, "size must be an integer"):
            Square(memoryview(b'unittests'), 13)


    def test_positive_inf_size_as_value(self):
        with self.assertRaisesRegex(TypeError, "size must be an integer"):
            Square(float('inf'), 4)

    def test_neg_inf_size_as_value(self):
        with self.assertRaisesRegex(TypeError, "size must be an integer"):
            Square(float('-inf'), 6)


    def test_nan_as_size_value(self):
        with self.assertRaisesRegex(TypeError, "size must be an integer"):
            Square(float('nan'), 6)


    def test_neg_size_value(self):
        with self.assertRaisesRegex(ValueError, "size must be > 0"):
            Square(-5, 2)


    def test_zero_as_size_value(self):
        with self.assertRaisesRegex(ValueError, "size must be > 0"):
            Square(0, 9)

class TestSquare_x_values(unittest.TestCase):
    """tests x instantiation with different data types"""

    def test_None_as_x_value(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(4, None)


    def test_str_as_x_value(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, "my string")


    def test_x_as_size(self):
         with self.assertRaisesRegex(TypeError, "x must be an integer"):
             Square(3, 3.335)


    def test_x_as_height_value(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(3, complex(2, 3))


    def test_dict_as_x_value(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(3, {"id1":7, "id2":6})


    def test_set_as_x_value(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, {2, 4, 6})


    def test_list_as_x_value(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, [3, 5, 7])


    def test_range_as_x_value(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(4, range(4))


    def test_tuple_as_x_value(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(4, (6, 8, 10))


    def test_frozen_set_as_x_value(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(4, frozenset({1, 5, 4, 8}))


    def test_bytes_as_x_value(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(3, b'unittesting')


    def test_bytearray_as_x_value(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(5, bytearray(b'bytes'))


    def test_memoryview_as_x_value(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(6, memoryview(b'unittests'))


    def test_positive_inf_as_x_value(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(4, float('inf'))

    def test_neg_inf_as_x_value(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(5, float('-inf'))


    def test_nan_as_x_value(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(5, float('nan'))


    def test_neg_x_value(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(3, -5)


    def test_zero_as_x_value(self):
        self.assertEqual(Square(9, 0).x, 0)

class TestSquare_y_values(unittest.TestCase):
    """tests y instantiation with different data types"""

    def test_None_as_y_value(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, None)


    def test_str_as_y_value(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 3, "my string")


    def test_y_as_size(self):
         with self.assertRaisesRegex(TypeError, "y must be an integer"):
             Square(3, 4, 3.335)


    def test_y_as_height_value(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(3, 3, complex(2, 3))


    def test_dict_as_y_value(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(3, 4, {"id1":7, "id2":6})


    def test_set_as_y_value(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, {2, 4, 6})


    def test_list_as_y_value(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, [3, 5, 7])


    def test_range_as_y_value(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(4, 3, range(4))


    def test_tuple_as_y_value(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(4, 3, (6, 8, 10))


    def test_frozen_set_as_y_value(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(4, 2, frozenset({1, 5, 4, 8}))


    def test_bytes_as_y_value(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(3, 3, b'unittesting')


    def test_bytearray_as_y_value(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(5, 3, bytearray(b'bytes'))


    def test_memoryview_as_y_value(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(6, 3, memoryview(b'unittests'))


    def test_positive_inf_as_y_value(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(4, 3, float('inf'))

    def test_neg_inf_height_as_y_value(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(5, 3, float('-inf'))


    def test_nan_as_y_value(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(5, 3, float('nan'))


    def test_neg_y_value(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(3, 2, -5)


    def test_zero_as_y_value(self):
        self.assertEqual(Square(9, 3, 0).y, 0)

class TestSquare_order_of_init_values(unittest.TestCase):
    """test order of attributes initalization"""

    def test_invalid_size_before_x(self):
        with self.assertRaisesRegex(TypeError, "size must be an integer"):
            Square("invalid size value", "invalid x")


    def test_invalid_size_before_y(self):
        with self.assertRaisesRegex(TypeError, "size must be an integer"):
            Square("invalid size value", 4, "invalid y")

    def test_invlaid_x_before_y(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "invalid x value", "invalid y value")

    def test_invlaid_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, "invalid y value")

class TestSquare_area(unittest.TestCase):
    """test area method of the Square class"""

    def test_area_small(self):
        square = Square(3, 3, 2, 3)
        self.assertEqual(9, square.area())

    def test_area_large(self):
        square = Square(999999999999999999, 0, 0, 12)
        self.assertEqual(999999999999999998000000000000000001, square.area())

    def test_area_changed_size(self):
        square = Square(3, 0, 0, 33)
        square.size = 8
        self.assertEqual(64, square.area())

    def test_area_with_arg(self):
        square = Square(8, 2, 3, 90)
        with self.assertRaises(TypeError):
            square.area(1)

class TestSquare_id(unittest.TestCase):
    """creates different test cases (methods) for the square cls"""
    def setUp(self):
        """this method is called before each test case"""
        # reset the id so as to properly set the __nb_objects of the base
        Base._Base__nb_objects = 0
    
    def test_constructor_with_id(self):
        """tests instances with ids"""
        square = Square(size=5, id=1)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 0)

    def test_constructor_without_id(self):
        """tests instances without ids,
        __nb_objects should assign corsquarely
        """
        square = Square(size=3)
        self.assertEqual(square.id, 1)  # id is generated automat.
        self.assertEqual(square.size, 3)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 0)

    def test_nb_objects(self):
        """tests how many objects created per instance"""
        square1 = Square(size=2)
        square2 = Square(2, 1)
        square2.size = 3
        square3 = Square(1, 2, 0, 23)

        # test square1
        self.assertEqual(square1.size, 2)
        self.assertEqual(square1.x, 0)
        self.assertEqual(square1.y, 0)

        # test square2
        self.assertEqual(square2.size, 3)
        self.assertEqual(square2.x, 1)
        self.assertEqual(square2.y, 0)

        # test square3
        self.assertEqual(square3.size, 1)
        self.assertEqual(square3.x, 2)
        self.assertEqual(square3.y, 0)

        # test total number of objects
        self.assertEqual(Base._Base__nb_objects, 3)

    def test_str_as_id(self):
        """tests str as id"""
        r1 = Square(3, 0, 0, 'str')
        self.assertEqual(r1.id, 'str')

class TestSquare_str_and_display(unittest.TestCase):
    """Unittests for str method and display method"""

    @staticmethod
    def output(square, method):
        """captures and return text output from a Square's display method

        Args:
            square (Square): The Square to capture output from
            method (str): The method to use for displaying
            ('print' or 'display')

        Returns:
            str: a string - The captured text output.
        """
        # create a stringIO object
        output = io.StringIO()
        
        # Redisquare stdout to the StringIO buffer
        sys.stdout = output

        # Choose the appropriate display method based on the input
        if method == "print":
            # use the 'print' method to display the Square.
            print(square)
        else:
            # Use the 'display' method to show the Square.
            square.display()

        # Restore the original stdout.
        sys.stdout = sys.__stdout__
        # Return the captured text output.
        return output

    # Tests the str method
    def test_str_print_size_and_height(self):
        s = Square(8, 3)
        output = type(self).output(s, "print")  # use print method
        expected = "[Square] ({}) 3/0 - 8\n".format(s.id)
        self.assertEqual(expected, output.getvalue())

    def test_str_method_size_x_y(self):
        s = Square(5, 5, 4)
        expected = "[Square] ({}) 5/4 - 5".format(s.id)
        self.assertEqual(expected, str(s))

    def test_str_method_size_x_y_id(self):
        square = Square(10, 3, 1, 88)
        self.assertEqual("[Square] (88) 3/1 - 10", str(square))

    def test_str_method_setter_attributes(self):
        s = Square(7, 0, 0, [4])
        s.size = 15
        s.x = 8
        s.y = 10
        self.assertEqual("[Square] ([4]) 8/10 - 15", str(s))

    def test_str_method_with_arg(self):
        square = Square(1, 3, 4, 5)
        with self.assertRaises(TypeError):
            square.__str__(1)

    # Test the display method of the square
    def test_display_size(self):
        square = Square(2, 0, 0, 0)
        output= type(self).output(square, "display")
        self.assertEqual("##\n##\n", output.getvalue())

    def test_display_size_x(self):
        square = Square(3, 1, 0, 1)
        output= type(self).output(square, "display")
        self.assertEqual(" ###\n ###\n \###", output.getvalue())


    def test_display_size_height_y(self):
        square= Square(4, 0, 1)
        output= type(self).output(square, "display")
        display = "\n####\n####\n####\n####\n"
        self.assertEqual(display, output.getvalue())

    def test_display_size_x_y(self):
        square = Square(2, 3, 2, 0)
        output= type(self).output(square, "display")
        display = "\n\n   ##\n   ##\n   ##\n   ##\n"
        self.assertEqual(display, output.getvalue())


    def test_display_one_arg(self):
        square = Square(5, 2, 4, 7)
        with self.assertRaises(TypeError):
            square.display(1)

class TestSquare_update_args(unittest.TestCase):
    """unit testings for updating the args attribute
    of the Square class"""

    def test_update_with_zero_args(self):
        r = Square(10, 10, 10, 10)
        r.update()
        self.assertEqual("[Square] (10) 10/10 - 10", str(r))

    def test_update_with_one_arg(self):
        r = Square(10, 10, 10, 10)
        r.update(89)
        self.assertEqual("[Square] (89) 10/10 - 10", str(r))

    def test_update_with_two_args(self):
        r = Square(10, 10, 10, 10)
        r.update(89, 2)
        self.assertEqual("[Square] (89) 10/10 - 2", str(r))

    def test_update_with_three_args(self):
        r = Square(10, 10, 10, 10)
        r.update(89, 2, 3)
        self.assertEqual("[Square] (89) 3/10 - 2", str(r))

    def test_update_with_four_args(self):
        r = Square(10, 10, 10, 10)
        r.update(89, 2, 3, 4)
        self.assertEqual("[Square] (89) 3/4 - 2", str(r))

    def test_update_with_more_than_four_args(self):
        r = Square(10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual("[Square] (89) 3/5 - 2", str(r))

    def test_update_args_None_id(self):
        r = Square(10, 10, 10, 10)
        r.update(None)
        corsquare = "[Square] ({}) 10/10 - 10".format(r.id)
        self.assertEqual(corsquare, str(r))

    def test_update_args_None_id_and_more(self):
        r = Square(10, 10, 10, 10)
        r.update(None, 4, 5, 2)
        corsquare = "[Square] ({}) 5/2 - 4".format(r.id)
        self.assertEqual(corsquare, str(r))

    def test_update_args_values_twice(self):
        r = Square(10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5, 6)
        r.update(5, 8, 2, 0, 0, 22)  # extra args beyond index
        self.assertEqual("[Square] (5) 2/0 - 8", str(r))

    def test_update_args_with_invalid_size_type(self):
        r = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "size must be an integer"):
            r.update(22, "invalid")

    def test_update_args_size_zero(self):
        r = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "size must be > 0"):
            r.update(18, 0)

    def test_update_args_size_negative(self):
        r = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "size must be > 0"):
            r.update(20, -5)

    def test_update_args_invalid_height_type(self):
        r = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(30, 12, "invalid")

    def test_update_args_invalid_x_type(self):
        r = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(800, 23, "invalid")

    def test_update_args_x_negative(self):
        r = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(890, 22, -6)

    def test_update_args_invalid_y(self):
        r = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(750, 8, 3, "invalid")

    def test_update_args_y_negative(self):
        r = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(75, 12, 23, -6)

    def test_update_args_invalid_size_before_height(self):
        r = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "size must be an integer"):
            r.update(750, "invalid", "invalid")

    def test_update_args_invalid_size_before_x(self):
        r = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "size must be an integer"):
            r.update(35, "invalid", 12, "invalid")

    def test_update_args_invalid_size_before_y(self):
        r = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "size must be an integer"):
            r.update(74, "invalid", 2, 3)

    def test_update_args_invalid_x_before_y(self):
        r = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(33, 95, "invalid", "invalid")

class TestSquare_updating_kwargs(unittest.TestCase):
    """unit tests for update kwargs method of the Square class"""

    def test_update_kwargs_with_one_arg(self):
        r = Square(10, 10, 10, 10)
        r.update(id=30)
        self.assertEqual("[Square] (30) 10/10 - 10", str(r))

    def test_update_kwargs_with_two_args(self):
        r = Square(10, 10, 10, 10)
        r.update(size=2, id=22)
        self.assertEqual("[Square] (22) 10/10 - 2", str(r))

    def test_update_kwargs_with_three_args(self):
        r = Square(10, 22, 3, 2)
        r.update(size=2, x=3, id=88)
        self.assertEqual("[Square] (88) 3/3 - 2", str(r))

    def test_update_kwargs_with_four(self):
        r = Square(10, 10, 10, 10)
        r.update(id=89, x=1, y=3, size=4)
        self.assertEqual("[Square] (89) 1/3 - 4", str(r))

    def test_update_kwargs_with_five(self):
        r = Square(10, 10, 10, 10)
        r.update(y=5, x=8, id=99, size=1, height=3)
        self.assertEqual("[Square] (99) 8/5 - 1", str(r))

    def test_update_kwargs_with_None_as_id(self):
        r = Square(10, 10, 10, 10)
        r.update(id=None)
        corsquare = "[Square] ({}) 10/10 - 10".format(r.id)
        self.assertEqual(corsquare, str(r))

    def test_update_kwargs_None_id_and_more(self):
        r = Square(10, 10, 10, 10)
        r.update(id=None, size=7, y=9)
        corsquare = "[Square] ({}) 10/9 - 7".format(r.id)
        self.assertEqual(corsquare, str(r))

    def test_update_kwargs_twice(self):
        r = Square(7, 3, 3, 232)
        r.update(id=400, x=1, size=2)
        r.update(y=3, size=2)
        self.assertEqual("[Square] (400) 1/3 - 2", str(r))

    def test_update_kwargs_with_invalid_size_type(self):
        r = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "size must be an integer"):
            r.update(size="string")

    def test_update_kwargs_size_with_zero(self):
        r = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "size must be > 0"):
            r.update(size=0)

    def test_update_kwargs_size_negative(self):
        r = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "size must be > 0"):
            r.update(size=-5)

    def test_update_kwargs_inavlid_x_type(self):
        r = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(x="invalid")

    def test_update_kwargs_x_negative(self):
        r = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(x=-5)

    def test_update_kwargs_invalid_y_type(self):
        r = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(y="invalid")

    def test_update_kwargs_y_negative(self):
        r = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(y=-5)

    def test_update_args_and_kwargs(self):
        r = Square(10, 10, 10, 10)
        r.update(89, 4, x=6)
        self.assertEqual("[Square] (89) 6/10 - 4", str(r))

    def test_update_kwargs_wrong_keys(self):
        r = Square(10, 10, 10, 10)
        r.update(a=5, b=10)
        self.assertEqual("[Square] (10) 10/10 - 10", str(r))

    def test_update_kwargs_some_wrong_keys(self):
        r = Square(10, 10, 10, 10)
        r.update(size=5, id=89, a=1, b=54, x=19, y=7)
        self.assertEqual("[Square] (89) 19/7 - 5", str(r))


class TestSquare_to_dict(unittest.TestCase):
    """Unittests for testing to_dictionary method of the Square class."""

    def test_to_dictionary_output(self):
        r = Square(10, 2, 1, 9)
        expected = {'x': 2, 'y': 1, 'id': 9, 'size': 10}
        self.assertDictEqual(expected, r.to_dictionary())

    def test_to_dictionary_two_instances(self):
        r1 = Square(10, 2, 1, 9)
        r2 = Square(5, 9, 1, 2)
        r2.update(**r1.to_dictionary())
        self.assertNotEqual(r1, r2)

    def test_to_dictionary_with_arg(self):
        r = Square(10, 2, 4, 2)
        with self.assertRaises(TypeError):
            r.to_dictionary(1)

if __name__ == '__main__':
    unittest.main()
