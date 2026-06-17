# Mutual Fund Analytics

## Project Overview

Mutual Fund Analytics is a Python-based data analytics project designed to analyze Indian mutual fund schemes using AMFI and MFAPI datasets. The project performs end-to-end data processing, exploratory data analysis, performance evaluation, risk assessment, investor behavior analysis, and dashboard visualization.

The objective is to provide actionable insights into mutual fund performance, investor trends, fund risk metrics, and portfolio concentration through advanced analytics and interactive reporting.



## Project Objectives

- Analyze mutual fund performance across different categories.
- Evaluate risk metrics such as Sharpe Ratio, Sortino Ratio, VaR, and CVaR.
- Study investor transaction behavior and SIP continuity.
- Identify top-performing funds based on risk-adjusted returns.
- Analyze portfolio concentration using the Herfindahl-Hirschman Index (HHI).
- Build an interactive Power BI dashboard for decision-making.



## Data Sources

### AMFI Dataset
Provides:
- Fund master information
- Scheme details
- Fund categories
- Assets Under Management (AUM)
- SIP inflows
- Investor folio statistics

### MFAPI Dataset
Provides:
- Historical NAV data
- Daily fund performance information



## ETL Pipeline


### Extract
- Load AMFI datasets from CSV files
- Fetch NAV history using MFAPI

### Transform
- Data cleaning
- Missing value handling
- Data validation
- Feature engineering
- Risk metric calculation

### Load
- Store processed datasets
- Generate analytical reports
- Create dashboard-ready datasets



## Project Structure
mutual_fund_analytics/ │ ├── data/ │ ├── raw/ │ └── processed/ │ ├── notebooks/ │ ├── EDA_Analysis.ipynb │ ├── Performance_Analytics.ipynb │ └── Advanced_Analytics.ipynb │ ├── scripts/ │ ├── data_ingestion.py │ ├── data_cleaning.py │ ├── sqlite_loader.py │ ├── live_nav_fetch.py │ └── recommender.py │ ├── reports/ │ ├── charts/ │ ├── var_cvar_report.csv │ ├── fund_scorecard.csv │ └── alpha_beta.csv │ ├── dashboard/ │ └── Dashboard.pdf │ ├── README.md └── requirements.txt

## Exploratory Data Analysis

Performed analysis on:

- Fund categories
- Fund houses
- AUM distribution
- SIP inflows
- Investor folios
- NAV trends
- Benchmark comparison

Generated visualizations include:

- AUM trends
- NAV growth trends
- Category-wise fund distribution
- Industry inflow analysis



## Performance Analytics

Calculated:

- 1-Year Returns
- 3-Year Returns
- 5-Year Returns
- Alpha
- Beta
- Sharpe Ratio
- Sortino Ratio
- Maximum Drawdown

Generated:

- Fund Scorecard
- Alpha-Beta Report
- Risk-Return Analysis



## Advanced Analytics

### Historical VaR and CVaR

Computed:

- 95% Historical Value at Risk (VaR)
- Conditional Value at Risk (CVaR)

for all mutual fund schemes.

### Rolling Sharpe Ratio

Calculated rolling 90-day Sharpe Ratio for selected funds and visualized performance trends.

### Investor Cohort Analysis

Analyzed investor cohorts based on first transaction year.

Metrics:

- Average SIP amount
- Total invested amount
- Top fund preference

### SIP Continuity Analysis

Identified investors with irregular SIP patterns.

Criteria:

- Average gap greater than 35 days
- Flagged as At-Risk Investors

### Fund Recommendation Engine

Developed a recommendation system based on:

- Risk Appetite
  - Low
  - Moderate
  - High

Recommendation Criteria:

- Top funds by Sharpe Ratio
- Matching risk profile

### Sector Concentration Analysis

Used Herfindahl-Hirschman Index (HHI):

HHI = Σ(weight²)

to measure portfolio concentration and diversification.



## Dashboard Features

### Executive Overview

- Total AUM
- Total SIP Inflow
- Total Folios
- Total Schemes

### Performance Dashboard

- Risk vs Return Analysis
- NAV vs Benchmark Comparison
- Fund Scorecard

### Investor Dashboard

- State-wise Investments
- Age Group Analysis
- SIP/Lumpsum Breakdown
- Monthly Transaction Trends

### Category Dashboard

- Category-wise Inflows
- Industry Trends
- Category Performance

### NAV Drillthrough Dashboard

- Individual Scheme NAV Trend Analysis



## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- SQLite
- Power BI
- Git
- GitHub
- MFAPI



## Key Insights

- Risk-adjusted performance varies significantly across fund categories.
- Certain investor cohorts contribute a larger share of investments.
- A subset of investors show SIP discontinuity risk.
- Some portfolios exhibit high sector concentration.
- Sharpe Ratio effectively identifies superior risk-adjusted performers.



## Author

*Diya Merin Abraham*
Capstone Project – Mutual Fund Analytics Dashboard & Risk Analysis
