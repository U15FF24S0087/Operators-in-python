def calculate(first_number, operator, second_number):
    if operator == "+":
        return first_number + second_number
    if operator == "-":
        return first_number - second_number
    if operator == "*":
        return first_number * second_number
    if operator == "/":
        if second_number == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return first_number / second_number
    if operator == "//":
        if second_number == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return first_number // second_number
    if operator == "%":
        if second_number == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return first_number % second_number
    raise ValueError("Unsupported operator. Use +, -, *, /, //, or %.")


def main():
    try:
        first_number = float(input("Enter the first number: "))
        operator = input("Enter an operator (+, -, *, /, //, %): ").strip()
        second_number = float(input("Enter the second number: "))

        result = calculate(first_number, operator, second_number)
        print("Result:", result)
    except (ValueError, ZeroDivisionError) as error:
        print("Error:", error)


if __name__ == "__main__":
    main()