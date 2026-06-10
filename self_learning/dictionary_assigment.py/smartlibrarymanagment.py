 # Smart Library Management System

# Dictionary containing library books
library = {
    "B101": {"title": "Python Basics", "author": "ABC", "copies": 5},
    "B102": {"title": "C Programming", "author": "XYZ", "copies": 2},
    "B103": {"title": "Data Science", "author": "PQR", "copies": 8},
    "B104": {"title": "Machine Learning", "author": "LMN", "copies": 1},
    "B105": {"title": "Java Fundamentals", "author": "DEF", "copies": 0}
}

while True:

    # Display menu
    print("\n===== SMART LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add a Book")
    print("2. Remove a Book")
    print("3. Search Book by ID")
    print("4. Search Book by Title")
    print("5. Update Available Copies")
    print("6. Issue a Book")
    print("7. Return a Book")
    print("8. Display Books with Fewer than 3 Copies")
    print("9. Display Unavailable Books")
    print("10. Find Most Available Book")
    print("11. Generate Restocking Report")
    print("12. Create Immediate Purchase Dictionary")
    print("13. Generate Complete Library Summary Report")
    print("14. Exit")

    choice = int(input("Enter your choice: "))

    # 1. Add a book
    if choice == 1:

        book_id = input("Enter Book ID: ")
        title = input("Enter Title: ")
        author = input("Enter Author: ")
        copies = int(input("Enter Copies: "))

        library[book_id] = {
            "title": title,
            "author": author,
            "copies": copies
        }

        print("Book Added Successfully")

    # 2. Remove a book
    elif choice == 2:

        book_id = input("Enter Book ID: ")

        if book_id in library:
            del library[book_id]
            print("Book Removed Successfully")
        else:
            print("Book Not Found")

    # 3. Search by Book ID
    elif choice == 3:

        book_id = input("Enter Book ID: ")

        if book_id in library:
            print(library[book_id])
        else:
            print("Book Not Found")

    # 4. Search by Title
    elif choice == 4:

        title = input("Enter Book Title: ")

        found = False

        for book_id, data in library.items():

            if data["title"].lower() == title.lower():

                print(book_id, data)
                found = True

        if found == False:
            print("Book Not Found")

    # 5. Update available copies
    elif choice == 5:

        book_id = input("Enter Book ID: ")

        if book_id in library:

            copies = int(input("Enter New Copies: "))
            library[book_id]["copies"] = copies

            print("Copies Updated Successfully")

        else:
            print("Book Not Found")

    # 6. Issue a book
    elif choice == 6:

        book_id = input("Enter Book ID: ")

        if book_id in library:

            if library[book_id]["copies"] > 0:

                library[book_id]["copies"] -= 1
                print("Book Issued Successfully")

            else:
                print("Book Not Available")

        else:
            print("Book Not Found")

    # 7. Return a book
    elif choice == 7:

        book_id = input("Enter Book ID: ")

        if book_id in library:

            library[book_id]["copies"] += 1
            print("Book Returned Successfully")

        else:
            print("Book Not Found")

    # 8. Books with fewer than 3 copies
    elif choice == 8:

        print("\nBooks With Less Than 3 Copies:")

        for book_id, data in library.items():

            if data["copies"] < 3:

                print(book_id, data)

    # 9. Unavailable books
    elif choice == 9:

        print("\nUnavailable Books:")

        for book_id, data in library.items():

            if data["copies"] == 0:

                print(book_id, data)

    # 10. Most available book
    elif choice == 10:

        max_book = ""
        max_copies = -1

        for book_id, data in library.items():

            if data["copies"] > max_copies:

                max_copies = data["copies"]
                max_book = book_id

        print("Most Available Book:")
        print(max_book, library[max_book])

    # 11. Restocking report
    elif choice == 11:

        print("\n===== RESTOCKING REPORT =====")

        for book_id, data in library.items():

            if data["copies"] < 3:

                print(book_id, data["title"], "- Need Restocking")

    # 12. Immediate purchase dictionary
    elif choice == 12:

        purchase_books = {}

        for book_id, data in library.items():

            if data["copies"] <= 1:

                purchase_books[book_id] = data

        print("\nBooks Requiring Immediate Purchase:")
        print(purchase_books)

    # 13. Complete Library Summary Report
    elif choice == 13:

        total_books = len(library)

        total_copies = 0

        unavailable = 0

        low_stock = 0

        for data in library.values():

            total_copies += data["copies"]

            if data["copies"] == 0:
                unavailable += 1

            if data["copies"] < 3:
                low_stock += 1

        max_book = ""
        max_copies = -1

        for book_id, data in library.items():

            if data["copies"] > max_copies:

                max_copies = data["copies"]
                max_book = book_id

        print("\n===== LIBRARY SUMMARY REPORT =====")

        print("Total Books =", total_books)

        print("Total Available Copies =", total_copies)

        print("Low Stock Books =", low_stock)

        print("Unavailable Books =", unavailable)

        print("Most Available Book =", max_book)

        print("Book Details =", library[max_book])

    # 14. Exit
    elif choice == 14:

        print("Program Ended Successfully")
        break

    else:
        print("Invalid Choice")