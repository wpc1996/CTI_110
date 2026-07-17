# William Littelfield
# July 15 2026
# P5Lab
# Cashier Register


import random

def disperse_change(change):
    change = round(change * 100)  # Convert to cents
   
    if change == 0:
        print("No change")

    num_dollars = change // 100
    change = change - (num_dollars * 100)

    num_quarters = change // 25
    change = change - (num_quarters * 25)

    num_dimes = change // 10
    change = change - (num_dimes * 10)

    num_nickels = change // 5
    change = change - (num_nickels * 5)

    num_pennies = change // 1
    change = change - (num_pennies * 1)

        

    if num_dollars > 0:
        if num_dollars == 1:
            print(f"{num_dollars} Dollar")
        else:
            print(f"{num_dollars} Dollars")

    if num_quarters > 0:
        if num_quarters == 1:
            print(f"{num_quarters} Quarter")
        else:
            print(f"{num_quarters} Quarters")

    if num_dimes > 0:
        if num_dimes == 1:
            print(f"{num_dimes} Dime")
        else:
            print(f"{num_dimes} Dimes")

    if num_nickels > 0:
        if num_nickels == 1:
            print(f"{num_nickels} Nickel")
        else:
            print(f"{num_nickels} Nickels")

    if num_pennies > 0:
        if num_pennies == 1:
            print(f"{num_pennies} Penny")
        else:
            print(f"{num_pennies} Pennies")

def main():
    print()

    # Generate random amount owed
    amount_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"Amount owed: ${amount_owed:.2f}")

    # Get user input
    money_given = float(input("How much Cash will you give Self-Checkout? $"))

    # Calculate change
    change = round(money_given - amount_owed, 2)
    print(f"Change owed: ${change:.2f}\n")

    # Call your function
    disperse_change(change)


main()
