mark = int(input("Enter your marks: "))                          # Output: Enter your marks: 99
promo = ("You are promoted")                                    # Output: You are promoted
special = ("You are promoted on special conditions")           # Output: You are promoted on special conditions

if mark >= 90:
    print("Grade: A")           # Output: Grade: A
    print(promo)                # Output: You are promoted
elif mark >= 80:
    print("Grade: B")           # Output: Grade: B
    print(promo)                # Output: You are promoted
elif mark >= 70:
    print("Grade: C")           # Output: Grade: C
    print(promo)                # Output: You are promoted
elif mark >= 60:
    print("Grade: D")           # Output: Grade: D
    print(special)              # Output: You are promoted on special conditions
else:
    print("Grade: F")           # Output: Grade: F
    print("You are Failed")  # Output: You are Failed
