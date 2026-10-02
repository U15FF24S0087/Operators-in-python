def determine_placement(age, marks, attendance, experience, has_backlog):
    experience_categories = {
        "0": "Fresher",
        "1-2": "Junior",
        ">2": "Experienced",
    }

    if experience not in experience_categories:
        raise ValueError('Experience must be "0", "1-2", or ">2".')

    is_eligible = marks >= 60 and attendance >= 75 and not has_backlog
    placement_status = "Yes" if is_eligible else "No"
    candidate_category = experience_categories[experience]
    return placement_status, candidate_category


def main():
    try:
        age = int(input("Enter the candidate's age: "))
        marks = float(input("Enter marks percentage: "))
        attendance = float(input("Enter attendance percentage: "))
        experience = input('Enter experience ("0", "1-2", or ">2"): ').strip()
        backlog_answer = input("Does the candidate have a backlog? (yes/no): ").strip().lower()

        if backlog_answer not in ("yes", "no"):
            raise ValueError("Backlog answer must be yes or no.")

        has_backlog = backlog_answer == "yes"
        
        placement_status, candidate_category = determine_placement(
            age, marks, attendance, experience, has_backlog
        )

        print("Placement eligible:", placement_status)
        print("Candidate category:", candidate_category)
    except ValueError as error:
        print("Error:", error)


if __name__ == "__main__":
    main()