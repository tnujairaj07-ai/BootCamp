import pandas as pd
import numpy as np

# Create data for 500 employees

empid = list(range(1, 501))

departments = ["IT", "HR", "Finance", "Marketing", "Sales"]

department = np.random.choice(departments, 500)

experience = np.random.randint(1, 31, 500)

salary = np.random.randint(25000, 100001, 500)

performance = np.random.randint(1, 6, 500)

# Create DataFrame

df = pd.DataFrame({
    "EmpID": empid,
    "Department": department,
    "Experience": experience,
    "Salary": salary,
    "Performance": performance
})

# 1. Save as CSV
df.to_csv("employees.csv", index=False)

# 2. Save as Excel
df.to_excel("employees.xlsx", index=False)

# 3. Read both files
csv_data = pd.read_csv("employees.csv")
excel_data = pd.read_excel("employees.xlsx")

# 4. Verify both files contain same data
print("Both files are identical:", csv_data.equals(excel_data))

# 5. Average salary department-wise
print("\nAverage Salary Department-wise")
print(df.groupby("Department")["Salary"].mean())

# 6. Highest Performer
highest = df[df["Performance"] == df["Performance"].max()]

print("\nHighest Performer")
print(highest)

# 7. Employees with salary greater than department average

avg_salary = df.groupby("Department")["Salary"].transform("mean")

high_salary = df[df["Salary"] > avg_salary]

print("\nEmployees with Salary Greater than Department Average")
print(high_salary)

# 8. Employees having experience >15 years and performance <3

result = df[(df["Experience"] > 15) & (df["Performance"] < 3)]

print("\nExperience >15 Years and Performance <3")
print(result)

# 9. Create Bonus column

bonus = []

for i in df["Performance"]:
    if i >= 4:
        bonus.append(0.10)
    else:
        bonus.append(0.05)

df["Bonus"] = df["Salary"] * bonus

print("\nData with Bonus")
print(df)

# 10. Export employees receiving bonus above Rs.10000

bonus_emp = df[df["Bonus"] > 10000]

bonus_emp.to_csv("Bonus_Employees.csv", index=False)

print("\nEmployees receiving bonus above Rs.10000")
print(bonus_emp)

print("\nBonus employee list exported successfully.")