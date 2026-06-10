import pandas as pd

df = pd.read_csv("data/raw/02_nav_history.csv")

# Date conversion
df["date"] = pd.to_datetime(df["date"])

# Sort
df = df.sort_values(["amfi_code", "date"])

# Remove duplicates
df = df.drop_duplicates()

# Remove invalid NAV values
df = df[df["nav"] > 0]

# Forward fill NAV within each fund
df["nav"] = df.groupby("amfi_code")["nav"].ffill()

# Save
df.to_csv(
    "data/processed/02_nav_history_clean.csv",
    index=False
)

print(df.shape)
print("NAV History Cleaned Successfully")