p = int(input("Enter lines: "))         # Output: Enter lines: 13
for i in range(1, p + 1):
    print("".join(str(j) for j in range(1, i + 1)))


# Output:

"""
        1
        12
        123
        1234
        12345
        123456
        1234567
        12345678
        123456789
        12345678910
        1234567891011
        123456789101112
        12345678910111213
"""