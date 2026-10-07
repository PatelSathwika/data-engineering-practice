
-- ============================================================
-- E-COMMERCE SALES ANALYTICS
-- SQL BUSINESS ANALYSIS
-- ============================================================


-- ============================================================
-- 1. Overall Business KPIs
-- ============================================================

SELECT
    COUNT(DISTINCT Order_ID) AS total_orders,
    SUM(Quantity) AS total_units,
    SUM(Revenue) AS total_revenue,
    SUM(Profit) AS total_profit,
    ROUND(
        SUM(Profit) / NULLIF(SUM(Revenue), 0) * 100,
        2
    ) AS profit_margin_percentage
FROM cleaned_sales;


-- ============================================================
-- 2. Monthly Revenue and Profit
-- ============================================================

SELECT
    YEAR(Order_Date) AS year,
    MONTH(Order_Date) AS month,
    SUM(Revenue) AS revenue,
    SUM(Profit) AS profit,
    COUNT(DISTINCT Order_ID) AS orders
FROM cleaned_sales
GROUP BY
    YEAR(Order_Date),
    MONTH(Order_Date)
ORDER BY
    year,
    month;


-- ============================================================
-- 3. Category Performance
-- ============================================================

SELECT
    Category,
    SUM(Revenue) AS revenue,
    SUM(Profit) AS profit,
    SUM(Quantity) AS units_sold,
    COUNT(DISTINCT Order_ID) AS orders,
    ROUND(
        SUM(Profit) / NULLIF(SUM(Revenue), 0) * 100,
        2
    ) AS profit_margin_percentage
FROM cleaned_sales
GROUP BY Category
ORDER BY revenue DESC;


-- ============================================================
-- 4. Sub-Category Performance
-- ============================================================

SELECT
    Category,
    Sub_Category,
    SUM(Revenue) AS revenue,
    SUM(Profit) AS profit,
    SUM(Quantity) AS units_sold
FROM cleaned_sales
GROUP BY
    Category,
    Sub_Category
ORDER BY revenue DESC;


-- ============================================================
-- 5. Regional Performance
-- ============================================================

SELECT
    Region,
    SUM(Revenue) AS revenue,
    SUM(Profit) AS profit,
    COUNT(DISTINCT Order_ID) AS orders,
    ROUND(
        SUM(Profit) / NULLIF(SUM(Revenue), 0) * 100,
        2
    ) AS profit_margin_percentage
FROM cleaned_sales
GROUP BY Region
ORDER BY revenue DESC;


-- ============================================================
-- 6. State-Level Performance
-- ============================================================

SELECT
    State,
    SUM(Revenue) AS revenue,
    SUM(Profit) AS profit,
    COUNT(DISTINCT Order_ID) AS orders
FROM cleaned_sales
GROUP BY State
ORDER BY revenue DESC;


-- ============================================================
-- 7. Top 10 Products by Revenue
-- ============================================================

SELECT
    Product,
    SUM(Revenue) AS revenue,
    SUM(Profit) AS profit,
    SUM(Quantity) AS units_sold
FROM cleaned_sales
GROUP BY Product
ORDER BY revenue DESC
LIMIT 10;


-- ============================================================
-- 8. Top 10 Customers by Revenue
-- ============================================================

SELECT
    Customer_ID,
    Customer_Name,
    COUNT(DISTINCT Order_ID) AS orders,
    SUM(Revenue) AS revenue,
    SUM(Profit) AS profit
FROM cleaned_sales
GROUP BY
    Customer_ID,
    Customer_Name
ORDER BY revenue DESC
LIMIT 10;


-- ============================================================
-- 9. Payment Method Analysis
-- ============================================================

SELECT
    Payment_Mode,
    COUNT(DISTINCT Order_ID) AS orders,
    SUM(Revenue) AS revenue,
    SUM(Profit) AS profit
FROM cleaned_sales
GROUP BY Payment_Mode
ORDER BY revenue DESC;


-- ============================================================
-- 10. Shipping Mode Analysis
-- ============================================================

SELECT
    Shipping_Mode,
    COUNT(DISTINCT Order_ID) AS orders,
    SUM(Revenue) AS revenue,
    SUM(Profit) AS profit
FROM cleaned_sales
GROUP BY Shipping_Mode
ORDER BY revenue DESC;


-- ============================================================
-- 11. High-Value Customers
-- ============================================================

SELECT
    Customer_ID,
    Customer_Name,
    SUM(Revenue) AS customer_revenue
FROM cleaned_sales
GROUP BY
    Customer_ID,
    Customer_Name
HAVING SUM(Revenue) > 50000
ORDER BY customer_revenue DESC;


-- ============================================================
-- 12. Low-Profit Products
-- ============================================================

SELECT
    Product,
    SUM(Revenue) AS revenue,
    SUM(Profit) AS profit,
    ROUND(
        SUM(Profit) / NULLIF(SUM(Revenue), 0) * 100,
        2
    ) AS profit_margin_percentage
FROM cleaned_sales
GROUP BY Product
HAVING SUM(Revenue) > 10000
ORDER BY profit_margin_percentage ASC;