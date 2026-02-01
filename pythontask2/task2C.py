# 1. Create a bytes datatype variable and assign the string "Welcome"
# The 'b' prefix creates a bytes literal
data = b"Welcome"

# 2. Print the ASCII character (integer value) of every letter
print("ASCII values of each character:")
for byte in data:
    print(f"Character: {chr(byte)} -> ASCII Value: {byte}")

# 3. Try changing one of the letters
try:
    print("\nAttempting to change 'W' to 'B'...")
    data[0] = 66  # ASCII for 'B'
except TypeError as e:
    # 4. Observe the error
    print(f"Error caught: {e}")
