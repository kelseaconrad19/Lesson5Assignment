# Task 1: Create functions for each arithmetic operation.
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


# Task 2: Implement user input to receive numbers and an operation choice.
num1 = int(input("What is your first number?: "))
operation = input("What operation do you want to perform? Type +, -, *, or /: ")
num2 = int(input("What is your second number?: "))
# Task 3: Ensure your program can handle division by zero and other potential errors.
if operation == "+":
    result = add(num1, num2)
    print(result)
elif operation == "-":
    result = subtract(num1, num2)
    print(result)
elif operation == "*":
    result = multiply(num1, num2)
    print(result)
elif operation == "/":
    if num2 == 0:
        print("Invalid operation")
    else:
        result = divide(num1, num2)
        print(result)
else:
    print("Invalid operation")
