import pandas as pd

# Load CSV
df = pd.read_csv("students.csv")

# Handle missing values
df.fillna(df.mean(numeric_only=True), inplace=True)

# Add total and average
df["Total"] = df["maths"] + df["science"] + df["english"]
df["Average"] = df["Total"] / 3

# Top 3 students
top3 = df.sort_values(by="Total", ascending=False).head(3)
print("Top 3 Students:\n", top3)

# Department-wise average
dept_avg = df.groupby("department")["Average"].mean()
print("Department Average:\n", dept_avg)

# Students scoring above 75 in all subjects
high_scorers = df[
    (df["maths"] > 75) &
    (df["science"] > 75) &
    (df["english"] > 75)
]
print("High Scorers:\n", high_scorers)