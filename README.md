# Student Performance Analyzer

A Python-based data analysis project that processes student marks from a
CSV file, calculates academic results and class statistics, and
visualizes performance using Matplotlib.

## Project Overview

The **Student Performance Analyzer** reads student records from
`students.csv`, validates marks in Maths, Physics, and Chemistry, and
generates each student's total marks, percentage, and letter grade. It
also calculates class-level statistics and displays graphical reports.

## Features

-   Reads student records dynamically from a CSV file.
-   Validates marks and accepts values from 0 to 100.
-   Skips records containing invalid marks.
-   Calculates total marks out of 300 and percentage.
-   Assigns grades automatically:
    -   **A:** 90% and above
    -   **B:** 75% to below 90%
    -   **C:** 60% to below 75%
    -   **D:** 40% to below 60%
    -   **F:** Below 40%
-   Calculates class mean, median, and standard deviation.
-   Identifies the class topper.
-   Calculates subject-wise average marks.
-   Displays a subject-average bar chart and a student-percentage
    histogram.

## Technologies Used

-   Python 3
-   Pandas
-   NumPy
-   Matplotlib
-   CSV for storing student records

## Project Files

``` text
Student-Performance-Analyzer/
├── one.py
├── students.csv
└── README.md
```

## Requirements

Install Python 3, then install the required libraries:

``` bash
pip install pandas numpy matplotlib
```

## CSV File Format

Create a file named `students.csv` in the same folder as `one.py`.

Each row should contain a student's name followed by marks in Maths,
Physics, and Chemistry:

``` csv
Aman,80,70,90
Riya,60,65,70
Karan,40,35,50
```

Marks should be numeric values between 0 and 100. Rows with invalid
marks are skipped by the program.

## How to Run

1.  Keep `one.py` and `students.csv` in the same folder.
2.  Open a terminal in that folder.
3.  Run:

``` bash
python one.py
```

4.  Follow the menu displayed by the program to view student results,
    class statistics, or exit.

## Testing

The project report records the following test cases as passed:

  -----------------------------------------------------------------------
  Test Case               Input / Action          Expected or Observed
                                                  Result
  ----------------------- ----------------------- -----------------------
  Normal valid input      Aman (80, 70, 90), Riya Correct totals,
                          (60, 65, 70), Karan     percentages, and grades
                          (40, 35, 50)            are displayed.

  Boundary values         Neha (100, 100, 100),   Neha receives 100% (A);
                          Ravi (0, 0, 0)          Ravi receives 0% (F).

  Invalid mark handling   Amit (85, `abc`, 70)    Invalid record is
                                                  skipped with an error
                                                  notification.

  Class statistics        Select the Statistics   Mean: 62.22%, median:
                          option                  65.00%, standard
                                                  deviation: 15.77;
                                                  topper: Aman.

  Matplotlib charts       Select Statistics with  Subject-average bar
                          charts enabled          chart and percentage
                                                  histogram are
                                                  displayed.
  -----------------------------------------------------------------------

## Output and Visualizations

The program displays student-wise results and class statistics in the
terminal. It also generates:

1.  **Subject-wise Average Marks:** A bar chart comparing average marks
    in Maths, Physics, and Chemistry.
2.  **Student Percentage Distribution:** A histogram showing the
    distribution of student percentages.

## Notes

-   The input file must be named `students.csv` and should be in the
    same directory as `one.py`.
-   The program uses the three subjects Maths, Physics, and Chemistry,
    with a maximum total of 300 marks.
-   The README describes the project structure and behavior documented
    in the project report.

## Author

**Yukti Sahu**\
BCA AI/ML (Association with Google)\
Rungta International Skills University
