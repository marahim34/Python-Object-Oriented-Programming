# Base class 1
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def person_info(self):
        return f"Name: {self.name}, Age: {self.age}"


# Base class 2
class Employee:
    def __init__(self, employee_id, department):
        self.employee_id = employee_id
        self.department = department

    def employee_info(self):
        return f"Employee ID: {self.employee_id}, Department: {self.department}"


# Derived class
class Manager(Person, Employee):
    def __init__(self, name, age, employee_id, department, team_size):
        Person.__init__(self, name, age)  # Initialize Person attributes
        Employee.__init__(
            self, employee_id, department
        )  # Initialize Employee attributes
        self.team_size = team_size

    def manager_info(self):
        return (
            f"{self.person_info()}, {self.employee_info()}, "
            f"Team Size: {self.team_size}"
        )


# Using the classes
manager = Manager("Alice", 35, "E123", "IT", 10)
print(manager.manager_info())
