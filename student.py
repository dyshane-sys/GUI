class StudentInfo:
    def __init__(self, name, age, idnum, email, phone):
        self.name = name
        self.age = age
        self.idnum = idnum
        self.email = email
        self.phone = phone

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_idnum(self):
        return self.idnum

    def get_email(self):
        return self.email

    def get_phone(self):
        return self.phone

    def __str__(self):
        return f"{self.name}, {self.age}, {self.idnum}, {self.email}, {self.phone}"
