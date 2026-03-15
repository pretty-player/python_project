from collections import Counter

# Sample Input
sales = [
    "Laptop", "Mobile", "Laptop", "Headphones", "Mobile",
    "Laptop", "Tablet", "Mobile", "Laptop", "Headphones",
    "Laptop", "Tablet", "Laptop"
]

# 1. Initialize the Counter
sales_count = Counter(sales)

# 2. Which product sold the most?
# most_common(1) returns a list like [('Product', Count)]
top_product, top_count = sales_count.most_common(1)[0]

# 3. How many times each product was sold?
# We can simply iterate through the Counter items
print("--- Daily Sales Report ---")
for product, count in sales_count.items():
    print(f"{product:12}: {count} units sold")

# 4. Which products are low-performing?
# We can define "low performing" as anything sold fewer than 3 times
low_performing = [product for product, count in sales_count.items() if count < 3]

print("-" * 25)
print(f"Top Seller: {top_product} ({top_count} sales)")
print(f"Low Performing: {', '.join(low_performing)}")