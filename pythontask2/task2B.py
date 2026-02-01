# Integer observations
print(bool(0))     # Output: False
print(bool(100))   # Output: True

# String observations
print(bool(""))    # Output: False
print(bool("Hi"))  # Output: True

# List observations
print(bool([]))    # Output: False
print(bool([0]))   # Output: True (Note: Even a list containing 0 is True because it isn't empty!)

# NoneType observation
print(bool(None))  # Output: False