#1️ Bar Chart Code
import matplotlib.pyplot as plt

# Sample Data
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [200, 250, 300, 280, 350, 400]

# Bar Chart
plt.bar(months, sales)
plt.title("Monthly Sales - Bar Chart")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()


#2️ Pie Chart Code
import matplotlib.pyplot as plt

# Sample Data
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [200, 250, 300, 280, 350, 400]

# Pie Chart
plt.pie(sales, labels=months, autopct="%1.1f%%")
plt.title("Monthly Sales Distribution")
plt.show() 

#3️ Histogram Code
import matplotlib.pyplot as plt

# Sample Data
sales = [200, 250, 300, 280, 350, 400]

# Histogram
plt.hist(sales, bins=5)
plt.title("Sales Distribution - Histogram")
plt.xlabel("Sales Range")
plt.ylabel("Frequency")
plt.show()


1 Overall Growth Trend:
The bar chart shows a steady increase in sales from January (200) to June (400), indicating consistent business growth over time.

2 Highest Contribution:
The pie chart reveals that June contributes the largest share (22.5%) of total sales, showing peak performance at the end of the period.

3 Temporary Dip:
There is a slight drop in April (280) compared to March (300), suggesting a minor slowdown before sales picked up again.

4 Sales Distribution:
The histogram shows most sales values are clustered between 250 and 350, indicating moderate consistency in performance.

5 Strong Upward Momentum:
The sharp increase from April to June suggests improved marketing, seasonal demand, or business expansion.
