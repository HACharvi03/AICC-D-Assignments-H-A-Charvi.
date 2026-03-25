import pandas as pd

data = {
    "Area": [600, 800, 1000, 1200, 1500],
    "Price": [3000000, 4000000, 5000000, 6000000, 7500000]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)

X = df[["Area"]]   
y = df["Price"]    

from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X, y)

print("Model trained successfully!")


new_area = [[1100]]

predicted_price = model.predict(new_area)

print("Predicted Price for 1100 sq.ft:", predicted_price[0])