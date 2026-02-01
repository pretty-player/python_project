username = "admin"
password = "Password123"

# Take input from the user
entered_username = input("Enter username: ")
entered_password = input("Enter password: ")

# Validate using 'and' logical operator
if entered_username == username and entered_password == password:
    print("Login successful! Welcome back.")
else:
    print("Access denied. Invalid username or password.")
