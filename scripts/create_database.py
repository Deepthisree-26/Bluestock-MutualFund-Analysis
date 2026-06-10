from sqlalchemy import create_engine
import pandas as pd

engine = create_engine(
    "sqlite:///data/db/bluestock_mf.db"
)

nav = pd.read_csv(
    "data/processed/02_nav_history_clean.csv"
)

performance = pd.read_csv(
    "data/processed/07_scheme_performance_clean.csv"
)

transactions = pd.read_csv(
    "data/processed/08_investor_transactions_clean.csv"
)

nav.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

performance.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

transactions.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

print("Database Created Successfully")