required_skills = ["Python", "SQL", "git", "html" , "css"]


def check_skill(skill_name):
    available_skills = [skill.lower() for skill in required_skills]
    if skill_name.strip().lower() in available_skills:
        return "Skill available"
    return "Skill not available"


def main():
    skill_name = input("Enter a skill name: ")
    print(check_skill(skill_name))


if __name__ == "__main__":
    main()