#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """defines different test cases and handles apropriately
    """
    def test_non_list_arguments(self):
        """Tests for non list arguments and raise a TypeError
        """
        with self.assertRaises(TypeError):
            max_integer(123495) #  Test with an integer
        with self.assertRaises(TypeError):
            max_integer("Best School")  # test for string
        with self.assertRaises(TypeError):
            max_integer({'key': 23, 'name': 'John'})  # Test with dict
        with self.assertRaises(TypeError):
            max_integer((1, 'string', ['l' 'i', 2]))  # Test with tuples
        with self.assertRaises(TypeError):
            max_integer(None)  # Test with None
        with self.assertRaises(TypeError):
            max_integer([[]])  # Test with a matrix

    def test_correct_outputs(self):
        """Test for correctness of output
        """
        self.assertIsNone(max_integer([]))  # Test empty list
        self.assertEqual(max_integer([1, 3, 5, 2, 10]), 10)  # Test +ve int
        self.assertEqual(max_integer([-1, -10, -3, -9]), -1)  # Test -ves
        self.assertEqual(max_integer([1]), 1)  # Test with single element
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)  # Test identical
        self.assertEqual(max_integer([2, 4, 6, 8, 10]), 10)  # Test sorted list

    def test_invalid_list_elements(self):
        """Test for invalid elements within list
        """
        with self.assertRaises(TypeError):
            max_integer([23.5, 8, 19.2, 0])  # Test with floats
        with self.assertRaises(TypeError):
            max_integer([1, 2, '3', 5])  # Test with char within list
        with self.assertRaises(TypeError):
            max_integer([10, 100, [1, 100, 23]])  # Test list within list
        with self.assertRaises(TypeError):
            max_integer([1000, 0, "School", 'Best'])  # Test str among list
        with self.assertRaises(TypeError):
            max_integer([2500, {'key': 10}, 20])  # Test dict inside list
        with self.assertRaises(TypeError):
            max_integer([20, 10, (1, 2, '5')])  # Test tuple within list
        with self.assertRaises(TypeError):
            max_integer([20, 1, 5, None, 2])  # Test for None within list
        with self.assertRaises(TypeError):
            max_integer([1e3, 2e5, 3e7])  # Test float in scientific repr
        with self.assertRaises(TypeError):
            max_integer([float('inf'), float('-inf')])  # Test inf floats
        with self.assertRaises(TypeError):
            max_integer([float('nan'), 42])  # Test with NaN float
        with self.assertRaises(TypeError):
            max_integer([1e100, 1e100 - 1])  # Test with large floats
    def test_mutability(self):
        """Test that the list is not modified after usage
        """
        input_list = [1, 2, 3, 4]
        max_integer(input_list)
        self.assertEqual(input_list, [1, 2, 3, 4])

    def test_with_large_list(self):
        """Test for large numbers
        """
        large_list = [i for i in range(1, 10001)]  # create large list
        expected_output = max(large_list)  # the max int in the list
        self.assertEqual(max_integer(large_list), expected_output)

    def test_with_multiplied_numbers(self):
        """test with multiplied numbers
        """
        small_list = [i * 10 for i in range(1, 10001)]
        expected_output = max(small_list)
        self.assertEqual(max_integer(small_list), expected_output)

if __name__ == '__main__':
    unittest.main()
