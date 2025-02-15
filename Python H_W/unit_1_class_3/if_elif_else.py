age = 55

if age < 5:
    print("Price of the ticket is $0")

elif age < 18:
    print("price of the ticket is $15")




# Multiple Elif :

age = 12

if age <4:
    price = 0
elif age < 18:
    price = 98
elif age <65:
    price = 88
else :
    price = 200

print(f"Your price is {price}")


# Multiple if:

c = 69
u = 30

if c > 10:
    print("C is greater than 10")
if u > 25:
    print("U is greater than 25")


number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"The number {number} is even.")
else:
    print(f"The number {number} is odd.")

if number % 5 == 0:
    print(f"The number {number} is divisible by 5.")
else:
    print(f"The number {number} is not divisible by 5.")