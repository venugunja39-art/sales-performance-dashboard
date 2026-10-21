# Sales Performance Dashboard (SQL + Excel + Power BI)

A portfolio-ready, end-to-end sales analytics project using a **synthetic retail dataset**.
It is designed to practise data quality checks, SQL analysis, Excel summaries and an
interactive Power BI dashboard. No real customer data is included.

## Project goals
- Track revenue, profit, orders, units sold and profit margin.
- Compare performance by month, region, product category and sales channel.
- Identify top products and sales trends.
- Demonstrate a reproducible workflow from raw CSV to business insights.

## Tools
- **Excel**: inspect the CSV, create PivotTables and charts.
- **PostgreSQL** (or SQLite with adjusted date syntax): query the dataset.
- **Power BI Desktop**: build interactive visuals and KPI cards.
- **Git + GitHub**: version control and publish the portfolio project.
- Optional: Python with pandas for additional data validation.

## Dataset
`data/sales_data.csv` contains 1,200 synthetic order records across 2024–2025.
Fields: OrderID, OrderDate, Region, Category, Product, Quantity, UnitPrice,
DiscountPct, Revenue, Cost, Profit, Channel.

All amounts are fictional and use generic currency units; do not describe them as actual
company sales. The data is generated for learning and demonstration.

## Quick start: see output without installing anything
1. Open `data/sales_data.csv` in Excel, or import it into Power BI Desktop.
2. In Power BI Desktop, choose **Home → Get data → Text/CSV** and select the CSV.
3. Check data types and click **Load**.
4. Add measures from `powerbi/dax_measures.txt`.
5. Build the report using the suggested layout below.

## Suggested Power BI report layout
**Top row — KPI cards**
- Total Revenue
- Total Profit
- Total Orders
- Profit Margin %

**Middle row**
- Line chart: Calendar[Date] by Total Revenue and Total Profit (use a secondary visual if scales differ)
- Bar chart: Region by Total Revenue
- Donut chart: Category by Total Revenue

**Bottom row**
- Bar chart: Product by Total Profit (sort descending; show top 10 if desired)
- Column chart: Channel by Total Revenue
- Slicers: Calendar[Year], Region, Category, Channel

Use clear titles, consistent number formats, and sensible sorting. Avoid claiming insights until you have inspected the report output.


## Optional: run a live dashboard locally (Python + Streamlit)
This preview lets you see a working interactive dashboard before building the Power BI `.pbix`.

1. Install Python 3.11+ from https://www.python.org/downloads/ and VS Code from https://code.visualstudio.com/.
2. Extract the ZIP, open the `sales-performance-dashboard` folder in VS Code, then open **Terminal → New Terminal**.
3. Create a virtual environment:
   - Windows: `py -m venv .venv`
   - Activate it in PowerShell: `.\.venv\Scripts\Activate.ps1`
4. Install packages: `python -m pip install -r requirements.txt`
5. Run: `python -m streamlit run app.py`
6. Your browser should open the local dashboard. If not, open the local URL printed in the terminal (usually `http://localhost:8501`).
7. Use the sidebar filters to change the year, region, category and channel.

If PowerShell blocks activation, you can skip activation and run:
`.\.venv\Scripts\python.exe -m pip install -r requirements.txt`
then
`.\.venv\Scripts\python.exe -m streamlit run app.py`

The Streamlit preview is an optional way to run the project. Your portfolio target remains SQL + Excel + Power BI.

## Excel steps
1. Open `data/sales_data.csv` in Excel.
2. Select the data and choose **Insert → PivotTable**.
3. Create a PivotTable with `Region` in Rows and `Revenue` in Values (Sum).
4. Add another PivotTable with `Category` in Rows and `Profit` in Values (Sum).
5. Put `OrderDate` in Rows and group by Months and Years, with `Revenue` in Values.
6. Add PivotCharts and format amounts as currency or a suitable numeric format.
7. Save your workbook as `sales_analysis.xlsx` (optional; do not commit temporary files).

## SQL steps (PostgreSQL)
1. Install PostgreSQL and open pgAdmin or use an existing PostgreSQL environment.
2. Create a database, for example `sales_analytics`.
3. Import `data/sales_data.csv` into a table named `sales_data`, matching column names and data types.
4. Run `sql/analysis_queries.sql` query by query.
5. Compare the SQL summary with Power BI totals as a basic reconciliation check.

## Data quality checks
- Confirm row count is 1,200.
- Check duplicate `OrderID` values.
- Check for null dates/revenue/profit and non-positive quantities.
- Reconcile total revenue and profit across Excel, SQL and Power BI.
- Document assumptions and any data issues you find.

## GitHub publishing
1. Create a GitHub account at https://github.com/ if needed.
2. Install Git from https://git-scm.com/downloads and sign in to GitHub in your browser.
3. Unzip/open this project folder in VS Code or your terminal.
4. Run:
   ```bash
   git init
   git add README.md data/sales_data.csv sql/analysis_queries.sql powerbi/dax_measures.txt .gitignore
   git commit -m "Create sales performance dashboard project"
   git branch -M main
   git remote add origin https://github.com/YOUR-USERNAME/sales-performance-dashboard.git
   git push -u origin main
   ```
5. Replace `YOUR-USERNAME` with your GitHub username. Create the empty repository on GitHub first.
6. After building the Power BI report, save your `.pbix` file in `powerbi/` and optionally add screenshots in `screenshots/`.
   Check your organisation's rules before publishing any non-synthetic data or proprietary PBIX files.

## Portfolio description (edit to match what you actually build)
Built a sales analytics project using SQL, Excel and Power BI to examine revenue, profit,
order volume and product/region/channel performance. Created data validation checks,
reusable SQL queries, DAX measures and an interactive report with filters.

## Suggested repository structure
```text
sales-performance-dashboard/
├── README.md
├── data/
│   └── sales_data.csv
├── sql/
│   └── analysis_queries.sql
├── powerbi/
│   └── dax_measures.txt
├── screenshots/
└── .gitignore
```

## Important
This project provides the dataset and starter queries/measures. You still need to build and
save the actual Power BI `.pbix` report yourself by following the steps above. Never claim
the dashboard is complete until you have built, checked and captured the report.
