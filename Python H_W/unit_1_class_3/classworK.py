name = input("Enter your full name: ") 
birth = input("Enter your birth year: ") 
year = input("Enter the current year: ") 

print(f"Hello {name}, was born in {birth} and present year is {year}")



number = float(input("Enter the number: "))

if number > 0:
    print(f"the number {number} is positive")

elif number == 0:
    print(f"the number is Zero")

else:
    print(f"the number {number} is negative.")




num_1 = float(input("Enter the first number: "))
num_2 = float(input("Enter the second number: "))
num_3 = float(input("Enter the third number: "))

if num_1 >= num_2 and num_1 >= num_3:
    largest = num_1

elif num_2 >= num_1 and num_2 >= num_3:
    largest = num_2

else:
    largest = num_3

print(f"The largest number is: {largest}")


number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"The number {number} is even.")
else:
    print(f"The number {number} is odd.")

if number % 5 == 0:
    print(f"The number {number} is divisible by 5.")
else:
    print(f"The number {number} is not divisible by 5.")