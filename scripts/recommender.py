import pandas as pd

df = pd.read_csv(
    "../data/raw/07_scheme_performance.csv"
)

risk = input(
    "Enter Risk Level: "
)

result = (
    df[df["risk_grade"]==risk]
      .sort_values(
          "sharpe_ratio",
          ascending=False
      )
      .head(3)
)

print(result[
    [
        "scheme_name",
        "fund_house",
        "sharpe_ratio"
    ]
])