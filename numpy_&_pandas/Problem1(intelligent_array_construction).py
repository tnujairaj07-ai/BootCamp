import numpy as np
# creating matrix
numbers = np.arange(1, 21)
matrix = numbers ** 2 + 1       
matrix = matrix.reshape(4, 5)

print("Original Matrix:")
print(matrix)

# relationship bettween consiquitive numbers
print("\nRelationship:")
print("Each value is equal to n^2 + 1, where n starts from 1.")

# doubled matrix
double_matrix = matrix * 2
print("\nMatrix with Double Values:")
print(double_matrix)

# 
new_matrix = matrix.copy()
new_matrix[new_matrix % 5 == 0] = -1
print("\nMatrix after replacing multiples of 5 with -1:")
print(new_matrix)

# 
count = np.sum(matrix % 5 == 0)
print("\nNumber of values replaced:", count)