"""
Contains unit tests for the src.calculator module.
"""
import unittest
from src.calculator import Calculator


class TestCalculator(unittest.TestCase):
    """
    Class for testing the calculator class.
    """

    def setUp(self):
        self.calc = Calculator()

    def test_result_equals_zero(self):
        """
        Tests if the starting result equals zero.
        """
        self.assertEqual(self.calc.get_value(), 0)

    def test_set_value(self):
        """
        Tests if the value is set correctly.
        """
        self.calc.set_value(17)
        self.assertEqual(self.calc.get_value(), 17)

    def test_add(self):
        """
        Tests if the add method works correctly.
        """
        self.calc.set_value(5)
        self.calc.add(5)
        self.assertEqual(self.calc.get_value(), 10)

    def test_subtract(self):
        """
        Tests if the subtract method works correctly.
        """
        self.calc.set_value(7)
        self.calc.subtract(3)
        self.assertEqual(self.calc.get_value(), 4)

    def test_multiply(self):
        """
        Tests if the multiply method works correctly.
        """
        self.calc.set_value(5)
        self.calc.multiply(5)
        self.assertEqual(self.calc.get_value(), 25)

    def test_divide_by_valid_number(self):
        """
        Tests if the divide method works correctly when dividing by a valid number.
        """
        self.calc.set_value(14)
        self.calc.divide(2)
        self.assertEqual(self.calc.get_value(), 7)

    def test_divide_by_zero(self):
        """
        Tests if the divide method raises an exception when dividing by zero.
        """
        self.calc.set_value(100)
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(0)

    def test_power(self):
        """
        Tests if the power method works correctly.
        """
        self.calc.set_value(2)
        self.calc.power(3)
        self.assertEqual(self.calc.get_value(), 8)

    def test_square_root(self):
        """
        Tests if the root method works correctly by default.
        """
        self.calc.set_value(16)
        self.calc.root()
        self.assertEqual(self.calc.get_value(), 4)

    def test_valid_root(self):
        """
        Tests if the root method works correctly when specifying a value for root.
        """
        self.calc.set_value(8)
        self.calc.root(3)
        self.assertEqual(self.calc.get_value(), 2)

    def test_invalid_root(self):
        """
        Tests if the root method raises an exception when specifying an invalid value for root.
        """
        self.calc.set_value(8)
        with self.assertRaises(ValueError):
            self.calc.root(0)
