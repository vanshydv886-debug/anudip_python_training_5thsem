# program for library book avilibility system 
books = {
    "Python": 5,
    "Java": 2,
    "DBMS": 4,
    "Networking": 1,
    "OS": 3,
    "AI": 6,
    "ML": 2,
    "Cloud": 5,
    "Cyber Security": 1,
    "Web Development": 4
}

print("Books Requiring Attention:")
for book, copies in books.items():
    if copies < 3:
        print(book)

max_book = max(books, key=books.get)
print("\nBook with Maximum Copies:")
print(max_book, "(", books[max_book], "copies)", sep="")

min_book = min(books, key=books.get)
print("\nBook with Minimum Copies:")
print(min_book, "(", books[min_book], "copies)", sep="")

total_copies = sum(books.values())
print("\nTotal Copies Available:", total_copies)

restocking = []

for book, copies in books.items():
    if copies < 3:
        restocking.append(book)

print("\nRestocking List:", restocking)