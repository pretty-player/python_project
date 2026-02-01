age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote!")
else:
    years_to_wait = 18 - age
    print(f"You are not eligible yet. Please wait {years_to_wait} more year(s).")
