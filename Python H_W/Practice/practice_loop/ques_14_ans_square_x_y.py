x, y = map(int, input("Enter X and Y: ").split())       # Output: Enter X and Y: 12 25
while x <= y:
    print(x**2, end=", ")
    x += 1
print("Reached!")       # Output: 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, Reached!
