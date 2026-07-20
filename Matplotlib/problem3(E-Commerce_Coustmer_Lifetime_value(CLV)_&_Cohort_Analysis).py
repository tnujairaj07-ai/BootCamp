import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read Dataset
df = pd.read_csv(r"C:\Users\LENOVO\Bootcamp\Matplotlib\ecommerce_data.csv")

# Convert InvoiceDate to datetime
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

# ----------------------------
# Create Total Amount
# ----------------------------

df["TotalAmount"] = df["Quantity"] * df["UnitPrice"]

# ----------------------------
# Find Cohort Month
# ----------------------------

df["InvoiceMonth"] = df["InvoiceDate"].dt.to_period("M")

df["CohortMonth"] = df.groupby("CustomerID")["InvoiceMonth"].transform("min")

# ----------------------------
# Calculate Cohort Index,
# ----------------------------

df["CohortIndex"] = (
    (df["InvoiceMonth"].dt.year - df["CohortMonth"].dt.year) * 12
    + (df["InvoiceMonth"].dt.month - df["CohortMonth"].dt.month)
    + 1
)

# ----------------------------
# Create Retention Matrix, 
# ----------------------------

cohort_data = df.groupby(["CohortMonth", "CohortIndex"])["CustomerID"].nunique()

retention = cohort_data.unstack()

cohort_size = retention.iloc[:, 0]

retention_matrix = retention.divide(cohort_size, axis=0) * 100

print("Retention Matrix (%)")
print(retention_matrix)

# ----------------------------
# NumPy Part
# Percentage Decay
# ----------------------------

decay = 100 - retention_matrix.fillna(0)

print("\nPercentage Decay")
print(decay)

# ----------------------------
# Rolling 30-Day Cumulative Spend
# ----------------------------

daily_spend = df.groupby(
    ["CustomerID", pd.Grouper(key="InvoiceDate", freq="D")]
)["TotalAmount"].sum()

daily_spend = daily_spend.reset_index()

rolling_spend = []

for customer in daily_spend["CustomerID"].unique():

    temp = daily_spend[daily_spend["CustomerID"] == customer]

    spend = temp["TotalAmount"].values

    cumulative = np.cumsum(spend)

    temp["CumulativeSpend"] = cumulative

    rolling_spend.append(temp)

rolling_spend = pd.concat(rolling_spend)

print("\nRolling Cumulative Spend")
print(rolling_spend)

# ----------------------------
# Heatmap + Scatter in one figure
# ----------------------------

fig, (ax_heat, ax_scatter) = plt.subplots(1, 2, figsize=(16, 6))

# Heatmap on ax_heat
heat_data = retention_matrix.fillna(0)

im = ax_heat.imshow(
    heat_data,
    cmap="YlGnBu",
    aspect="auto"
)

fig.colorbar(im, ax=ax_heat, label="Retention %")

# X-axis for heatmap
ax_heat.set_xticks(range(len(retention_matrix.columns)))
ax_heat.set_xticklabels(retention_matrix.columns)

# Y-axis for heatmap
ax_heat.set_yticks(range(len(retention_matrix.index)))
ax_heat.set_yticklabels(retention_matrix.index.astype(str))

# Add Percentage Values on heatmap
for i in range(retention_matrix.shape[0]):
    for j in range(retention_matrix.shape[1]):
        value = retention_matrix.iloc[i, j]
        if not np.isnan(value):
            ax_heat.text(
                j,
                i,
                f"{value:.1f}%",
                ha="center",
                va="center",
                fontsize=8,
                color="black"
            )

ax_heat.set_title("Customer Cohort Retention Heatmap")
ax_heat.set_xlabel("Months Since First Purchase")
ax_heat.set_ylabel("Cohort Month")

# Scatter on ax_scatter: CohortIndex vs Retention %
for i, cohort in enumerate(retention_matrix.index):
    for j, month in enumerate(retention_matrix.columns):
        value = retention_matrix.iloc[i, j]
        if not np.isnan(value):
            ax_scatter.scatter(
                month,     # x: CohortIndex (month number)
                value,     # y: Retention %
                s=25,
                alpha=0.7
            )

ax_scatter.set_title("Retention vs Months Since First Purchase")
ax_scatter.set_xlabel("Cohort Index (Months)")
ax_scatter.set_ylabel("Retention (%)")
ax_scatter.grid(True)

plt.tight_layout()
plt.show()