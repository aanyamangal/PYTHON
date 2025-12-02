# tests/test_inventory.py
import os
from pathlib import Path
import tempfile
import json

from library_manager.book import Book
from library_manager.inventory import LibraryInventory

def test_add_and_search_and_issue_return(tmp_path):
    # Use a temporary file so tests don't touch real data
    file_path = tmp_path / "books_test.json"
    file_path.write_text("[]", encoding="utf-8")

    inv = LibraryInventory(str(file_path))
    b = Book("Test Driven Development", "Kent Beck", "ISBN-TDD-001")
    inv.add_book(b)

    # Search by isbn
    found = inv.search_by_isbn("ISBN-TDD-001")
    assert found is not None
    assert found.title == "Test Driven Development"

    # Issue book
    issued = inv.issue_book("ISBN-TDD-001")
    assert issued is True
    assert inv.search_by_isbn("ISBN-TDD-001").status == "issued"

    # Return book
    returned = inv.return_book("ISBN-TDD-001")
    assert returned is True
    assert inv.search_by_isbn("ISBN-TDD-001").status == "available"

    # Cleanup
    assert file_path.exists()
