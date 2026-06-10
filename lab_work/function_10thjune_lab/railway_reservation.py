A railway coach has seats represented as follows: seats = [     "Booked", "Available", "Booked", "Booked",     "Available", "Available", "Booked", "Available",     "Booked", "Booked", "Available", "Booked" ] Requirements Create the following functions: 1. count_seats(seats) Returns the number of booked and available seats. 2. first_available(seats) Returns the seat number of the first available seat. 3. occupancy_percentage(seats) Returns the percentage of occupied seats. 4. display_available_seats(seats) Displays all available seat numbers. 

#program for railway reservatio seat analyzer
  # List of seats
seats = [
    "Booked", "Available", "Booked", "Booked",
    "Available", "Available", "Booked", "Available",
    "Booked", "Booked", "Available", "Booked"
]

# Function to count booked and available seats
def count_seats(seats):

    booked = seats.count("Booked")
    available = seats.count("Available")

    print("Booked Seats =", booked)
    print("Available Seats =", available)


# Function to find first available seat
def first_available(seats):

    for i in range(len(seats)):

        if seats[i] == "Available":
            print("First Available Seat =", i + 1)
            break


# Function to calculate occupancy percentage
def occupancy_percentage(seats):

    booked = seats.count("Booked")

    percentage = (booked / len(seats)) * 100

    print("Occupancy Percentage =", percentage)


# Function to display available seat numbers
def display_available_seats(seats):

    print("Available Seat Numbers:")

    for i in range(len(seats)):

        if seats[i] == "Available":
            print(i + 1)


# Function Calls
count_seats(seats)
first_available(seats)
occupancy_percentage(seats)
display_available_seats(seats)