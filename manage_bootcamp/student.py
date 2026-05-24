FILE_NAME = "bootcamp.txt"
FILE_NOT_FOUND = "File not found."
EMPTY_ERROR_MSG = "Error: can't be empty!"
VALID_AGE_MSG = "Please enter valid age."
VALID_EMAIL_MSG = "Please enter valid e-mail address."
NAME_INP_MSG = "Enter student's name: "
AGE_INP_MSG = "Enter student's age? "
EMAIL_INPUT_MSG = "Enter student's e-mail address? "
REMOVE_INPUT_MSG = "Enter the name of student that should be removed? "
SEARCH_INPUT_MSG = "Enter name to search for a student: "
EMPTY_LIST_MSG = "There are no students on the list."
STUDENT_NOT_FOUND_MSG = "Student not found."
LIST_MSG = "Here is the list of all students: "
SEARCH_RESULT_MSG = "Search results: "
REMOVED_MSG = "Students removed: "


class StudentManager:
    def __init__(self, file_name=FILE_NAME):
        self.file_name = file_name
    
    def _read_lines(self):
        try:
            with open(self.file_name, "r") as f:
                return f.readlines()
        except FileNotFoundError:
            return []
        except OSError as e:
            print(f"File error: {e}")
            return []

    def add_student(self):
        while True:
            try:
                name = input(NAME_INP_MSG)
                if not name.strip():
                    raise ValueError(EMPTY_ERROR_MSG)
                break
            except ValueError as e:
                print(e)

        while True:
            try:
                age = input(AGE_INP_MSG)

                if not age.strip():
                    raise ValueError(EMPTY_ERROR_MSG)
                
                age = int(age)

                if not 1 <= age <= 100:
                    raise ValueError(VALID_AGE_MSG)
                
                break
                
            except ValueError as e:
                print(e)

        while True:
            try:
                email = input(EMAIL_INPUT_MSG)
                if not email.strip():
                    raise ValueError(EMPTY_ERROR_MSG)
                if "@" not in email or "." not in email:
                    raise ValueError(VALID_EMAIL_MSG)
                break
            except ValueError as e:
                print(e)
        
        try:
            with open(self.file_name, 'a') as f:
                f.write(f"{name},{age},{email}\n")
            print("Student added.")
        except OSError as e:
            print(f"File error: {e}")
            return
        except Exception as e:
            print(f"Unexpected error: {e}")
            return

    def remove_student(self):
        lines = self._read_lines()

        if not lines:
            print(EMPTY_LIST_MSG)
            return
        
        n = input(REMOVE_INPUT_MSG).lower()

        removed_count = 0

        try:
            with open(self.file_name, "w") as f:
                for line in lines:
                    student_name = line.split(",")[0].lower()

                    if student_name == n:
                        removed_count += 1 #will skip the line -> remove it 
                    else:
                        f.write(line) # it will keep the line/rewrite it

            if removed_count:
                print(REMOVED_MSG + str(removed_count))
            else:
                print(STUDENT_NOT_FOUND_MSG)
        except OSError as e:
            print(f"File error: {e}")
            return
        except Exception as e:
            print(f"Unexpected error: {e}")
            return
            

    def list_students(self):
        lines = self._read_lines()
        
        if not lines: 
            print(EMPTY_LIST_MSG)
            return
        print(LIST_MSG)
        print("".join(lines))
                        

    def search_student(self):
        
    
        lines = self._read_lines()
        
        if not lines:
            print(FILE_NOT_FOUND)
            return

        n = input(SEARCH_INPUT_MSG )
        print(SEARCH_RESULT_MSG)
        found = False

        for line in lines:
            student_name = line.split(",")[0]
            if student_name.lower() == n.lower():
                print(line.strip())
                found = True
            
        if not found:
            print(STUDENT_NOT_FOUND_MSG)
            
    

