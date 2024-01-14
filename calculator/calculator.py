#!/usr/bin/env python3

"""
Defines a simple calculator program that prompts the user
for input and computes the output.
"""

from typing import Union


def intro():
    """
    Print an introductory message for the calculator.
    """
    print("=======================================")
    print("==========SIMPLE CLI CALCULATOR========")
    print("===Accepted Operands (+, -, *, /, %)===")
    print("=======================================")


def calculate(arg1: float, arg2: str, arg3: float) -> Union[float, str]:
    """
    Perform the calculation based on user input.

    Parameters:
    - arg1 (float): The first number
    - arg2 (str): The operator (+, -, *, /, %).
    - arg3 (float): The second number.

    Returns:
    - The result of the calculation.
    """
    operands = ["+", "-", "*", "/", "%"]

    if arg2 not in operands:
        return "Operand is invalid"
    elif arg2 == "+":
        return arg1 + arg3
    elif arg2 == "-":
        return arg1 - arg3
    elif arg2 == "*":
        return arg1 * arg3
    elif arg2 == "/":
        return arg1 / arg3
    else:
        return arg1 % arg3


if __name__ == "__main__":
    intro()

    while True:
        try:
            arg1 = float(input("First number: "))
            operand = input('Operand (type "quit" to exit): ')
            if operand.lower() == "quit":
                print("Exiting the calculator.")
                break

            arg3 = float(input("Second number: "))

            result = calculate(arg1, operand, arg3)
            print()
            print(f"Result: {result}")
            print()
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except ZeroDivisionError:
            print("Cannot divide by zero. Please enter a non-zero second number.")
