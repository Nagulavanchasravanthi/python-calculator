def calculator():
    print("🧮 Welcome to the Python Calculator!")
    print("You can use +, -, *, / operators.")
    print("Type 'exit' or 'quit' at any time to stop.\n")

    while True:
        num1_input = input("Enter the first number (or 'exit'/'quit'): ")
        if num1_input.lower() in ['exit', 'quit']:
            print("👋 Thanks for using the calculator!")
            break

        operator = input("Enter operator (+, -, *, /): ")
        if operator.lower() in ['exit', 'quit']:
            print("👋 Thanks for using the calculator!")
            break

        num2_input = input("Enter the second number (or 'exit'/'quit'): ")
        if num2_input.lower() in ['exit', 'quit']:
            print("👋 Thanks for using the calculator!")
            break

        try:
            num1 = float(num1_input)
            num2 = float(num2_input)

            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 == 0:
                    print("❌ Error: Division by zero is not allowed.\n")
                    continue
                result = num1 / num2
            else:
                print("❌ Invalid operator. Use +, -, *, or /.\n")
                continue

            print(f"✅ Result: {num1} {operator} {num2} = {result}\n")

        except ValueError:
            print("❌ Invalid input. Please enter valid numbers.\n")

calculator()
