import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------------
# Read the Dataset
# -----------------------------------

df = pd.read_csv(r"C:\Users\LENOVO\Bootcamp\Matplotlib\energy_data.csv")

# Convert Timestamp into datetime
df["Timestamp"] = pd.to_datetime(df["Timestamp"])

# Set DateTime Index
df = df.set_index("Timestamp")

# -----------------------------------
# Pandas Part
# -----------------------------------

# Extract Hour, Day of Week and Month
df["Hour"] = df.index.hour
df["Day"] = df.index.dayofweek
df["Month"] = df.index.month

# Average Consumption by Hour
hour_data = df.groupby("Hour")["kWh"].mean()

print("Average Hourly Consumption")
print(hour_data)

# Average Consumption by Day
day_data = df.groupby("Day")["kWh"].mean()

print("\nAverage Daily Consumption")
print(day_data)

# Average Consumption by Month
month_data = df.groupby("Month")["kWh"].mean()

print("\nAverage Monthly Consumption")
print(month_data)

# Create Seasons
def season(month):
    if month in [12, 1, 2]:
        return "Winter"
    elif month in [3, 4, 5]:
        return "Spring"
    elif month in [6, 7, 8]:
        return "Summer"
    else:
        return "Autumn"

df["Season"] = df["Month"].apply(season)

# Pivot Table
pivot_table = df.pivot_table(
    values="kWh",
    index="Hour",
    columns="Season",
    aggfunc="mean"
)

print("\nPivot Table")
print(pivot_table)

# -----------------------------------
# NumPy Part
# Fast Fourier Transform
# -> The Fast Fourier Transform (FFT) is a mathematical algorithm that converts a signal from its original domain (like time or space) into the frequency domain.
# -----------------------------------

fft_values = np.fft.fft(df["kWh"])

magnitude = np.abs(fft_values)

print("\nFFT Magnitude")
print(magnitude)

# -----------------------------------
# Matplotlib
# -----------------------------------

plt.figure(figsize=(12,5))

# Raw Signal
plt.plot(
    df.index,
    df["kWh"],
    label="Raw Signal"
)

# Smoothed Trend Line
smooth = df["kWh"].rolling(20).mean()

plt.plot(
    df.index,
    smooth,
    color="red",
    label="Smoothed Trend"
)

plt.title("Energy Consumption Over Time")
plt.xlabel("Date")
plt.ylabel("kWh")
plt.legend()

plt.show()

# -----------------------------------
# Weekday vs Weekend
# -----------------------------------

df["Type"] = np.where(df["Day"] < 5, "Weekday", "Weekend")

usage = df.groupby("Type")["kWh"].mean()

plt.figure(figsize=(5,5))

plt.bar(
    usage.index,
    usage.values
)

plt.title("Average Energy Usage")
plt.xlabel("Day Type")
plt.ylabel("Average kWh")

plt.show()