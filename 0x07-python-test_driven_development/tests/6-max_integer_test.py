#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """defines different test cases and handles apropriately
    """
    def test_correct_outputs(self):
        """Test for correctness of output
        """
        self.assertIsNone(max_integer([]))  # Test empty list
        self.assertEqual(max_integer([1, 3, 5, 2, 10]), 10)  # Test +ve int
        self.assertEqual(max_integer([-1, -10, -3, -9]), -1)  # Test -ves
        self.assertEqual(max_integer([1]), 1)  # Test with single element
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)  # Test identical
        self.assertEqual(max_integer([2, 4, 6, 8, 10]), 10)  # Test sorted list
        self.assertEqual(max_integer([-1, 4, 9, 220]), 220)  # only 1 neg.
        self.assertEqual(max_integer([100, 2000, 1]), 2000)  # max in mid
        self.assertEqual(max_integer([2000, 123, 11]), 2000)  # max at beg
        self.assertEqual(max_integer([2, 100, 259, 800]), 800)  # max @end
    
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
