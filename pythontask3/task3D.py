stored_password = "pass123"
max_attempts = 3

for attempt in range(1, max_attempts + 1):
    entered_password = input(f"Attempt {attempt}/{max_attempts} - Enter password: ")
    
    if entered_password == stored_password:
        print("Access Granted")
        break  # Stops the loop immediately
else:
    # This runs only if the loop finishes 3 times WITHOUT a break
    print("Account Locked")
