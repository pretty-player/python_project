num = int(input("Enter a number: "))

# Use the bitwise AND operator
if (num & 1) == 0:
    print(f"{num} is an Even number.")
else:
    print(f"{num} is an Odd number.")
