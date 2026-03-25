import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "month": ["Jan", "Feb", "Mar", "Apr", "May"],
    "revenue": [200, 250, 300, 280, 350],
    "marketing": [50, 60, 70, 65, 80],
    "profit": [100, 120, 150, 140, 180]
}

df = pd.DataFrame(data)

# Line plot
plt.plot(df["month"], df["revenue"])
plt.title("Revenue Trend")
plt.show()

# Scatter plot
plt.scatter(df["marketing"], df["profit"])
plt.xlabel("Marketing Spend")
plt.ylabel("Profit")
plt.show()

# Correlation heatmap
sns.heatmap(df.corr(numeric_only=True), annot=True)
plt.show()