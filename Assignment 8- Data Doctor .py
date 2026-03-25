import pandas as pd

df = pd.read_csv("data.csv")

print("Original Dataset Shape:", df.shape)

print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())

numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

categorical_cols = df.select_dtypes(include=['object']).columns
for col in categorical_cols:
    df[col].fillna(df[col].mode()[0], inplace=True)

df.drop_duplicates(inplace=True)

for col in categorical_cols:
    df[col] = df[col].str.strip()  
    df[col] = df[col].str.lower()   

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

print("\nCleaned Dataset Shape:", df.shape)

print("\nFirst 5 Rows After Cleaning:")
print(df.head())