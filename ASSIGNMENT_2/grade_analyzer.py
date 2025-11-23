# ---------------------------------------------
# GradeBook Analyzer
# Name: AANYA MANGAL
# Date:
# ---------------------------------------------

import csv

# ------------------------------------------------
# TASK 1 – WELCOME MESSAGE + MENU
# ------------------------------------------------

print("===========================================")
print("       WELCOME TO GRADEBOOK ANALYZER")
print("===========================================")
print("This tool helps you analyse student marks,")
print("generate statistics, assign grades, and more.")
print("-------------------------------------------\n")


# ------------------------------------------------
# TASK 3 – STATISTICAL FUNCTIONS
# ------------------------------------------------

def calculate_average(marks):
    return sum(marks.values()) / len(marks)

def calculate_median(marks):
    scores = sorted(marks.values())
    n = len(scores)
    mid = n // 2

    if n % 2 == 0:
        return (scores[mid - 1] + scores[mid]) / 2
    else:
        return scores[mid]

def find_max_score(marks):
    return max(marks.values())

def find_min_score(marks):
    return min(marks.values())


# ------------------------------------------------
# TASK 4 – GRADE ASSIGNMENT
# ------------------------------------------------

def assign_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


# ------------------------------------------------
# TASK 2 – DATA INPUT (MANUAL / CSV)
# ------------------------------------------------

def get_data_manual():
    marks = {}
    n = int(input("Enter number of students: "))

    for i in range(n):
        name = input(f"Enter name of student {i+1}: ")
        score = int(input(f"Enter marks of {name}: "))
        marks[name] = score

    return marks


def get_data_csv():
    marks = {}
    filename = input("Enter CSV filename (with .csv): ")

    with open(filename, newline='') as file:
        reader = csv.reader(file)
        next(reader)   # skip header

        for row in reader:
            name = row[0]
            score = int(row[1])
            marks[name] = score

    return marks


# ------------------------------------------------
# TASK 6 – RESULT DISPLAY TABLE
# ------------------------------------------------

def display_table(marks, grades):
    print("\nName\t\tMarks\tGrade")
    print("-------------------------------------")

    for name in marks:
        print(f"{name}\t\t{marks[name]}\t{grades[name]}")


# ------------------------------------------------
# MAIN PROGRAM LOOP
# ------------------------------------------------

while True:
    print("\n=== MAIN MENU ===")
    print("1. Enter Data Manually")
    print("2. Load Data from CSV File")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        marks = get_data_manual()

    elif choice == "2":
        marks = get_data_csv()

    elif choice == "3":
        print("\nThank you for using GradeBook Analyzer!")
        print("Goodbye 😊")
        break

    else:
        print("Invalid option. Please try again.")
        continue


    # Grade calculation (Task 4)
    grades = {name: assign_grade(score) for name, score in marks.items()}

    # Pass/Fail List Comprehension (Task 5)
    passed = [name for name, m in marks.items() if m >= 40]
    failed = [name for name, m in marks.items() if m < 40]

    # Statistics (Task 3)
    print("\n--- STATISTICS ---")
    print("Average Score:", calculate_average(marks))
    print("Median Score:", calculate_median(marks))
    print("Highest Score:", find_max_score(marks))
    print("Lowest Score:", find_min_score(marks))

    # Grade Distribution
    print("\n--- GRADE DISTRIBUTION ---")
    for g in ["A", "B", "C", "D", "F"]:
        count = list(grades.values()).count(g)
        print(f"{g}: {count}")

    # Pass / Fail Display
    print("\nPassed Students:", passed)
    print("Failed Students:", failed)

    # Final Table
    display_table(marks, grades)

    # Repeat?
    again = input("\nDo you want to run analysis again? (y/n): ")
    if again.lower() != "y":
        print("\nThank you for using GradeBook Analyzer!")
        break