
import pandas as pd
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


# --------------------------------------------------
# 2. Load cleaned data
# --------------------------------------------------

df = pd.read_csv(INPUT_FILE)

df["order_date"] = pd.to_datetime(df["order_date"])


print("=" * 60)
print("E-COMMERCE SALES ANALYTICS")
print("=" * 60)


# --------------------------------------------------
# 3. Overall KPIs
# --------------------------------------------------

total_revenue = df["revenue"].sum()
total_profit = df["profit"].sum()
total_orders = df["order_id"].nunique()
total_units = df["quantity"].sum()

average_order_value = (
    total_revenue / total_orders
)

profit_margin = (
    total_profit / total_revenue
) * 100


print("\nKEY BUSINESS KPIs")
print("-" * 60)

print(f"Total Revenue       : ₹{total_revenue:,.2f}")
print(f"Total Profit        : ₹{total_profit:,.2f}")
print(f"Total Orders        : {total_orders:,}")
print(f"Units Sold          : {total_units:,}")
print(f"Average Order Value : ₹{average_order_value:,.2f}")
print(f"Profit Margin       : {profit_margin:.2f}%")


# --------------------------------------------------
# 4. Revenue by category
# --------------------------------------------------

category_sales = (
    df.groupby("category")
    .agg(
        Revenue=("revenue", "sum"),
        Profit=("profit", "sum"),
        Units=("quantity", "sum")
    )
    .sort_values(
        "Revenue",
        ascending=False
    )
)


print("\nREVENUE BY CATEGORY")
print("-" * 60)
print(category_sales)


# --------------------------------------------------
# 5. Revenue by region
# --------------------------------------------------

region_sales = (
    df.groupby("region")
    .agg(
        Revenue=("revenue", "sum"),
        Profit=("profit", "sum"),
        Orders=("order_id", "nunique")
    )
    .sort_values(
        "Revenue",
        ascending=False
    )
)


print("\nREVENUE BY REGION")
print("-" * 60)
print(region_sales)


# --------------------------------------------------
# 6. Top 10 products
# --------------------------------------------------

top_products = (
    df.groupby("product")
    .agg(
        Revenue=("revenue", "sum"),
        Profit=("profit", "sum"),
        Units=("quantity", "sum")
    )
    .sort_values(
        "Revenue",
        ascending=False
    )
    .head(10)
)


print("\nTOP 10 PRODUCTS")
print("-" * 60)
print(top_products)


# --------------------------------------------------
# 7. Monthly revenue trend
# --------------------------------------------------

df["year_month"] = (
    df["order_date"]
    .dt.to_period("M")
    .astype(str)
)

monthly_sales = (
    df.groupby("year_month")
    .agg(
        Revenue=("revenue", "sum"),
        Profit=("profit", "sum"),
        Orders=("order_id", "nunique")
    )
    .reset_index()
)


print("\nMONTHLY SALES TREND")
print("-" * 60)
print(monthly_sales)


# --------------------------------------------------
# 8. Payment method analysis
# --------------------------------------------------

payment_analysis = (
    df.groupby("payment_mode")
    .agg(
        Revenue=("revenue", "sum"),
        Orders=("order_id", "nunique")
    )
    .sort_values(
        "Revenue",
        ascending=False
    )
)


print("\nPAYMENT METHOD ANALYSIS")
print("-" * 60)
print(payment_analysis)


# --------------------------------------------------
# 9. Customer analysis
# --------------------------------------------------

customer_analysis = (
    df.groupby(
        ["customer_id", "customer_name"]
    )
    .agg(
        Orders=("order_id", "nunique"),
        Revenue=("revenue", "sum"),
        Profit=("profit", "sum"),
        Units=("quantity", "sum")
    )
    .sort_values(
        "Revenue",
        ascending=False
    )
)


print("\nTOP 10 CUSTOMERS")
print("-" * 60)
print(customer_analysis.head(10))


# --------------------------------------------------
# 10. Save analytical outputs
# --------------------------------------------------

OUTPUT_DIR = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "analysis"
)

OUTPUT_DIR.mkdir(
    parents=True,
    exist_ok=True
)


category_sales.to_csv(
    OUTPUT_DIR / "category_sales.csv"
)

region_sales.to_csv(
    OUTPUT_DIR / "region_sales.csv"
)

top_products.to_csv(
    OUTPUT_DIR / "top_products.csv"
)

monthly_sales.to_csv(
    OUTPUT_DIR / "monthly_sales.csv",
    index=False
)

payment_analysis.to_csv(
    OUTPUT_DIR / "payment_analysis.csv"
)

customer_analysis.to_csv(
    OUTPUT_DIR / "customer_analysis.csv"
)


print("\n" + "=" * 60)
print("ANALYSIS COMPLETED SUCCESSFULLY")
print("=" * 60)

print(f"Analysis files saved to: {OUTPUT_DIR}")