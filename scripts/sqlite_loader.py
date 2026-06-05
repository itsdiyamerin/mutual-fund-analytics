import pandas as pd
import sqlite3

conn = sqlite3.connect("mutual_fund.db")

pd.read_csv(
    "data/processed/cleaned_nav_history.csv"
).to_sql(
    "fact_nav",
    conn,
    if_exists="replace",
    index=False
)

pd.read_csv(
    "data/processed/cleaned_investor_transactions.csv"
).to_sql(
    "fact_transactions",
    conn,
    if_exists="replace",
    index=False
)

pd.read_csv(
    "data/processed/cleaned_scheme_performance.csv"
).to_sql(
    "fact_performance",
    conn,
    if_exists="replace",
    index=False
)

print("SQLite database loaded successfully")

conn.close()