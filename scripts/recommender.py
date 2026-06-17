import pandas as pd

performance = pd.read_csv("data/raw/07_scheme_performance.csv")

risk_appetite = input("Enter risk appetite (Low/Moderate/High): ")

recommendations = performance[
    performance["risk_grade"].str.contains(risk_appetite, case=False, na=False)
].sort_values(
    "sharpe_ratio",
    ascending=False
).head(3)

print("\nTop Recommended Funds:")
print(recommendations[
    ["scheme_name", "fund_house", "risk_grade", "sharpe_ratio"]
])