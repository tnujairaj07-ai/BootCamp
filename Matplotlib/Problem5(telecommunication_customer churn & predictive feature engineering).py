import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Read the Dataset
# -----------------------------

df = pd.read_csv(r"C:\Users\LENOVO\Bootcamp\Matplotlib\telecom_data.csv")

# -----------------------------
# Fix Data Types
# -----------------------------

df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
df["MonthlyCharges"] = pd.to_numeric(df["MonthlyCharges"], errors="coerce")
df["Tenure"] = pd.to_numeric(df["Tenure"], errors="coerce")

# Remove missing values
df = df.dropna()

# -----------------------------
# One-Hot Encoding
# -----------------------------

df = pd.get_dummies(df, columns=["ContractType"])

print("After One-Hot Encoding")
print(df.head())

# -----------------------------
# Divide Tenure into 4 Groups
# -----------------------------

df["TenureGroup"] = pd.qcut(
    df["Tenure"],
    q=4,
    labels=["Low", "Medium", "High", "Very High"]
)

print("\nTenure Groups")
print(df[["Tenure", "TenureGroup"]].head())

# -----------------------------
# NumPy Part
# Detect Outliers using IQR
# -----------------------------

Q1 = np.percentile(df["TotalCharges"], 25)
Q3 = np.percentile(df["TotalCharges"], 75)

IQR = Q3 - Q1

Lower = Q1 - 1.5 * IQR
Upper = Q3 + 1.5 * IQR

outliers = df[
    (df["TotalCharges"] < Lower) |
    (df["TotalCharges"] > Upper)
]

print("\nOutliers")
print(outliers)

# -----------------------------
# Matplotlib
# 3 x 3 Grid of Subplots
# -----------------------------

fig, axes = plt.subplots(3, 3, figsize=(15, 12))

# Histogram - Monthly Charges
axes[0,0].hist(
    df[df["Churn"]=="Yes"]["MonthlyCharges"],
    alpha=0.6,
    label="Churn"
)
axes[0,0].hist(
    df[df["Churn"]=="No"]["MonthlyCharges"],
    alpha=0.6,
    label="Retained"
)
axes[0,0].set_title("Monthly Charges")
axes[0,0].legend()

# Histogram - Total Charges
axes[0,1].hist(
    df[df["Churn"]=="Yes"]["TotalCharges"],
    alpha=0.6
)
axes[0,1].hist(
    df[df["Churn"]=="No"]["TotalCharges"],
    alpha=0.6
)
axes[0,1].set_title("Total Charges")

# Histogram - Tenure
axes[0,2].hist(
    df[df["Churn"]=="Yes"]["Tenure"],
    alpha=0.6
)
axes[0,2].hist(
    df[df["Churn"]=="No"]["Tenure"],
    alpha=0.6
)
axes[0,2].set_title("Tenure")

# Boxplot - Monthly Charges
axes[1,0].boxplot([
    df[df["Churn"]=="Yes"]["MonthlyCharges"],
    df[df["Churn"]=="No"]["MonthlyCharges"]
])
axes[1,0].set_xticklabels(["Yes","No"])
axes[1,0].set_title("Monthly Charges")

# Boxplot - Total Charges
axes[1,1].boxplot([
    df[df["Churn"]=="Yes"]["TotalCharges"],
    df[df["Churn"]=="No"]["TotalCharges"]
])
axes[1,1].set_xticklabels(["Yes","No"])
axes[1,1].set_title("Total Charges")

# Boxplot - Tenure
axes[1,2].boxplot([
    df[df["Churn"]=="Yes"]["Tenure"],
    df[df["Churn"]=="No"]["Tenure"]
])
axes[1,2].set_xticklabels(["Yes","No"])
axes[1,2].set_title("Tenure")

# Bar Chart - Churn Count
count = df["Churn"].value_counts()

axes[2,0].bar(count.index, count.values)
axes[2,0].set_title("Churn Count")

# Pie Chart - Contract Types
contract = df.filter(like="ContractType").sum()

axes[2,1].pie(
    contract,
    labels=contract.index,
    autopct="%1.1f%%"
)
axes[2,1].set_title("Contract Type")

# Scatter Plot
axes[2,2].scatter(
    df["MonthlyCharges"],
    df["TotalCharges"]
)
axes[2,2].set_title("Monthly vs Total Charges")
axes[2,2].set_xlabel("Monthly Charges")
axes[2,2].set_ylabel("Total Charges")

plt.tight_layout()
plt.show()