library = []

def add_book(book_name):
    library.append(book_name)
    print(f'"{book_name}" has been added to the library.\n')

def display_books():
    if library:
        print("Books available in the library:")
        for book in library:
            print(f"• {book}")
    else:
        print("No books are currently available.")
    print()

def borrow_book(book_name):
    if book_name in library:
        library.remove(book_name)
        print(f'You have borrowed "{book_name}".\n')
    else:
        print(f'Sorry, "{book_name}" is not available.\n')

def return_book(book_name):
    library.append(book_name)
    print(f'Thank you for returning "{book_name}".\n')

# Menu loop
while True:
    print("=== Library Menu ===")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        name = input("Enter book name to add: ")
        add_book(name)

    elif choice == "2":
        display_books()

    elif choice == "3":
        name = input("Enter book name to borrow: ")
        borrow_book(name)

    elif choice == "4":
        name = input("Enter book name to return: ")
        return_book(name)

    elif choice == "5":
        print("Exiting the library system. Goodbye!")
        break

    else:
        print("Invalid choice. Try again.\n")
