def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y

def modulus(x, y):
    return x % y

def exponentiate(x, y):
    return x ** y
def calculator():
    print("Welcome to the Python Calculator!")
    print("Select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    operation = input("Enter the number of the operation (1-6): ")
    if operation not in ['1', '2', '3', '4', '5', '6']:
        print("Invalid operation. Please try again.")
        return
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return
    if operation == '1':
        print(f"The result of addition: {add(num1, num2)}")
    elif operation == '2':
        print(f"The result of subtraction: {subtract(num1, num2)}")
    elif operation == '3':
        print(f"The result of multiplication: {multiply(num1, num2)}")
    elif operation == '4':
        print(f"The result of division: {divide(num1, num2)}")
    elif operation == '5':
        print(f"The result of modulus: {modulus(num1, num2)}")
    elif operation == '6':
        print(f"The result of exponentiation: {exponentiate(num1, num2)}")
calculator()
