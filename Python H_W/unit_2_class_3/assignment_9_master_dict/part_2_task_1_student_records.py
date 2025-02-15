students = {
    1: {"Name": "Ali", "Age": 20, "Subjects": {"Math": 85, "Science": 90}},
    2: {"Name": "Adrik", "Age": 22, "Subjects": {"Math": 75, "Science": 80}},
    3: {"Name": "Zarif", "Age": 21, "Subjects": {"Math": 95, "Science": 85}}
}


print("Name:", students[2]["Name"])             # Output: Name: Adrik
print("Age:", students[2]["Age"])               # Output: Age: 22

students[1]["Subjects"]["English"] = 88       

students[3]["Subjects"]["Math"] = 98            

print(students)                     # Output:  {1: {'Name': 'Ali', 'Age': 20, 'Subjects': {'Math': 85, 'Science': 90, 'English': 88}}, 
                                            #  2: {'Name': 'Adrik', 'Age': 22, 'Subjects': {'Math': 75, 'Science': 80}},
                                            #  3: {'Name': 'Zarif', 'Age': 21, 'Subjects': {'Math': 98, 'Science': 85}}}
