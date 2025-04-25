# 📚 Library Management System

This is a basic Library Management System built using Python. It helps manage book records, user information, and borrowing/returning functionality using a simple object-oriented structure. Data is stored in JSON format for persistence.

---

## 🚀 Features

- 📖 Add, remove, and update books
- 👤 Register and manage users
- 🔄 Borrow and return books
- 🔍 View available books and search by title/author
- 💾 Persistent data storage using JSON files

---

## 📁 Project Structure

```plaintext
library_system/
│
├── data/
│   ├── books.json               # Stores all book records
│   └── users.json               # Stores user information
│
├── models/
│   ├── book.py                  # Book class definition
│   └── user.py                  # User class definition
│
├── services/
│   ├── library.py               # Library system class with core logic
│   └── data_manager.py          # Utility for reading/writing JSON data
│
├── main.py                      # Entry point to run the program
├── requirements.txt             # List of Python dependencies (if needed)
└── README.md                    # Project documentation

```
---

## 🧱 Module Descriptions

### 📄 `models/book.py`
Defines the `Book` class responsible for creating book objects. Each book has:
- `book_id` (str): Unique identifier
- `title` (str): Title of the book
- `author` (str): Author of the book
- `is_available` (bool): Indicates whether the book is available for borrowing

### 📄 `models/user.py`
Defines the `User` class used to manage users of the library. Each user has:
- `user_id` (str): Unique user identifier
- `name` (str): User’s full name
- `borrowed_books` (list): A list of book IDs the user has currently borrowed

### 🛠️ `services/library.py`
Main controller of the system — defines the `Library` class which encapsulates core functionalities:
- Add, remove, and search for books
- Register new users
- Borrow and return books
- Track which books are available or borrowed

### 💾 `services/data_manager.py`
Utility module that manages reading from and writing to JSON files:
- `load_books()` / `save_books()`: For book data
- `load_users()` / `save_users()`: For user data

Ensures data persistence between sessions.

### 🚀 `main.py`
The main execution script and CLI interface. Responsibilities include:
- Displaying the main menu
- Accepting user input
- Triggering library actions via `Library` class methods

Acts as the entry point to the application.

