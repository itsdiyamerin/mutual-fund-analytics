-- Top 5 funds by 1 year return

SELECT
scheme_name,
return_1yr_pct
FROM fact_performance
ORDER BY return_1yr_pct DESC
LIMIT 5;

-- Average NAV

SELECT AVG(nav)
FROM fact_nav;

-- Total SIP amount

SELECT SUM(amount_inr)
FROM fact_transactions
WHERE transaction_type='SIP';

-- Transaction count by type

SELECT
transaction_type,
COUNT(*)
FROM fact_transactions
GROUP BY transaction_type;

-- Top categories

SELECT
category,
COUNT(*)
FROM fact_performance
GROUP BY category;