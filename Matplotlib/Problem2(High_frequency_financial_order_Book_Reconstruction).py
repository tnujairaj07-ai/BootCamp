import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ----------------------------
# Read the Excel dataset
# ----------------------------

df = pd.read_excel(r"C:\Users\LENOVO\Bootcamp\Matplotlib\yahoo_data.xlsx")

# Clean column names
df.columns = df.columns.str.strip()

# Rename columns to match your code
df = df.rename(columns={
    "Date": "Timestamp",
    "Close*": "Price"
})

# Convert timestamp
df["Timestamp"] = pd.to_datetime(df["Timestamp"])

# Add required columns
df["Ticker"] = "AAPL"
df["Action"] = np.random.choice(["Buy", "Sell"], size=len(df))

# Keep only columns needed by your script
df = df[["Timestamp", "Ticker", "Price", "Volume", "Action"]].copy()

# Sort the data
df = df.sort_values(["Ticker", "Timestamp"])

# ----------------------------
# Calculate VWAP
# ----------------------------

df["PriceVolume"] = df["Price"] * df["Volume"]

vwap = df.groupby(
    ["Ticker", pd.Grouper(key="Timestamp", freq="1D")]
).agg(
    TotalPriceVolume=("PriceVolume", "sum"),
    TotalVolume=("Volume", "sum")
)

vwap["VWAP"] = vwap["TotalPriceVolume"] / vwap["TotalVolume"]

print("VWAP")
print(vwap)

# ----------------------------
# Bid-Ask Spread
# ----------------------------

buy_price = df[df["Action"] == "Buy"]["Price"]
sell_price = df[df["Action"] == "Sell"]["Price"]

spread = sell_price.mean() - buy_price.mean()
print("\nAverage Bid-Ask Spread =", spread)

# ----------------------------
# Market Depth (10 Levels)
# ----------------------------

price_levels = np.sort(df["Price"].unique())
depth = np.zeros(10)

for price in df["Price"]:
    index = np.searchsorted(price_levels, price)
    if index < 10:
        depth[index] += 1

print("\nMarket Depth")
print(depth)

# ----------------------------
# Create OHLC Data
# ----------------------------

ohlc = df.set_index("Timestamp").resample("1D").agg(
    {
        "Price": ["first", "max", "min", "last"],
        "Volume": "sum"
    }
)

ohlc.columns = ["Open", "High", "Low", "Close", "Volume"]

print("\nOHLC Data")
print(ohlc)

# ----------------------------
# Plot
# ----------------------------

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

ax1.plot(ohlc.index, ohlc["Close"], label="Close Price")
ax1.plot(vwap.index.get_level_values(1), vwap["VWAP"], color="red", label="VWAP")
ax1.set_title("OHLC Close Price with VWAP")
ax1.set_ylabel("Price")
ax1.legend()

ax2.bar(ohlc.index, ohlc["Volume"], width=0.003)
ax2.set_title("Volume")
ax2.set_ylabel("Volume")
ax2.set_xlabel("Time")

plt.tight_layout()
plt.show()