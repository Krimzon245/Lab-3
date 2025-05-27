"""
Author: Daniel Momoh
Student Number: 041114358
Date: 2025-05-27

This program simulates a simple shopping cart.
Users can add items, specify quantities, and see the total cost.
The program uses exception handling to manage invalid inputs.
"""
print("Welcome to the Shopping Cart Program!")

try:
    total_cost = 0  # grand total

    while True:
        items = int(input("How many items do you want to buy? "))
        item_name = input("What is the name of the item you are buying? ")
        price = float(input("What is the price of the item? "))
        subtotal = items * price
        total_cost += subtotal

        more = input("Would you like to add more? (Y/N) ").strip().upper()
        if more != "Y":
            break

    # Apply discount if needed
    if total_cost > 100:
        discount = total_cost * 0.1
        total_cost -= discount
        print(f"\nYou saved ${discount:.2f} with a 10% discount!")

    print(f"\nFinal total: ${total_cost:.2f}")
    print("Thank you for shopping with us!")

except ValueError:
    print("Invalid input! Please enter numbers only where expected.")
