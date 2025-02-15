times = list(map(int, input("Enter finish times: ").split()))   # Output: Enter finish times: 12 9 15 8 10

sorted_times = sorted(enumerate(times), key=lambda x: x[1])

print("First Place:", sorted_times[0][0])       # Output: First Place: 3
print("Second Place:", sorted_times[1][0])      # Output: Second Place: 1
print("Third Place:", sorted_times[2][0])       # Output: Third Place: 4
