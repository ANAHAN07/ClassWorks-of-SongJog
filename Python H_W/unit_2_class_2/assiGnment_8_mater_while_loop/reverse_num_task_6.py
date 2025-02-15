number = 69694206969
reverse = 0
while number > 0:
    reverse = reverse * 10 + number % 10
    number //= 10
print(f"Reversed number: {reverse}")   # Output: Reversed number: 96960249696
