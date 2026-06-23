def calculator():
    print("===== Calculator =====")
    print("Operations:")
    print("+  : Addition")
    print("-  : Subtraction")
    print("*  : Multiplication")
    print("/  : Division")
    print("%  : Modulus")
    print("** : Power")
    print("Type 'exit' to quit\n")

    while True:
        operation = input("Enter operation (+, -, *, /, %, **): ")

        if operation.lower() == "exit":
            print("Calculator closed.")
            break

        if operation not in ['+', '-', '*', '/', '%', '**']:
            print("Invalid operation! Try again.\n")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if operation == '+':
                result = num1 + num2

            elif operation == '-':
                result = num1 - num2

            elif operation == '*':
                result = num1 * num2

            elif operation == '/':
                if num2 == 0:
                    print("Error: Cannot divide by zero!\n")
                    continue
                result = num1 / num2

            elif operation == '%':
                if num2 == 0:
                    print("Error: Cannot perform modulus by zero!\n")
                    continue
                result = num1 % num2

            elif operation == '**':
                result = num1 ** num2

            print(f"Result: {result}\n")

        except ValueError:
            print("Please enter valid numbers!\n")


# Run the calculator
calculator()