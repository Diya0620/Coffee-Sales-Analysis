
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load cleaned dataset
df = pd.read_csv("data/cleaned_coffee_sales.csv")

# Create folder for graphs
os.makedirs("outputs", exist_ok=True)

# Set graph style
sns.set_style("whitegrid")

# 1. Store-wise Revenue Analysis
store_sales = df.groupby("store_location")["revenue"].sum().sort_values(ascending=False)

print("\nRevenue by Store:")
print(store_sales)

plt.figure(figsize=(9, 5))
sns.barplot(x=store_sales.index, y=store_sales.values)
plt.title("Revenue by Store Location")
plt.xlabel("Store Location")
plt.ylabel("Total Revenue ($)")
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig("outputs/store_revenue.png")
plt.show()


# 2. Product Category Analysis
category_sales = df.groupby("product_category")["revenue"].sum().sort_values(ascending=False)

print("\nRevenue by Product Category:")
print(category_sales)

plt.figure(figsize=(10, 5))
sns.barplot(x=category_sales.values, y=category_sales.index)
plt.title("Revenue by Product Category")
plt.xlabel("Total Revenue ($)")
plt.ylabel("Product Category")
plt.tight_layout()
plt.savefig("outputs/category_revenue.png")
plt.show()


# 3. Hourly Sales Analysis
hourly_sales = df.groupby("transaction_hour")["revenue"].sum().sort_index()

print("\nRevenue by Hour:")
print(hourly_sales)

plt.figure(figsize=(10, 5))
sns.lineplot(x=hourly_sales.index, y=hourly_sales.values, marker="o")
plt.title("Hourly Sales Trend")
plt.xlabel("Transaction Hour")
plt.ylabel("Total Revenue ($)")
plt.xticks(range(6, 21))
plt.tight_layout()
plt.savefig("outputs/hourly_sales.png")
plt.show()


# 4. Top 10 Best-Selling Products
top_products = df.groupby("product_detail")["transaction_qty"].sum().sort_values(ascending=False).head(10)

print("\nTop 10 Best-Selling Products:")
print(top_products)

plt.figure(figsize=(10, 6))
sns.barplot(x=top_products.values, y=top_products.index)
plt.title("Top 10 Best-Selling Products")
plt.xlabel("Quantity Sold")
plt.ylabel("Product")
plt.tight_layout()
plt.savefig("outputs/top_products.png")
plt.show()


print("\nEDA completed successfully!")
print("All graphs saved in the outputs folder.")
