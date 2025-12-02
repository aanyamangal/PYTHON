Library Management System (Python)

A simple and modular Library Management System built using Python.
This project uses functions, classes, modular structure, file handling, and CLI menus, fulfilling all assignment requirements.

Features

✅ Add Book
Store a new book with:
Title
Author
ISBN

✅ Issue Book
Marks a book as issued if available.

✅ Return Book
Marks a previously issued book as returned.

✅ View All Books
Displays all books with their status (Available / Issued).

✅ Search Book by Title
Searches through the catalog using exact or partial title.

✅ Persistent Storage
All books are saved in catalog.json automatically.

Project Structure
python-3 library manager/
│
├── cli/
│   └── main.py               # Contains the main menu and user interface
│
├── library_manager/
│   ├── _init_.py
│   ├── book.py               # Defines the Book class
│   └── inventory.py          # Handles library operations and file storage
│
├── tests
│  └── test_inventory.py
├── catalog.json              # Stores all book records permanently
│
├── requirements.txt
└── README.md                 # Project documentation

How to Run the Program
Step 1: Open Terminal inside project folder
Step 2: Run the CLI menu
python -m cli.main


You will see:
Library Menu
1. Add Book
2. Issue Book
3. Return Book
4. View All Books
5. Search Book By Title
6. Exit

Technologies Used
Python
File Handling (JSON)
Object-Oriented Programming
Modular Programming
