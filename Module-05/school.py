class Student:
    def __init__(self, name,current_class, id):
        self.name = name
        self.current_class = current_class
        self.id = id
    
    def __repr__(self) -> str:
        return f'Student with name {self.name}, class: {self.current_class}, id: {self.id}'
    
class Teacher:
    def __init__(self, name, subject, id):
        self.name = name
        self.subject = subject
        self.id = id
    
    def __repr__(self) -> str:
        return f'Teacher with name {self.name}, subject: {self.subject}, id: {self.id}'

class School:
    def __init__(self, name) -> None:
        self.name = name
        self.teachers = []
        self.students = [

        ]

    def add_teacher(self, name, subject):
        id = len(self.teachers) + 100
        teacher = Teacher(name, subject, id)
        self.teachers.append(teacher)

    def enroll(self, name, fee):
        if fee < 6500:
            return 'not enough fee'
        else:
            id = len(self.students) + 1
            student = Student(name, 'C', id)
            self.students.append(student)
            return f'{name} is enrolled with id: {id} and extra money = {fee - 6500}'
        
    def __repr__(self) -> str:
        result = f'Welcome to {self.name}\n'
        result += '---------Our Teachers---------\n'
        for teacher in self.teachers:
            result += str(teacher) + '\n'
        result += '---------Our Students---------\n'
        for student in self.students:
            result += str(student) + '\n'
        return result



# Margaret = Student('Margaret Thatcher', 9, 1)
# Donald = Student('Donald Trump', 9, 1)
# Joe = Student('Joe Biden', 9, 1)
# Stephen = Student('Stephen Hawkings', 9, 1)


# Newton = Teacher('Newton', 'Physics', 1)

# print(Margaret)
# print(Newton)

phitron = School('Phitron')
phitron.enroll('Donald Trump', 5220)
phitron.enroll('Joe Biden', 12220)
phitron.enroll('Bill Clinton', 9220)
phitron.enroll('John Kenedy', 25020)


phitron.add_teacher('NewTon', 'Phy')
phitron.add_teacher('Stephen Hawkings', 'Che')
phitron.add_teacher('Aristotle', 'PS')


print(phitron)