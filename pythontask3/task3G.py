# Define the list of reserved seats
reserved_seats = [4, 5, 12]

# Loop through seats 1 to 20
for seat in range(1, 21):
    if seat in reserved_seats:
        continue
    
    # Print only for available seats
    print(f"Seat {seat} is available")
