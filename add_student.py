from student import StudentInfo 

class AddStudent:
    def __init__(self, student_database):
        self.database = student_database

    def add_student(self, name, age, idnum, email, phone):
        new_student = StudentInfo(name, int(age), idnum, email, phone)
        self.database.add_student(new_student)
        self.save_to_file(new_student)

    def save_to_file(self, student):
        with open("students.txt", "a") as file:
            file.write(f"{student.get_name()}, {student.get_age()}, {student.get_idnum()}, {student.get_email()}, {student.get_phone()}\n")

    def add_students_from_file(self, filepath):
        try:
            self.database.load_students(filepath)
        except Exception as e:
            print(f"An error occurred while adding students from file: {e}")
