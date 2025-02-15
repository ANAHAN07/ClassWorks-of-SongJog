with open("unit_2_class_10\Assignment_11\student.txt", "r") as file:
    for line_num, line in enumerate(file, start=1):
        print(f"{line_num}: {line.strip()}")  # Output: 1: Name: Ali, Age: 20, Subjects: Math: 85, Science: 90
                                                    #   2: Name: Adrik, Age: 22, Subjects: Math: 75, Science: 80
                                                    #   3: Name: Zarif, Age: 21, Subjects: Math: 95, Science: 85
                                                    #   4: Name: Hecky, Age: 18, Subjects: Math: 70, Science: 69