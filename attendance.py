class Attendance:
    def __init__(self):
        self.records = {}

    def mark_attendance(self, roll_number, status):
        self.records[roll_number] = status

    def get_attendance(self, roll_number):
        return self.records.get(roll_number, "No attendance record found")
