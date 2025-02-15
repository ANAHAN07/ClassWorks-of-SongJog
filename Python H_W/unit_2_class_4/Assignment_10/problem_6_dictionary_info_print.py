def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key.capitalize()}")
        for sub_key, sub_value in value.items():
            print(f"  {sub_key.capitalize()}: {sub_value}")
        print()

print_info(
    obito={"age": 31, "role": "Antagonist"},
    madara={"age": 90, "role": "Legendary Shinobi"},
    itachi={"age": 21, "role": "Antihero"},
    kakashi={"age": 30, "role": "Sensei"},
    naruto={"age": 17, "role": "Protagonist"}
)



# Output: Obito
        #   Age: 31
        #   Role: Antagonist
# Output: Madara
        #    Age: 90
        #    Role: Legendary Shinobi
# Output: Itachi
        #    Age: 21
        #    Role: Antihero
# Output: Kakashi
        #    Age: 30
        #    Role: Antihero
# Output: Naruto
        #    Age: 17
        #    Role: Protagonist
