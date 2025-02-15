x = int(input("Enter repeat: "))       # Output: Enter repeat: 4
max_num = float('-inf')
for _ in range(x):
    num = int(input("Enter number: "))  # Output: Enter number: 9867 | Enter number: 2536 | Enter number: 9873 | Enter number: 9986 
    if num > max_num:
        max_num = num
print("Maximum:", max_num)      # Output: Maximum: 9986
