def sum_all_numbers(*args):
    """Adds any number of numerical inputs together."""
    total = sum(args)
    return total

def print_student_details(**kwargs):
    """Prints student information provided as keyword arguments."""
    print("\n--- Student Profile ---")
    for key, value in kwargs.items():
        # Capitalize key for a cleaner look (e.g., 'name' becomes 'Name')
        print(f"{key.capitalize()}: {value}")

# --- Testing the Functions ---

# 1. Testing *args with different amounts of numbers
result1 = sum_all_numbers(10, 20)
result2 = sum_all_numbers(5, 15, 25, 40, 100)

print(f"Sum of 2 numbers: {result1}")
print(f"Sum of 5 numbers: {result2}")

# 2. Testing **kwargs with different student details
print_student_details(name="Alex", age=20, grade="A")
print_student_details(name="Jordan", major="Physics", graduation_year=2025, gpa=3.8)