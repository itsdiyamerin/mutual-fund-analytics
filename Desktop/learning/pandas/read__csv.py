import pandas as pd
df=pd.read_csv("students.csv")
print("First 2 rows:")
print(df.head())

print("\nStatistics:")
print(df.describe())