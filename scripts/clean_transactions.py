import pandas as pd

df = pd.read_csv("data/raw/08_investor_transactions.csv")

# Date conversion
df["transaction_date"] = pd.to_datetime(df["transaction_date"])

# Standardize transaction type
df["transaction_type"] = (
    df["transaction_type"]
    .str.strip()
    .str.title()
)

# Keep valid values
valid = ["Sip", "Lumpsum", "Redemption"]

df = df[df["transaction_type"].isin(valid)]

# Amount validation
df = df[df["amount_inr"] > 0]

# KYC validation
valid_kyc = ["Verified", "Pending"]

df = df[df["kyc_status"].isin(valid_kyc)]

# Save
df.to_csv(
    "data/processed/08_investor_transactions_clean.csv",
    index=False
)

print(df.shape)
print("Transactions Cleaned Successfully")