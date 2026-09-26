books = []
filename = "books.txt"


def load_books():
    try:
        file = open(filename, "r")
        lines = file.readlines()
        file.close()
        for line in lines:
            line = line.strip()
            if line != "":
                parts = line.split(",")
                title = parts[0]
                author = parts[1]
                status = parts[2]
                books.append([title, author, status])
    except:
        pass


def save_books():
    file = open(filename, "w")
    for book in books:
        line = book[0] + "," + book[1] + "," + book[2]
        file.write(line + "\n")
    file.close()


def add_book():
    print("\n-- Add Book --")
    title = input("Enter title: ").strip()
    author = input("Enter author: ").strip()
    books.append([title, author, "Available"])
    save_books()
    print("Book added!\n")


def view_books():
    print("\n-- Library Books --")
    if len(books) == 0:
        print("No books in the library yet.\n")
        return

    count = 1
    for book in books:
        print(str(count) + ". " + book[0] + " by " + book[1] + " - " + book[2])
        count = count + 1
    print("")


def borrow_book():
    view_books()
    if len(books) == 0:
        return

    choice = input("Enter the number of the book to borrow: ").strip()
    if choice.isdigit():
        index = int(choice) - 1
        if 0 <= index < len(books):
            if books[index][2] == "Available":
                books[index][2] = "Borrowed"
                save_books()
                print("You borrowed:", books[index][0], "\n")
            else:
                print("That book is already borrowed.\n")
        else:
            print("Invalid number.\n")
    else:
        print("Please enter a valid number.\n")


def return_book():
    view_books()
    if len(books) == 0:
        return

    choice = input("Enter the number of the book to return: ").strip()
    if choice.isdigit():
        index = int(choice) - 1
        if 0 <= index < len(books):
            if books[index][2] == "Borrowed":
                books[index][2] = "Available"
                save_books()
                print("You returned:", books[index][0], "\n")
            else:
                print("That book was not borrowed.\n")
        else:
            print("Invalid number.\n")
    else:
        print("Please enter a valid number.\n")


def remove_book():
    view_books()
    if len(books) == 0:
        return

    choice = input("Enter the number of the book to remove: ").strip()
    if choice.isdigit():
        index = int(choice) - 1
        if 0 <= index < len(books):
            removed = books.pop(index)
            save_books()
            print("Removed:", removed[0], "\n")
        else:
            print("Invalid number.\n")
    else:
        print("Please enter a valid number.\n")


def show_menu():
    print("========================================")
    print("           LIBRARY BOOK MANAGER")
    print("========================================")
    print("1. Add book")
    print("2. View books")
    print("3. Borrow book")
    print("4. Return book")
    print("5. Remove book")
    print("6. Exit")


load_books()

while True:
    show_menu()
    choice = input("Choose an option (1-6): ").strip()

    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        borrow_book()
    elif choice == "4":
        return_book()
    elif choice == "5":
        remove_book()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.\n")
