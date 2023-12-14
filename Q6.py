import pandas as pd

data = {
    'Student_ID': [1, 2,3],
    'Name': ['Nithin', 'Philip', 'Shon'],
    'Age': [18, 20, 22],
    'GPA': [4.5, 3.8, 3.6]
}


student_data = pd.DataFrame(data)

print("Original DataFrame:")
print(student_data)


filtered_students = student_data[student_data['Age'] >= 20]
print("\nStudents who are 20 years old or older:")
print(filtered_students)


average_gpa = student_data['GPA'].mean()
print("\nAverage GPA of all students:", average_gpa)


sorted_students = student_data.sort_values(by='GPA', ascending=False).head(5)
print("\nTop 5 students with the highest GPAs:")
print(sorted_students)


average_gpa_by_age = student_data.groupby('Age')['GPA'].mean()
print("\nAverage GPA by age group:")
print(average_gpa_by_age)
