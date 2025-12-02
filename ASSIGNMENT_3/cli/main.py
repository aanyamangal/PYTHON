# cli/main.py
"""Command-line interface for Library Inventory Manager."""

from library_manager.book import Book
from library_manager.inventory import LibraryInventory

def print_menu() -> None:
    print()
    print("=== Library Inventory Manager ===")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. View All Books")
    print("5. Search Book")
    print("6. Remove Book")
    print("7. Exit")
    print()

def safe_input(prompt: str) -> str:
    """Wrap input to handle KeyboardInterrupt gracefully."""
    try:
        return input(prompt)
    except (KeyboardInterrupt, EOFError):
        print("\nInput aborted by user. Returning to menu.")
        return ""

def add_book_cli(inv: LibraryInventory) -> None:
    print("\n--- Add Book ---")
    title = safe_input("Title: ").strip()
    if not title:
        print("Title required.")
        return
    author = safe_input("Author: ").strip() or "Unknown"
    isbn = safe_input("ISBN: ").strip()
    if not isbn:
        print("ISBN required.")
        return
    try:
        inv.add_book(Book(title=title, author=author, isbn=isbn))
        print("Book added successfully.")
    except ValueError as e:
        print("Error:", e)
    except Exception as e:
        print("Unexpected error:", e)

def issue_book_cli(inv: LibraryInventory) -> None:
    print("\n--- Issue Book ---")
    isbn = safe_input("ISBN to issue: ").strip()
    if not isbn:
        print("ISBN required.")
        return
    if inv.issue_book(isbn):
        print("Book issued.")
    else:
        print("Failed to issue book (not found or already issued).")

def return_book_cli(inv: LibraryInventory) -> None:
    print("\n--- Return Book ---")
    isbn = safe_input("ISBN to return: ").strip()
    if not isbn:
        print("ISBN required.")
        return
    if inv.return_book(isbn):
        print("Book returned.")
    else:
        print("Failed to return book (not found or not issued).")

def view_all_cli(inv: LibraryInventory) -> None:
    print("\n--- All Books ---")
    books = inv.display_all()
    if not books:
        print("No books in the library.")
        return
    for b in books:
        print(b)

def search_cli(inv: LibraryInventory) -> None:
    print("\n--- Search Book ---")
    mode = safe_input("Search by (title/isbn): ").strip().lower()
    if mode == "title":
        q = safe_input("Enter title substring: ").strip()
        if not q:
            print("Search term required.")
            return
        results = inv.search_by_title(q)
        if results:
            for b in results:
                print(b)
        else:
            print("No results.")
    elif mode == "isbn":
        isbn = safe_input("Enter ISBN: ").strip()
        if not isbn:
            print("ISBN required.")
            return
        book = inv.search_by_isbn(isbn)
        print(book if book else "Not found.")
    else:
        print("Invalid search mode; choose 'title' or 'isbn'.")

def remove_book_cli(inv: LibraryInventory) -> None:
    print("\n--- Remove Book ---")
    isbn = safe_input("ISBN to remove: ").strip()
    if not isbn:
        print("ISBN required.")
        return
    if inv.remove_book(isbn):
        print("Book removed.")
    else:
        print("Book not found.")

def main() -> None:
    inv = LibraryInventory()  # uses data/books.json by default
    while True:
        print_menu()
        choice = safe_input("Select an option (1-7): ").strip()
        if not choice:
            continue
        if choice == "1":
            add_book_cli(inv)
        elif choice == "2":
            issue_book_cli(inv)
        elif choice == "3":
            return_book_cli(inv)
        elif choice == "4":
            view_all_cli(inv)
        elif choice == "5":
            search_cli(inv)
        elif choice == "6":
            remove_book_cli(inv)
        elif choice == "7":
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice; enter a number between 1 and 7.")

if __name__ == "__main__":
    main()
