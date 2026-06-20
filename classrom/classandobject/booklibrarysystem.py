 # Book Library System using Class and Object

# Creating Book class
class Book:

    # Constructor to initialize book details
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True

    # Method to issue a book
    def issue_book(self):
        if self.available:
            self.available = False
            print("Book Issued Successfully.")
        else:
            print("Book is already issued.")

    # Method to return a book
    def return_book(self):
        if not self.available:
            self.available = True
            print("Book Returned Successfully.")
        else:
            print("Book is already available in library.")

    # Method to display book details
    def display_details(self):
        print("\n----- Book Details -----")
        print("Book ID            :", self.book_id)
        print("Title              :", self.title)
        print("Author             :", self.author)

        if self.available:
            print("Availability Status: Available")
        else:
            print("Availability Status: Not Available")


# Taking input from user
book_id = input("Enter Book ID: ")
title = input("Enter Book Title: ")
author = input("Enter Author Name: ")

# Creating object
book = Book(book_id, title, author)

# Menu Driven Program
while True:

    print("\n===== BOOK LIBRARY SYSTEM =====")
    print("1. Display Book Details")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Exit")

    try:
        choice = int(input("Enter Your Choice: "))

        if choice == 1:
            book.display_details()

        elif choice == 2:
            book.issue_book()

        elif choice == 3:
            book.return_book()

        elif choice == 4:
            print("Program Ended Successfully.")
            break

        else:
            print("Invalid Choice! Please select between 1 and 4.")

    except ValueError:
        print("Invalid Input! Enter a number only.")
        
