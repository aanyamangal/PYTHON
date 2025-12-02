# library_manager/__init__.py
"""
library_manager package initializer.
Contains Book and LibraryInventory classes in separate modules.
"""
from .book import Book
from .inventory import LibraryInventory

__all__ = ["Book", "LibraryInventory"]
