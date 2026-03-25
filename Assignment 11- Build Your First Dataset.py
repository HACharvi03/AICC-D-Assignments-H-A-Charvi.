import pandas as pd

data = {
    "Study_Hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "Marks": [35, 40, 50, 55, 65, 70, 80, 90]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)

X = df[["Study_Hours"]]   
y = df["Marks"]          

from sklearn.linear_model import LinearRegression

model = LinearRegression()

model.fit(X, y)

predicted_marks = model.predict([[9]])

print("\nPredicted Marks for 9 Study Hours:", predicted_marks[0])