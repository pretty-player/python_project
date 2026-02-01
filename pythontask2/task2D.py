# 1. Create a bytearray variable and assign "Hello world!"
# Note: Strings must be encoded (e.g., 'utf-8') to be stored in a bytearray
data = bytearray("Hello world!", "utf-8")
print(f"Original: {data.decode()}")

# 2. Add " All " in between (Hello All World!)
# Using slice assignment to 'insert' a byte sequence at index 5
data[5:5] = b" All"
print(f"After Insertion: {data.decode()}")

# 3. Change "All" to "Hi"
# Use the .replace() method which works on bytearray objects
# Note: .replace() returns a new bytearray, so we reassign it
data = data.replace(b"All", b"Hi")
print(f"After Replacement: {data.decode()}")
