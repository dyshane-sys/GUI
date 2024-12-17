from tkinter import *
from tkinter import ttk
from functools import partial
from tkinter.messagebox import showinfo, askyesno
from add_student import AddStudent
from all_students import StudentDatabase
from functions import (find_student, clear_content, show_all_students_info,
                        show_other_student_info, show_add_student_form, show_student_info)


stu_db = StudentDatabase()
add_stu = AddStudent(stu_db)
add_stu.add_students_from_file("students.txt")


def center_window(win, width, height):
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    win.geometry(f"{width}x{height}+{x}+{y}")


def splash_screen():
    splash = Tk()
    splash.title("Welcome")
    splash.configure(bg="#34495E")
    center_window(splash, 500, 300) 

    Label(splash, text="Student Management System", font=("Arial", 24, "bold"), bg="#34495E", fg="white").pack(expand=True)
    Label(splash, text="Loading...", font=("Arial", 14), bg="#34495E", fg="white").pack(pady=20)
    splash.after(2000, splash.destroy) 
    splash.mainloop()


def main_app(student):
    win = Tk()
    win.title("Student Management System")
    win.configure(bg="#f4f4f4")
    center_window(win, 1000, 600)  

    header_frame = Frame(win, bg="#2C3E50", height=60)
    header_frame.pack(side="top", fill="x")

    menu_frame = Frame(win, bg="#34495E", width=200)
    menu_frame.pack(side="left", fill="y")

    content_frame = Frame(win, bg="white")
    content_frame.pack(side="right", fill="both", expand=True)

    Label(header_frame, text="Student Management System", font=("Arial", 20, "bold"), bg="#2C3E50", fg="white").pack(pady=10)

    def view_info():
        clear_content(content_frame)
        show_student_info(content_frame, stu_db, student.idnum)

    def add_student():
        clear_content(content_frame)
        show_add_student_form(content_frame, add_stu)

    def view_all_students():
        clear_content(content_frame)
        show_all_students_info(content_frame, stu_db)

    def view_other_student():
        clear_content(content_frame)
        show_other_student_info(content_frame, stu_db)

    def confirm_exit():
        if askyesno("Exit", "Are you sure you want to exit?"):
            win.destroy()

    # Menu Buttons
    def create_menu_button(text, command):
        return Button(menu_frame, text=text, command=command, font=("Arial", 12), bg="#34495E", fg="white", 
                      activebackground="#1ABC9C", activeforeground="white", bd=0, relief=FLAT)

    menu_buttons = [
        ("View My Info", view_info),
        ("Add New Student", add_student),
        ("View All Students", view_all_students),
        ("View Other's Info", view_other_student),
        ("Exit", confirm_exit)
    ]

    for btn_text, btn_command in menu_buttons:
        create_menu_button(btn_text, btn_command).pack(fill="x", pady=5, padx=5)

    win.mainloop()


def login_screen():
    login_win = Tk()
    login_win.title("Login")
    login_win.configure(bg="#ecf0f1")
    center_window(login_win, 400, 300)  # Center login window

    # Login Widgets
    Label(login_win, text="Login", font=("Arial", 20, "bold"), bg="#ecf0f1", fg="#2C3E50").pack(pady=20)
    Label(login_win, text="Enter Student ID:", font=("Arial", 14), bg="#ecf0f1", fg="#34495E").pack()

    student_id_entry = ttk.Entry(login_win, font=("Arial", 12))
    student_id_entry.pack(pady=10)

    def login():
        student_id = student_id_entry.get().strip()
        for student in stu_db.get_all_students():
            if student.idnum == student_id:
                login_win.destroy()
                main_app(student)
                return
        Label(login_win, text="Invalid ID. Try again.", fg="red", font=("Arial", 12), bg="#ecf0f1").pack()

    Button(login_win, text="Login", command=login, font=("Arial", 12), bg="#2C3E50", fg="white", activebackground="#1ABC9C", activeforeground="white").pack(pady=20)
    login_win.mainloop()


if __name__ == "__main__":
    splash_screen()
    login_screen()
