import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Read your climate dataset
# -----------------------------

df = pd.read_csv(r"C:\Users\LENOVO\Bootcamp\Matplotlib\GlobalTemperatures.csv")

# Clean column names just in case
df.columns = df.columns.str.strip()

# Rename dt to Timestamp
df = df.rename(columns={"dt": "Timestamp"})

# Convert Timestamp to datetime
df["Timestamp"] = pd.to_datetime(df["Timestamp"], errors="coerce")

# Use LandAverageTemperature as Temperature
df["Temperature"] = pd.to_numeric(df["LandAverageTemperature"], errors="coerce")

# Fill the columns needed by your previous code
n = len(df)

countries = ["India", "USA", "UK", "Brazil", "Canada", "Australia", "Japan", "Germany"]
states = ["State1", "State2", "State3", "State4", "State5", "State6", "State7", "State8"]

df["Country"] = np.random.choice(countries, n)
df["State"] = np.random.choice(states, n)
df["Latitude"] = np.random.uniform(-90, 90, n)
df["Quality_Flag"] = np.random.choice(["Good", "Bad"], n, p=[0.85, 0.15])

# Keep only the columns your analysis uses
df = df[["Country", "State", "Timestamp", "Latitude", "Temperature", "Quality_Flag"]].copy()

# Save the prepared file
df.to_csv("climate_data.csv", index=False)

# -----------------------------------
# Read the dataset in chunks
# -----------------------------------

chunks = []

for data in pd.read_csv("climate_data.csv", chunksize=10000):
    data = data.dropna()
    data["Timestamp"] = pd.to_datetime(data["Timestamp"], errors="coerce")
    data.loc[data["Quality_Flag"] != "Good", "Temperature"] = np.nan
    chunks.append(data)

df = pd.concat(chunks, ignore_index=True)

# -----------------------------------
# Set MultiIndex
# -----------------------------------

df = df.set_index(["Country", "State", "Timestamp"])

# -----------------------------------
# Replace missing values
# using rolling median
# -----------------------------------

df = df.sort_index()

rolling_median = (
    df["Temperature"]
    .groupby(level=[0, 1])
    .transform(lambda x: x.rolling(5, min_periods=1).median())
)

df["Temperature"] = np.where(
    df["Temperature"].isna(),
    rolling_median,
    df["Temperature"]
)

# -----------------------------------
# Calculate yearly temperature anomaly
# -----------------------------------

df = df.reset_index()

df["Year"] = df["Timestamp"].dt.year

global_mean = df["Temperature"].mean()

df["Anomaly"] = df["Temperature"] - global_mean

annual_anomaly = df.groupby("Year")["Anomaly"].mean()

# -----------------------------------
# Latitude Band
# -----------------------------------

df["Latitude_Band"] = pd.cut(
    df["Latitude"],
    bins=[-90, -60, -30, 0, 30, 60, 90],
    labels=[
        "90S-60S",
        "60S-30S",
        "30S-0",
        "0-30N",
        "30N-60N",
        "60N-90N"
    ]
)

heatmap_data = df.pivot_table(
    values="Temperature",
    index="Latitude_Band",
    columns="Year",
    aggfunc=np.std
)

# -----------------------------------
# Plot
# -----------------------------------

fig, ax1 = plt.subplots(figsize=(12, 6))

ax1.plot(
    annual_anomaly.index,
    annual_anomaly.values,
    color="blue",
    marker="o"
)

ax1.set_xlabel("Year")
ax1.set_ylabel("Global Temperature Anomaly")
ax1.set_title("Global Climate Change & Thermal Anomaly Tracking")

ax2 = fig.add_axes([0.65, 0.25, 0.3, 0.55])

image = ax2.imshow(
    heatmap_data,
    aspect="auto",
    cmap="hot"
)

ax2.set_xticks(range(len(heatmap_data.columns)))
ax2.set_xticklabels(heatmap_data.columns, rotation=90)

ax2.set_yticks(range(len(heatmap_data.index)))
ax2.set_yticklabels(heatmap_data.index)

ax2.set_title("Std Dev Heatmap")

plt.colorbar(image, ax=ax2)
plt.tight_layout()
plt.show()