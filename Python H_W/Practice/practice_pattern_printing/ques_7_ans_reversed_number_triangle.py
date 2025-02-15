x = 15

for i in range(1, x + 1):
    print(''.join(str(j) for j in range(i, 0, -1)))

# Output:

"""
    1
    21
    321
    4321
    54321
    654321
    7654321
    87654321
    987654321
    10987654321
    1110987654321
    121110987654321
    13121110987654321
    1413121110987654321
    151413121110987654321
"""


# Here the number are started from right side and ends in left side. like : 6, 5, 4, 3, 2, 1 (reverse counting)