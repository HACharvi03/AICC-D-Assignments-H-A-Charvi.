import pandas as pd
df = pd.read_csv("data.csv")

print("===== Top 5 Rows =====")
print(df.head())

numeric_cols = df.select_dtypes(include=['int64', 'float64'])

highest_column = numeric_cols.max().idxmax()
highest_value = numeric_cols.max().max()

print("\nColumn with Highest Value:", highest_column)
print("Highest Value in Dataset:", highest_value)

print("\n===== Missing Values =====")
print(df.isnull().sum())

print("\n===== Dataset Summary =====")
print(df.describe())