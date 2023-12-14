import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


# Sample data
hours_of_study = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
student_marks = np.array([40, 50, 60, 70, 80, 90, 100, 110, 120, 130])


# Create a linear regression model
model = LinearRegression()


# Fit the model to the data
model.fit(hours_of_study.reshape(-1, 1), student_marks)


# Predict student marks for a new set of study hours
new_hours_of_study = np.array([11, 12, 13, 14, 15]).reshape(-1, 1)
predicted_marks = model.predict(new_hours_of_study)


# Plot the data points
plt.scatter(hours_of_study, student_marks, label='Actual Data')


# Plot the linear regression line
plt.plot(new_hours_of_study, predicted_marks, label='Linear Regression', color='red')


# Set labels and show the plot
plt.xlabel('Hours of Study')
plt.ylabel('Student Marks')
plt.legend()
plt.show()
