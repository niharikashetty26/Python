def basic_calculator():
    while True:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operator = input("Enter an operator (+, -, *, /) or 'q' to quit= ")

        if operator == 'q':
            break
        elif operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                print("Error: Division by zero.")
                continue
            result = num1 / num2
        else:
            print("Invalid operator.")
            continue

        print(f"Result: {num1} {operator} {num2} = {result}")
print(basic_calculator())