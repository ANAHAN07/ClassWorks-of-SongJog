Brand = ["Tesla", "Cyber truck", "Tesla Type X", "Tesla Type Y"]

while Brand:
    print(Brand)
    Brand.pop(0)

print(Brand)


# Output: ['Tesla', 'Cyber truck', 'Tesla Type X', 'Tesla Type Y']
# Output: ['Cyber truck', 'Tesla Type X', 'Tesla Type Y']
# Output: ['Tesla Type X', 'Tesla Type Y']
# Output: ['Tesla Type Y']
# Output: []
