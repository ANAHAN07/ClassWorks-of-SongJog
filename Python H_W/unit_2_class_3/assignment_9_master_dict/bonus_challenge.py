employee = {
    420: {"Name": "Kishimoto", "Age": 30, "Department": "HR"},
    204: {"Name": "Obito", "Age": 25, "Department": "Engineering"},
    469: {"Name": "RIN", "Age": 28, "Department": "Engineering"}
}

department = "Engineering"
for emp_id, details in employee.items():
    if details["Department"] == department:
        print(details["Name"]) # Output: Obito
                                    # RIN
                                    