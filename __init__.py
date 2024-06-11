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

def main():
    print("Welcome to the simple calculator!")

    while True:
        print("Choose an operation: +, -, *, / or type 'exit' to quit")
        operation = input()

        if operation == "exit":
            break

        if operation not in ['+', '-', '*', '/']:
            print("Invalid operation. Please try again.")
            continue

        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        if operation == '+':
            print(f"Result: {add(num1, num2)}")
        elif operation == '-':
            print(f"Result: {subtract(num1, num2)}")
        elif operation == '*':
            print(f"Result: {multiply(num1, num2)}")
        elif operation == '/':
            print(f"Result: {divide(num1, num2)}")

    print("Thank you for using the calculator. Goodbye!")

if __name__ == "__main__":
    main()
