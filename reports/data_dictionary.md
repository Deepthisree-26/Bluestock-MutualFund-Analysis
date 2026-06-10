# Bluestock Mutual Fund Capstone - Data Dictionary

## 01_fund_master.csv

| Column             | Data Type | Description                   |
| ------------------ | --------- | ----------------------------- |
| amfi_code          | Integer   | Unique AMFI scheme identifier |
| fund_house         | Text      | Mutual fund company           |
| scheme_name        | Text      | Name of scheme                |
| category           | Text      | Equity or Debt                |
| sub_category       | Text      | Fund subtype                  |
| plan               | Text      | Direct/Regular                |
| launch_date        | Date      | Scheme launch date            |
| benchmark          | Text      | Benchmark index               |
| expense_ratio_pct  | Float     | Expense ratio percentage      |
| exit_load_pct      | Float     | Exit load percentage          |
| min_sip_amount     | Float     | Minimum SIP amount            |
| min_lumpsum_amount | Float     | Minimum lumpsum investment    |
| fund_manager       | Text      | Fund manager name             |
| risk_category      | Text      | Risk level                    |
| sebi_category_code | Text      | SEBI classification code      |

## 02_nav_history.csv

| Column    | Data Type | Description       |
| --------- | --------- | ----------------- |
| amfi_code | Integer   | Scheme identifier |
| date      | Date      | NAV date          |
| nav       | Float     | Net Asset Value   |

## 07_scheme_performance.csv

| Column         | Data Type | Description             |
| -------------- | --------- | ----------------------- |
| return_1yr_pct | Float     | 1 year return           |
| return_3yr_pct | Float     | 3 year return           |
| return_5yr_pct | Float     | 5 year return           |
| sharpe_ratio   | Float     | Risk adjusted return    |
| sortino_ratio  | Float     | Downside risk metric    |
| alpha          | Float     | Excess return           |
| beta           | Float     | Market sensitivity      |
| aum_crore      | Float     | Assets under management |

## 08_investor_transactions.csv

| Column             | Data Type | Description                |
| ------------------ | --------- | -------------------------- |
| investor_id        | Text      | Unique investor identifier |
| transaction_date   | Date      | Transaction date           |
| transaction_type   | Text      | SIP / Lumpsum / Redemption |
| amount_inr         | Float     | Investment amount          |
| state              | Text      | Investor state             |
| city               | Text      | Investor city              |
| city_tier          | Text      | T30/B30 classification     |
| age_group          | Text      | Investor age segment       |
| gender             | Text      | Investor gender            |
| annual_income_lakh | Float     | Annual income              |
| payment_mode       | Text      | Payment method             |
| kyc_status         | Text      | KYC verification status    |
