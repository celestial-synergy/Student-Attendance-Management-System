def calculate_percentage(present, total):
    if total == 0:
        return 0

    return (present / total) * 100


def attendance_status(percentage):
    if percentage >= 75:
        return "Eligible"
    else:
        return "Short Attendance"


def display_report(name, present, total):
    percentage = calculate_percentage(present, total)
    status = attendance_status(percentage)

    print("\n===== ATTENDANCE REPORT =====")
    print("Student:", name)
    print("Total Classes:", total)
    print("Present:", present)
    print("Attendance:", round(percentage, 2), "%")
    print("Status:", status)
