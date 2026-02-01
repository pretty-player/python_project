import string

password = input("Enter your password: ")
is_strong = False

for char in password:
    # Check if character is special (punctuation)
    if char in string.punctuation:
        is_strong = True
        break

# Check result
if is_strong:
    print("Strong password")
else:
    print("Weak password")
