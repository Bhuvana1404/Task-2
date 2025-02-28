import argparse
import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

def power(a, b):
    return a ** b

def sqrt(a):
    if a < 0:
        return "Error! Square root of negative number."
    return math.sqrt(a)

def modulo(a, b):
    return a % b

def main():
    parser = argparse.ArgumentParser(description="CLI Calculator")
    parser.add_argument("operation", type=str, help="Choose an operation: add, sub, mul, div, pow, sqrt, mod")
    parser.add_argument("num1", type=float, help="First number")

    # num2 is optional for operations like sqrt
    parser.add_argument("num2", type=float, nargs="?", default=None, help="Second number (not needed for sqrt)")

    args = parser.parse_args()

    if args.operation == "add":
        print(add(args.num1, args.num2))
    elif args.operation == "sub":
        print(subtract(args.num1, args.num2))
    elif args.operation == "mul":
        print(multiply(args.num1, args.num2))
    elif args.operation == "div":
        print(divide(args.num1, args.num2))
    elif args.operation == "pow":
        print(power(args.num1, args.num2))
    elif args.operation == "sqrt":
        print(sqrt(args.num1))  # Only one number needed
    elif args.operation == "mod":
        print(modulo(args.num1, args.num2))
    else:
        print("Invalid operation! Use add, sub, mul, div, pow, sqrt, or mod.")

if __name__ == "__main__":
    main() 
