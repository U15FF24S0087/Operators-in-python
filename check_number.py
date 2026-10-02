def check_number(number):
    return {
        "parity": "even" if number % 2 == 0 else "odd",
        "divisible_by_3": number % 3 == 0,
        "divisible_by_5": number % 5 == 0,
    }


def main():
    try:
        number = int(input("Enter an integer: "))
        results = check_number(number)

        print(number, "is", results["parity"])
        print("Divisible by 3:", results["divisible_by_3"])
        print("Divisible by 5:", results["divisible_by_5"])
    except ValueError:
        print("Please enter a valid integer.")


if __name__ == "__main__":
    main()