
import pandas as pd
from pathlib import Path


# --------------------------------------------------
# 1. Define project paths
# --------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent

INPUT_FILE = PROJECT_ROOT / "data" / "raw" / "ecommerce_sales.csv"
OUTPUT_FILE = PROJECT_ROOT / "data" / "processed" / "cleaned_sales.csv"


# --------------------------------------------------
# 2. Load raw data
# --------------------------------------------------

print("Loading raw data...")

df = pd.read_csv(INPUT_FILE)

print(f"Initial rows: {len(df)}")
print(f"Initial columns: {len(df.columns)}")


# --------------------------------------------------
# 3. Standardize column names
# --------------------------------------------------

df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)


# --------------------------------------------------
# 4. Convert date column
# --------------------------------------------------

df["order_date"] = pd.to_datetime(
    df["order_date"],
    errors="coerce"
)


# --------------------------------------------------
# 5. Handle missing values
# --------------------------------------------------

print("\nMissing values before cleaning:")
print(df.isnull().sum())

# City → replace missing values
df["city"] = df["city"].fillna("Unknown")

# Payment mode → replace missing values
df["payment_mode"] = df["payment_mode"].fillna("Unknown")


# --------------------------------------------------
# 6. Remove duplicate records
# --------------------------------------------------

duplicate_count = df.duplicated().sum()

print(f"\nDuplicate rows found: {duplicate_count}")

df = df.drop_duplicates()

print(f"Rows after removing duplicates: {len(df)}")


# --------------------------------------------------
# 7. Validate numerical columns
# --------------------------------------------------

numeric_columns = [
    "quantity",
    "unit_price",
    "discount",
    "gross_sales",
    "discount_amount",
    "revenue",
    "cost",
    "profit",
    "profit_margin"
]

for column in numeric_columns:
    df[column] = pd.to_numeric(
        df[column],
        errors="coerce"
    )


# --------------------------------------------------
# 8. Remove invalid records
# --------------------------------------------------

df = df[df["quantity"] > 0]
df = df[df["unit_price"] >= 0]


# --------------------------------------------------
# 9. Recalculate important business metrics
# --------------------------------------------------

df["gross_sales"] = (
    df["quantity"] * df["unit_price"]
)

df["discount_amount"] = (
    df["gross_sales"] * df["discount"]
)

df["revenue"] = (
    df["gross_sales"] - df["discount_amount"]
)

df["profit"] = (
    df["revenue"] - df["cost"]
)

df["profit_margin"] = (
    df["profit"] / df["revenue"]
).fillna(0)


# --------------------------------------------------
# 10. Create processed-data directory
# --------------------------------------------------

OUTPUT_FILE.parent.mkdir(
    parents=True,
    exist_ok=True
)


# --------------------------------------------------
# 11. Save cleaned data
# --------------------------------------------------

df.to_csv(
    OUTPUT_FILE,
    index=False
)


# --------------------------------------------------
# 12. Data-quality summary
# --------------------------------------------------

print("\n" + "=" * 50)
print("DATA CLEANING COMPLETED")
print("=" * 50)

print(f"Final rows      : {len(df)}")
print(f"Final columns   : {len(df.columns)}")
print(f"Output file     : {OUTPUT_FILE}")

print("\nMissing values after cleaning:")
print(df.isnull().sum())

print("\nSample cleaned data:")
print(df.head())