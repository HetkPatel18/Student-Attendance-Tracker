# Student Attendance Tracker

A simple command-line program for keeping track of college attendance
across different subjects.

You can add subjects, record the classes you attended or missed, check
your current attendance percentage, and see whether you can afford to
miss more classes or need to attend a certain number of classes to get
back to the 75% requirement.

All attendance data is stored locally, so it stays available when you
run the program again.

## Features

-   Add subjects with course code, subject name, total classes held, and
    classes attended
-   View an attendance dashboard for all subjects
-   Record attended and missed classes
-   Check attendance against the 75% requirement
-   See how many classes can be missed while staying at or above 75%
-   See how many classes need to be attended to reach 75% if attendance
    is below the requirement
-   Delete subjects
-   Automatically save attendance data

## Project Structure

``` text
attendance-tracker/
│
├── main.py          # Program entry point and menu
├── tracker.py       # Attendance calculations and data handling
├── test_tracker.py  # Tests for attendance calculations
└── README.md        # Project documentation
```

## Requirements

-   Python 3.6 or higher
-   No external libraries are required

The project only uses Python's built-in `os` module.

## How to Run

### 1. Check Python

Open a terminal and run:

``` bash
python --version
```

If that does not work, try:

``` bash
python3 --version
```

Make sure `main.py` and `tracker.py` are in the same folder.

### 2. Run the Program

No dependencies need to be installed. Start the program with:

``` bash
python main.py
```

The program will create `attendance_data.txt` automatically when you add
your first subject.

## How to Use

When the program starts, the following menu is displayed:

``` text
=== Student Attendance Tracker ===
1. View Attendance Dashboard
2. Add a Subject
3. Log Today's Classes
4. Check Bunks & Warnings
5. Delete a Subject
6. Exit
```

Choose an option by entering its number and pressing Enter.

### 1. View Attendance Dashboard

Shows the attendance details for each subject, including:

-   Total classes held
-   Classes attended
-   Attendance percentage

### 2. Add a Subject

Enter the basic details of a subject:

``` text
Course Code: CSE101
Subject Name: Data Structures
Total classes held: 20
Classes attended: 16
```

The subject is then added to the tracker.

### 3. Log Today's Classes

Enter the course code and record how many classes you attended and
missed that day.

The program updates the subject's total classes and attendance
automatically.

### 4. Check Bunks & Warnings

This option helps you understand your current attendance situation.

If your attendance is **75% or higher**, the program shows how many more
classes you can miss while remaining at or above 75%.

If your attendance is **below 75%**, it shows how many classes you need
to attend in a row to reach the requirement.

### 5. Delete a Subject

Enter the course code of the subject you want to remove.

### 6. Exit

Closes the program.

## Example

``` text
Enter choice (1-6): 2

Course Code: CSE101
Subject Name: Data Structures
Total classes held: 20
Classes attended: 16

Added CSE101 successfully.
```

## Running the Tests

The project includes `test_tracker.py` for testing the attendance
calculations.

To run the tests:

``` bash
python -m unittest test_tracker.py
```

The tests cover:

-   Attendance percentage
-   Safe-bunk calculations
-   Classes needed to reach 75%

## Notes

-   Attendance percentage is rounded to 2 decimal places.
-   Classes attended cannot be greater than total classes held when
    adding a subject.
-   Safe-bunk and needed-class calculations consider future classes one
    at a time.
-   The calculations do not account for cancelled classes.
-   To reset all stored attendance data, delete the
    `attendance_data.txt` file.

## Author

Student Attendance Tracker --- Het Ketankumar Patel
