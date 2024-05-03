from pytemplate.domain.models import operands_factory
from pytemplate.service.calculator import Calculator


def main():
    print("Calculator CLI!")

    first_operand = int(input("Enter the first operand: "))
    second_operand = int(input("Enter the second operand: "))
    action = input("Enter the action (add/subtract/multiply/divide): ")

    # Create Calculator instance and operands object
    calculator = Calculator()
    operands = operands_factory(first_operand, second_operand)

    if action == "add":
        result = calculator.add(operands)
    elif action == "subtract":
        result = calculator.subtract(operands)
    elif action == "multiply":
        result = calculator.multiply(operands)
    elif action == "divide":
        result = calculator.divide(operands)
    else:
        print("Invalid action. Please enter add/subtract/multiply/divide.")
        return

    print("Result:", result)
