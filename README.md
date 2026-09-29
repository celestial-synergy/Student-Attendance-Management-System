# Student Attendance Management System

A Python-based Student Attendance Management System for managing student records, attendance, and attendance reports.

## 1. Project Overview

The Student Attendance Management System is a menu-driven Python application designed to simplify student attendance management.

The system allows users to add student details, search and view students, mark attendance, calculate attendance percentages, and generate attendance reports.

## 2. Problem Statement

Manual attendance management can be time-consuming and may result in errors while maintaining records and calculating attendance percentages.

This project provides a simple computerized solution for storing student information and managing attendance records.

## 3. Objectives

* Store student information.
* Record student attendance.
* Calculate attendance percentages automatically.
* Generate attendance reports.
* Identify students with sufficient or short attendance.
* Reduce manual calculation errors.

## 4. Main Features

### Student Management

* Add new students.
* View all students.
* Search students using roll number.

### Attendance Management

* Mark students as Present or Absent.
* View individual attendance records.
* Store attendance information.

### Attendance Reporting

* Calculate attendance percentage.
* Display Present and Absent counts.
* Display attendance eligibility status.

## 5. Technologies Used

* Python
* JSON
* Git
* GitHub
* Python unittest

## 6. Project Structure

```text
Student-Attendance-Management-System/
│
├── main.py
├── student.py
├── attendance.py
├── reports.py
├── database.py
├── validation.py
├── exceptions.py
├── test_attendance.py
├── statement.md
├── README.md
└── students.json
```

## 7. Module Description

| File                 | Purpose                                      |
| -------------------- | -------------------------------------------- |
| `main.py`            | Main menu and program workflow               |
| `student.py`         | Student class and student details            |
| `attendance.py`      | Attendance-related functionality             |
| `reports.py`         | Attendance percentage and status calculation |
| `database.py`        | JSON data storage                            |
| `validation.py`      | Input validation                             |
| `exceptions.py`      | Custom error handling                        |
| `test_attendance.py` | Unit testing                                 |

## 8. System Workflow

```text
Start
  ↓
Display Main Menu
  ↓
Select Operation
  ↓
Add / View / Search Student
  ↓
Mark Attendance
  ↓
Calculate Attendance Percentage
  ↓
Generate Attendance Report
  ↓
Exit
```

## 9. Attendance Calculation

Attendance percentage is calculated using:

```text
Attendance Percentage = (Number of Present Classes / Total Classes) × 100
```

The system displays the calculated percentage and attendance status.

## 10. Testing

The project includes a Python unit testing file named `test_attendance.py`.

The tests verify:

* Attendance percentage calculation.
* Eligible attendance status.
* Short attendance status.

## 11. Non-Functional Requirements

* **Usability:** Simple menu-driven interface.
* **Performance:** Fast attendance calculations and report generation.
* **Reliability:** Organized storage of student and attendance information.
* **Error Handling:** Invalid inputs are handled.
* **Maintainability:** Functionality is divided into separate modules.
* **Resource Efficiency:** Uses lightweight Python and JSON-based storage.

## 12. Future Enhancements

Possible future improve
