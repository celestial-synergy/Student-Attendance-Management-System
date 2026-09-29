class Student:
    def __init__(self, roll_number, name, course):
        self.roll_number = roll_number
        self.name = name
        self.course = course

    def display_student(self):
        print("Roll Number:", self.roll_number)
        print("Name:", self.name)
        print("Course:", self.course)
