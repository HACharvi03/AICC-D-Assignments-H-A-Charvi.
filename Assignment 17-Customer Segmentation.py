import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
# Sample Mall Dataset
data = {
    "Annual_Income": [15, 18, 20, 25, 30, 40, 60, 65, 70, 75, 85, 90, 100, 110],
    "Spending_Score": [39, 45, 50, 60, 65, 70, 40, 45, 55, 60, 80, 85, 90, 95]
}

df = pd.DataFrame(data)

print(df.head())
X = df[["Annual_Income", "Spending_Score"]]
kmeans = KMeans(n_clusters=3, random_state=0)
df["Cluster"] = kmeans.fit_predict(X)

print(df)
plt.scatter(df["Annual_Income"], df["Spending_Score"], c=df["Cluster"])
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.title("Customer Segmentation")
plt.show()