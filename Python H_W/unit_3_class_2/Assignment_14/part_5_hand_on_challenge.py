import time

def log_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time:.4f} seconds")  # Output: Execution time: 0.0000 seconds
        return result
    return wrapper

class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def display_details(self):
        print(f"Name: {self.name}, Position: {self.position}, Salary: {self.salary}")

    @log_execution_time
    def increase_salary(self, percentage):
        increase = self.salary * (percentage / 100)
        self.salary += increase
        print(f"Salary increased by {percentage}%")

    @staticmethod
    def tax_bracket(salary):
        if salary < 40000:
            return "Low"
        elif 40000 <= salary <= 80000:
            return "Medium"
        else:
            return "High"

emp_1 = Employee("Madara", "Developer", 80000)
emp_1.display_details()                 # Output: Name: Madara, Position: Developer, Salary: 80000
emp_1.increase_salary(10)               # Output: Salary increased by 10%
print(Employee.tax_bracket(emp_1.salary))  # Output: High

emp_2 = Employee("Obito", "Developer", 30000)
emp_2.display_details()                 # Output: Name: Obito, Position: Developer, Salary: 30000
emp_2.increase_salary(10)               # Output: Salary increased by 10% 
print(Employee.tax_bracket(emp_2.salary))  # Output: Low