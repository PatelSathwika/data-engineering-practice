
import pandas as pd
import numpy as np
import random
from pathlib import Path


# ============================================================
# 1. REPRODUCIBILITY
# ============================================================

np.random.seed(42)
random.seed(42)


# ============================================================
# 2. PROJECT PATH
# ============================================================

PROJECT_ROOT = Path.cwd()

OUTPUT_FILE = (
    PROJECT_ROOT
    / "data"
    / "raw"
    / "ecommerce_sales.csv"
)


# ============================================================
# 3. MASTER DATA
# ============================================================

regions = {
    "North": {
        "states": [
            "Delhi",
            "Punjab",
            "Haryana",
            "Uttar Pradesh"
        ],
        "cities": [
            "Delhi",
            "Amritsar",
            "Gurgaon",
            "Noida"
        ]
    },

    "South": {
        "states": [
            "Telangana",
            "Karnataka",
            "Tamil Nadu",
            "Kerala"
        ],
        "cities": [
            "Hyderabad",
            "Bangalore",
            "Chennai",
            "Kochi"
        ]
    },

    "East": {
        "states": [
            "West Bengal",
            "Odisha",
            "Bihar",
            "Jharkhand"
        ],
        "cities": [
            "Kolkata",
            "Bhubaneswar",
            "Patna",
            "Ranchi"
        ]
    },

    "West": {
        "states": [
            "Maharashtra",
            "Gujarat",
            "Rajasthan",
            "Goa"
        ],
        "cities": [
            "Mumbai",
            "Ahmedabad",
            "Jaipur",
            "Panaji"
        ]
    }
}


products = {

    "Electronics": {

        "Mobile": [
            "iPhone",
            "Samsung Galaxy",
            "OnePlus",
            "Redmi"
        ],

        "Laptop": [
            "Dell Laptop",
            "HP Laptop",
            "Lenovo Laptop",
            "MacBook"
        ],

        "Accessories": [
            "Headphones",
            "Keyboard",
            "Mouse",
            "Power Bank"
        ]
    },


    "Furniture": {

        "Chair": [
            "Office Chair",
            "Gaming Chair",
            "Dining Chair"
        ],

        "Table": [
            "Study Table",
            "Office Table",
            "Dining Table"
        ],

        "Storage": [
            "Bookshelf",
            "Cabinet",
            "Storage Rack"
        ]
    },


    "Clothing": {

        "Men": [
            "Men Shirt",
            "Men Jeans",
            "Men Jacket"
        ],

        "Women": [
            "Women Dress",
            "Women Saree",
            "Women Jacket"
        ],

        "Kids": [
            "Kids Shirt",
            "Kids Dress",
            "Kids Jeans"
        ]
    },


    "Home & Kitchen": {

        "Kitchen": [
            "Mixer Grinder",
            "Microwave",
            "Cookware Set"
        ],

        "Appliances": [
            "Air Conditioner",
            "Refrigerator",
            "Washing Machine"
        ],

        "Decor": [
            "Wall Clock",
            "Lamp",
            "Curtains"
        ]
    }
}


payment_modes = [
    "Credit Card",
    "Debit Card",
    "UPI",
    "Net Banking",
    "Cash on Delivery"
]


shipping_modes = [
    "Standard",
    "Express",
    "Same Day"
]


customer_names = [
    "Rahul Sharma",
    "Priya Reddy",
    "Amit Kumar",
    "Sneha Patel",
    "Arjun Singh",
    "Anjali Gupta",
    "Vikram Rao",
    "Neha Verma",
    "Kiran Kumar",
    "Pooja Mehta",
    "Rohit Joshi",
    "Divya Nair",
    "Suresh Reddy",
    "Swathi Rao",
    "Naveen Kumar"
]


# ============================================================
# 4. GENERATE TRANSACTION DATA
# ============================================================

number_of_records = 10000

records = []


