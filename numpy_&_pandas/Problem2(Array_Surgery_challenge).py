import numpy as np

# Create the matrix
A = np.arange(1, 101).reshape(10, 10)
print("Original Matrix:")
print(A)

# 1. Extract prime-number rows (2nd, 3rd, 5th, 7th rows)
# Row numbers are 2,3,5,7 -> Indexes are 1,2,4,6
prime_rows = A[[1, 2, 4, 6], :]
print("\nPrime Number Rows:")
print(prime_rows)

# 2. Reverse every alternate column
alternate_columns = A.copy()
# Reverse columns 2,4,6,8,10 (indexes 1,3,5,7,9)
alternate_columns[:, 1::2] = alternate_columns[::-1, 1::2]
print("\nAlternate Columns Reversed:")
print(alternate_columns)

# 3. Replace the diagonal with zeros
diagonal_zero = A.copy()
np.fill_diagonal(diagonal_zero, 0)
print("\nMatrix after replacing diagonal with 0:")
print(diagonal_zero)

# 4. Sum of border elements only
top = np.sum(A[0, :])
bottom = np.sum(A[-1, :])
left = np.sum(A[1:-1, 0])
right = np.sum(A[1:-1, -1])
border_sum = top + bottom + left + right
print("\nSum of Border Elements:", border_sum)

# 5. Rotate the matrix 90° clockwise
rotated = np.rot90(A, -1)
print("\n90 Degree Clockwise Rotated Matrix:")
print(rotated)