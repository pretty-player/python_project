from collections import namedtuple

# 1. Define the NamedTuple structure
Flight = namedtuple('Flight', ['flight_id', 'airline', 'route', 'duration', 'fare'])

# 2. Create the dataset
flights = [
    Flight(101, "SkyHigh", ("NYC", "LON"), 420, 550.0),
    Flight(102, "BlueJet", ("SFO", "TYO"), 600, 850.0),
    Flight(103, "SkyHigh", ("LON", "PAR"), 60, 120.0),
    Flight(104, "BlueJet", ("TYO", "SIN"), 400, 300.0),
    Flight(105, "StarWay", ("DXB", "LAX"), 960, 1200.0)
]

# --- Task 1: Print Flight Details in a Readable Format ---
print("--- All Flight Details ---")
for f in flights:
    # Accessing by descriptive names
    source, dest = f.route
    print(f"ID: {f.flight_id} | {f.airline:8} | {source} -> {dest} | {f.duration}m | ${f.fare}")

# --- Task 2: Sort Flights by Duration ---
print("\n--- Flights Sorted by Duration (Shortest to Longest) ---")
# Using a lambda to access the .duration attribute
sorted_flights = sorted(flights, key=lambda x: x.duration)

for f in sorted_flights:
    print(f"{f.duration} mins: Flight {f.flight_id} ({f.airline})")

# --- Task 3: Find the Longest Route per Airline ---
print("\n--- Longest Route per Airline ---")
longest_per_airline = {}

for f in flights:
    # If airline isn't in dict, or current flight is longer than the one stored
    if f.airline not in longest_per_airline or f.duration > longest_per_airline[f.airline].duration:
        longest_per_airline[f.airline] = f

for airline, f in longest_per_airline.items():
    source, dest = f.route
    print(f"{airline}: {source} to {dest} ({f.duration} minutes)")