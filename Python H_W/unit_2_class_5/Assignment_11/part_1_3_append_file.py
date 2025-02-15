more_quotes = [
    "When a man learns to love, he also has to endure the pain."" "" - Obito Uchiha",
    "It is too late for regret."" "" - Obito Uchiha" ,
    "I won't let my comrades die."" "" - Kakashi Hatake"
]

with open("unit_2_class_10\Assignment_11\quotes.txt", "a") as file:
    for quote in more_quotes:
        file.write(quote + "\n")


# Output: When a man learns to love, he also has to endure the pain.  - Obito Uchiha
        #   It is too late for regret.  - Obito Uchiha
        #   I won't let my comrades die.  - Kakashi Hatake