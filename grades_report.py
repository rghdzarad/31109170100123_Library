# Student Grades Analysis
# A simple script that reads student grades and prints a short summary.
# All data is dummy content, used for practicing Git & GitHub.

import pandas as pd

# Load the grades from the CSV file.
grades = pd.read_csv("grades.csv")

# Show the first few rows so we can see what the data looks like.
print("First rows of the grades:")
print(grades.head())
print()

# The average score across every row.
overall_average = grades["score"].mean()
print("Overall average score:", round(overall_average, 1))
print()

# The average score for each student.
print("Average score by student:")
average_by_student = grades.groupby("name")["score"].mean()
print(average_by_student)
print()

# The student with the highest average score.
top_student = average_by_student.idxmax()
print("Top student:", top_student)
