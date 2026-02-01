num = int(input("Enter the number for the multiplication table: "))

limit = int(input("Enter the limit (e.g., 10 or 20): "))

print(f"\nMultiplication Table for {num}:")
print("-" * 20)
for i in range(1, limit + 1):
    result = num * i
    print(f"{num} x {i:2} = {result}")
