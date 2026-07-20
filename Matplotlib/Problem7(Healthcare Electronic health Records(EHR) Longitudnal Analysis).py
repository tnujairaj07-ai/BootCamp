import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------------
# Read the Dataset
# -----------------------------------

df = pd.read_csv(r"C:\Users\LENOVO\Bootcamp\Matplotlib\ehr_data.csv")

# Convert VisitDate into datetime
df["VisitDate"] = pd.to_datetime(df["VisitDate"])

# Sort data by date
df = df.sort_values("VisitDate")

# -----------------------------------
# Pandas Part
# -----------------------------------

# Forward fill missing values (maximum 2 consecutive values)
df = df.ffill(limit=2)

# Aggregate Statistics for the whole dataset
summary = df[["SystolicBP", "DiastolicBP", "Cholesterol", "BloodSugar"]].agg(
    ["min", "max", "mean"]
)

print("Overall Summary")
print(summary)

# -----------------------------------
# NumPy Part
# Calculate BP Trend using polyfit
#-> polyfit is a mathematical function—most commonly used in data analysis libraries like Python's NumPy and MATLAB—that fits a smooth polynomial curve to a set of data points
# -----------------------------------

print("\nBlood Pressure Trend")

x = np.arange(len(df))
y = df["SystolicBP"].values

if len(x) > 1:
    slope, intercept = np.polyfit(x, y, 1)
    print("Slope:", round(slope, 2))
    print("Intercept:", round(intercept, 2))

# -----------------------------------
# Matplotlib Part
# Single Plot
# -----------------------------------

plt.figure(figsize=(12, 6))

plt.plot(
    df["VisitDate"],
    df["SystolicBP"],
    marker="o",
    label="Systolic BP"
)

plt.plot(
    df["VisitDate"],
    df["DiastolicBP"],
    marker="o",
    label="Diastolic BP"
)

# High-risk zone
# plt.axhspan (Axis Horizontal Span) is a Matplotlib function used to draw a shaded horizontal rectangle across a plot
plt.axhspan(
    140,
    200,
    color="red",
    alpha=0.2,
    label="High Risk"
)

plt.title("EHR Blood Pressure Over Time")
plt.xlabel("Visit Date")
plt.ylabel("Blood Pressure")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()