from pytemplate.domain.models import Operands


class Calculator:
    @staticmethod
    def add(operands: Operands) -> int:
        return operands.first_operand + operands.second_operand

    @staticmethod
    def subtract(operands: Operands) -> int:
        return operands.first_operand - operands.second_operand

    @staticmethod
    def multiply(operands: Operands) -> int:
        return operands.first_operand * operands.second_operand

    @staticmethod
    def divide(operands: Operands) -> float:
        if operands.second_operand == 0:
            raise ValueError("Cannot divide by zero")
        return operands.first_operand / operands.second_operand
