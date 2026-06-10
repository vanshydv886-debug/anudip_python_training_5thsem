# Function to read contacts from file
def read_contacts():

    contacts = []

    f = open("contacts.txt", "r")

    for line in f:

        name, number = line.strip().split(",")

        contacts.append([name, number])

    f.close()

    return contacts


# Function to save contacts back to file
def save_contacts(contacts):

    f = open("contacts.txt", "w")

    for contact in contacts:
        f.write(contact[0] + "," + contact[1] + "\n")

    f.close()


# Function to display all contacts
def display_contacts():

    contacts = read_contacts()

    print("\nAll Contacts")

    for contact in contacts:
        print(contact[0], "-", contact[1])


# Function to search contact
def search_contact():

    contacts = read_contacts()

    name = input("Enter Name: ")

    found = False

    for contact in contacts:

        if contact[0].lower() == name.lower():

            print("Name :", contact[0])
            print("Number :", contact[1])

            found = True

    if found == False:
        print("Contact Not Found")


# Function to add contact
def add_contact():

    contacts = read_contacts()

    name = input("Enter Name: ")
    number = input("Enter Number: ")

    contacts.append([name, number])

    save_contacts(contacts)

    print("Contact Added Successfully")


# Function to update contact number
def update_contact():

    contacts = read_contacts()

    name = input("Enter Name to Update: ")

    found = False

    for contact in contacts:

        if contact[0].lower() == name.lower():

            new_number = input("Enter New Number: ")

            contact[1] = new_number

            found = True

            print("Contact Updated")

    if found == False:
        print("Contact Not Found")

    save_contacts(contacts)


# Function to delete contact
def delete_contact():

    contacts = read_contacts()

    name = input("Enter Name to Delete: ")

    new_contacts = []

    found = False

    for contact in contacts:

        if contact[0].lower() != name.lower():

            new_contacts.append(contact)

        else:

            found = True

    if found:
        save_contacts(new_contacts)
        print("Contact Deleted")

    else:
        print("Contact Not Found")


# Function to display contacts starting with vowels
def vowel_contacts():

    contacts = read_contacts()

    print("\nContacts Starting With Vowels")

    for contact in contacts:

        if contact[0][0].lower() in "aeiou":

            print(contact[0], "-", contact[1])


# Main Menu
while True:

    print("\n===== CONTACT MANAGEMENT SYSTEM =====")
    print("1. Display All Contacts")
    print("2. Search Contact")
    print("3. Add Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Display Vowel Contacts")
    print("7. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        display_contacts()

    elif choice == 2:
        search_contact()

    elif choice == 3:
        add_contact()

    elif choice == 4:
        update_contact()

    elif choice == 5:
        delete_contact()

    elif choice == 6:
        vowel_contacts()

    elif choice == 7:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")