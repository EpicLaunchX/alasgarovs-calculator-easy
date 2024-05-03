import unittest

from src.pytemplate.domain.models import operands_factory
from src.pytemplate.service.calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        operands = operands_factory(45, 35)
        result = self.calculator.add(operands)
        self.assertEqual(result, 80)

    def test_subtract(self):
        operands = operands_factory(45, 35)
        result = self.calculator.subtract(operands)
        self.assertEqual(result, 10)

    def test_multiply(self):
        operands = operands_factory(4, 5)
        result = self.calculator.multiply(operands)
        self.assertEqual(result, 20)

    def test_divide(self):
        operands = operands_factory(20, 4)
        result = self.calculator.divide(operands)
        self.assertEqual(result, 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calculator.divide(operands_factory(20, 0))
