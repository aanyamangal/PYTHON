"""
LibraryInventory: manages list of Book objects with JSON persistence.
Handles missing/corrupted files gracefully and logs events.
"""

import json
import logging
from pathlib import Path
from typing import List, Optional

from .book import Book

# ---------------------- LOGGING SETUP ----------------------
LOG_DIR = Path("logs")
LOG_DIR.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    filename=str(LOG_DIR / "library.log"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# -----------------------------------------------------------


class LibraryInventory:
    """Manage a library of Book objects with JSON persistence."""

    def __init__(self, file_path: str = "data/books.json"):
        self.file_path = Path(file_path)
        self.books: List[Book] = []

        # Ensure data directory exists
        self.file_path.parent.mkdir(parents=True, exist_ok=True)

        self._ensure_file_exists()
        self.load_books()

    def _ensure_file_exists(self) -> None:
        """Create an empty JSON file if missing."""
        if not self.file_path.exists():
            try:
                self.file_path.write_text("[]", encoding="utf-8")
                logging.info(f"Created new data file at {self.file_path}")
            except Exception as e:
                logging.error(f"Failed to create data file {self.file_path}: {e}")

    def load_books(self) -> None:
        """Load books from JSON with handling for corrupted files."""
        try:
            with self.file_path.open("r", encoding="utf-8") as f:
                data = json.load(f)

            if not isinstance(data, list):
                raise ValueError("JSON root is not a list")

            self.books = []
            for entry in data:
                try:
                    book = Book(
                        title=entry.get("title", ""),
                        author=entry.get("author", ""),
                        isbn=entry.get("isbn", ""),
                        status=entry.get("status", "available"),
                    )
                    self.books.append(book)
                except Exception as e:
                    logging.error(f"Skipping invalid JSON entry: {entry} | error: {e}")

            logging.info(f"Loaded {len(self.books)} books from {self.file_path}")

        except json.JSONDecodeError as e:
            backup = self.file_path.with_suffix(".corrupt.json")
            self.file_path.replace(backup)
            logging.error(f"Corrupted JSON moved to {backup}: {e}")
            self.file_path.write_text("[]", encoding="utf-8")
            self.books = []

        except FileNotFoundError:
            logging.warning(f"{self.file_path} not found; creating a new file.")
            self.file_path.write_text("[]", encoding="utf-8")
            self.books = []

        except Exception as e:
            logging.error(f"Unexpected error loading books: {e}")
            self.books = []

    def save_books(self) -> None:
        """Save current books to JSON."""
        try:
            serializable = [book.to_dict() for book in self.books]
            with self.file_path.open("w", encoding="utf-8") as f:
                json.dump(serializable, f, ensure_ascii=False, indent=4)
            logging.info(f"Saved {len(self.books)} books to {self.file_path}")
        except Exception as e:
            logging.error(f"Failed to save books: {e}")

    def add_book(self, book: Book) -> None:
        """Add new book if ISBN is unique."""
        if self.search_by_isbn(book.isbn):
            raise ValueError(f"A book with ISBN {book.isbn} already exists.")
        self.books.append(book)
        self.save_books()
        logging.info(f"Added book {book.isbn} - {book.title}")

    def search_by_title(self, title_substring: str) -> List[Book]:
        """Search for books containing the title substring."""
        query = title_substring.lower().strip()
        return [b for b in self.books if query in b.title.lower()]

    def search_by_isbn(self, isbn: str) -> Optional[Book]:
        """Return book matching ISBN."""
        isbn = isbn.strip()
        return next((b for b in self.books if b.isbn == isbn), None)

    def display_all(self) -> List[Book]:
        """Return all books."""
        return list(self.books)

    def issue_book(self, isbn: str) -> bool:
        """Issue a book if available."""
        book = self.search_by_isbn(isbn)
        if book and book.issue():
            self.save_books()
            logging.info(f"Issued book {isbn}")
            return True
        logging.info(f"Failed to issue {isbn}: not found or unavailable")
        return False

    def return_book(self, isbn: str) -> bool:
        """Return a book if it was issued."""
        book = self.search_by_isbn(isbn)
        if book and book.return_book():
            self.save_books()
            logging.info(f"Returned book {isbn}")
            return True
        logging.info(f"Failed to return {isbn}: not found or not issued")
        return False

    def remove_book(self, isbn: str) -> bool:
        """Remove a book by ISBN."""
        book = self.search_by_isbn(isbn)
        if book:
            self.books.remove(book)
            self.save_books()
            logging.info(f"Removed book {isbn}")
            return True
        return False
