# Statement

## Problem Statement

Many colleges require students to maintain at least 75% attendance in every subject, but working out — subject by subject — how many classes can be missed or how many must be attended to stay compliant is tedious to do by hand. Student Attendance Tracker addresses this by calculating it automatically from the attendance data the student enters.

## Scope of the Project

Student Attendance Tracker is a single-user, local command-line application. It covers adding subjects, logging daily attendance, viewing an attendance dashboard, and calculating safe-bunk / classes-needed figures against a fixed 75% threshold. It does not cover multiple attendance thresholds, timetable or scheduling features, multi-user accounts, or any syncing with a college's official attendance system.

## Target Users

College students who want a fast, offline way to check whether they're meeting their attendance requirement in each subject, and to know exactly how much room they have (or how much ground they need to make up) before it becomes a problem.

## High-Level Features

- Add a subject with a course code, name, total classes held, and classes attended so far
- View an attendance dashboard showing total, attended, and percentage for every subject
- Log today's classes for a subject (attended and missed), updating its totals
- Check compliance against the 75% rule: safe classes to bunk if compliant, or classes needed in a row if not
- Delete a subject
- All data is saved locally and reloaded automatically the next time the program runs
- Core calculations are covered by automated unit tests (test_tracker.py)
