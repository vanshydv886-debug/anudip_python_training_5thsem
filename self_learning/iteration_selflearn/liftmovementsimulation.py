# Lift starts at floor 0
current_floor = 0

# Track total movement
total_travel = 0

while True:

    # Display current floor
    print("Current Floor:", current_floor)

    # Input destination floor
    destination = int(input("Enter Destination Floor (-1 to stop): "))

    # Stop condition
    if destination == -1:
        break

    # Calculate floors travelled
    travelled = abs(destination - current_floor)

    print("Travelled:", travelled, "floors")

    # Add to total travel
    total_travel += travelled

    # Update current floor
    current_floor = destination

# Display total floors travelled
print("Total Travelled:", total_travel, "floors")