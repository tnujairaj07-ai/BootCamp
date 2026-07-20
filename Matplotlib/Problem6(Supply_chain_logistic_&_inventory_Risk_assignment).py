import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Read the single dataset
# -----------------------------

data = pd.read_csv(r"C:\Users\LENOVO\Bootcamp\Matplotlib\sales_data.csv")  # replace with your file name

# Convert Date column into datetime
data["Date"] = pd.to_datetime(data["Date"])

print("Data from single file")
print(data.head())

# -----------------------------
# Calculate Moving Averages
# -----------------------------
# Use Product ID instead of SkuID

data = data.sort_values(["Product ID", "Date"])

data["MA_7"] = data.groupby("Product ID")["Demand"].transform(
    lambda x: x.rolling(7, min_periods=1).mean()
)

data["MA_30"] = data.groupby("Product ID")["Demand"].transform(
    lambda x: x.rolling(30, min_periods=1).mean()
)

print("\nMoving Averages")
print(data[["Product ID", "Date", "MA_7", "MA_30"]])

# -----------------------------
# Stockout Risk
# -----------------------------
# Inventory Level acts as CurrentStock.
# SafetyStockLevel is derived from Demand (example rule).

data["SafetyStockLevel"] = data.groupby("Product ID")["Demand"].transform(
    lambda x: x.rolling(30, min_periods=1).mean() * 0.3
)

data["StockoutRisk"] = (
    data["Inventory Level"] <= data["SafetyStockLevel"]
)

print("\nStockout Risk")
print(data[["Product ID", "Inventory Level", "SafetyStockLevel", "StockoutRisk"]])

# -----------------------------
# NumPy Part
# Assign Priority Levels
# -----------------------------

conditions = [
    data["Inventory Level"] <= data["SafetyStockLevel"] * 0.5,
    data["Inventory Level"] <= data["SafetyStockLevel"],
    data["Inventory Level"] > data["SafetyStockLevel"]
]

choices = [
    "High",
    "Medium",
    "Low"
]

data["Priority"] = np.select(
    conditions,
    choices,
    default="Low"
)

print("\nPriority Levels")
print(data[["Product ID", "Inventory Level", "Priority"]])

# -----------------------------
# Matplotlib Plot
# Make chart less congested
# -----------------------------

# 1) Optionally focus on a single Product ID (uncomment and change ID)
# product_data = data[data["Product ID"] == "P0001"]
# else use all data:
product_data = data.copy()

# 2) Set Date as index
product_data = product_data.set_index("Date")

# 3) Resample weekly only for numeric columns
# Select numeric columns (Inventory Level and SafetyStockLevel)
numeric_cols = ["Inventory Level", "SafetyStockLevel"]

weekly = product_data[numeric_cols].resample("W").mean()  # mean only on numeric cols [web:617][web:620]

plt.figure(figsize=(14, 7))

# Step Plot using weekly Inventory Level
plt.step(
    weekly.index,
    weekly["Inventory Level"],
    where="mid",
    label="Inventory Level (weekly avg)"
)

# Safety Stock Line using weekly SafetyStockLevel mean
plt.axhline(
    y=weekly["SafetyStockLevel"].mean(),
    color="green",
    linestyle="--",
    label="Safety Stock Level"
)

# Highlight negative stock
negative = weekly[weekly["Inventory Level"] < 0]

plt.scatter(
    negative.index,
    negative["Inventory Level"],
    color="red",
    label="Below Zero"
)

plt.title("Weekly Stock Levels")
plt.xlabel("Date")
plt.ylabel("Inventory Level")
plt.legend()

# Make chart more readable
plt.grid(alpha=0.3)          # light grid [web:608]
plt.xticks(rotation=45)      # rotate date labels [web:610]
plt.tight_layout()
plt.show()