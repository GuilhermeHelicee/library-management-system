from database import get_connection

# adding new book to the library
def add_book():
    title = input("Enter book title: ")
    author = input("Enter author: ")

    while True:
        try:
            year = int(input("Enter publication year: "))
            break
        except ValueError:
            print("Please enter a valid year.")
    
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO books (title, author, year)
        VALUES (?, ?, ?)
    """, (title, author, year))

    connection.commit()
    connection.close()

    print("Book added successfully!")

# Listing all books in the library
def list_books():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()

    connection.close()

    if not books:
        print("No books found.")
        return

    print("\n===== BOOKS =====")

    for book in books:
        print(
            f"ID: {book[0]} | "
            f"Title: {book[1]} | "
            f"Author: {book[2]} | "
            f"Year: {book[3]}"
        )

# searching for a book by title
def search_book():
    title = input("Enter the book title: ")

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM books WHERE title LIKE ?",
        (f"%{title}%",)
    )

    books = cursor.fetchall()

    connection.close()

    if not books:
        print("No books found.")
        return

    print("\n===== SEARCH RESULTS =====")

    for book in books:
        print(
            f"ID: {book[0]} | "
            f"Title: {book[1]} | "
            f"Author: {book[2]} | "
            f"Year: {book[3]}"
        )

# updating a book's information
def update_book():
  while True:
    try:
        book_id = int(input("Enter the book ID:"))
    except ValueError:
        print("Please enter a valid ID.")
    title = input("Enter the new title: ")
    author = input("Enter the new author: ")

    while True:
        try:
            year = int(input("Enter the new publication year: "))
            break
        except ValueError:
            print("Please enter a valid year.")
    year = int(input("Enter the new publication year: "))

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE books
        SET title = ?, author = ?, year = ?
        WHERE id = ?
    """, (title, author, year, book_id))

    connection.commit()

    if cursor.rowcount == 0:
        print("Book not found.")
    else:
        print("Book updated successfully!")

# deleting a book from the library
def delete_book():
    while True:
        try:
         book_id = int(input("Enter the book ID: "))
         break
        except ValueError:
            print("Please enter a valid ID.")

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM books WHERE id = ?",
        (book_id,)
    )

    connection.commit()

    if cursor.rowcount == 0:
        print("Book not found.")
    else:
        print("Book deleted successfully!")