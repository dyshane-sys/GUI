from tkinter import Label, Entry, Button  # Import necessary tkinter widgets

def find_student(database, student_id):
    for student in database.get_all_students():
        if student.idnum == student_id:
            return student
    return None

def clear_content(widget):
    for child in widget.winfo_children():
        child.destroy()

def show_student_info(content_frame, database, student_id):
    student = find_student(database, student_id)
    if student:
        Label(content_frame, text=f"Name: {student.name}", font=("Arial", 14)).pack(pady=5)
        Label(content_frame, text=f"Age: {student.age}", font=("Arial", 14)).pack(pady=5)
        Label(content_frame, text=f"ID: {student.idnum}", font=("Arial", 14)).pack(pady=5)
        Label(content_frame, text=f"Email: {student.email}", font=("Arial", 14)).pack(pady=5)
        Label(content_frame, text=f"Phone: {student.phone}", font=("Arial", 14)).pack(pady=5)
    else:
        Label(content_frame, text="Student not found.", font=("Arial", 14), fg="red").pack()

def show_other_student_info(content_frame, database):
    """ Allow user to view other students' information using their ID """
    Label(content_frame, text="View Student Info by ID", font=("Arial", 14)).pack(pady=10)
    entry = Entry(content_frame, font=("Arial", 12))
    entry.pack(pady=5)

    def search():
        student_id = entry.get().strip()
        clear_content(content_frame)
        show_student_info(content_frame, database, student_id)

    Button(content_frame, text="Search", command=search, font=("Arial", 12)).pack(pady=10)

def show_add_student_form(content_frame, add_student_obj):
    Label(content_frame, text="Add New Student", font=("Arial", 14)).pack(pady=10)
    entries = {}
    for field in ["Name", "Age", "ID", "Email", "Phone"]:
        Label(content_frame, text=field, font=("Arial", 12)).pack()
        entry = Entry(content_frame, font=("Arial", 12))
        entry.pack(pady=5)
        entries[field] = entry

    def submit():
        name = entries["Name"].get().strip()
        age = entries["Age"].get().strip()
        idnum = entries["ID"].get().strip()
        email = entries["Email"].get().strip()
        phone = entries["Phone"].get().strip()

        if name and age and idnum and email and phone:
            add_student_obj.add_student(name, age, idnum, email, phone)
            Label(content_frame, text="Student Added Successfully!", fg="green", font=("Arial", 12)).pack()
        else:
            Label(content_frame, text="Please fill in all fields.", fg="red", font=("Arial", 12)).pack()

    Button(content_frame, text="Add Student", command=submit, font=("Arial", 12)).pack(pady=10)

def show_all_students(content_frame, database):
    Label(content_frame, text="All Students", font=("Arial", 14)).pack(pady=10)
    students = database.get_all_students()
    if not students:
        Label(content_frame, text="No students available.", font=("Arial", 12), fg="red").pack()
    else:
        for student in students:
            Label(content_frame, text=str(student), font=("Arial", 12)).pack(pady=2)

def show_all_students_info(content_frame, database):
    """ Display information for all students in the database """
    students = database.get_all_students()
    if not students:
        Label(content_frame, text="No students available.", font=("Arial", 12), fg="red").pack()
    else:
        Label(content_frame, text="All Students", font=("Arial", 14)).pack(pady=10)
        for student in students:
            Label(content_frame, text=str(student), font=("Arial", 12)).pack(pady=2)
