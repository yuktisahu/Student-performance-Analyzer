# ==============================================================
#                 STUDENT PERFORMANCE ANALYZER
#              Rungta International Skills University
#                         Python 3 Project
# ==============================================================
# Project No. : 97
# Libraries   : Pandas, NumPy, Matplotlib
# Input File  : students.csv
# ==============================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


# --------------------------------------------------------------
# FUNCTION 1: LOAD STUDENT DATA FROM CSV FILE
# --------------------------------------------------------------

def load_student_data(filename="students.csv"):
    """Read student data and skip rows containing invalid marks."""

    # Check whether the CSV file is present in the project folder.
    if not os.path.exists(filename):
        print(f"Error: {filename} file not found.")
        print("Keep students.csv in the same folder as this Python file.")
        return pd.DataFrame()

    try:
        # Read CSV as text first so values such as 'abc' can be validated.
        # header=None supports the exact input format in the assignment.
        raw_data = pd.read_csv(filename, header=None, dtype=str)

    except pd.errors.EmptyDataError:
        print("Error: students.csv is empty.")
        return pd.DataFrame()

    except Exception as error:
        print("Error while reading CSV file:", error)
        return pd.DataFrame()

    if raw_data.empty:
        print("No student records found.")
        return pd.DataFrame()

    # Support both formats: with a header or without a header.
    first_cell = str(raw_data.iloc[0, 0]).strip().lower()

    if first_cell in ["name", "student", "student_name"]:
        raw_data = raw_data.iloc[1:].reset_index(drop=True)

    valid_records = []

    # Each row must contain: Name, Maths, Physics, Chemistry.
    for _, row in raw_data.iterrows():

        if len(row) < 4:
            print("Invalid student data. Row skipped.")
            continue

        name = str(row.iloc[0]).strip()

        if not name or name.lower() == "nan":
            print("Invalid student name. Row skipped.")
            continue

        marks = []
        invalid_subject = None
        invalid_value = None

        # Validate marks one subject at a time.
        subjects = ["Maths", "Physics", "Chemistry"]

        for column, subject in zip([1, 2, 3], subjects):

            value = str(row.iloc[column]).strip()

            try:
                mark = float(value)

            except (ValueError, TypeError):
                invalid_subject = subject
                invalid_value = value
                break

            # Marks must be between 0 and 100.
            if mark < 0 or mark > 100:
                invalid_subject = subject
                invalid_value = value
                break

            marks.append(mark)

        # Skip the complete row if any subject mark is invalid.
        if invalid_subject is not None:
            print(
                f"Invalid marks for {name} in {invalid_subject}: "
                f"'{invalid_value}'. Row skipped."
            )
            continue

        valid_records.append([
            name,
            marks[0],
            marks[1],
            marks[2]
        ])

    # Convert valid records into a Pandas DataFrame.
    students = pd.DataFrame(
        valid_records,
        columns=["Name", "Maths", "Physics", "Chemistry"]
    )

    return students


# --------------------------------------------------------------
# FUNCTION 2: CALCULATE TOTAL, PERCENTAGE AND GRADE
# --------------------------------------------------------------

def calculate_results(students):
    """Calculate total marks, percentage and grade."""

    if students.empty:
        return students

    # Calculate total marks out of 300.
    subjects = ["Maths", "Physics", "Chemistry"]
    students["Total"] = students[subjects].sum(axis=1)

    # Calculate percentage out of 100.
    students["Percentage"] = (students["Total"] / 300) * 100

    # Assign grades according to the assignment criteria.
    def calculate_grade(percentage):

        if percentage >= 90:
            return "A"

        elif percentage >= 75:
            return "B"

        elif percentage >= 60:
            return "C"

        elif percentage >= 40:
            return "D"

        else:
            return "F"

    students["Grade"] = students["Percentage"].apply(calculate_grade)

    return students


# --------------------------------------------------------------
# FUNCTION 3: DISPLAY STUDENT RESULTS
# --------------------------------------------------------------

