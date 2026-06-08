# Bus Seat Reservation Analysis

seats = [1, 0, 1, 1, 0, 0, 1, 1, 1, 0]

booked = 0
available = 0

# Count booked and available seats
for i in seats:
    if i == 1:
        booked += 1
    else:
        available += 1

# Find first available seat
first_available = -1

for i in range(len(seats)):
    if seats[i] == 0:
        first_available = i + 1
        break

# Create list of available seat numbers
available_seats = []

for i in range(len(seats)):
    if seats[i] == 0:
        available_seats.append(i + 1)

# Calculate occupancy percentage
occupancy = (booked / len(seats)) * 100

# Display output
print("Booked Seats:", booked)
print("Available Seats:", available)
print("First Available Seat:", first_available)
print("Available Seat Numbers:", available_seats)
print("Bus Occupancy:", occupancy, "%")

if occupancy > 70:
    print("Status: More Than 70% Occupied")
else:
    print("Status: Not More Than 70% Occupied")