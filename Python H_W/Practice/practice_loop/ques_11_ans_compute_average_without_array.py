y = int(input("Enter compute: "))       # Output: Enter compute: 4
total = 0
for _ in range(y):
    total += int(input("Enter number: ")) 
    # Output: 
""" 
Enter number: 69
Enter number: 90
Enter number: 50
Enter number: 38 
"""
    
print("Average:", total / y)        # Output: Average: 61.75
