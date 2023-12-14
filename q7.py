import matplotlib.pyplot as plt
import numpy as np

# Hypothetical exam scores dataset
exam_scores = [60, 65, 70, 75, 80, 85, 90, 95, 100, 120]

# Create a histogram
plt.hist(exam_scores, bins=5, edgecolor='k', alpha=0.7, color='blue')
plt.xlabel('Exam Scores')
plt.ylabel('Frequency')
plt.title('Histogram of Exam Scores')

# Calculate quartiles
q1 = np.percentile(exam_scores, 25)
q2 = np.percentile(exam_scores, 50)
q3 = np.percentile(exam_scores, 75)

# Plot quartiles
plt.axvline(q1, color='red', linestyle='dashed', label='Q1')
plt.axvline(q2, color='green', linestyle='dashed', label='Q2 (Median)')
plt.axvline(q3, color='yellow', linestyle='dashed', label='Q3')

plt.legend()
plt.show()
