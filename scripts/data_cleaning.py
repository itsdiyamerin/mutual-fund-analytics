import pandas as pd
import os

os.makedirs("data/processed", exist_ok=True)

# =========================
# NAV HISTORY CLEANING
# =========================

nav = pd.read_csv("data/raw/02_nav_history.csv")

nav["date"] = pd.to_datetime(nav["date"])

nav = nav.sort_values(
    ["amfi_code", "date"]
)

nav = nav.drop_duplicates()

nav = nav[nav["nav"] > 0]

nav.to_csv(
    "data/processed/cleaned_nav_history.csv",
    index=False
)

print("NAV History cleaned")

# =========================
# INVESTOR TRANSACTIONS
# =========================

txn = pd.read_csv(
    "data/raw/08_investor_transactions.csv"
)

txn["transaction_date"] = pd.to_datetime(
    txn["transaction_date"]
)

valid_types = [
    "SIP",
    "Lumpsum",
    "Redemption"
]

txn = txn[
    txn["transaction_type"].isin(valid_types)
]

txn = txn[
    txn["amount_inr"] > 0
]

txn.to_csv(
    "data/processed/cleaned_investor_transactions.csv",
    index=False
)

print("Investor transactions cleaned")

# =========================
# SCHEME PERFORMANCE
# =========================

perf = pd.read_csv(
    "data/raw/07_scheme_performance.csv"
)

numeric_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "alpha",
    "beta",
    "sharpe_ratio",
    "sortino_ratio"
]

for col in numeric_cols:
    perf[col] = pd.to_numeric(
        perf[col],
        errors="coerce"
    )

perf = perf.dropna()

perf.to_csv(
    "data/processed/cleaned_scheme_performance.csv",
    index=False
)

print("Scheme performance cleaned")

print("Day 2 data cleaning completed")