import numpy as np
import matplotlib.pyplot as plt

study_hours = np.array([2, 3, 4, 5, 6])
exam_scores = np.array([60, 75, 85, 90, 95])

mean_study_hours = np.mean(study_hours)
mean_exam_scores = np.mean(exam_scores)

m = np.sum((study_hours - mean_study_hours) * (exam_scores - mean_exam_scores)) / np.sum((study_hours - mean_study_hours) ** 2)

b = mean_exam_scores - m * mean_study_hours

def predict_exam_score(hours):
    return m * hours + b

predicted_score = predict_exam_score(4)
print(f"Predicted Exam Score for 4 hours of study: {predicted_score}")

regression_line = m * study_hours + b
plt.scatter(study_hours, exam_scores, color='blue', label='Actual Data')
plt.plot(study_hours, regression_line, color='red', label='Regression Line')
plt.scatter(4, predicted_score, color='green', label='Predicted Point (4 hours)')
plt.xlabel('Study Hours')
plt.ylabel('Exam Score')
plt.title('Simple Linear Regression')
plt.legend()
plt.show()