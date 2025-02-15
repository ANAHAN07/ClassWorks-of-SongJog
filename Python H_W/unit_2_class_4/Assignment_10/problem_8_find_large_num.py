def find_largest(*args):
    if not args:
        return "No numbers provided."
    return max(args)

numbers = (5, 10, 3, 69, 420, 1080, 720)
largest = find_largest(*numbers)
print(f"The largest number is: {largest}") # Output: 1080


# OR

def find_largest(a, b, c):
    return max(a, b, c)

print(find_largest(720, 420, 69))  # Output: 720