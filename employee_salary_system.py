# Base Class
class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary


# Subclass 1: Manager
class Manager(Employee):
    def calculate_salary(self):
        bonus = 0.20 * self.base_salary   # 20% bonus
        return self.base_salary + bonus


# Subclass 2: Developer
class Developer(Employee):
    def calculate_salary(self):
        bonus = 0.10 * self.base_salary   # 10% bonus
        return self.base_salary + bonus


# Subclass 3: Intern
class Intern(Employee):
    def calculate_salary(self):
        deduction = 0.05 * self.base_salary   # 5% deduction
        return self.base_salary - deduction


# Creating objects
manager = Manager("Anita", 80000)
developer = Developer("Rahul", 60000)
intern = Intern("Sneha", 20000)

employees = [manager, developer, intern]

# Display salary details
for emp in employees:
    print("Name:", emp.name)
    print("Final Salary:", emp.calculate_salary())
    print("----------------------")