-- Sales Performance Dashboard | SQL starter queries
-- Works in PostgreSQL. Import data/sales_data.csv into a table named sales_data.
-- Suggested column types: OrderID TEXT, OrderDate DATE, Region TEXT, Category TEXT,
-- Product TEXT, Quantity INTEGER, UnitPrice NUMERIC(12,2), DiscountPct NUMERIC(5,2),
-- Revenue NUMERIC(12,2), Cost NUMERIC(12,2), Profit NUMERIC(12,2), Channel TEXT.

-- 1. Overall KPI summary
SELECT
    COUNT(DISTINCT OrderID) AS total_orders,
    SUM(Quantity) AS units_sold,
    ROUND(SUM(Revenue), 2) AS total_revenue,
    ROUND(SUM(Profit), 2) AS total_profit,
    ROUND(100.0 * SUM(Profit) / NULLIF(SUM(Revenue), 0), 2) AS profit_margin_pct,
    ROUND(AVG(Revenue), 2) AS average_order_value
FROM sales_data;

-- 2. Monthly revenue and profit trend
SELECT
    DATE_TRUNC('month', OrderDate)::date AS sales_month,
    ROUND(SUM(Revenue), 2) AS revenue,
    ROUND(SUM(Profit), 2) AS profit
FROM sales_data
GROUP BY 1
ORDER BY 1;

-- 3. Performance by region
SELECT
    Region,
    ROUND(SUM(Revenue), 2) AS revenue,
    ROUND(SUM(Profit), 2) AS profit,
    COUNT(DISTINCT OrderID) AS orders
FROM sales_data
GROUP BY Region
ORDER BY revenue DESC;

-- 4. Category and product performance
SELECT
    Category, Product,
    SUM(Quantity) AS units_sold,
    ROUND(SUM(Revenue), 2) AS revenue,
    ROUND(SUM(Profit), 2) AS profit
FROM sales_data
GROUP BY Category, Product
ORDER BY revenue DESC;

-- 5. Channel performance
SELECT
    Channel,
    COUNT(DISTINCT OrderID) AS orders,
    ROUND(SUM(Revenue), 2) AS revenue,
    ROUND(SUM(Profit), 2) AS profit
FROM sales_data
GROUP BY Channel
ORDER BY revenue DESC;

-- 6. Data quality checks
SELECT COUNT(*) AS row_count FROM sales_data;
SELECT OrderID, COUNT(*) FROM sales_data GROUP BY OrderID HAVING COUNT(*) > 1;
SELECT * FROM sales_data
WHERE OrderDate IS NULL OR Revenue IS NULL OR Profit IS NULL OR Quantity <= 0;
