import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

data = {
    "income": [50000, 60000, 25000, 40000, 70000],
    "loan": [20000, 25000, 15000, 20000, 30000],
    "approved": [1, 1, 0, 1, 1]
}

df = pd.DataFrame(data)

X = df[["income", "loan"]]
y = df["approved"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LogisticRegression()
model.fit(X_train, y_train)

pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, pred))

# New prediction
print("New Customer Prediction:", model.predict([[55000, 22000]]))