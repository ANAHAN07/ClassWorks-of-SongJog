language = {"Python": 1991, "Java": 1995, "C++": 1969, "CSS": 1996}

language["C++"] = 1985

language["JavaScript"] = 1995

del language["Python"]

print(language)       # Output: {'Java': 1995, 'C++': 1985, 'CSS': 1996, 'JavaScript': 1995}
