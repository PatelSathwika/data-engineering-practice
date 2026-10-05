
import pandas as pd

# 1. Read raw data
df = pd.read_csv("../data/sales_data.csv")

print("Original Data:")
print(df)

# 2. Check missing values
print("\n Missing Values:")
print(df.isnull().sum())

# 3. Remove duplicate records
df = df.drop_duplicates()

# 4. Handle missing quantity
df["quantity"] = df["quantity"].fillna(0)

# 5. Calculate revenue
df["revenue"] = df["quantity"] * df["price"]

# 6. Display cleaned data
print("\nCleaned Data:")
print(df)

# 7. Calculate total revenue
total_revenue = df["revenue"].sum()

print("\nTotal Revenue:", total_revenue)

# 8. Save processed data
df.to_csv("../data/processed_sales.csv", index=False)

print("\nProcessed file created successfully.")
