from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

BASE = Path(__file__).resolve().parent
CHARTS = BASE / "charts"
CHARTS.mkdir(exist_ok=True)

df = pd.read_csv(BASE / "retail_sales.csv", parse_dates=["Date"])

# TASK 2: Exploratory Data Analysis
print("\n--- Dataset shape ---")
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")
print("\n--- First five rows ---")
print(df.head())
print("\n--- Data types ---")
print(df.dtypes)
print("\n--- Missing values by column ---")
print(df.isna().sum())
print("\n--- Numeric summary ---")
print(df[["Quantity", "Unit_Price_INR", "Sales_INR"]].describe().round(2))

monthly = df.groupby(df["Date"].dt.to_period("M"))["Sales_INR"].sum()
category_sales = df.groupby("Category")["Sales_INR"].sum().sort_values(ascending=False)
product_qty = df.groupby("Product")["Quantity"].sum().sort_values(ascending=False)
region_sales = df.groupby("Region", dropna=True)["Sales_INR"].sum().sort_values(ascending=False)

print("\n--- Monthly sales (INR) ---\n", monthly)
print("\n--- Sales by category (INR) ---\n", category_sales)
print("\n--- Sales by region (INR; missing region excluded) ---\n", region_sales)
print("\n--- Total sales (INR) ---", int(df["Sales_INR"].sum()))
print("Top sales category:", category_sales.idxmax())
print("Top quantity product:", product_qty.idxmax())

# TASK 3: Data Visualization
plt.figure(figsize=(8, 5))
monthly.index = monthly.index.astype(str)
monthly.plot(kind="line", marker="o", title="Monthly Retail Sales")
plt.xlabel("Month"); plt.ylabel("Sales (INR)"); plt.tight_layout()
plt.savefig(CHARTS / "monthly_sales.png", dpi=160); plt.close()

plt.figure(figsize=(8, 5))
category_sales.plot(kind="bar", title="Sales by Product Category")
plt.xlabel("Category"); plt.ylabel("Sales (INR)"); plt.xticks(rotation=20); plt.tight_layout()
plt.savefig(CHARTS / "category_sales.png", dpi=160); plt.close()

plt.figure(figsize=(8, 5))
product_qty.sort_values().plot(kind="barh", title="Quantity Sold by Product")
plt.xlabel("Quantity sold"); plt.ylabel("Product"); plt.tight_layout()
plt.savefig(CHARTS / "product_quantity.png", dpi=160); plt.close()

plt.figure(figsize=(8, 5))
df["Sales_INR"].plot(kind="hist", bins=8, title="Distribution of Transaction Sales")
plt.xlabel("Sales per transaction (INR)"); plt.ylabel("Frequency"); plt.tight_layout()
plt.savefig(CHARTS / "sales_distribution.png", dpi=160); plt.close()

print(f"\nCharts saved to: {CHARTS}")
print("EDA note: Region has missing values; investigate or label them as 'Unknown' before region-level reporting.")
