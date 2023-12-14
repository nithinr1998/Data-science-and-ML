import numpy as np

grades = np.array([85, 90, 78, 92, 88, 76, 95, 89, 84, 91])
average_grade = np.mean(grades)
print("Average grade:",average_grade)
above_90 = np.sum(grades > 90)
print("Number of Students scoring above 90:",above_90)
std_deviation = np.std(grades)
print("standard deviation of the grades:",std_deviation)