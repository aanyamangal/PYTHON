# library_manager/book.py
"""Book model for library inventory."""

from typing import Dict


class Book:
    """Represents a book in the library."""

    def __init__(self, title: str, author: str, isbn: str, status: str = "available"):
        """
        Initialize a Book.

        Args:
            title: Book title.
            author: Book author.
            isbn: Book ISBN - used as unique identifier.
            status: "available" or "issued".
        """
        self.title = title.strip()
        self.author = author.strip()
        self.isbn = isbn.strip()
        self.status = status if status in ("available", "issued") else "available"

    def __str__(self) -> str:
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - {self.status}"

    def to_dict(self) -> Dict[str, str]:
        """Return dictionary suitable for JSON serialization."""
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "status": self.status,
        }

    def issue(self) -> bool:
        """Mark book as issued if it is available. Returns True on success."""
        if self.status == "available":
            self.status = "issued"
            return True
        return False

    def return_book(self) -> bool:
        """Mark book as available if currently issued. Returns True on success."""
        if self.status == "issued":
            self.status = "available"
            return True
        return False

    def is_available(self) -> bool:
        """Check availability."""
        return self.status == "available"
