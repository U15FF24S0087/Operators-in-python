def check_eligibility(marks, attendance_percentage, has_backlog):
    if marks >= 60 and attendance_percentage >= 75 and not has_backlog:
        return "Eligible"
    return "Not eligible"


def main():
    try:
        marks = float(input("Enter the student's marks: "))
        attendance_percentage = float(input("Enter attendance percentage: "))
        backlog_status = input("Does the student have a backlog? (yes/no): ").strip().lower()

        if backlog_status not in ("yes", "no"):
            raise ValueError("Enter yes or no for backlog status.")

        has_backlog = backlog_status == "yes"
        result = check_eligibility(marks, attendance_percentage, has_backlog)
        print("Result:", result)
    except ValueError as error:
        print("Error:", error)


if __name__ == "__main__":
    main()