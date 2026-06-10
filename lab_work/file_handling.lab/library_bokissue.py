#program for book issue 
  # Function to read all book records from file
def read_books():

    # Empty list to store books
    books = []

    # Open file in read mode
    f = open("books.txt", "r")

    # Read file line by line
    for line in f:

        # Split each record using comma
        bookid, title, qty = line.strip().split(",")

        # Add record into list
        books.append([bookid, title, int(qty)])

    # Close file
    f.close()

    # Return complete book list
    return books


# Function to update file after issue/return operation
def update_file(books):

    # Open file in write mode
    f = open("books.txt", "w")

    # Write updated records back to file
    for book in books:
        f.write(f"{book[0]},{book[1]},{book[2]}\n")

    # Close file
    f.close()


# Infinite loop for menu
while True:

    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Display all books")
    print("2. Search book by ID")
    print("3. Issue a book")
    print("4. Return a book")
    print("5. Display unavailable books")
    print("6. Display books requiring restocking")
    print("7. Exit")

    # Take user choice
    choice = int(input("Enter choice: "))

    # Read all books from file
    books = read_books()

    # Display all books
    if choice == 1:

        print("\nBook Records")

        for book in books:
            print(book[0], book[1], book[2])

    # Search book using Book ID
    elif choice == 2:

        search_id = input("Enter Book ID: ")

        found = False

        for book in books:

            if book[0] == search_id:

                print("Book ID :", book[0])
                print("Title   :", book[1])
                print("Quantity:", book[2])

                found = True
                break

        if found == False:
            print("Book not found")

    # Issue a book
    elif choice == 3:

        issue_id = input("Enter Book ID to issue: ")

        found = False

        for book in books:

            if book[0] == issue_id:

                found = True

                # Check availability
                if book[2] > 0:

                    # Reduce quantity by 1
                    book[2] -= 1

                    print("Book issued successfully")

                else:
                    print("Book not available")

                break

        if found == False:
            print("Book not found")

        # Save updated records into file
        update_file(books)

    # Return a book
    elif choice == 4:

        return_id = input("Enter Book ID to return: ")

        found = False

        for book in books:

            if book[0] == return_id:

                # Increase quantity by 1
                book[2] += 1

                found = True

                print("Book returned successfully")

                break

        if found == False:
            print("Book not found")

        # Save updated records into file
        update_file(books)

    # Display unavailable books
    elif choice == 5:

        print("\nUnavailable Books")

        for book in books:

            if book[2] == 0:
                print(book[0], book[1])

    # Display books with quantity less than 2
    elif choice == 6:

        print("\nBooks Requiring Restocking")

        for book in books:

            if book[2] < 2:
                print(book[0], book[1], book[2])

    # Exit from program
    elif choice == 7:

        print("Program Ended")
        break

    # Invalid menu choice
    else:

        print("Invalid Choice")