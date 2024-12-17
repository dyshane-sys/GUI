from student import StudentInfo 

class StudentDatabase:
    def __init__(self):
        self.students = []

    def get_all_students(self):
        return self.students

    def add_student(self, student):
        self.students.append(student)

    def load_students(self, filepath):
        with open(filepath, "r") as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip() 
                if line:  
                    try:
                        name, age, idnum, email, phone = line.split(", ")
                        self.add_student(StudentInfo(name, int(age), idnum, email, phone))  
                    except ValueError as e:
                        print(f"Error parsing line: {line}. Error: {e}")
                        continue 
