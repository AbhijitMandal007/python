import matplotlib.pyplot as plt

months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun',
          'jul', 'aug', 'sep', 'oct', 'nov', 'dec']

sales = [45000, 52000, 48000, 61000, 58000, 65000,
         62000, 70000, 68000, 75000, 72000, 80000]

max_sales = max(sales)
min_sales = min(sales)

max_month = months[sales.index(max_sales)]
min_month = months[sales.index(min_sales)]

print("Highest Sales:", max_month, max_sales)
print("Lowest Sales:", min_month, min_sales)

# Line chart
plt.figure(figsize=(10, 5))
plt.plot(months, sales, marker='o')
plt.title("Monthly Sales - Line Chart")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)
plt.show()

# Bar chart
plt.figure(figsize=(10, 5))
plt.bar(months, sales, color='skyblue')
plt.title("Monthly Sales - Bar Chart")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
