import pandas as pd
import numpy as np

# Create data for 100 students

roll = list(range(1, 101))
name = []

for i in range(1, 101):
    name.append("Student" + str(i))

python = np.random.randint(0, 101, 100)
java = np.random.randint(0, 101, 100)
ml = np.random.randint(0, 101, 100)
cloud = np.random.randint(0, 101, 100)

attendance = np.random.randint(50, 101, 100)

# Create DataFrame

df = pd.DataFrame({
    "Roll": roll,
    "Name": name,
    "Python": python,
    "Java": java,
    "ML": ml,
    "Cloud": cloud,
    "Attendance": attendance
})

# 1. Calculate Total
df["Total"] = df["Python"] + df["Java"] + df["ML"] + df["Cloud"]

# 2. Calculate Percentage
df["Percentage"] = df["Total"] / 4

# 3. Assign Grade
grade = []

for per in df["Percentage"]:
    if per >= 90:
        grade.append("A+")
    elif per >= 80:
        grade.append("A")
    elif per >= 70:
        grade.append("B")
    elif per >= 60:
        grade.append("C")
    elif per >= 40:
        grade.append("D")
    else:
        grade.append("F")

df["Grade"] = grade

# 4. Rank Students
df["Rank"] = df["Percentage"].rank(ascending=False, method="min")

# Display DataFrame
print("Student Data")
print(df)

# 5. Top 10 Students
print("\nTop 10 Students")
top10 = df.sort_values(by="Percentage", ascending=False).head(10)
print(top10)

# 6. Students below 40% in at least two subjects
condition = (
    (df["Python"] < 40).astype(int) +
    (df["Java"] < 40).astype(int) +
    (df["ML"] < 40).astype(int) +
    (df["Cloud"] < 40).astype(int)
)

below40 = df[condition >= 2]

print("\nStudents below 40% in at least two subjects")
print(below40)

# 7. Department Topper
topper = df.sort_values(by="Percentage", ascending=False).head(1)

print("\nDepartment Topper")
print(topper)

# 8. Attendance below 75%
low_attendance = df[df["Attendance"] < 75]

print("\nAttendance below 75%")
print(low_attendance)

# 9. Export Topper List
topper.to_csv("Topper_List.csv", index=False)

print("\nTopper list exported successfully.")