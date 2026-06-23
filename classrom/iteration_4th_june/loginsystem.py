#program for login system
password = ""

while password != "admin123":
    password = input("Enter Password: ")

    if password == "admin123":
        print("Login Successful.")
    else:
        print("Invalid Password.")