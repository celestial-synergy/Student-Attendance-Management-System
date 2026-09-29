def validate_roll_number(roll_number):
    return roll_number.isdigit()


def validate_name(name):
    return name.replace(" ", "").isalpha()


def validate_attendance_status(status):
    return status.upper() in ["P", "A"]
