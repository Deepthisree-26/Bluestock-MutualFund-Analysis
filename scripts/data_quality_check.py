import pandas as pd

fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

print("Fund Master Columns:")
print(fund_master.columns.tolist())

print("\nNAV History Columns:")
print(nav_history.columns.tolist())

fund_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

missing_codes = fund_codes - nav_codes

print("\nTotal Fund Master Codes:", len(fund_codes))
print("Total NAV History Codes:", len(nav_codes))

print("\nMissing Codes:")
print(missing_codes)

if len(missing_codes) == 0:
    print("\n✅ All AMFI codes are present in NAV History")
else:
    print("\n⚠ Some AMFI codes are missing")