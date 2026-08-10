from database import create_tables
from books import add_book, list_books, search_book, update_book, delete_book


def main():
    create_tables()

    while True:
        print("\n===== LIBRARY SYSTEM =====")
        print("1. Add Book")
        print("2. List Books")
        print("3. Search Book")
        print("4. Update Book")
        print("5. Delete Book")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()

        elif choice == "2":
            list_books()

        elif choice == "3":
            search_book()

        elif choice == "4":
            update_book()

        elif choice == "5":
            delete_book()

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()