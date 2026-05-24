from student import StudentManager

def open_menu():

    student = StudentManager()

    while True:
        print("Menu:")
        print("1: Add new student")
        print("2: Search for a student")
        print("3: Remove student")
        print("4: List all students")
        print("5: Exit")

        option = input("What would you like to do? ")

        if option == "1":
            student.add_student()

        elif option == "2":
            student.search_student()

        elif option == "3":
            student.remove_student()

        elif option == "4":
            student.list_students()

        elif option == "5":
            print("Good bye!")
            break

        else:
            print("Error: Select the number from 1 to 5.")


