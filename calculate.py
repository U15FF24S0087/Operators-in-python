def calculate(a, operator, b):
    if operator == "+":
        return a + b
    if operator == "-":
        return a - b
    if operator == "*":
        return a * b
    if operator == "/":
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b
    if operator == "//":
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a // b
    if operator == "%":
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a % b
    raise ValueError("Invalid operator. Use +, -, *, /, //, or %.")