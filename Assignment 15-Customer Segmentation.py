import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

data = {
    "Annual_Income": [15, 16, 17, 18, 19, 60, 62, 63, 65, 68, 100, 102, 105, 108],
    "Spending_Score": [39, 40, 42, 45, 48, 50, 52, 55, 58, 60, 80, 85, 88, 90]
}

df = pd.DataFrame(data)

print(df.head())
X = df[["Annual_Income", "Spending_Score"]]
kmeans = KMeans(n_clusters=3)
df["Cluster"] = kmeans.fit_predict(X)

print(df)
plt.scatter(df["Annual_Income"], df["Spending_Score"], c=df["Cluster"])
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.title("Customer Segmentation")
plt.show()