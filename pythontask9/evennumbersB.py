def even_number_generator(numbers):
    """
    A generator function that yields only even 
    numbers from the provided list.
    """
    for num in numbers:
        if num % 2 == 0:
            yield num

# --- Testing the Generator ---

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# Initialize the generator object
evens = even_number_generator(my_list)

print("--- 🔢 Filtering Even Numbers ---")

# We can iterate through it just like a list
for even_num in evens:
    print(f"Found Even Number: {even_num}")

# Note: After the loop above, 'evens' is exhausted. 
# If you try to loop again, it will be empty!