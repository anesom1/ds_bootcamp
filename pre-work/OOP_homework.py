class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def describe(self):
        print(f"{self.name} is {self.age} years old.")

class Student(Person):
    def __init__(self, name, age, student_id, gender):
        Person.__init__(self, name, age)
        self.student_id = student_id
        self.gender = gender

    def describe(self):
        super().describe()
        print(f"{self.name} is {self.age} years old {self.gender} with id: {self.student_id} ")

class Course():
    def __init__(self, name, teacher, students):
        self.name = name
        self.teacher = teacher
        self.students = []
    
    def add_student(self, student):
        self.students.append(student)

    def list_students(self):
        for student in self.students:
            print(student.name)


st1 = Student("John", 21, 1, "male")
st2 = Student("Maria", 35, 2, "female")
st3 = Student("Kate", 28, 4, "male")

c1 = Course("Data Science", "John D", [] )

c1.add_student(st1)
c1.add_student(st2)
c1.add_student(st3)


c1.list_students()