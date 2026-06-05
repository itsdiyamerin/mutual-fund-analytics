CREATE TABLE fact_nav (
    amfi_code INTEGER,
    date DATE,
    nav REAL
);

CREATE TABLE fact_transactions (
    investor_id TEXT,
    transaction_date DATE,
    amfi_code INTEGER,
    transaction_type TEXT,
    amount_inr REAL
);

CREATE TABLE fact_performance (
    amfi_code INTEGER,
    scheme_name TEXT,
    category TEXT,
    return_1yr_pct REAL,
    return_3yr_pct REAL,
    return_5yr_pct REAL
);