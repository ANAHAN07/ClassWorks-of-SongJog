naruto_info = {
    "Naruto Uzumaki": {"Rank": "Hokage", "Age": 32, "Special Ability": "Nine-Tails Chakra Mode"},
    "Sasuke Uchiha": {"Rank": "Rogue Ninja", "Age": 32, "Special Ability": "Rinnegan & Sharingan"},
    "Kakashi Hatake": {"Rank": "Hokage (Retired)", "Age": 48, "Special Ability": "Sharingan & Lightning Blade"},
    "Shikamaru Nara": {"Rank": "Jonin", "Age": 32, "Special Ability": "Shadow Possession Jutsu"},
    "Hinata Hyuga": {"Rank": "Chunin", "Age": 32, "Special Ability": "Byakugan & Gentle Fist"},
    "Gaara": {"Rank": "Kazekage", "Age": 32, "Special Ability": "Sand Manipulation"}
}


for name, info in naruto_info.items():
    print(f"{name}: Rank - {info['Rank']}, Age - {info['Age']}, Special Ability - {info['Special Ability']}")

print(naruto_info["Naruto Uzumaki"])


stud_grade = [
    {"Name":"Uchiha MADARA", "grade": "S++"},
    {"Name": "Obito Uchiha", "grade": "S+"} ,
    {"Name": "Itachi Uchiha", "grade": "S+"},
]

print(stud_grade)