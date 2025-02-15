z = 10

for i in range(1, z + 1):
    print(''.join(str(j) for j in range(1, i + 1)))


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
"""