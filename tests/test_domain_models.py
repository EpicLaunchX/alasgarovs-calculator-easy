from src.pytemplate.domain.models import Operands, operands_factory


class TestOperands:
    def test_operands_creation(self):
        # Test Operands class creation
        first_operand = 15
        second_operand = 25
        operands = Operands(first_operand, second_operand)
        assert operands.first_operand == first_operand
        assert operands.second_operand == second_operand

    def test_operands_factory(self):
        # Test operands_factory function
        first_operand = 15
        second_operand = 25
        operands = operands_factory(first_operand, second_operand)
        assert operands.first_operand == first_operand
        assert operands.second_operand == second_operand
