"""Docstring."""

import unittest
from tasks.calculator import Calculator


class TestCalculator(unittest.TestCase):
    """Docstring."""

    def setUp(self):
        self.calculator = Calculator()

    def test_sum(self):
        self.assertEqual(self.calculator.sum(10,5), 15)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(10,5), 50)

    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(10,5), 5)

    def test_divide(self):
        self.assertEqual(self.calculator.divide(10,5), 2)

    def test_sqrt(self):
        self.assertEqual(self.calculator.sqrt(100), 10.00)

    def test_pi(self):
        self.assertEqual(self.calculator.pi(180), 3.14)


if __name__ == "__main__":
    unittest.main()
