#William Littlefield
#6-13-2026
#P1HW2
# creating a progream for basic math
#pseudocode logic

print()
print("This program calculates and displays travel expenses")
print()


budget = int(input("Enter your travel budget:"))

destination = input("Enter your travel destination:")

gas = int(input("Enter the estimated cost of gas:"))
accomodations = int(input("Enter the estimated cost of accomodations:"))
food = int(input("Enter the estimated cost of food:"))

total_expenses = gas + accomodations + food

remaining_budget = budget - total_expenses

print()

print("-------Travel Expenses-------")
print("Destination;", destination)
print("Budget: $", budget)
print()

print("gas: $", gas)
print("Accomodations: $", accomodations)
print("Food: $", food)


print()
print("Total Expenses: $", total_expenses)
print("Remaining Balance: $", remaining_budget)