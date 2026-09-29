import unittest
from reports import calculate_percentage, attendance_status


class TestAttendance(unittest.TestCase):

    def test_percentage(self):
        result = calculate_percentage(8, 10)
        self.assertEqual(result, 80)

    def test_eligible_status(self):
        result = attendance_status(80)
        self.assertEqual(result, "Eligible")

    def test_short_attendance_status(self):
        result = attendance_status(60)
        self.assertEqual(result, "Short Attendance")


if __name__ == "__main__":
    unittest.main()
