import math
import art
import os


# Add Function
def add(n1, n2):
    return n1 + n2


# Subtract Function
def subtract(n1, n2):
    return n1 - n2


# Multiply Function
def multiply(n1, n2):
    return n1 * n2


# Division Function
def division(n1, n2):
    return n1 / n2


# Percentage Function
def percentage(n1, n2):
    return round((n1 * n2) / 100.0, 4)


# Exponential Function
def exponential(n1, n2):
    return pow(n1, n2)


# Square Root Function
def root(n1):
    return round(math.sqrt(n1), 4)


# Square Function
def square(n1):
    return pow(n1, 2)


calculator_operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": division,
    "%": percentage,
    "exp": exponential,
    "sqrt": root,
    "sqr": square
}


def calculator():
    print(art.logo)
    num1 = float(input(" What's the first number? "))
    # Printing Operators/Symbols
    for operator in calculator_operators:
        print("   " + operator)
    continue_calculation = True
    while continue_calculation:
        operation_symbol = input("\n Pick an operation : ")
        if operation_symbol == "sqrt" or operation_symbol == "sqr":
            calculation_function = calculator_operators[operation_symbol]
            answer = calculation_function(num1)
            print(f"  {operation_symbol} of {num1} = {answer}")
        else:
            num2 = float(input("\n What's the next number? "))

            calculation_function = calculator_operators[operation_symbol]
            answer = calculation_function(num1, num2)
            print(f"  {num1} {operation_symbol} {num2} = {answer}")

        another_calculation = input(f"\n Type 'y or Y' to continue calculating with {answer}, or type 'n or N' to "
                                    f"start a new calculation "
                                    f"\n And to EXIT from CALCULATOR type 'exit or EXIT'. : ").lower()
        if another_calculation == 'y':
            num1 = answer
        elif another_calculation == 'exit':
            exit()
        else:
            continue_calculation = False
            os.system('cls')
            calculator()


calculator()
