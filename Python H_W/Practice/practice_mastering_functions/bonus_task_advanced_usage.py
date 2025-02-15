def student_grades(**grades):
    return "\n".join([f"{student}: {grade}%" for student, grade in grades.items()])

print(student_grades(Madara=100,Obito=99, Itachi=97, Kakashi=95, Naruto=92, Shikamaru=91, Sasuke=90, Hinata=85))

# Output:

"""
        Madara: 100%
        Obito: 99%
        Itachi: 97%
        Kakashi: 95%
        Naruto: 92%
        Shikamaru: 91%
        Sasuke: 90%
        Hinata: 85%
"""