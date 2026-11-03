# Financial-dashboard
📊 Financial Dashboard | Python • SQL • Power BI  A data analytics project for analyzing financial performance, including revenue, expenses, profit, budget variance, KPIs, and business insights using Python, MySQL, and Power BI.
# 📊 Financial Dashboard

## 📌 Project Overview

The **Financial Dashboard** is a data analytics project developed to analyze financial performance using **Python, MySQL, and Power BI**.

The project processes financial data such as **revenue, expenses, budget, and profit** and converts the raw data into meaningful visualizations and business insights through an interactive Power BI dashboard.

---

## 🎯 Project Objective

The main objective of this project is to:

- Analyze monthly revenue and expenses.
- Calculate monthly and total profit.
- Compare actual expenses with the planned budget.
- Calculate budget variance.
- Track important financial KPIs.
- Identify financial trends and business insights.
- Create an interactive financial dashboard using Power BI.

---

## 🛠️ Technologies Used

- **Python** – Data loading, cleaning, and analysis
- **Pandas** – Data processing
- **MySQL** – SQL-based data analysis
- **Power BI** – Dashboard and data visualization
- **CSV** – Dataset and processed output
- **GitHub** – Project version control and sharing

---

## 📂 Project Structure

```text
Financial-Dashboard/
│
├── finance.csv
├── main.py
├── analysis.sql
├── requirements.txt
├── README.md
│
└── output/
    └── analysis_results.csv
```

---

## 🔄 Project Workflow

```text
Financial Data
      ↓
finance.csv
      ↓
Data Loading
      ↓
Data Cleaning
      ↓
Data Analysis
      ↓
Profit Calculation
      ↓
Budget Variance Calculation
      ↓
analysis_results.csv
      ↓
SQL Analysis
      ↓
Power BI Import
      ↓
Dashboard Creation
      ↓
KPI Analysis
      ↓
Business Insights
```

---

## 📊 Dataset

The dataset contains monthly financial information:

| Column | Description |
|---|---|
| `month` | Financial month |
| `revenue` | Monthly revenue |
| `expenses` | Monthly expenses |
| `budget` | Planned monthly budget |

---

## 🧮 Key Calculations

### Profit

```text
Profit = Revenue - Expenses
```

### Budget Variance

```text
Budget Variance = Expenses - Budget
```

- Negative value → Expenses are below budget.
- Positive value → Expenses are above budget.
- Zero → Expenses equal the budget.

---

## 🐍 Python Analysis

Python is used to:

1. Load the CSV dataset.
2. Check for missing values.
3. Calculate profit.
4. Calculate budget variance.
5. Generate the processed `analysis_results.csv` file.

Run the Python program using:

```bash
python main.py
```

---

## 🗄️ SQL Analysis

MySQL is used to analyze the financial dataset.

Example query:

```sql
SELECT
    month,
    revenue,
    expenses,
    revenue - expenses AS profit,
    expenses - budget AS budget_variance
FROM finance
ORDER BY month;
```

SQL analysis is used to calculate total revenue, expenses, profit, highest-profit month, and budget performance.

---

## 📈 Power BI Dashboard

The Power BI dashboard contains:

### KPI Cards

- **Total Revenue:** ₹877,000
- **Total Expenses:** ₹588,000
- **Total Profit:** ₹289,000

### Charts

- Revenue vs Expenses
- Budget vs Expenses
- Monthly Profit Analysis
- Budget Variance by Month
- Month Slicer

---

## 💡 Business Insights

- Total revenue is **₹877,000**.
- Total expenses are **₹588,000**.
- Total profit is **₹289,000**.
- **June** has the highest monthly profit of **₹57,000**.
- **April** has the lowest monthly profit of **₹41,000**.
- Expenses were above budget in **April and May by ₹2,000** each.
- Overall, the business is profitable and shows a positive financial trend.

---

## ✅ Advantages

- Easy financial performance monitoring.
- Saves time through automated calculations.
- Interactive data visualization.
- Helps monitor budget performance.
- Makes business insights easier to understand.
- Supports better business decision-making.
- Reduces manual data analysis.

---

## 🚀 Future Scope

- Real-time financial data integration.
- AI-based revenue and profit prediction.
- Expense forecasting.
- Automated budget alerts.
- Mobile dashboard.
- Multi-year financial analysis.
- Department-wise financial analysis.
- Automated financial reports.

---

## 📌 Conclusion

The **Financial Dashboard** successfully combines Python, MySQL, and Power BI to transform raw financial data into meaningful information.

The dashboard helps users monitor **revenue, expenses, profit, and budget performance**, identify trends, and understand important business insights for better decision-making.

---

## 👨‍💻 Project Type

**Data Analytics / Business Intelligence Mini Project**

**Technologies:** Python | Pandas | MySQL | Power BI | GitHub
