num_list = [228, 424, 129, 6222, 134, 494, 3416, 2993, 919, 2013]
odd_sum = even_sum = odd_count = even_count = 0

for idx, num in enumerate(num_list):
    if num % 2 == 0:
        even_count += 1
        even_sum += idx
    else:
        odd_count += 1
        odd_sum += idx
        
print("Odd numbers:", odd_count)                        # Output: Odd numbers: 4
print("Even numbers:", even_count)                      # Output: Even numbers: 6
print("Sum of indices of odd numbers:", odd_sum)        # Output: Sum of indices of odd numbers: 26
print("Sum of indices of even numbers:", even_sum)      # Output: Sum of indices of even numbers: 19
