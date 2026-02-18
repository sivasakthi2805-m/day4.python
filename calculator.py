def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            raise ZeroDivisionError("Error: Division by zero is not allowed.")
        return num1 / num2
    else:
        raise ValueError("Error: Invalid operator.")


try:
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    result = calculate(num1, num2, operator)
    print("Result:", result)

except ValueError:
    print("Error: Please enter valid numbers or operator.")
except ZeroDivisionError as e:
    print(e)
except Exception:
    print("Unexpected error occurred.")
finally:
    print("Calculator closed.")
