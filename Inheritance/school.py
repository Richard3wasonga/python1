class Student:
    def __init__(self,name,age,marks):
        self.name = name
        self.age = age
        self.marks = marks

sophie = Student("Sophie",19,85)
kylie = Student("Kylie",20,95)
beth = Student("Beth",21,90)



class Course:
    def __init__(self,course_name):
        self.course_name = course_name
        self.students = []

    def add_student(self,student):
        self.students.append(student)

    def course_average(self):
        count = 0
        for student in self.students:
            count += student.marks

        print(count / len(self.students))


medicine = Course("medicine")
medicine.add_student(kylie)
medicine.add_student(beth)
medicine.add_student(sophie)
medicine.course_average()
