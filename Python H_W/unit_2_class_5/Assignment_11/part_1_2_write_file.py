quotes = [
    "Hard work is worthless for those that don't believe in themselves."" "" - Naruto Uzumaki",
    "The moment people come to know love, they run the risk of carrying hate."" "" - Obito Uchiha",
    "Growth occurs when one goes beyond one's limits. Realizing that is also part of training."" "" - Itachi Uchiha",
    "The concept of hope is nothing more than giving up. A word that holds no true meaning."" ""- Madara Uchiha",
    "To Protect Something... Another Must be Sacrificed."" "" - Madara Uchiha"
]

with open("quotes.txt", "w") as file:
    for quote in quotes:
        file.write(quote + "\n")


# Output: Hard work is worthless for those that don't believe in themselves.  - Naruto Uzumaki
         #  The moment people come to know love, they run the risk of carrying hate.  - Obito Uchiha
         #  Growth occurs when one goes beyond one's limits. Realizing that is also part of training.  - Itachi Uchiha
         #  The concept of hope is nothing more than giving up. A word that holds no true meaning. - Madara Uchiha
         #  To Protect Something... Another Must be Sacrificed.  - Madara Uchiha