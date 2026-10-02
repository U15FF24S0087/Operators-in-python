def check_result(marks):
    if marks >= 75:
        return "Distinction"
    if marks >= 35:
        return "Pass"
    return "Fail"


def main():
    try:
        marks = float(input("Enter the student's marks: "))
        print("Result:", check_result(marks))
    except ValueError:
        print("Please enter a valid number of marks.")


if __name__ == "__main__":
    main()