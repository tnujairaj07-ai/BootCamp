import numpy as np

# Generate data (30 days, 5 departments)
patients = np.random.randint(50, 251, size=(30, 5))

print("Patient Data:")
print(patients)

# 1. Department-wise Mean
mean = np.mean(patients, axis=0)
print("\nDepartment-wise Mean:")
print(mean)

# 2. Department-wise Median
median = np.median(patients, axis=0)
print("\nDepartment-wise Median:")
print(median)

# 3. Department-wise Standard Deviation
std = np.std(patients, axis=0)
print("\nDepartment-wise Standard Deviation:")
print(std)

# 4. Highest patient day (maximum value in each department)
highest = np.max(patients, axis=0)
print("\nHighest Patient Count:")
print(highest)

# 5. Lowest patient day (minimum value in each department)
lowest = np.min(patients, axis=0)
print("\nLowest Patient Count:")
print(lowest)

# 6. Detect Outliers (Mean ± 2*SD)
lower_limit = mean - 2 * std
upper_limit = mean + 2 * std
outliers = (patients < lower_limit) | (patients > upper_limit)
print("\nOutlier Positions (True = Outlier):")
print(outliers)

# 7. Replace outliers with department mean
new_patients = patients.copy()
new_patients[outliers] = np.take(mean, np.where(outliers)[1])
print("\nData after replacing outliers with department mean:")
print(new_patients)
