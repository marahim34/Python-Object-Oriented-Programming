from school import School
from person import Student, Teacher
from subject import Subject
from classroom import ClassRoom

school = School("XYZ School", "Finland")

# Adding classroom
seven = ClassRoom("Seven")
eight = ClassRoom("Eight")
nine = ClassRoom("Nine")

school.add_classroom(seven)
school.add_classroom(eight)
school.add_classroom(nine)

# Adding student
donald = Student("Donald Trump", eight)
joe = Student("Joe Biden", seven)
elon = Student("Elon Mask", eight)
austin = Student("Steve Austin", nine)

school.student_admission(donald)
school.student_admission(joe)
school.student_admission(elon)
school.student_admission(austin)

# Adding teachers
newton = Teacher("NewTon")
stephen = Teacher("Stephen Hawking")
aristotle = Teacher("Aristotle")
rousseau = Teacher("Rousseau")

# Adding subjects
mathematics = Subject("Mathematics", newton)
physics = Subject("Physics", stephen)
biology = Subject("Biology", aristotle)
philosophy = Subject("Philosophy", rousseau)

eight.add_subject(mathematics)
eight.add_subject(physics)
nine.add_subject(biology)
nine.add_subject(philosophy)
seven.add_subject(mathematics)
seven.add_subject(physics)

eight.take_semester_final_exam()

print(school)
