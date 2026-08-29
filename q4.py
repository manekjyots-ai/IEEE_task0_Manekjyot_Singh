"""
Creates NumPy arrays for hours studied, attendance, previous scores,
and final scores, then performs various NumPy operations on them.
"""

import numpy as np

# Sample data values used - completely random
hours_studied = np.array([5, 8, 2, 7, 6, 9])
attendance = np.array([85, 92, 60, 78, 88, 95])          # in percentage
previous_scores = np.array([65, 89, 55, 80, 72, 61])
final_scores = np.array([70, 91, 58, 87, 76, 99])

# Print the arrays for convenience
print("Hours studied:", hours_studied)
print("Attendance:", attendance)
print("Previous scores:", previous_scores)
print("Final scores:", final_scores)

# For formatting, print a blank line
print()

# Print the shape, data type of each array
print("Hours studied --> shape:", hours_studied.shape, "and dtype:", hours_studied.dtype)
print("Attendance --> shape:", attendance.shape, "and dtype:", attendance.dtype)
print("Previous scores --> shape:", previous_scores.shape, "and dtype:", previous_scores.dtype)
print("Final scores --> shape:", final_scores.shape, "and dtype:", final_scores.dtype)

print()

# Find the mean final score
mean_final_score = final_scores.mean()
print(f"Mean final score: {mean_final_score:.2f} (to 2 d.p.)")

# Find the maximum and minimum final score
max_final_score = final_scores.max()
min_final_score = final_scores.min()
print("Max final score:", max_final_score)
print("Min final score:", min_final_score)

# Find the standard deviation of final scores
std_final_score = final_scores.std()
print(f"Standard deviation of final scores: {std_final_score:.2f} (to 2 d.p.)")

print()

# Add 5 bonus marks to every final score
# I've created a new array so original data isn't lost
final_scores_with_bonus = final_scores + 5
print("Final scores with bonus:", final_scores_with_bonus)

# Create a Boolean array showing which students scored >= 75
scored_75_or_more = final_scores >= 75
print("Scored greater than or equal to 75 (Boolean array):", scored_75_or_more)

# Print only the scores >= 75
print("Scores greater than or equal to 75:", final_scores[scored_75_or_more])