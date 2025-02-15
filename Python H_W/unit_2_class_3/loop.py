my_info = {
    "Name": "AHAN",
    "Age": 16, 
    "Blood group": "B+",
    "School":"Willes Little Flower School and Collage"
    }

for key in my_info.keys():
    print(key)

for value in my_info.values():
    print(value)

for key, values in my_info.items():
    print(f"{key} : {value}")
