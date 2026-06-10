from pathlib import Path
import pandas as pd

data_path = Path("data/raw")

print("=" * 60)
print("BLUESTOCK MUTUAL FUND DATA INGESTION")
print("=" * 60)

for file in data_path.glob("*.csv"):
    print("\n" + "=" * 60)
    print(f"FILE: {file.name}")

    try:
        df = pd.read_csv(file)

        print("Shape:", df.shape)

        print("\nColumns:")
        print(df.columns.tolist())

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

    except Exception as e:
        print(f"Error reading {file.name}: {e}")