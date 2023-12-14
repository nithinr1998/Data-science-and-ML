import numpy as np
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([6, 7, 8, 9, 10])
result_add = arr1 + arr2
print("Addition:",result_add)
result_multiply = arr1 * arr2
print("Multiply:",result_multiply)
mean_result_add = np.mean(result_add)
print("Mean:",mean_result_add)
max_value_muliply = np.max(result_multiply)
print("Max value:",max_value_muliply)