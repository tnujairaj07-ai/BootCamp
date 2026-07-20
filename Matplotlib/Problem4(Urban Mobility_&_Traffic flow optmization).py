import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ----------------------------
# Read Dataset
# ----------------------------

df = pd.read_csv(r"C:\Users\LENOVO\Bootcamp\Matplotlib\traffic_data.csv")

# Convert Timestamp into datetime
df["Timestamp"] = pd.to_datetime(df["Timestamp"])

# Sort data by VehicleID and Time
df = df.sort_values(["VehicleID", "Timestamp"])

# ----------------------------
# Pandas Part
# Calculate Haversine Distance
# ----------------------------

# Previous Latitude and Longitude
df["PrevLat"] = df.groupby("VehicleID")["Latitude"].shift(1)
df["PrevLon"] = df.groupby("VehicleID")["Longitude"].shift(1)

# Haversine Function
def haversine(lat1, lon1, lat2, lon2):

    R = 6371

    lat1 = np.radians(lat1)
    lon1 = np.radians(lon1)
    lat2 = np.radians(lat2)
    lon2 = np.radians(lon2)

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = np.sin(dlat/2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2)**2

    c = 2 * np.arcsin(np.sqrt(a))

    return R * c

# Calculate Distance
df["Distance(km)"] = haversine(
    df["PrevLat"],
    df["PrevLon"],
    df["Latitude"],
    df["Longitude"]
)

# Replace NaN values
df["Distance(km)"] = df["Distance(km)"].fillna(0)

# ----------------------------
# Create Grid
# ----------------------------

df["LatGrid"] = df["Latitude"].round(2)
df["LonGrid"] = df["Longitude"].round(2)

grid_data = df.groupby(["LatGrid", "LonGrid"])["Speed"].mean()

print("Average Speed by Grid")
print(grid_data)

# ----------------------------
# NumPy Part
# Traffic Categories
# ----------------------------

bins = [0, 20, 40, 200]

labels = ["Gridlock", "Slow", "Free Flow"]

df["TrafficState"] = np.digitize(df["Speed"], bins)

print("\nTraffic State")
print(df[["Speed", "TrafficState"]])

# ----------------------------
# Acceleration Trend
# ----------------------------

df["Acceleration"] = df.groupby("VehicleID")["Speed"].transform(
    lambda x: np.append(0, np.diff(x))
)

print("\nAcceleration")
print(df[["VehicleID", "Speed", "Acceleration"]])

# ----------------------------
# Day of Week
# ----------------------------

df["Day"] = df["Timestamp"].dt.day_name()

day_speed = df.groupby("Day")["Speed"].mean()

# ----------------------------
# Scatter Plot
# ----------------------------

plt.figure(figsize=(8,6))

scatter = plt.scatter(
    df["Longitude"],
    df["Latitude"],
    c=df["Speed"],
    cmap="viridis"
)

plt.colorbar(scatter, label="Speed")

plt.title("Traffic Congestion Map")
plt.xlabel("Longitude")
plt.ylabel("Latitude")

plt.show()

# ----------------------------
# Radar Chart
# ----------------------------

days = day_speed.index.tolist()

values = day_speed.values.tolist()

# Close the circle
values += values[:1]

angles = np.linspace(0, 2*np.pi, len(days), endpoint=False).tolist()
angles += angles[:1]

plt.figure(figsize=(6,6))

ax = plt.subplot(111, polar=True)

ax.plot(angles, values)

ax.fill(angles, values, alpha=0.25)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(days)

plt.title("Average Speed by Day")

plt.show()