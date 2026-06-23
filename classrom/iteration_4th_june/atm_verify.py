#program for atm verification 
pin = "1234"

while True:
    user_pin = input("Enter PIN: ")

    if user_pin == pin:
        print("Access Granted.")
        break
    else:
        print("Incorrect PIN. Try again.")