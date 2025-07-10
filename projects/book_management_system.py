# Book Management System

books = []

def add_book():
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    book = {'Title': title, 'Author': author}
    books.append(book)
    print("Book added successfully!\n")

def view_books():
    if not books:
        print("No books available.\n")
        return
    print("\nList of Books:")
    for i, book in enumerate(books, 1):
        print(f"{i}. Title: {book['Title']}, Author: {book['Author']}")
    print()

def search_book():
    keyword = input("Enter title or author to search: ").lower()
    found = False
    for book in books:
        if keyword in book['Title'].lower() or keyword in book['Author'].lower():
            print(f"Found -> Title: {book['Title']}, Author: {book['Author']}")
            found = True
    if not found:
        print("No matching book found.\n")

def delete_book():
    title = input("Enter the title of the book to delete: ")
    global books
    books = [book for book in books if book['Title'].lower() != title.lower()]
    print("Book deleted if it existed.\n")

def main():
    while True:
        print("=== Book Management System ===")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Delete Book")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_book()
        elif choice == '2':
            view_books()
        elif choice == '3':
            search_book()
        elif choice == '4':
            delete_book()
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
