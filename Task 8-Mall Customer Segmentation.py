import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

data = {
    "Age": [25, 30, 45, 35, 22, 40],
    "Income": [40000, 60000, 80000, 50000, 30000, 70000],
    "Spending": [60, 70, 40, 65, 80, 50]
}

df = pd.DataFrame(data)

kmeans = KMeans(n_clusters=3)
df["Cluster"] = kmeans.fit_predict(df)

# Plot
plt.scatter(df["Income"], df["Spending"], c=df["Cluster"])
plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], marker='X')
plt.xlabel("Income")
plt.ylabel("Spending")
plt.show()