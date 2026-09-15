from calculator import add, subtract, multiply, divide


def main():
    print("Welcome to the Calculator!")
    print("Operations: add, subtract, multiply, divide")
    print("Type 'exit' to quit.")

    while True:
        operation = input("\nEnter an operation: ").lower()

        if operation == "exit":
            print("Goodbye!")
            break

        if operation not in ["add", "subtract", "multiply", "divide"]:
            print("Invalid operation. Please try again.")
            continue

        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if operation == "add":
                result = add(num1, num2)
            elif operation == "subtract":
                result = subtract(num1, num2)
            elif operation == "multiply":
                result = multiply(num1, num2)
            else:
                result = divide(num1, num2)

            print(f"Result: {result}")

        except ValueError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()