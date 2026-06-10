-- Top 5 funds by AUM
SELECT scheme_name, aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- Average NAV
SELECT amfi_code, AVG(nav)
FROM fact_nav
GROUP BY amfi_code;

-- Transactions by State
SELECT state, COUNT(*)
FROM fact_transactions
GROUP BY state;

-- Expense Ratio < 1%
SELECT scheme_name, expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- Category Count
SELECT category, COUNT(*)
FROM fact_performance
GROUP BY category;

-- Gender Split
SELECT gender, COUNT(*)
FROM fact_transactions
GROUP BY gender;

-- SIP Transactions
SELECT COUNT(*)
FROM fact_transactions
WHERE transaction_type='Sip';

-- Average Investment
SELECT AVG(amount_inr)
FROM fact_transactions;

-- Top States by Investment
SELECT state,SUM(amount_inr)
FROM fact_transactions
GROUP BY state
ORDER BY SUM(amount_inr) DESC;

-- Risk Category Distribution
SELECT risk_grade,COUNT(*)
FROM fact_performance
GROUP BY risk_grade;