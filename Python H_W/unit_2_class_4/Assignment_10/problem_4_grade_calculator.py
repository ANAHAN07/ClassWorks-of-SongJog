def calcul_grade(marks):
    if marks >= 90:
        return "Grade A"
    elif marks >= 80:
        return "Grade B"
    elif marks >= 70:
        return "Grade C"
    elif marks >= 40:
        return "Grade D"
    else:
        return "Grade F"

print(calcul_grade(85))  # Output: "Grade B"