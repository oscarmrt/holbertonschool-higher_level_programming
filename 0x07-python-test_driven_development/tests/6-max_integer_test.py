#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unittest class for max_integer"""
    def test_module_docstring(self):
        """test for module"""
        module = __import__("6-max_integer").__doc__
        self.assertTrue(len(module) > 1)

    def test_function_docstring(self):
        """test for function"""
        function = __import__("6-max_integer").max_integer.__doc__
        self.assertTrue(len(function) > 1)

    def test_empty(self):
        """test for empty list"""
        self.assertIsNone(max_integer())

    def test_str(self):
        """test for string"""
        list = [1, 2, 'holberton', 6]
        with self.assertRaises(TypeError):
            max_integer(list)

if __name__ == "__main__":
    unittest.main()
