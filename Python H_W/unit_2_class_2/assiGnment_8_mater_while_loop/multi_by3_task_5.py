z = 3
while z < 30:
    print(z, end=", " if z < 27 else "\n")  # Output: 3, 6, 9, 12, 15, 18, 21, 24, 27
    z += 3
