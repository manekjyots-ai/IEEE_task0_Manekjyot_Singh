"""
Reads student_performance.csv and performs analysis
"""

import pandas as pd

# Load the CSV into a DataFrame
df = pd.read_csv("data/student_performance.csv")

# Print the first five rows
print("First five rows:")
print(df.head())

print()

# Print the number of rows and columns
rows, cols = df.shape
print(f"Number of rows: {rows}")
print(f"Number of columns: {cols}")

print()

# Display the column names
print("Column names:", list(df.columns))

print()

# Check whether the dataset contains missing values
print("Missing values per column:")
print(df.isnull().sum())

print()

print("Does the dataset contain any missing values (overall)?", df.isnull().values.any())

print()

# Calculate the average final score
average_final_score = df["Final_Score"].mean()
print(f"Average Final_Score: {average_final_score:.2f}")

print()

# Find the student with the highest final score
top_student_row = df.loc[df["Final_Score"].idxmax()]
print("Student with highest Final_Score:")
print(top_student_row)

print()

# Create a new column for improvement
df["Improvement"] = df["Final_Score"] - df["Previous_Score"]

# Display only students with attendance >= 80
high_attendance_students = df[df["Attendance"] >= 80]
print("Students with Attendance greater than or equal to 80:")
print(high_attendance_students)

print()

# Sort the DataFrame by final scores in descending order
df_sorted = df.sort_values(by="Final_Score", ascending=False)
print("DataFrame sorted by Final_Score (descending order):")
print(df_sorted.head())
print()

# 11. Save the processed DataFrame
df_sorted.to_csv("data/processed_student_performance.csv", index=False)
print("Saved processed data to processed_student_performance.csv in data folder")