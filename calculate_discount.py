def calculate_discount(purchase_amount):
    if purchase_amount < 0:
        raise ValueError("Purchase amount cannot be negative.")

    if purchase_amount >= 5000:
        discount_rate = 0.20
    elif purchase_amount >= 3000:
        discount_rate = 0.10
    else:
        discount_rate = 0.05

    discount_amount = purchase_amount * discount_rate
    final_amount = purchase_amount - discount_amount
    return discount_amount, final_amount


def main():
    try:
        purchase_amount = float(input("Enter the purchase amount in rupees: "))
        discount, final_amount = calculate_discount(purchase_amount)

        print(f"Discount amount: Rs. {discount:.2f}")
        print(f"Final payable amount: Rs. {final_amount:.2f}")
    except ValueError as error:
        print("Error:", error)


if __name__ == "__main__":
    main()