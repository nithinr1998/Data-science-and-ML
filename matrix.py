import numpy as np

matrix_A = np.array([[1, 2, 3],[4, 5, 6], [7, 8, 9]])

matrix_B = np.array([[9, 8, 7],  [6, 5, 4], [3, 2, 1]])

matrix_sum = matrix_A + matrix_B
print("matrix sum:",matrix_sum)
matrix_product = matrix_A * matrix_B
print("matrix element-wise product:",matrix_product)

matrix_dot = np.dot(matrix_A, matrix_B)
print("Matrix Dot Product:",matrix_dot)

matrix_A_transpose = np.transpose(matrix_A)
print("Matrix A Transpose:",matrix_A_transpose)

determinant_B = np.linalg.det(matrix_B)
print("Determinant of Matrix B:",determinant_B)

eigenvalues_A, eigenvectors_A = np.linalg.eig(matrix_A)
print("Eigenvalues of Matrix A:",eigenvalues_A)
print("Eigenvectors of Matrix A:",eigenvectors_A)
