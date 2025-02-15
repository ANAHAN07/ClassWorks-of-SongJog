i = int(input("Enter number: "))            # Output: Enter number: 5647645

count = sum(1 for i in range(1, i + 1) if i % 3 == 0 and i % 7 == 0)
print("Count:", count)      # Output: Count: 268935
