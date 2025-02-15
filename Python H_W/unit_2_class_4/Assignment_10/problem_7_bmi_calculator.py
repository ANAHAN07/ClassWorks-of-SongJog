def calculate_bmi():
    def get_positive_float(cmd):
        while True:
            try:
                value = float(input(cmd))
                if value > 0:
                    return value
                else:
                    print("Please enter a positive number.")         # Output: Please enter a positive number.
            except:
                print("Invalid input. Please enter a valid number.")  # Output: Invalid input. Please enter a valid number.
    
    
    weight = get_positive_float("Enter your weight in kilograms: ")          # Output: Enter your weight in kilograms: 51
    height_in_feet = get_positive_float("Enter your height in feet: ")       # Output: Enter your height in feet: 5.5
    
    height_in_meters = height_in_feet * 0.3048    # (1 foot = 0.3048 meters)

    bmi = weight / (height_in_meters ** 2)
    bmi = round(bmi, 2)

    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal weight"
    elif 25 <= bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obesity"

    print(f"\nYour BMI is: {bmi}")                  # Output: Your BMI is: 18.15
    print(f"You are categorized as: {category}")    # Output: You are categorized as: Underweight

calculate_bmi()