def display_results(students):
    """Display total, percentage and grade of every student."""

    if students.empty:
        print("No valid student records available.")
        return

    print("\nSTUDENT RESULTS")

    # Display results in the same format as the expected output.
    for _, student in students.iterrows():

        print(
            f"{student['Name']} | "
            f"{student['Total']:.0f} | "
            f"{student['Percentage']:.2f}% | "
            f"{student['Grade']}"
        )


# --------------------------------------------------------------
# FUNCTION 4: DISPLAY CLASS STATISTICS
# --------------------------------------------------------------

def display_statistics(students):
    """Calculate and display class statistics and topper."""

    if students.empty:
        print("No valid student records available.")
        return

    # Calculate mean, median and population standard deviation.
    percentages = students["Percentage"]

    mean_percentage = np.mean(percentages)
    median_percentage = np.median(percentages)
    std_deviation = np.std(percentages, ddof=0)

    # Find the student with the highest percentage.
    topper = students.loc[students["Percentage"].idxmax()]

    # Calculate average marks for each subject using Pandas.
    subject_averages = students[
        ["Maths", "Physics", "Chemistry"]
    ].mean()

    print("\nCLASS STATISTICS")

    print(
        f"Mean %: {mean_percentage:.2f} | "
        f"Median %: {median_percentage:.2f} | "
        f"Std Dev: {std_deviation:.2f}"
    )

    print(
        f"Topper: {topper['Name']} "
        f"({topper['Percentage']:.2f}%)"
    )

    print(
        f"Subject averages: Maths {subject_averages['Maths']:.2f}, "
        f"Physics {subject_averages['Physics']:.2f}, "
        f"Chemistry {subject_averages['Chemistry']:.2f}"
    )

    # Display the charts required by the assignment.
    display_charts(students, subject_averages)


# --------------------------------------------------------------
# FUNCTION 5: DISPLAY BAR CHART AND HISTOGRAM
# --------------------------------------------------------------

def display_charts(students, subject_averages):
    """Plot subject-wise average bar chart and percentage histogram."""

    # BAR CHART: Subject-wise average marks.
    plt.figure(figsize=(8, 5))

    bars = plt.bar(
        subject_averages.index,
        subject_averages.values
    )

    plt.title("Subject-wise Average Marks")
    plt.xlabel("Subjects")
    plt.ylabel("Average Marks (out of 100)")
    plt.ylim(0, 110)
    plt.grid(axis="y", linestyle="--", alpha=0.5)

    # Display average values above each bar.
    for bar in bars:
        height = bar.get_height()

        plt.text(
            bar.get_x() + bar.get_width() / 2,
            height + 1,
            f"{height:.2f}",
            ha="center"
        )

    plt.tight_layout()
    plt.show()

    # HISTOGRAM: Student percentage distribution.
    plt.figure(figsize=(8, 5))

    plt.hist(
        students["Percentage"],
        bins=5,
        edgecolor="black"
    )

    plt.title("Student Percentage Distribution")
    plt.xlabel("Percentage")
    plt.ylabel("Number of Students")
    plt.grid(axis="y", linestyle="--", alpha=0.5)

    plt.tight_layout()
    plt.show()


# --------------------------------------------------------------
# MAIN FUNCTION: MENU-DRIVEN PROGRAM
# --------------------------------------------------------------

def main():

    print("=" * 55)
    print("             STUDENT PERFORMANCE ANALYZER")
    print("=" * 55)

    # Load student data from the CSV file.
    students = load_student_data("students.csv")

    if students.empty:
        return

    # Calculate total, percentage and grade.
    students = calculate_results(students)

    # Display menu until the user selects Exit.
    while True:

        print("\n1. Result")
        print("2. Statistics")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            display_results(students)

        elif choice == "2":
            display_statistics(students)

        elif choice == "3":
            print("Program closed successfully.")
            break

        else:
            print("Invalid choice. Please enter 1, 2 or 3.")


# --------------------------------------------------------------
# PROGRAM EXECUTION STARTS HERE
# --------------------------------------------------------------

if __name__ == "__main__":
    main()