for i in range(number_of_records):

    order_id = f"ORD{100001 + i}"


    # Customer
    customer_number = np.random.randint(1, 2501)

    customer_id = (
        f"CUST{customer_number:05d}"
    )

    customer_name = random.choice(
        customer_names
    )


    # Region
    region = random.choice(
        list(regions.keys())
    )

    state = random.choice(
        regions[region]["states"]
    )

    city = random.choice(
        regions[region]["cities"]
    )


    # Product
    category = random.choice(
        list(products.keys())
    )

    sub_category = random.choice(
        list(products[category].keys())
    )

    product = random.choice(
        products[category][sub_category]
    )


    # Date
    order_date = (
        pd.Timestamp("2024-01-01")
        + pd.to_timedelta(
            np.random.randint(0, 730),
            unit="D"
        )
    )


    # Sales information
    quantity = np.random.randint(
        1,
        6
    )

    unit_price = round(
        np.random.uniform(
            500,
            100000
        ),
        2
    )


    discount = round(
        np.random.choice(
            [
                0,
                0.05,
                0.10,
                0.15,
                0.20,
                0.25
            ]
        ),
        2
    )


    payment_mode = random.choice(
        payment_modes
    )

    shipping_mode = random.choice(
        shipping_modes
    )


    records.append(
        [
            order_id,
            order_date,
            customer_id,
            customer_name,
            region,
            state,
            city,
            category,
            sub_category,
            product,
            quantity,
            unit_price,
            discount,
            payment_mode,
            shipping_mode
        ]
    )


# ============================================================
# 5. CREATE DATAFRAME
# ============================================================

columns = [

    "Order_ID",
    "Order_Date",
    "Customer_ID",
    "Customer_Name",
    "Region",
    "State",
    "City",
    "Category",
    "Sub_Category",
    "Product",
    "Quantity",
    "Unit_Price",
    "Discount",
    "Payment_Mode",
    "Shipping_Mode"

]


df = pd.DataFrame(
    records,
    columns=columns
)


# ============================================================
# 6. CALCULATE BUSINESS METRICS
# ============================================================

df["Gross_Sales"] = (
    df["Quantity"]
    * df["Unit_Price"]
)


df["Discount_Amount"] = (
    df["Gross_Sales"]
    * df["Discount"]
)


df["Revenue"] = (
    df["Gross_Sales"]
    - df["Discount_Amount"]
)


# Assume 70% of revenue is product cost
df["Cost"] = (
    df["Revenue"]
    * 0.70
)


df["Profit"] = (
    df["Revenue"]
    - df["Cost"]
)


df["Profit_Margin"] = (
    df["Profit"]
    / df["Revenue"]
)


# ============================================================
# 7. CREATE DATA QUALITY ISSUES
# ============================================================

# Missing City values
missing_city_indexes = np.random.choice(
    df.index,
    size=100,
    replace=False
)

df.loc[
    missing_city_indexes,
    "City"
] = np.nan


# Missing Payment Mode values
missing_payment_indexes = np.random.choice(
    df.index,
    size=50,
    replace=False
)

df.loc[
    missing_payment_indexes,
    "Payment_Mode"
] = np.nan


# Duplicate records
duplicates = df.sample(
    50,
    random_state=42
)

df = pd.concat(
    [
        df,
        duplicates
    ],
    ignore_index=True
)


# ============================================================
# 8. SAVE DATASET
# ============================================================

OUTPUT_FILE.parent.mkdir(
    parents=True,
    exist_ok=True
)


df.to_csv(
    OUTPUT_FILE,
    index=False
)


# ============================================================
# 9. SUMMARY
# ============================================================

print("=" * 60)

print(
    "E-COMMERCE DATASET CREATED SUCCESSFULLY"
)

print("=" * 60)

print(
    f"Rows      : {len(df)}"
)

print(
    f"Columns   : {len(df.columns)}"
)

print(
    f"File      : {OUTPUT_FILE}"
)

print(
    f"Revenue   : ₹{df['Revenue'].sum():,.2f}"
)

print(
    f"Profit    : ₹{df['Profit'].sum():,.2f}"
)

print("=" * 60)