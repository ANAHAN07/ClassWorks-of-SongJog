Counter = input("Enter the word: ")         # Output: Enter the word: Gigabyte

vowel_count = sum(1 for char in Counter.lower() if char in "aeiou")
print("Number of vowels:", vowel_count)     # Output: Number of vowels: 3