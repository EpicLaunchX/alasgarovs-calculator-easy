from src.pytemplate.domain.models import operands_factory
from src.pytemplate.service.calculator import Calculator


def get_operands():
    first_operand = int(input("Enter the first operand: "))
    second_operand = int(input("Enter the second operand: "))
    return operands_factory(first_operand, second_operand)


def perform_calculation(operands, action):
    calculator = Calculator()  # Create an instance of Calculator
    if action == "add":
        return calculator.add(operands)
    elif action == "subtract":
        return calculator.subtract(operands)
    elif action == "multiply":
        return calculator.multiply(operands)
    elif action == "divide":
        return calculator.divide(operands)
    else:
        raise ValueError("Invalid action. Please enter add/subtract/multiply/divide.")


def main():
    print("Calculator CLI!")

    operands = get_operands()
    action = input("Enter the action (add/subtract/multiply/divide): ")

    try:
        result = perform_calculation(operands, action)
        print("Result:", result)
    except ValueError as e:
        print("Error:", e)
