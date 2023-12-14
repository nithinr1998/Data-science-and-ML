import numpy as np
import matplotlib.pyplot as plt

# Generate a sample dataset (exam scores)
np.random.seed(42)  # for reproducibility
exam_scores = np.random.randint(0, 100, 100)

# Plot histogram
plt.figure(figsize=(10, 6))
plt.hist(exam_scores, bins=10, edgecolor='black', alpha=0.7, color='skyblue')
plt.xlabel('Exam Scores')
plt.ylabel('Frequency')
plt.title('Histogram of Exam Scores with Quartiles')
plt.axvline(np.percentile(exam_scores, 25), color='red', linestyle='dashed', linewidth=2, label='Q1')
plt.axvline(np.percentile(exam_scores, 50), color='green', linestyle='dashed', linewidth=2, label='Q2 (Median)')
plt.axvline(np.percentile(exam_scores, 75), color='blue', linestyle='dashed', linewidth=2, label='Q3')
plt.legend()
plt.show()
