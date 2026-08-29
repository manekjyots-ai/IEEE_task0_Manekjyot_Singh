"""
Uses the processed data from Q5
to create four visualizations, each saved as a PNG image.
"""

import pandas as pd
import matplotlib.pyplot as plt

# Load the processed data from Q5
df = pd.read_csv("data/processed_student_performance.csv")

# Bar chart: Student names vs final scores
# Please Note: the dataset has 80 students, so plotting every single name
# on the x-axis was making the data unreadable.
# To keep the graph readable,
# I've shown the top 15 students by Final_Score.
top_n = 15
top_students = df.sort_values(by="Final_Score", ascending=False).head(top_n)

plt.figure(figsize=(10, 6))
plt.bar(top_students["Student"], top_students["Final_Score"], color="steelblue")
plt.title(f"Top {top_n} Students by Final Score")
plt.xlabel("Student")
plt.ylabel("Final Score")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("plots/final_scores.png")
plt.close()

# Scatter plot: Hours studied vs final score
plt.figure(figsize=(8, 6))
plt.scatter(df["Hours_Studied"], df["Final_Score"], color="darkorange", alpha=0.7)
plt.title("Hours Studied vs Final Score")
plt.xlabel("Hours Studied")
plt.ylabel("Final Score")
plt.tight_layout()
plt.savefig("plots/study_vs_score.png")
plt.close()

# Histogram: Distribution of final scores
plt.figure(figsize=(8, 6))
plt.hist(df["Final_Score"], bins=10, range=(30, 80), color="mediumseagreen", edgecolor="black")
plt.title("Distribution of Final Scores")
plt.xlabel("Final Score")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.savefig("plots/score_distribution.png")
plt.close()

# Custom plot: Attendance vs Improvement
# Shows whether higher attendance is associated with bigger improvements in score.
plt.figure(figsize=(8, 6))
plt.scatter(df["Attendance"], df["Improvement"], color="crimson", alpha=0.7)
plt.axhline(y=0, color="gray", linestyle="--", linewidth=1)  # reference line at 0 improvement
plt.title("Attendance vs Improvement in Score")
plt.xlabel("Attendance (%)")
plt.ylabel("Improvement (Final Score - Previous Score)")
plt.tight_layout()
plt.savefig("plots/custom_plot.png")
plt.close()
# There is a decently positive relationship between attendance and score improvement,
# as seen in the scatter plot.

print("All four graphs saved in plots: final_scores.png, study_vs_score.png, score_distribution.png, custom_plot.png")