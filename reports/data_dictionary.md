# Data Dictionary

## fact_nav

| Column | Description |
|----------|-------------|
| amfi_code | Fund identifier |
| date | NAV date |
| nav | Net Asset Value |

## fact_transactions

| Column | Description |
|----------|-------------|
| investor_id | Investor ID |
| transaction_date | Transaction date |
| amfi_code | Fund code |
| transaction_type | SIP/Lumpsum/Redemption |
| amount_inr | Transaction amount |

## fact_performance

| Column | Description |
|----------|-------------|
| amfi_code | Fund code |
| scheme_name | Scheme name |
| category | Fund category |
| return_1yr_pct | 1 year return |
| return_3yr_pct | 3 year return |
| return_5yr_pct | 5 year return |