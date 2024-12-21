# Base class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def person_info(self):
        return f"Name: {self.name}, Age: {self.age}"


# Derived class 1
class Employee(Person):
    def __init__(self, name, age, employee_id):
        Person.__init__(self, name, age)  # Call the base class constructor explicitly
        self.employee_id = employee_id

    def employee_info(self):
        return f"Employee ID: {self.employee_id}"


# Derived class 2
class Student(Person):
    def __init__(self, name, age, student_id):
        Person.__init__(self, name, age)  # Call the base class constructor explicitly
        self.student_id = student_id

    def student_info(self):
        return f"Student ID: {self.student_id}"


# Final derived class
class Intern(Employee, Student):
    def __init__(self, name, age, employee_id, student_id, stipend):
        # Explicitly call both parent class constructors
        Employee.__init__(self, name, age, employee_id)
        Student.__init__(self, name, age, student_id)
        self.stipend = stipend

    def intern_info(self):
        return (
            f"{self.person_info()}, {self.employee_info()}, "
            f"{self.student_info()}, Stipend: {self.stipend} USD"
        )


# Using the classes
intern = Intern("Alice", 22, "E123", "S456", 500)
print(intern.intern_info())
