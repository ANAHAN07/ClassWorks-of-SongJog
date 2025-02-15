g = 75
a, b = 0, 1
while a <= g:
    print(a, end=", " if b <= g else "\n")  # Output: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55A
    a, b = b, a + b
