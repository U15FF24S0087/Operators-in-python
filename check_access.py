def check_access(age, has_id, is_employee):
    if (age >= 18 and has_id) or is_employee:
        return "Access granted"
    return "Access denied"


def ask_yes_no(prompt):
    answer = input(prompt).strip().lower()
    if answer not in ("yes", "no"):
        raise ValueError("Please answer yes or no.")
    return answer == "yes"


def main():
    try:
        age = int(input("Enter your age: "))
        has_id = ask_yes_no("Do you have an ID? (yes/no): ")
        is_employee = ask_yes_no("Are you an employee? (yes/no): ")
        print(check_access(age, has_id, is_employee))
    except ValueError as error:
        print("Error:", error)


if __name__ == "__main__":
    main()