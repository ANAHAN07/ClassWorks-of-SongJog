with open("unit_2_class_10\Assignment_11\quotes.txt", "r") as file:
    content = file.read()
    word_count = len(content.split())
    print(f"Total number of words: {word_count}")  # Output: Total number of words: 113