# PIN Verification System
# This program allows user to enter PIN until correct PIN is entered

# Correct PIN set by system
pin = 1234

# Initial value (wrong PIN to start loop)
user_pin = 0

# Loop will run until correct PIN is entered
while user_pin != pin:

    # Take PIN input from user
    user_pin = int(input("Enter PIN: "))

    # Check if PIN is correct
    if user_pin == pin:
        print("Access Granted")   # Correct PIN entered
    else:
        print("Incorrect PIN. Try Again.")  # Wrong PIN entered