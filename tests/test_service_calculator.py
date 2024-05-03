import unittest

from src.pytemplate.domain.models import operands_factory
from src.pytemplate.service.calculator import Calculator


class TestCalculator(unittest.TestCase):

    def test_add(self):
        result = Calculator.add(operands_factory(45, 35))
        self.assertEqual(result, 80)

    def test_subtract(self):
        result = Calculator.subtract(operands_factory(45, 35))
        self.assertEqual(result, 10)

    def test_multiply(self):
        result = Calculator.multiply(operands_factory(4, 5))
        self.assertEqual(result, 20)

    def test_divide(self):
        result = Calculator.divide(operands_factory(20, 4))
        self.assertEqual(result, 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            Calculator.divide(operands_factory(20, 0))
