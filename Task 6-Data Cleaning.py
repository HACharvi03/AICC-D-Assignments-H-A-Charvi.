import pandas as pd
from sklearn.preprocessing import MinMaxScaler

data = {
    "age": [25, None, 30, 22, 25],
    "salary": [50000, 60000, None, 45000, 50000],
    "city": ["Hyderabad", "hyderabad", "Bangalore", "Bangalore", "HYDERABAD"],
    "experience": [2, 3, 5, 2, 2]
}

df = pd.DataFrame(data)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Handle missing values
df["age"].fillna(df["age"].mean(), inplace=True)
df["salary"].fillna(df["salary"].mean(), inplace=True)

# Standardize city names
df["city"] = df["city"].str.lower()

# Min-Max Scaling
scaler = MinMaxScaler()
df[["age", "salary"]] = scaler.fit_transform(df[["age", "salary"]])

print("Cleaned Data:\n", df)