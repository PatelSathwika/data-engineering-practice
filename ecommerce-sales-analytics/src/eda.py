
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


# --------------------------------------------------
# 1. Project paths
# --------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent

INPUT_FILE = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "cleaned_sales.csv"
)

OUTPUT_DIR = (
    PROJECT_ROOT
    / "reports"
    / "charts"
)

OUTPUT_DIR.mkdir(
    parents=True,
    exist_ok=True
)


# --------------------------------------------------
# 2. Load data
# --------------------------------------------------

df = pd.read_csv(INPUT_FILE)

df["order_date"] = pd.to_datetime(
    df["order_date"]
)


# --------------------------------------------------
# 3. Monthly Revenue Trend
# --------------------------------------------------

df["year_month"] = (
    df["order_date"]
    .dt.to_period("M")
    .astype(str)
)

monthly_revenue = (
    df.groupby("year_month")["revenue"]
    .sum()
)

plt.figure(figsize=(12, 6))

monthly_revenue.plot()

plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "monthly_revenue_trend.png"
)

plt.close()


# --------------------------------------------------
# 4. Revenue by Category
# --------------------------------------------------

category_revenue = (
    df.groupby("category")["revenue"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 6))

category_revenue.plot(
    kind="bar"
)

plt.title("Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Revenue")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "revenue_by_category.png"
)

plt.close()


# --------------------------------------------------
# 5. Profit by Category
# --------------------------------------------------

category_profit = (
    df.groupby("category")["profit"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 6))

category_profit.plot(
    kind="bar"
)

plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "profit_by_category.png"
)

plt.close()


# --------------------------------------------------
# 6. Revenue by Region
# --------------------------------------------------

region_revenue = (
    df.groupby("region")["revenue"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 6))

region_revenue.plot(
    kind="bar"
)

plt.title("Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Revenue")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "revenue_by_region.png"
)

plt.close()


# --------------------------------------------------
# 7. Top 10 Products
# --------------------------------------------------

top_products = (
    df.groupby("product")["revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .sort_values()
)

plt.figure(figsize=(10, 6))

top_products.plot(
    kind="barh"
)

plt.title("Top 10 Products by Revenue")
plt.xlabel("Revenue")
plt.ylabel("Product")

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "top_10_products.png"
)

plt.close()


# --------------------------------------------------
# 8. Payment Method Analysis
# --------------------------------------------------

payment_revenue = (
    df.groupby("payment_mode")["revenue"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 6))

payment_revenue.plot(
    kind="bar"
)

plt.title("Revenue by Payment Method")
plt.xlabel("Payment Method")
plt.ylabel("Revenue")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "payment_method_revenue.png"
)

plt.close()


# --------------------------------------------------
# 9. Completion message
# --------------------------------------------------

print("=" * 60)
print("EDA COMPLETED SUCCESSFULLY")
print("=" * 60)

print(f"\nCharts saved to:")
print(OUTPUT_DIR)

print("\nGenerated charts:")

for file in sorted(OUTPUT_DIR.glob("*.png")):
    print(f"- {file.name}")