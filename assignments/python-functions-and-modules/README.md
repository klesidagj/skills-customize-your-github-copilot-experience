# 📘 Assignment: Python Functions and Modules

## 🎯 Objective

Learn how to write reusable functions, split code across modules, and import helper code into a small Python program. You will build a simple study tracker that calculates a student's average quiz score and final letter grade.

## 📝 Tasks

### 🛠️ Create Reusable Helper Functions

#### Description
Implement the core logic in `helpers.py` so the program can calculate averages, assign letter grades, and format a summary message.

#### Requirements
Completed program should:

- Define `average_score(scores)` to return the average of a list of quiz scores.
- Define `letter_grade(score)` to return `A`, `B`, `C`, `D`, or `F` based on a numeric score.
- Define `format_report(name, average, grade)` to return one clean summary string.


### 🛠️ Build the Study Tracker App

#### Description
Use `starter-code.py` as the main program. Import the helper functions, collect a student's information, and display the final report.

#### Requirements
Completed program should:

- Import the functions from `helpers.py`.
- Ask the user for a student name and three quiz scores.
- Convert the quiz scores to numbers before calculating the average.
- Print the formatted report using the helper functions.