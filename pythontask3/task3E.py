# 1. Define the list of products
products = ["laptop", "out_of_stock", "mouse", "keyboard", "out_of_stock"]

# 2. Iterate and filter
print("Available products:")
for item in products:
    if item == "out_of_stock":
        continue  # Skips the current iteration and moves to the next item
    
    print(item)
