import numpy as np

original_array = np.array([1, 2, 3, 4, 5])
appended_array = np.append(original_array, [6, 7, 8])
inserted_array = np.insert(original_array, 2, [10, 11])

deleted_array = np.delete(original_array, [1, 3])

unique_elements = np.unique(original_array) 

sorted_array = np.sort(original_array)

np.savetxt('array.txt', original_array)

loaded_array = np.loadtxt('array.txt')

print("Original array:", original_array)
print("Appended array:", appended_array)
print("Inserted array:", inserted_array)
print("Deleted array:", deleted_array)
print("Unique elements:", unique_elements)
print("Sorted array:", sorted_array)
print("Loaded array:", loaded_array)
