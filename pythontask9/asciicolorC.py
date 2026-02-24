import inspect

def style_code(color_code):
    """Decorator that takes a color code and prints the function's source code."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            # ASCII Codes: \033[1m is Bold, \033[0m resets formatting
            BOLD = "\033[1m"
            COLOR = f"\033[{color_code}m"
            RESET = "\033[0m"

            # Get the source code of the function being called
            source = inspect.getsource(func)
            
            print(f"--- 📜 Displaying Source Code for: {func.__name__} ---")
            print(f"{BOLD}{COLOR}{source}{RESET}")
            
            # Execute the actual function
            return func(*args, **kwargs)
        return wrapper
    return decorator

# --- Applying the Decorator ---

# Color Code 31 = Red, 32 = Green, 34 = Blue, 33 = Yellow
@style_code(32) 
def calculate_area(radius):
    import math
    return math.pi * (radius ** 2)

@style_code(34)
def greet_user(name):
    return f"Hello, {name}!"

# Running the functions
area = calculate_area(5)
print(f"Result: {area:.2f}\n")

greeting = greet_user("Silambarasan")
print(f"Result: {greeting}")