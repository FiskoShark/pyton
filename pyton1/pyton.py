class Student:
    def __init__(self, name, age, subject):
        self.name = name
        self.age = age
        self.subject = subject
    def __str__(self):
        return f"ім'я: {self.name}, вік: {self.age}, предмет: {self.subject}"

stud1 = Student("Михайло", 52, "Pyton")
stud2 = Student("Перепічка", 16, "Gta")
stud3 = Student("Стас", 22, "Html-css")
stud4 = Student("Макс", 30, "JavaScript ")
stud5 = Student("Рома", 20, "C++")

students_list = [stud1, stud2, stud3, stud4, stud5]
for student in students_list:
    print(student)


