from student import Student
from reports import calculate_percentage, attendance_status
from database import load_data, save_data
from validation import validate_roll_number, validate_name, validate_attendance_status


students = {}
attendance_records = {}


def load_students():
    global students, attendance_records

    data = load_data()

    for roll_number, details in data.items():
        students[roll_number] = Student(
            roll_number,
            details["name"],
            details["course"]
        )

        attendance_records[roll_number] = details["attendance"]


def save_students():
    data = {}

    for roll_number, student in students.items():
        data[roll_number] = {
            "name": student.name,
            "course": student.course,
            "attendance": attendance_records[roll_number]
        }

    save_data(data)


def add_student():
    roll_number = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")
    course = input("Enter Course: ")

    if not validate_roll_number(roll_number):
        print("Invalid roll number. Please enter numbers only.")
        return

    if not validate_name(name):
        print("Invalid name. Please enter letters only.")
        return

    if roll_number in students:
        print("Student already exists.")
        return

    students[roll_number] = Student(roll_number, name, course)
    attendance_records[roll_number] = []

    save_students()

    print("Student added successfully!")


def view_students():
    if not students:
        print("No students found.")
        return

    print("\n===== STUDENT LIST =====")

    for student in students.values():
        print(
            "Roll Number:", student.roll_number,
            "| Name:", student.name,
            "| Course:", student.course
        )


def search_student():
    roll_number = input("Enter Roll Number to search: ")

    if roll_number in students:
        student = students[roll_number]

        print("\n===== STUDENT FOUND =====")
        student.display_student()
    else:
        print("Student not found.")


def mark_attendance():
    roll_number = input("Enter Roll Number: ")

    if roll_number not in students:
        print("Student not found.")
        return

    status = input("Enter Attendance (P/A): ")

    if not validate_attendance_status(status):
        print("Invalid attendance. Please enter P or A.")
        return

    attendance_records[roll_number].append(status.upper())

    save_students()

    print("Attendance marked successfully!")


def view_attendance():
    roll_number = input("Enter Roll Number: ")

    if roll_number not in students:
        print("Student not found.")
        return

    records = attendance_records[roll_number]

    if not records:
        print("No attendance records found.")
        return

    total = len(records)
    present = records.count("P")
    absent = records.count("A")

    percentage = calculate_percentage(present, total)

    print("\n===== ATTENDANCE =====")
    print("Student:", students[roll_number].name)
    print("Total Classes:", total)
    print("Present:", present)
    print("Absent:", absent)
    print("Attendance:", round(percentage, 2), "%")


def attendance_report():
    if not students:
        print("No students found.")
        return

    print("\n===== ATTENDANCE REPORT =====")

    for roll_number, student in students.items():

        records = attendance_records[roll_number]
        total = len(records)

        if total == 0:
            percentage = 0
        else:
            present = records.count("P")
            percentage = calculate_percentage(present, total)

        status = attendance_status(percentage)

        print(
            student.name,
            "|",
            round(percentage, 2),
            "%",
            "|",
            status
        )


def main():

    load_students()

    while True:

        print("\n====================================")
        print("   STUDENT ATTENDANCE MANAGEMENT")
        print("====================================")

        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Mark Attendance")
        print("5. View Attendance")
        print("6. Attendance Report")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            mark_attendance()

        elif choice == "5":
            view_attendance()

        elif choice == "6":
            attendance_report()

        elif choice == "7":
            print("Thank you for using the system!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
