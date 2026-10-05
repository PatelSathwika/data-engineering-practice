

# Python Sales Data Cleaning and ETL Pipeline

## Project Overview

This project demonstrates a simple Data Engineering ETL pipeline using Python and Pandas.

The pipeline reads raw sales data from a CSV file, performs data quality checks and transformations, calculates revenue, and generates a processed CSV file.

## Technologies Used

* Python
* Pandas
* CSV
* VS Code
* Git & GitHub

## ETL Process

### 1. Extract

Read raw sales data from `sales.csv`.

### 2. Transform

The pipeline:

* Checks for missing values
* Removes duplicate records
* Handles missing quantity values
* Calculates revenue
* Performs basic data cleaning

Revenue is calculated as:

`Revenue = Quantity × Price`

### 3. Load

The cleaned data is saved as:

`processed_sales.csv`

## Input Data

The input file contains:

* Order ID
* Customer
* Product
* Quantity
* Price
* City

## Data Quality Handling

The sample dataset contains:

* Duplicate order records
* One missing quantity value

The duplicate record is removed and the missing quantity is replaced with `0`.

## Project Structure

```text
01-python-sales-project/
│
├── data/
│   ├── sales.csv
│   └── processed_sales.csv
│
├── src/
│   └── sales.py
│
└── README.md
```

## How to Run

Open the terminal inside the `src` folder and run:

```bash
python sales.py
```

## Output

The pipeline successfully generated:

* Cleaned sales data
* Revenue column
* `processed_sales.csv`
* Total revenue: `240100`

## Key Data Engineering Concepts

This project demonstrates:

* ETL
* Data cleaning
* Missing-value handling
* Duplicate removal
* Data transformation
* Derived columns
* CSV processing
* Python/Pandas
* Basic data quality checks
