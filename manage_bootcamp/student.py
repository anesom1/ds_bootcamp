file = "bootcamp.txt"

class Student:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def add_student(self):
        name = input("What is the student's name? ")
        age = input("What is the studen's age? ")
        email = input("What is the student's e-mail address? ")
        
        with open(file, 'a') as f:
            f.write(f"{name} {age} {email}\n")
        print("Student added.")


    def remove_student(self):
        n = input("What is the student's name that should be removed?")

        with open(file, "r") as f:
            lines = f.readlines()
        with open("bootcamp.txt", "w") as f:
            for line in lines:
                if not line.startswith(n + " "):
                    f.write(line)
        print("Student removed.")


    def list_students(self):
         with open(file, 'r') as f:
             data = f.read()
             print("Here is the list of all students:")
             print(data)

    def search_student(self):
        n = input("Give the student's name to search: ")

        with open(file, "r") as f:
            lines = f.readlines()
            for line in lines:
                if n in line:
                    print("Student found:")
                    print(line)






