from src.pytemplate.domain.models import Operands


class TestOperands:
    def test_operands_creation(self):
        # Test Operands class creation
        first_operand = 15
        second_operand = 25
        operands = Operands(first_operand, second_operand)
        assert operands.first_operand == first_operand
        assert operands.second_operand == second_operand
