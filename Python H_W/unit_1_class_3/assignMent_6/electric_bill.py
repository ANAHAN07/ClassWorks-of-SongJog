units = int(input("Enter the number of units: ")) # Output: Enter the number of units: 69
bill = 0

if units <= 100:
    bill = units * 0.5
elif units <= 200:
    bill = 100 * 0.5 + (units - 100) * 0.75
else:
    bill = 100 * 0.5 + 100 * 0.75 + (units - 200) * 1

print(f"Total electricity bill: ${bill:.2f}") # Output: Total electricity bill: $34.50
print("Pay the Bill as soon as possible, otherwise your electricity will be cut off.") # Output: Pay the Bill as soon as possible, otherwise your electricity will be cut off.
