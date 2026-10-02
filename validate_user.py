def validate_user(username, password):
    if username == "admin" and password == "python123":
        return "Valid"
    return "Invalid"


def main():
    username = input("Enter username: ")
    password = input("Enter password: ")
    print("User:", validate_user(username, password))


if __name__ == "__main__":
    main()