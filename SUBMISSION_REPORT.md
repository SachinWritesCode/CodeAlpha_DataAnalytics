# CodeAlpha Data Analytics Internship Submission
## Task 2: Exploratory Data Analysis (EDA)
## Task 3: Data Visualization

### Objective
Explore a small retail sales dataset, check data quality, identify patterns, and communicate findings through charts.

### Tools
Python, Pandas, Matplotlib.

### Data quality
The dataset contains transaction date, region, product, category, quantity, unit price, and sales value. The `Region` field has two missing entries. Those records are included in overall sales totals but excluded from region comparisons where the region is unknown.

### Questions explored
1. What is the total recorded sales value?
2. Which product category contributes the most sales?
3. How do sales change month by month?
4. Which products have the highest quantities sold?
5. Are there missing values that could affect conclusions?

### Charts produced
- `monthly_sales.png`: monthly sales trend.
- `category_sales.png`: sales totals by category.
- `product_quantity.png`: quantity sold by product.
- `sales_distribution.png`: distribution of transaction values.

### How to reproduce
Run `python analysis.py`; outputs and summary statistics are generated from the included CSV.

### Limitation
This is an illustrative sample dataset created for practice, not a real business dataset. Findings demonstrate the analysis process and should not be generalized to actual retail businesses.
