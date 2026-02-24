# 1. List Comprehension: Creates a list of squares
# Syntax: [expression for item in iterable]
squares = [x**2 for x in range(1, 11)]

# 2. Dictionary Comprehension: Maps number to its cube
# Syntax: {key_expr: value_expr for item in iterable}
cubes_dict = {x: x**3 for x in range(1, 11)}

# 3. Set Comprehension: Extracts only even numbers
# Syntax: {expression for item in iterable if condition}
even_set = {x for x in range(1, 11) if x % 2 == 0}

# --- Displaying Results ---
print(f"List of Squares: {squares}")
print(f"Dictionary of Cubes: {cubes_dict}")
print(f"Set of Even Numbers: {even_set}")