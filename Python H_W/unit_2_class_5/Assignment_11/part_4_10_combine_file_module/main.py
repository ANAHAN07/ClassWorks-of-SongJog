import stats

with open("numbers.txt", "r") as file:
    numbers = [int(line.strip()) for line in file]

average = stats.calculate_average(numbers)
maximum = stats.calculate_maximum(numbers)

with open("results.txt", "w") as file:
    file.write(f"Average: {average}\n")
    file.write(f"Maximum: {maximum}\n")

print("Results have been written to 'results.txt'.")
